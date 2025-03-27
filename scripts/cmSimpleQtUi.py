import maya.cmds as cmds
import maya.OpenMayaUI as omui
import re

from lib_python_velan.mayaRigUtils.scripts import skincluster as skn
from lib_python_velan.mayaRigUtils.scripts import rigUtils as rigu
from lib_python_velan.mayaRigUtils.scripts import surfaces as srf
from lib_python_velan.mayaRigUtils.scripts import omUtil as omu
from lib_python_velan.mayaRigUtils.scripts import curves as crv
from lib_python_velan.mayaRigUtils.scripts import meshes as msh
from lib_python_velan.mayaRigUtils.scripts import nodes as nde

from lib_python_velan.mayaRigComponents.scripts import iKfKCurve
from lib_python_velan.mayaRigComponents.scripts import rdCtl as rdCtl
from lib_python_velan.mayaRigComponents.scripts import strapRigs as stprg
from lib_python_velan.mayaRigComponents.scripts import strap

from . import cmSimpleUi as customUI

try: # maya 2024
    from PySide2 import QtCore, QtGui, QtWidgets
    import shiboken2 as shi
except: # maya 2025
    from PySide6 import QtCore, QtGui, QtWidgets
    import shiboken6 as shi





#############################################################################################


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return shi.wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
     
         
class ControlMainWindow(QtWidgets.QMainWindow):

    
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        # self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = customUI.Ui_MainWindow()
        self.ui.setupUi(self)

        ### Locals
        self.strpGde = None
        self.ikfkGde = None
        self.rebuild = None

        self.ui.btn_setCtlSize.clicked.connect(self.setCtlSize)
        self.ui.btn_setCtlShape.clicked.connect(self.setCtlShape)
        self.ui.btn_setCtlColor.clicked.connect(self.setCtlColor)
        self.ui.btn_setCtlVis.clicked.connect(self.setCtlVis)

        # Attrs
        self.ui.btn_axisGo.clicked.connect(self.lockUnlockAttr)
        self.ui.btn_globalSclObj.clicked.connect(self.globalScaleObj)
        self.ui.btn_globalScaleConnect.clicked.connect(self.globalScaleConnect)
        self.ui.btn_directConnect.clicked.connect(self.directConnect)
        self.ui.btn_createMatCon.clicked.connect(self.parentConstraint)
        self.ui.btn_delMatCon.clicked.connect(self.delParentConstraint)

        # Strap Guide
        self.ui.btn_prepSrf.clicked.connect(self.prepSrfDir)
        self.ui.btn_swapUV.clicked.connect(stprg.revSrfDir)
        self.ui.btn_goGuidesOnSrf.clicked.connect(self.strapGuide)
        # Strap Rig
        self.ui.btn_goStrapRig.clicked.connect(self.strapRig)
        # Create on Srf
        self.ui.btn_utilPrepSrf.clicked.connect(self.prepSrfDir)
        self.ui.btn_utilSwapUV.clicked.connect(stprg.revSrfDir)
        self.ui.btn_utilCreateOnSrf.clicked.connect(self.createOnSrf)
        self.ui.btn_utilConstrainToSrf.clicked.connect(self.constrainToSrf)
        # Build : Mesh
        self.ui.btn_meshMatchPoint.clicked.connect(self.matchPointPos)
        self.ui.btn_meshUpdateOrig.clicked.connect(self.updateOrig)
        # MM
        self.ui.btn_mmGo.clicked.connect(self.matchMoveAutoBuild)
        self.ui.btn_jntOnVtx.clicked.connect(self.jntOnVtx)
        # Curve
        self.ui.btn_crvGo.clicked.connect(self.createOnCrv)
        self.ui.btn_crvConstGo.clicked.connect(self.constrainToCrv)
        self.ui.btn_crvUpObjGet.clicked.connect(self.getUpObj)
        # rdCtl
        self.ui.btn_ctlPreBindMat.clicked.connect(self.ctlPreBindMat)
        # IK/FK Chain
        self.ui.btn_gdeOnCrvGo.clicked.connect(self.curveGuide)
        self.ui.btn_bldCrvRigGo.clicked.connect(self.curveRig)
        # Singles
        self.ui.btn_singleCtl.clicked.connect(self.singleCtl)
        self.ui.btn_singlePatch.clicked.connect(self.singlePatch)
        # SKIN
        self.ui.btn_resetBindPose.clicked.connect(self.setBindPose)
        self.ui.btn_selectClstrInfl.clicked.connect(self.selectClstrInfl)
        self.ui.btn_importWeights.clicked.connect(skn.importSkinWeights)
        self.ui.btn_exportWeights.clicked.connect(skn.exportSkinWeights)
        self.ui.btn_transferWeights.clicked.connect(lambda: [skn.transferWeights(remove=self.ui.chk_transferWeightsRemove.isChecked())])
        self.ui.btn_selBySuffix.clicked.connect(self.selectBySuffix)
        # MISC
        self.ui.btn_delUnShp.clicked.connect(msh.deleteUnusedShapesMsh)
        self.ui.btn_smoothEdges.clicked.connect(self.smoothEdges)




    def getUpObj(self):
        if len(cmds.ls(sl=1)) == 1:
            self.ui.lne_crvUpObj.setText(cmds.ls(sl=1)[0])

    def globalVars(self):
        margin   = self.ui.spn_globAutoColorMargin.value()
        ctlSize  = self.ui.spn_globCtlSize.value()
        ctlShape = self.ui.cbo_globCtlShape.currentText()
        # ctlShapeFormat = ctlShape.replace(ctlShape[0], ctlShape[0].lower())
        ctlSuffix = self.ui.lne_globCtlSuffix.text()
        jntSuffix = self.ui.lne_globJntSuffix.text()

        # ctlIdx of 0 or 1 will auto color based on worldSpace
        ctlIdx = self.ui.cbo_globCtlColor.currentIndex()
        if ctlIdx in [0,1,2]:
            ctlColor = self.ui.cbo_globCtlColor.currentIndex()
        else:
            ctlColor = self.ui.cbo_globCtlColor.currentText()

        if jntSuffix:
            jntSfx = jntSuffix
        else:
            jntSfx = 'bind'

        if ctlSuffix:
            ctlSfx = 'ctlSuffix'
        else:
            ctlSfx = 'anim'

        return margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix

    def lockUnlockAttr(self):
        if cmds.ls(sl=1):
            for item in cmds.ls(sl=True):
                if cmds.objectType(item)=='transform':
                    axisLst = []
                    if self.ui.chk_axisTX.isChecked():
                        axisLst.append('tx')
                    if self.ui.chk_axisTY.isChecked():
                        axisLst.append('ty')
                    if self.ui.chk_axisTZ.isChecked():
                        axisLst.append('tz')
                    if self.ui.chk_axisRX.isChecked():
                        axisLst.append('rx')
                    if self.ui.chk_axisRY.isChecked():
                        axisLst.append('ry')
                    if self.ui.chk_axisRZ.isChecked():
                        axisLst.append('rz')
                    if self.ui.chk_axisSX.isChecked():
                        axisLst.append('sx')
                    if self.ui.chk_axisSY.isChecked():
                        axisLst.append('sy')
                    if self.ui.chk_axisSZ.isChecked():
                        axisLst.append('sz')

                    attrVis = self.ui.cbo_hideUnhide.currentIndex()
                    lock    = self.ui.cbo_axisLockUnlock.currentIndex()
                    
                    if attrVis > 0:
                        rigu.hideUnhideSRT(item, attrVis-1, axisLst=axisLst)
                    if lock > 0:
                        rigu.lockUnlockSRT(item, lock-1, axisLst=axisLst)

    def directConnect(self):
        '''
        Direct connect attrs. Select driven obj(s) then driver obj
        '''
        if len(cmds.ls(sl=1)) > 1:
            axisLst = []
            source = cmds.ls(sl=1)[0]
            target = cmds.ls(sl=1)[1:]
            if self.ui.chk_axisTX.isChecked():
                axisLst.append('.tx')
            if self.ui.chk_axisTY.isChecked():
                axisLst.append('.ty')
            if self.ui.chk_axisTZ.isChecked():
                axisLst.append('.tz')
            if self.ui.chk_axisRX.isChecked():
                axisLst.append('.rx')
            if self.ui.chk_axisRY.isChecked():
                axisLst.append('.ry')
            if self.ui.chk_axisRZ.isChecked():
                axisLst.append('.rz')
            if self.ui.chk_axisSX.isChecked():
                axisLst.append('.sx')
            if self.ui.chk_axisSY.isChecked():
                axisLst.append('.sy')
            if self.ui.chk_axisSZ.isChecked():
                axisLst.append('.sz')

            for tgt in target:
                [cmds.connectAttr(source+axis, tgt+axis, f=1) for axis in axisLst]
        else:
            raise IndexError('Select driver, then driven')

    def parentConstraint(self):
        if len(cmds.ls(sl=1)) > 1:
            parent = cmds.ls(sl=1)[0]
            child  = cmds.ls(sl=1)[1:]
            tLst = []
            rLst = []
            sLst = []
            if self.ui.chk_axisTX.isChecked():
                tLst.append('x')
            if self.ui.chk_axisTY.isChecked():
                tLst.append('y')
            if self.ui.chk_axisTZ.isChecked():
                tLst.append('z')

            if self.ui.chk_axisRX.isChecked():
                rLst.append('x')
            if self.ui.chk_axisRY.isChecked():
                rLst.append('y')
            if self.ui.chk_axisRZ.isChecked():
                rLst.append('z')

            if self.ui.chk_axisSX.isChecked():
                sLst.append('x')
            if self.ui.chk_axisSY.isChecked():
                sLst.append('y')
            if self.ui.chk_axisSZ.isChecked():
                sLst.append('z')

            mo = self.ui.chk_maintainOffset.isChecked()

            for c in child:
                rigu.parentConstraint(parent, c, t=tLst, r=rLst, s=sLst, mo=mo)
                print('***** Done *****')
        else:
            raise IndexError('Select Parent, then Child')

    def delParentConstraint(self):
        axisLst = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz', ]
        for sel in cmds.ls(sl=1):
            nde = None
            for axis in axisLst:
                if cmds.listConnections(sel+axis):
                    if '_rigUParCon' in cmds.listConnections(sel+axis)[0]:
                        nde = cmds.listConnections(sel+axis)[0]
            if nde != None:
                cmds.delete(nde)



    def setCtlSize(self):
        if not cmds.ls(sl=1):
            raise IndexError('Select a Control')
        globalVars = None
        globalVars  = self.globalVars() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix

        ctrls = []
        for ctl in cmds.ls(sl=1):
            if cmds.nodeType(ctl)!='joint':
                pass
            else:
                ctlSuffix = ctl.split('_')[-1] # Get ctl suffix to re-instance properly
                ctrl = rdCtl.Control(ctl, ctlSuffix=ctlSuffix)
                ctrls.append(ctrl)

        if ctrls:
            for ctl in ctrls:
                ctl.size=globalVars[1]

    def setCtlShape(self):
        if not cmds.ls(sl=1):
            raise IndexError('Select a Control')

        globalVars  = self.globalVars() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix

        ctrls = []
        for ctl in cmds.ls(sl=1):
            if cmds.nodeType(ctl)!='joint':
                pass
            else:
                ctlSuffix = ctl.split('_')[-1] # Get ctl suffix to re-instance properly
                ctrl = rdCtl.Control(ctl, ctlSuffix=ctlSuffix)
                ctrls.append(ctrl)

        if ctrls:
            for ctl in ctrls:
                ctl.shape=globalVars[2]

    def setCtlColor(self):
        if not cmds.ls(sl=1):
            raise IndexError('Select a Control')

        globalVars  = self.globalVars() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix

        ctrls = []
        for ctl in cmds.ls(sl=1):
            if cmds.nodeType(ctl)!='joint':
                pass
            else:
                ctlSuffix = ctl.split('_')[-1] # Get ctl suffix to re-instance properly
                ctrl = rdCtl.Control(ctl, ctlSuffix=ctlSuffix)
                ctrls.append(ctrl)

        if ctrls:
            for ctl in ctrls:
                rigu.rdCtlSideColor(ctl, globalVars[3], globalVars[0])

    def setCtlVis(self):
        if not cmds.ls(sl=1):
            raise IndexError('Select a Control')

        visIco = 'faceUI_C0_ctl'
        if not cmds.objExists(visIco):
            raise RuntimeError('Head UI Host not present in the scene. "faceUI_C0_ctl"')

        for attr in ['bodySecondaryCtls', 'bodyTertiaryCtls']:
            if not cmds.attributeQuery(attr, node=visIco, ex=True):
                print(attr, '<'*80)
                raise RuntimeError('Missing Visibility attributes on faceUI_C0_ctl')
        
        globalVars  = self.globalVars() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix

        if globalVars[3] in [1,2]: # make sure ctlColor is set to Secondary or Tertiary
            visDict = {1:'bodySecondaryCtls', 2:'bodyTertiaryCtls'}
            for ctl in cmds.ls(sl=1):
                rigu.lockUnlockSRT(ctl, 0, axisLst='v') # unlock .v
                cmds.connectAttr(visIco+'.'+visDict[globalVars[3]], ctl+'.v', f=True)
                if not cmds.attributeQuery('visProp', node=ctl, ex=True):
                    cmds.addAttr(ctl, ci=True, dt='string', sn='visProp') # For reconnect vis functions
                cmds.setAttr(ctl+'.visProp', str(visDict[globalVars[3]]), type='string')
        else:
            raise RuntimeError('Select Secondary or Tertiary from Ctl Color drop down menu')

    
    def prepSrfDir(self):
        #fold
        self.prepSrf = stprg.prepSrfDir()

    def strapGuide(self):
        gdeRow = self.ui.spn_strapGuideRow.value()
        gdeCol = self.ui.spn_strapGuideColumn.value()
        skpLst = self.ui.chk_strapSkipLast.isChecked()
        stprg.strapGuide(gdeRow, gdeCol, skpLst)

    def strapRig(self):
        globalVars  = self.globalVars() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        jntRows     = self.ui.spn_strapJntRow.value()
        jntColumns  = self.ui.spn_strapJntColumn.value()
        makeFK      = self.ui.chk_makeCtlFK.isChecked()
        ikSpline    = self.ui.chk_ikSpline.isChecked()
        ikSplineNum = self.ui.spn_ikSplineNum.value()
        ctlSuffix   = self.ui.lne_globCtlSuffix.text()
        jntSuffix   = self.ui.lne_globJntSuffix.text()
        localAxis   = self.ui.chk_lra.isChecked()
        skipLast    = self.ui.chk_strapSkipLast.isChecked()

        if self.ui.lne_globalSclObj.text() == '':
            globSclObj = self.ui.lne_globalSclObj.placeholderText()
        else:
            globSclObj = self.ui.lne_globalSclObj.text()

        stprg.strapRig(globalVars, jntRows, jntColumns, makeFK, ikSpline, ikSplineNum,
                ctlSuffix, jntSuffix, localAxis, skipLast, globSclObj)

    def singleCtl(self):
        if not self.ui.lne_singlesName.text():
            raise NameError('Supply a name')

        ctlNme = self.ui.lne_singlesName.text()
        ctlJnt = self.ui.chk_singleJnt.isChecked()
        globalVars = self.globalVars() #margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        
        stprg.singleCtl(globalVars, ctlNme, ctlJnt)

    def singlePatch(self):
        if not self.ui.lne_singlesName.text():
            raise NameError('Supply a name')

        ctlNme = self.ui.lne_singlesName.text()
        ctlJnt = self.ui.chk_singleJnt.isChecked()
        globalVars = self.globalVars() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        
        stprg.singlePatch(globalVars, ctlNme, ctlJnt)

    def ctlPreBindMat(self):
        '''
        Connect parents of joints to skincluster prebind matrix.

        dorLst = ([]) List of joints, and obj with skincluster as [-1]
        '''
        if cmds.ls(sl=1):
            dorLst = cmds.ls(sl=1)
        else:
            raise IndexError('Make selection of joints, then obj with skinCluster')

        jntSuffix = '_'+self.ui.cbo_preBindJoint.currentText()
        bfrSuffix = '_'+self.ui.cbo_preBindBfr.currentText()

        rigu.rdCtlPreBindMat(dorLst, jntSuffix=jntSuffix, bfrSuffix=bfrSuffix)


    def curveGuide(self):
        if cmds.ls(sl=1):
            if cmds.objectType(cmds.ls(sl=1)[0]) == 'transform':
                if cmds.objectType(omu.getDagPath(cmds.ls(sl=1)[0], shape=1)) == 'nurbsCurve':
                    bseCrv = cmds.ls(sl=1)[0]
                    if bseCrv.endswith('_gdeCrv'):
                        cnsCrv = bseCrv
                    else:
                        # Duplicate curve to remove transforms, and use as guide
                        newCrv = cmds.duplicate(cmds.ls(sl=1)[-1])
                        cmds.makeIdentity(newCrv[0], apply=True, t=1, r=1, s=1, n=0, pn=1)
                        cmds.setAttr(bseCrv+'.v', 0)
                        cmds.setAttr(newCrv[0]+'.v', 1)
                        cnsCrv = cmds.rename(newCrv, bseCrv+'_gdeCrv')
                        cmds.delete(bseCrv)
        else:
            raise TypeError('Select a nurbsCurve')

        gdeNum = self.ui.spn_gdeOnCrv.value()
        self.ikfkGde = iKfKCurve.IkFk() # Instance IkFk class to local variable
        self.ikfkGde.buildGuide(cnsCrv, gdeNum)

    def curveRig(self):
        rigTyp     = self.ui.cbo_crvRigType.currentIndex()
        globalVars = self.globalVars() # margin, ctlSize, ctlShape, ctlColor
        ctlSuffix  = self.ui.lne_globCtlSuffix.text()
        jntSuffix  = self.ui.lne_globJntSuffix.text()

        if self.ikfkGde == None:
            self.ikfkGde = iKfKCurve.IkFk() # Used for current selection

        if rigTyp == 0:
            self.ikfkGde.buildIkFkRig(ctlShape=globalVars[2], ctlSize=globalVars[1], ctlColor=globalVars[3], 
                              ctlSuffix=ctlSuffix, jntSuffix=jntSuffix)
        if rigTyp == 1:
            self.ikfkGde.buildFkRig(ctlShape=globalVars[2], ctlSize=globalVars[1], ctlColor=globalVars[3], 
                              ctlSuffix=ctlSuffix, jntSuffix=jntSuffix)

        self.ikfkGde = None


    def createOnSrf(self):
        if cmds.ls(sl=1):
            if cmds.objectType(omu.getDagPath(cmds.ls(sl=1)[0], shape=1)) != 'nurbsSurface':
                print(cmds.ls(sl=1)[0], '<'*50)
                raise TypeError('Selection is not of type nurbsSurface')
        else:
            raise IndexError('Select a nurbsSurface')

        globalVars = self.globalVars() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        gdeRow = self.ui.spn_utilRow.value()
        gdeCol = self.ui.spn_utilColumn.value()
        gdeTyp = self.ui.cbo_utilObjType.currentText()
        skpLst = self.ui.chk_srfSkipLast.isChecked()

        if globalVars[5]:
            suffix = globalVars[5]
        else:
            suffix = 'ctlGde'

        self.strpGde = strap.Strap() # Instance strap class to local variable
        self.strpGde.buildGuide(cmds.ls(sl=True)[0], gdeRow, gdeCol, objType=gdeTyp.lower(), 
                                suffix=suffix, skipLast=skpLst, constrain=0)

    def createOnCrv(self):
        if len(cmds.ls(sl=1)) == 1:
            if cmds.objectType(cmds.ls(sl=1)[0]) == 'transform':
                if cmds.objectType(omu.getDagPath(cmds.ls(sl=1)[0], shape=1)) == 'nurbsCurve':
                    bseCrv = cmds.ls(sl=1)[0]
                    if bseCrv.endswith('_gdeCrv'):
                        cnsCrv = bseCrv
                    else:
                        # Duplicate curve to remove transforms, and use as guide
                        newCrv = cmds.duplicate(cmds.ls(sl=1)[0])
                        rigu.lockUnlockSRT2(newCrv, 1, 0, t=['x','y','z'], r=['x','y','z'], s=['x','y','z'])
                        cmds.makeIdentity(newCrv[0], apply=True, t=1, r=1, s=1, n=0, pn=1)
                        cmds.setAttr(bseCrv+'.v', 0)
                        cmds.setAttr(newCrv[0]+'.v', 1)
                        cnsCrv = cmds.rename(newCrv, bseCrv+'_gdeCrv')
                        cmds.delete(bseCrv)
                else:
                    raise TypeError('Selection is not of type nurbsCurve')
            else:
                raise TypeError('Selection is not a transform')
        else:
            raise IndexError('Select a single nurbs curve')

        globalVars = self.globalVars() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        objType    = self.ui.cbo_crvNumOf.currentText()
        objFormat  = objType[:-1].lower()
        count      = self.ui.spn_crvNumOf.value()
        chain      = self.ui.chk_crvJntAsChain.isChecked()

        # Check for optional suffix
        if globalVars[5]:
            suffix = globalVars[5]
        else:
            suffix = 'gde'

        crv.createEvenAlongCrv(objFormat, cnsCrv, count, cnsCrv, chain=chain, jntAxis='xyz', keepCrv=1, suffix=suffix)

    def matchMoveAutoBuild(self):
        if not cmds.ls(sl=True): # Something needs to be selected
            raise TypeError('Make a vertex selection')
        if not cmds.filterExpand(sm=31): # Checks for vertex selection
            raise TypeError('Make a vertex selection')

        globalVars = self.globalVars() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        orient    = self.ui.chk_mmOrient.isChecked()
        duplicate = self.ui.chk_mmDorito.isChecked()

        if duplicate == True:
            duplicateEnv = 1
        else:
            duplicateEnv = 0
       
        vtxLst = cmds.ls(sl=True, flatten=True)

        vtxDic = {}
        for vtx in vtxLst:
            vtxId = re.search(r"\[([A-Za-z0-9_]+)\]", vtx) # gets vtx id in brackets (vtx[1256])
            # print(vtxId.group(1))
            mshNme = vtx.split('.')[0] # Gets obj name from vertex
            vtxDic[vtx , mshNme+'_vtx'+vtxId.group(1)] = [orient, globalVars[2], globalVars[1], globalVars[3], globalVars[4], globalVars[5]] # orient, ctlShape, ctlSize, ctlColor, ctlSuffix, jntSuffix

        rigu.rdCtlOnVtx(vtxDic, margin=globalVars[0], duplicate=duplicate, duplicateEnv=duplicateEnv)

        cmds.select(None)

    def matchPointPos(self):
        if len(cmds.ls(sl=1)) != 2:
            raise IndexError('Select Driver obj, then Driven obj')

        driver, driven = cmds.ls(sl=1)
        rigu.matchPointPosition(driver, driven)

        print('*** Done ***')

    def updateOrig(self):
        #auto update multiple.
        #select source objects
        if self.ui.chk_updateAuto.isChecked():
            if cmds.ls(sl=1):
                print('Running mesh update(s).....')
                msh.updateOrigMulti(cmds.ls(sl=1), delete=False)
            else:
                raise IndexError('Select source mesh')

        #update single selection
        else:
            if len(cmds.ls(sl=1)) != 2:
                raise IndexError('Select two objects. Source > Target')
            else:
                source = cmds.ls(sl=1)[0]
                target = cmds.ls(sl=1)[1]

            msh.autoUpdate(source, target)

        print('*** Done ***')


    def globalScaleObj(self):
        if not cmds.ls(sl=1):
            self.ui.lne_globalSclObj.setText('')
            return
        if not len(cmds.ls(sl=1))==1:
            raise IndexError('Select one object that contains a globalScale attr')
        self.ui.lne_globalSclObj.setText(cmds.ls(sl=1)[0])

    def globalScaleConnect(self, obj=None):
        if self.ui.lne_globalSclObj.text() == '':
            gblObj = self.ui.lne_globalSclObj.placeholderText()
        else:
            gblObj = self.ui.lne_globalSclObj.text()

        if not obj:
            obj = cmds.ls(sl=1)

        if cmds.objExists(gblObj):
            if cmds.attributeQuery('globalScale', node=gblObj, ex=True):
                for item in obj:
                    sclAxs = ['.sx', '.sy', '.sz']
                    [cmds.connectAttr(gblObj+'.globalScale', item+axis) for axis in sclAxs]
            else:
                cmds.warning('globalScale attribute does not exist on specified object')
        else:
            cmds.warning('Global Scale object does not exist in the scene')


    def constrainToSrf(self):
        cnsTyp = self.ui.cbo_utilConsMethod.currentIndex()
        translate = self.ui.chk_srfConTra.isChecked()
        rotate = self.ui.chk_srfConRot.isChecked()
        offset = self.ui.chk_srfPositionOffset.isChecked()
        
        if len(cmds.ls(sl=1)) > 1:
            if cmds.objectType(omu.getDagPath(cmds.ls(sl=1)[-1], shape=1))=='nurbsSurface':
                cnsSrf = cmds.ls(sl=1)[-1]
                cnsLst = cmds.ls(sl=1)
                cnsLst.pop() # Remove NurbsSurface

                if cnsTyp == 0:
                    [srf.constToSrfMatrix(obj, cnsSrf, translate=translate, rotate=rotate, offset=offset) for obj in cnsLst]
                if cnsTyp == 1:
                    [srf.constToSrfFol(obj, cnsSrf, translate=translate, rotate=rotate, offset=offset) for obj in cnsLst]
            else:
                raise TypeError('Last selection is not of type NurbsSurface')
        else:
            raise IndexError('Select at least one transform, then nurbsSurface')

    def constrainToCrv(self):
        if len(cmds.ls(sl=1)) > 1:
            if cmds.objectType(cmds.ls(sl=1)[-1])=='transform':
                if cmds.objectType(omu.getDagPath(cmds.ls(sl=1)[-1], shape=1))=='nurbsCurve':
                    cnsCrv = cmds.ls(sl=1)[-1]
                    cnsLst = cmds.ls(sl=1)
                    cnsLst.pop() # Remove NurbsCurve
                    cnsLst.sort()

                    upType = self.ui.cbo_crvConstType.currentIndex()
                    upObj  = self.ui.lne_crvUpObj.text()
                    offset = self.ui.chk_crvPositionOffset.isChecked()
                    rotate = self.ui.chk_crvPositionOnly.isChecked()
                    rotate = not rotate # Position Only
                   
                    if self.ui.chk_crvParametric.isChecked():
                        crv.consToCrvParametric(cnsLst, cnsCrv, upType=upType, inverseUp=0, 
                                                inverseFront=0, frontAxis=0, upAxis=2, upObj=upObj,
                                                offset=offset, rotate=rotate)
                    else:
                        crv.consToCrvNonParametric(cnsLst, cnsCrv, upType=upType, inverseUp=0, 
                                                inverseFront=0, frontAxis=0, upAxis=2, upObj=upObj,
                                                offset=offset, rotate=rotate)
                else:
                    raise TypeError('Last selection is not of type nurbsCurve')
            else:
                raise TypeError('Last selection is not a transform')
        else:
            raise IndexError('Select at least one transform, then nurbsCurve')

    def jntOnVtx(self):
        jntSuffix = self.ui.lne_globJntSuffix.text()
        rigu.jntOnVtx(jntSuffix)

    def setBindPose(self):
        if cmds.ls(sl=1):
            mshLst = []
            for item in cmds.ls(sl=1):
                if cmds.objectType(omu.getDagPath(item, shape=1))=='mesh':
                    mshLst.append(item)
        else:
            raise TypeError('Selected items are not of type mesh')

        if mshLst:
            mshSkn = []
            for item in mshLst:
                sknCls = skn.getSkinClusters(item)
                if sknCls:
                    mshSkn.append(item)

        if mshSkn != []:
            setAngle = self.ui.chk_bindPoseAngle.isChecked()
            for msh in mshSkn:
                skn.setBindPose(msh, setAngle)
        else:
            raise IndexError('Selection does not contain skinCluster(s)')

        print('DONE')

    def selectClstrInfl(self):
        jtsLst = []
        for item in cmds.ls(sl=1):
            sknCls = skn.getSkinClusters(item)
            if sknCls:
                jtsLst.append(skn.getSkinClusterInfluences(sknCls))
        cmds.select([jnt for jnt in jtsLst for jnt in jnt])



    def selectBySuffix(self):
        if not cmds.ls(sl=1):
            raise IndexError('Nothing selected')

        suffix = self.ui.cbo_selSuffix.currentText()
        allObj = [cmds.ls(sl=1), cmds.listRelatives(ad=True)]
        selObj = []
        for lst in allObj:
            for i in lst:
                if i.endswith('_'+suffix):
                    selObj.append(i)

        cmds.select(selObj, r=True)

    def smoothEdges(self):
        for sel in cmds.ls(sl=1):
            cmds.select(sel, r=True)
            msh.smoothEdges(sel)



if 'simpleWin' in locals():
    simpleWin.hide()

simpleWin = ControlMainWindow(parent=maya_main_window())
simpleWin.show()