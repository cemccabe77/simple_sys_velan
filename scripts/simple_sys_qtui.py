import maya.cmds as cmds
import maya.OpenMayaUI as omui
import re

from lib_python_velan.mayaRigUtils.scripts import skincluster as skn
from lib_python_velan.mayaRigUtils.scripts import rigUtils as rigu
from lib_python_velan.mayaRigUtils.scripts import surfaces as srf
from lib_python_velan.mayaRigUtils.scripts import omUtil as omu
from lib_python_velan.mayaRigUtils.scripts import curves as crv
from lib_python_velan.mayaRigUtils.scripts import meshes as msh

from lib_python_velan.mayaRigComponents.scripts import iKfKCurve
from lib_python_velan.mayaRigComponents.scripts import rdCtl as rdCtl
from lib_python_velan.mayaRigComponents.scripts import strap

from . import simple_sys_ui as customUI

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

        self.ui.btn_setCtlSize.clicked.connect(self.set_ctl_size)
        self.ui.btn_setCtlShape.clicked.connect(self.set_ctl_shape)
        self.ui.btn_setCtlColor.clicked.connect(self.set_ctl_color)
        self.ui.btn_setCtlVis.clicked.connect(self.set_ctl_visibility)

        # Attrs
        self.ui.btn_axisGo.clicked.connect(self.lock_unlock_attr)
        self.ui.btn_globalSclObj.clicked.connect(self.get_global_scale_object)
        self.ui.btn_globalScaleConnect.clicked.connect(self.global_scale_connect)
        self.ui.btn_directConnect.clicked.connect(self.direct_connect)
        self.ui.btn_createMatCon.clicked.connect(self.parent_constraint)
        self.ui.btn_delMatCon.clicked.connect(rigu.delete_parentConstraint)

        # Strap Guide
        self.ui.btn_prepSrf.clicked.connect(self.prep_surface)
        self.ui.btn_swapUV.clicked.connect(srf.surface_reverse_direction)
        self.ui.btn_goGuidesOnSrf.clicked.connect(self.strap_guide)
        # Strap Rig
        self.ui.btn_goStrapRig.clicked.connect(self.strap_rig)
        # Create on Srf
        self.ui.btn_utilPrepSrf.clicked.connect(self.prep_surface)
        self.ui.btn_utilSwapUV.clicked.connect(srf.surface_reverse_direction)
        self.ui.btn_utilCreateOnSrf.clicked.connect(self.create_on_surface)
        # Constrain to Srf
        self.ui.btn_utilConstrainToSrf.clicked.connect(self.constrain_to_surface)
        self.ui.btn_drvObjGet.clicked.connect(self.get_driver_object)
        # Build : Mesh
        self.ui.btn_meshMatchPoint.clicked.connect(self.match_point_position)
        self.ui.btn_meshUpdateOrig.clicked.connect(self.update_orig)
        # MM
        self.ui.btn_mmGo.clicked.connect(self.match_move_auto_build)
        self.ui.btn_jntOnVtx.clicked.connect(self.joint_on_vtx)
        # Curve
        self.ui.btn_crvGo.clicked.connect(self.create_on_curve)
        self.ui.btn_crvConstGo.clicked.connect(self.constrain_to_curve)
        self.ui.btn_crvUpObjGet.clicked.connect(self.get_up_object)
        # rdCtl
        self.ui.btn_ctlPreBindMat.clicked.connect(self.ctl_pre_bind_matrix)
        # IK/FK Chain
        self.ui.btn_gdeOnCrvGo.clicked.connect(self.curve_guide)
        self.ui.btn_bldCrvRigGo.clicked.connect(self.curve_rig)
        # Singles
        self.ui.btn_singleCtl.clicked.connect(self.single_control)
        self.ui.btn_singlePatch.clicked.connect(self.single_patch)
        # SKIN
        self.ui.btn_resetBindPose.clicked.connect(self.set_bind_pose)
        self.ui.btn_selectClstrInfl.clicked.connect(self.select_cluster_influences)
        self.ui.btn_importWeights.clicked.connect(skn.import_skin_weights)
        self.ui.btn_exportWeights.clicked.connect(skn.export_skin_weights)
        self.ui.btn_transferWeights.clicked.connect(lambda: [skn.transfer_weights(remove=self.ui.chk_transferWeightsRemove.isChecked())])
        self.ui.btn_selBySuffix.clicked.connect(self.select_by_suffix)
        # MISC
        self.ui.btn_delUnShp.clicked.connect(msh.delete_unused_shapes_mesh)




    def get_up_object(self):
        if len(cmds.ls(sl=1)) == 1:
            self.ui.lne_crvUpObj.setText(cmds.ls(sl=1)[0])

    def get_driver_object(self):
        if len(cmds.ls(sl=1)) == 1:
            self.ui.lne_drvObj.setText(cmds.ls(sl=1)[0])

    def global_variables(self):
        margin = self.ui.spn_globAutoColorMargin.value()
        ctl_size = self.ui.spn_globCtlSize.value()
        ctl_shape = self.ui.cbo_globCtlShape.currentText()
        ctl_suffix = self.ui.lne_globCtlSuffix.text()
        joint_suffix = self.ui.lne_globJntSuffix.text()

        # ctl_index of 0 or 1 will auto color based on worldSpace
        ctl_index = self.ui.cbo_globCtlColor.currentIndex()
        
        if ctl_index in [0,1,2]:
            ctl_color = self.ui.cbo_globCtlColor.currentIndex()
        else:
            ctl_color = self.ui.cbo_globCtlColor.currentText()

        if joint_suffix:
            joint_suffix = joint_suffix
        else:
            joint_suffix = 'bind'

        if ctl_suffix:
            ctlSfx = 'ctl_suffix'
        else:
            ctlSfx = 'anim'

        return margin, ctl_size, ctl_shape, ctl_color, ctl_suffix, joint_suffix

    def lock_unlock_attr(self):
        if cmds.ls(sl=1):
            for item in cmds.ls(sl=True):
                if cmds.objectType(item)=='transform':
                    t_list = []
                    r_list = []
                    s_list = []
                    if self.ui.chk_axisTX.isChecked():
                        t_list.append('x')
                    if self.ui.chk_axisTY.isChecked():
                        t_list.append('y')
                    if self.ui.chk_axisTZ.isChecked():
                        t_list.append('z')
                    
                    if self.ui.chk_axisRX.isChecked():
                        r_list.append('x')
                    if self.ui.chk_axisRY.isChecked():
                        r_list.append('y')
                    if self.ui.chk_axisRZ.isChecked():
                        r_list.append('z')
                    
                    if self.ui.chk_axisSX.isChecked():
                        s_list.append('x')
                    if self.ui.chk_axisSY.isChecked():
                        s_list.append('y')
                    if self.ui.chk_axisSZ.isChecked():
                        s_list.append('z')

                    attr_vis  = self.ui.cbo_hideUnhide.currentIndex()
                    attr_lock = self.ui.cbo_axisLockUnlock.currentIndex()
                    
                    for attr_list in [t_list, r_list, s_list]:
                        if attr_vis > 0:
                            rigu.hide_unhide_srt(item, attr_vis-1, t=t_list, r=r_list, s=s_list)
                        if attr_lock > 0:
                            rigu.lock_unlock_srt(item, attr_vis-1, attr_lock-1, t=t_list, r=r_list, s=s_list)

    def direct_connect(self):
        '''
        Direct connect attrs. Select driven obj(s) then driver obj
        '''
        if len(cmds.ls(sl=1)) > 1:
            axis_list = []
            source = cmds.ls(sl=1)[0]
            target = cmds.ls(sl=1)[1:]
            if self.ui.chk_axisTX.isChecked():
                axis_list.append('.tx')
            if self.ui.chk_axisTY.isChecked():
                axis_list.append('.ty')
            if self.ui.chk_axisTZ.isChecked():
                axis_list.append('.tz')
            if self.ui.chk_axisRX.isChecked():
                axis_list.append('.rx')
            if self.ui.chk_axisRY.isChecked():
                axis_list.append('.ry')
            if self.ui.chk_axisRZ.isChecked():
                axis_list.append('.rz')
            if self.ui.chk_axisSX.isChecked():
                axis_list.append('.sx')
            if self.ui.chk_axisSY.isChecked():
                axis_list.append('.sy')
            if self.ui.chk_axisSZ.isChecked():
                axis_list.append('.sz')

            for target in target:
                [cmds.connectAttr(source+axis, target+axis, f=1) for axis in axis_list]
        else:
            raise IndexError('Select driver, then driven')

    def parent_constraint(self):
        if len(cmds.ls(sl=1)) > 1:
            parent = cmds.ls(sl=1)[0]
            children  = cmds.ls(sl=1)[1:]
            t_list = []
            r_list = []
            s_list = []
            if self.ui.chk_axisTX.isChecked():
                t_list.append('x')
            if self.ui.chk_axisTY.isChecked():
                t_list.append('y')
            if self.ui.chk_axisTZ.isChecked():
                t_list.append('z')

            if self.ui.chk_axisRX.isChecked():
                r_list.append('x')
            if self.ui.chk_axisRY.isChecked():
                r_list.append('y')
            if self.ui.chk_axisRZ.isChecked():
                r_list.append('z')

            if self.ui.chk_axisSX.isChecked():
                s_list.append('x')
            if self.ui.chk_axisSY.isChecked():
                s_list.append('y')
            if self.ui.chk_axisSZ.isChecked():
                s_list.append('z')

            mo = self.ui.chk_maintainOffset.isChecked()

            for child in children:
                rigu.parentConstraint(parent, child, t=t_list, r=r_list, s=s_list, mo=mo)
        else:
            raise IndexError('Select Parent, then Child')


    def set_ctl_size(self):
        if not cmds.ls(sl=1):
            raise IndexError('Select a Control')
        
        global_variables = self.global_variables() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix

        controls = []
        for control in cmds.ls(sl=1):
            if cmds.nodeType(control)!='joint':
                pass
            else:
                ctl_suffix = control.split('_')[-1] # Get control suffix to re-instance properly
                control = rdCtl.Control(control, ctlSuffix=ctl_suffix)
                controls.append(control)

        if controls:
            for control in controls:
                control.size=global_variables[1]

    def set_ctl_shape(self):
        if not cmds.ls(sl=1):
            raise IndexError('Select a Control')

        global_variables = self.global_variables() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix

        controls = []
        for control in cmds.ls(sl=1):
            if cmds.nodeType(control)!='joint':
                pass
            else:
                ctl_suffix = control.split('_')[-1] # Get ctl suffix to re-instance properly
                control = rdCtl.Control(control, ctlSuffix=ctl_suffix)
                controls.append(control)

        if controls:
            for control in controls:
                control.shape=global_variables[2]

    def set_ctl_color(self):
        if not cmds.ls(sl=1):
            raise IndexError('Select a Control')

        global_variables = self.global_variables() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix

        controls = []
        for control in cmds.ls(sl=1):
            if cmds.nodeType(control)!='joint':
                pass
            else:
                ctl_suffix = control.split('_')[-1] # Get control suffix to re-instance properly
                ctrl = rdCtl.Control(control, ctlSuffix=ctl_suffix)
                controls.append(ctrl)

        if controls:
            for control in controls:
                rigu.rdctl_side_color(control=control, priority=global_variables[3], margin=global_variables[0])

    def set_ctl_visibility(self):
        print('set_ctl_visibility() not in use')
        '''
        if not cmds.ls(sl=1):
            raise IndexError('Select a Control')

        visIco = 'faceUI_C0_ctl'
        if not cmds.objExists(visIco):
            raise RuntimeError('Head UI Host not present in the scene. "faceUI_C0_ctl"')

        for attr in ['bodySecondaryCtls', 'bodyTertiaryCtls']:
            if not cmds.attributeQuery(attr, node=visIco, ex=True):
                raise RuntimeError('Missing Visibility attributes on faceUI_C0_ctl')
        
        global_variables  = self.global_variables() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix

        if global_variables[3] in [1,2]: # make sure ctlColor is set to Secondary or Tertiary
            visDict = {1:'bodySecondaryCtls', 2:'bodyTertiaryCtls'}
            for ctl in cmds.ls(sl=1):
                rigu.lock_unlock_srt(ctl, 0, axisLst='v') # unlock .v
                cmds.connectAttr(visIco+'.'+visDict[global_variables[3]], ctl+'.v', f=True)
                if not cmds.attributeQuery('visProp', node=ctl, ex=True):
                    cmds.addAttr(ctl, ci=True, dt='string', sn='visProp') # For reconnect vis functions
                cmds.setAttr(ctl+'.visProp', str(visDict[global_variables[3]]), type='string')
        else:
            raise RuntimeError('Select Secondary or Tertiary from Ctl Color drop down menu')
        '''
    
    def prep_surface(self):
        surfaces = []
        if cmds.ls(sl=1):
            for selection in cmds.ls(sl=1):
                if cmds.objectType(selection) != 'transform':
                    raise TypeError('Select transform of object, Not shapes or nodes')
                if cmds.objectType(omu.get_dag_path(selection, shape=1)) != 'nurbsSurface':
                    raise TypeError(f'Selection is not of type nurbsSurface >> {selection}')
                else:
                    surfaces.append(selection)

            for nurbs in surfaces:
                srf.nurb_surf_prep(nurbs)

        else:
            srf.nurb_surf_prep(create=True)

    def strap_guide(self):
        gde_row = self.ui.spn_strapGuideRow.value()
        gde_col = self.ui.spn_strapGuideColumn.value()
        skp_lst = self.ui.chk_strapSkipLast.isChecked()

        nurbs_list = []
        if cmds.ls(sl=1):
            for selection in cmds.ls(sl=1):
                if cmds.objectType(omu.get_dag_path(selection, shape=1)) == 'nurbsSurface':
                    nurbs_list.append(selection)
                else:
                    raise TypeError(f'Selection is not of type nurbsSurface >> {selection}')
        else:
            raise IndexError('Select some nurbsSurface(s)')

        if nurbs_list != []:
            for nurb in nurbs_list:
                rigu.lock_unlock_srt(nurb, attrVis=1, lock=0)
                cmds.delete(nurb, ch=True)
                guide = None
                guide = strap.Strap() # Instance strap class to local variable
                guide.build_guide(surface_name=nurb, rows=gde_row, columns=gde_col)
                guide = None
            cmds.select(nurbs_list)

    def strap_rig(self):
        '''
        global_variables = ([ ]) List of rdCtl settings (margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix)
        joint_rows = (int) Number of rows of skin joints
        joint_columns = (int) Number of columns of skin joints in each row
        make_fk = (bol) Build rdCtls in FK heirarchy with FK off switch attr
        ik_spline = (bol) Build additional IK spline down nurbs U
        ik_spline_count = (int) If > 0, create a ikSpline on dorito surface with ik_spline_count of joints
        ctl_suffix  = (str) Suffix to give to rdCtls
        joint_suffix = (str) Suffix to give to rdCtl jnts
        localAxis = (bol) Display joint local axis
        skipLast = (bol) Skip joints on nurbs end V border
        global_scale_obj = (str) Object to control global scale (looks for globalScale attr for connection)
        '''

        global_variables = self.global_variables() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        joint_rows = self.ui.spn_strapJntRow.value()
        joint_columns = self.ui.spn_strapJntColumn.value()
        make_fk = self.ui.chk_makeCtlFK.isChecked()
        ik_spline = self.ui.chk_ikSpline.isChecked()
        ik_spline_count = self.ui.spn_ikSplineNum.value()
        ctl_suffix  = self.ui.lne_globCtlSuffix.text()
        joint_suffix = self.ui.lne_globJntSuffix.text()
        local_axis = self.ui.chk_lra.isChecked()

        if self.ui.lne_globalSclObj.text() == '':
            global_scale_obj = self.ui.lne_globalSclObj.placeholderText()
        else:
            global_scale_obj = self.ui.lne_globalSclObj.text()

        nurb_list = []
        if cmds.ls(sl=1):
            for obj in cmds.ls(sl=1):
                if cmds.objectType(omu.get_dag_path(obj, shape=1)) == 'nurbsSurface':
                    nurb_list.append(obj)
                else:
                    raise TypeError(f'Selection is not of type nurbsSurface >> {obj}')
        else:
            raise IndexError('Select a nurbsSurface(s)')


        if nurb_list != []:
            for nurb in nurb_list:
                strpGde = None
                strpGde = strap.Strap()
                stpRig = strpGde.build_rig(surface_name=nurb, joint_rows=joint_rows, joint_columns=joint_columns, 
                    ctl_shape=global_variables[2], ctl_size=global_variables[1], ctl_color=global_variables[3], 
                    ctl_suffix=ctl_suffix, joint_suffix=joint_suffix, make_fk=make_fk, ik_spline=ik_spline, 
                    ik_spline_count=ik_spline_count, margin=global_variables[0], lra=local_axis) 
                    # returns srfDor[0], allCtls, ctlGrp, dorJts
                
                # ctlRef's
                # stpRig[2] = strap top group transform
                ctlRef = [i for i in cmds.listRelatives(stpRig[2], ad=True, type='transform') if i.endswith('_ctlRef')]
                if cmds.objExists(global_scale_obj):
                    if cmds.attributeQuery('globalScale', node=global_scale_obj, ex=True):
                        scale_axis = ['.sx', '.sy', '.sz']
                        for ctl in ctlRef:
                            [cmds.connectAttr(f'{global_scale_obj}.globalScale', ctl+axis) for axis in scale_axis]

                if joint_rows > 0: # dorito joints exist
                    dorito_joints = [jnt for sublist in stpRig[3] for jnt in sublist]
                    if cmds.objExists(global_scale_obj):
                        if cmds.attributeQuery('globalScale', node=global_scale_obj, ex=True):
                            scale_axis = ['.sx', '.sy', '.sz']
                            for jnt in dorito_joints:
                                [cmds.connectAttr(f'{global_scale_obj}.globalScale', jnt+axis) for axis in scale_axis]

                strpGde = None

    def single_control(self):
        if not self.ui.lne_singlesName.text():
            raise NameError('Supply a name for the single control')

        name = self.ui.lne_singlesName.text()
        ctl_joint = self.ui.chk_singleJnt.isChecked()
        global_variables = self.global_variables() #margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        
        rigu.single_control(global_variables, name, ctl_joint)

    def single_patch(self):
        if not self.ui.lne_singlesName.text():
            raise NameError('Supply a name')

        name = self.ui.lne_singlesName.text()
        ctl_joint = self.ui.chk_singleJnt.isChecked()
        global_variables = self.global_variables() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        
        rigu.single_patch(global_variables, name, ctl_joint)

    def ctl_pre_bind_matrix(self):
        '''
        Connect parents of joints to skincluster prebind matrix.

        dorito_list = ([]) List of joints, and obj with skincluster as [-1]
        '''

        if cmds.ls(sl=1):
            dorito_list = cmds.ls(sl=1)
        else:
            raise IndexError('Make selection of joints, then obj with skinCluster')

        joint_suffix = '_'+self.ui.cbo_preBindJoint.currentText()
        buffer_suffix = '_'+self.ui.cbo_preBindBfr.currentText()

        rigu.rdctl_prebind_matrix(dorito_list=dorito_list, joint_suffix=joint_suffix, buffer_suffix=buffer_suffix)


    def curve_guide(self):
        if cmds.ls(sl=1):
            if cmds.objectType(cmds.ls(sl=1)[0]) == 'transform':
                if cmds.objectType(omu.get_dag_path(cmds.ls(sl=1)[0], shape=1)) == 'nurbsCurve':
                    base_curve = cmds.ls(sl=1)[0]
                    if base_curve.endswith('_gdeCrv'):
                        constrain_curve = base_curve
                    else:
                        # Duplicate curve to remove transforms, and use as guide
                        new_curve = cmds.duplicate(cmds.ls(sl=1)[-1])
                        cmds.makeIdentity(new_curve[0], apply=True, t=1, r=1, s=1, n=0, pn=1)
                        cmds.setAttr(base_curve+'.v', 0)
                        cmds.setAttr(new_curve[0]+'.v', 1)
                        constrain_curve = cmds.rename(new_curve, f'{base_curve}_gdeCrv')
                        cmds.delete(base_curve)
        else:
            raise TypeError('Select a nurbsCurve')

        guide_count = self.ui.spn_gdeOnCrv.value()
        self.ikfkGde = iKfKCurve.IkFk() # Instance IkFk class to local variable
        self.ikfkGde.build_guide(curve_name=constrain_curve, guide_count=guide_count)

    def curve_rig(self):
        rig_type = self.ui.cbo_crvRigType.currentIndex()
        global_variables = self.global_variables() # margin, ctlSize, ctlShape, ctlColor
        ctl_suffix = self.ui.lne_globCtlSuffix.text()
        joint_suffix = self.ui.lne_globJntSuffix.text()

        if self.ikfkGde == None:
            self.ikfkGde = iKfKCurve.IkFk() # Used for current selection

        if rig_type == 0:
            self.ikfkGde.build_ik_fk_rig(ctl_shape=global_variables[2], ctl_size=global_variables[1], ctl_color=global_variables[3], 
                              ctl_suffix=ctl_suffix, joint_suffix=joint_suffix)
        if rig_type == 1:
            self.ikfkGde.build_fk_rig(ctl_shape=global_variables[2], ctl_size=global_variables[1], ctl_color=global_variables[3], 
                              ctl_suffix=ctl_suffix, joint_suffix=joint_suffix)

        self.ikfkGde = None


    def create_on_surface(self):
        if cmds.ls(sl=1):
            if cmds.objectType(omu.get_dag_path(cmds.ls(sl=1)[0], shape=1)) != 'nurbsSurface':
                raise TypeError('Selection is not of type nurbsSurface')
        else:
            raise IndexError('Select a nurbsSurface')

        surface_name = cmds.ls(sl=1)[0]
        global_variables = self.global_variables() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        guide_rows = self.ui.spn_utilRow.value()
        guide_columns = self.ui.spn_utilColumn.value()
        guide_type = self.ui.cbo_utilObjType.currentText()

        if global_variables[5]:
            suffix = global_variables[5]
        else:
            suffix = 'ctlGde'

        # Create row curves
        row_curves = []
        if guide_rows == 1:
            row_curves = [srf.curve_along_surface(surface_name=surface_name, uv='u')]
        else:
            row_curves = srf.curve_along_surface_multi(surface_name=surface_name, rows=guide_rows, uv='u')

        # Create objects along curves
        for i, curve in enumerate(row_curves):
            transform = cmds.createNode('transform', n=f'row_{str(i)}_{surface_name}')
            guides = crv.create_evenly_along_curve(object_type=guide_type.lower(), object_name=f'row_{str(i)}_{surface_name}', 
                                    count=guide_columns, curve_name=curve, chain=0, joint_axis='xyz', keep_curve=0, 
                                    suffix=suffix, radius=0.3, lra=True)
            cmds.parent(guides, transform)
            cmds.parent(transform, surface_name)

        cmds.select(surface_name)

    def create_on_curve(self):
        for obj in cmds.ls(sl=1):
            if cmds.objectType(obj) == 'transform':
                if cmds.objectType(omu.get_dag_path(obj, shape=1)) == 'nurbsCurve':
                    global_variables = self.global_variables() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
                    object_type = self.ui.cbo_crvNumOf.currentText()
                    object_format = object_type[:-1].lower()
                    count = self.ui.spn_crvNumOf.value()
                    chain = self.ui.chk_crvJntAsChain.isChecked()

                    if object_type == 'Joints':
                        suffix = 'jnt'
                    else:
                        suffix = 'loc'

                    crv.create_evenly_along_curve(object_type=object_format, object_name=f'{obj}', count=count, 
                                        curve_name=obj, chain=chain, joint_axis='xyz', keep_curve=1, suffix=suffix)

                else:
                    raise TypeError('Selection is not of type nurbsCurve')
            else:
                raise TypeError('Selection is not a transform')



    def match_move_auto_build(self):
        if not cmds.ls(sl=True):
            raise TypeError('Make a vertex selection')
        if not cmds.filterExpand(sm=31): # Checks for vertex selection
            raise TypeError('Make a vertex selection')

        global_variables = self.global_variables() # margin, ctlSize, ctlShape, ctlColor, ctlSuffix, jntSuffix
        orient    = self.ui.chk_mmOrient.isChecked()
        duplicate = self.ui.chk_mmDorito.isChecked()

        if duplicate == True:
            duplicate_skin = 1
        else:
            duplicate_skin = 0
       
        vertex_list = cmds.ls(sl=True, flatten=True)

        vertex_dict = {}
        for vtx in vertex_list:
            vertex_id = re.search(r"\[([A-Za-z0-9_]+)\]", vtx) # gets vtx id in brackets (vtx[1256])
            
            mshNme = vtx.split('.')[0] # Gets obj name from vertex
            
            vertex_dict[vtx , f'{mshNme}_vtx{vertex_id.group(1)}'] = [orient, global_variables[2], global_variables[1], 
            global_variables[3], global_variables[4], global_variables[5]] 
            # orient, ctlShape, ctlSize, ctlColor, ctlSuffix, jntSuffix

        rigu.rdctl_on_vtx(vtx_dict=vertex_dict, margin=global_variables[0], duplicate=duplicate, duplicate_skin=duplicate_skin)

        cmds.select(None)

    def match_point_position(self):
        if len(cmds.ls(sl=1)) != 2:
            raise IndexError('Select Driver object, then Driven object')

        driver, driven = cmds.ls(sl=1)
        
        rigu.match_point_position(driver, driven)

        print('*** Done ***')

    def update_orig(self):
        # update multiple selection.
        if self.ui.chk_updateAuto.isChecked():
            if cmds.ls(sl=1):
                print('Running mesh update(s).....')
                msh.update_orig_multi(new_mesh=cmds.ls(sl=1), delete=False)
            else:
                raise IndexError('Select source mesh')

        # update single selection
        else:
            if len(cmds.ls(sl=1)) != 2:
                raise IndexError('Select two objects. Source > Target')
            else:
                source = cmds.ls(sl=1)[0]
                target = cmds.ls(sl=1)[1]

            msh.auto_update(source, target)

        print('*** Done ***')


    def get_global_scale_object(self):
        if not cmds.ls(sl=1):
            self.ui.lne_globalSclObj.setText('')
            return

        if not len(cmds.ls(sl=1))==1:
            raise IndexError('Select one object that contains a globalScale attr')

        self.ui.lne_globalSclObj.setText(cmds.ls(sl=1)[0])

    def global_scale_connect(self, obj=None):
        if self.ui.lne_globalSclObj.text() == '':
            global_object = self.ui.lne_globalSclObj.placeholderText()
        else:
            global_object = self.ui.lne_globalSclObj.text()

        if not obj:
            obj = cmds.ls(sl=1)

        if cmds.objExists(global_object):
            if cmds.attributeQuery('globalScale', node=global_object, ex=True):
                for item in obj:
                    sclAxs = ['.sx', '.sy', '.sz']
                    [cmds.connectAttr(global_object+'.globalScale', item+axis) for axis in sclAxs]
            else:
                cmds.warning('globalScale attribute does not exist on specified object')
        else:
            cmds.warning('Global Scale object does not exist in the scene')


    def constrain_to_surface(self):
        constrain_type = self.ui.cbo_utilConsMethod.currentIndex()
        translate = self.ui.chk_srfConTra.isChecked()
        rotate = self.ui.chk_srfConRot.isChecked()
        offset = self.ui.chk_srfPositionOffset.isChecked()
        driver = self.ui.lne_drvObj.text()
        
        if len(cmds.ls(sl=1)) > 1:
            if cmds.objectType(omu.get_dag_path(cmds.ls(sl=1)[-1], shape=1))=='nurbsSurface':
                constrain_surface = cmds.ls(sl=1)[-1]
                constrain_list = cmds.ls(sl=1)
                constrain_list.pop() # Remove NurbsSurface

                if driver:
                    return_pos=True
                else:
                    return_pos=False

                if constrain_type == 0:
                    [srf.constrain_to_surface_matrix(object_name=obj, surface_name=constrain_surface, 
                        translate=translate, rotate=rotate, offset=offset, return_pos=return_pos, 
                        driver_obj=driver) for obj in constrain_list]
                
                if constrain_type == 1:
                    [srf.constrain_to_surface_follicle(object_name=obj, surface_name=constrain_surface, 
                        translate=translate, rotate=rotate, offset=offset, return_pos=return_pos, 
                        driver_obj=driver) for obj in constrain_list]
            else:
                raise TypeError('Last selection is not of type NurbsSurface')
        else:
            raise IndexError('Select at least one transform, then nurbsSurface')

    def constrain_to_curve(self):
        if len(cmds.ls(sl=1)) > 1:
            if cmds.objectType(cmds.ls(sl=1)[-1])=='transform':
                if cmds.objectType(omu.get_dag_path(cmds.ls(sl=1)[-1], shape=1))=='nurbsCurve':
                    constrain_curve = cmds.ls(sl=1)[-1]
                    constrain_list = cmds.ls(sl=1)
                    constrain_list.pop() # Remove NurbsCurve
                    constrain_list.sort()

                    up_type = self.ui.cbo_crvConstType.currentIndex()
                    up_object = self.ui.lne_crvUpObj.text()
                    offset = self.ui.chk_crvPositionOffset.isChecked()
                    rotate = self.ui.chk_crvPositionOnly.isChecked()
                    rotate = not rotate # Position Only
                   
                    if self.ui.chk_crvParametric.isChecked():
                        crv.constrain_to_curve_parametric(constrained=constrain_list, curve_name=constrain_curve, 
                            up_type=up_type, inverse_up=0, inverse_front=0, front_axis=0, up_axis=2, up_object=up_object,
                            offset=offset, rotate=rotate)
                    else:
                        crv.constrain_to_curve_nonparametric(constrained=constrain_list, curve_name=constrain_curve, 
                            up_type=up_type, inverse_up=0, inverse_front=0, front_axis=0, up_axis=2, up_object=up_object,
                            offset=offset, rotate=rotate)
                else:
                    raise TypeError('Last selection is not of type nurbsCurve')
            else:
                raise TypeError('Last selection is not a transform')
        else:
            raise IndexError('Select at least one transform, then nurbsCurve')

    def joint_on_vtx(self):
        rigu.joint_on_vtx(joint_suffix=self.ui.lne_globJntSuffix.text())

    def set_bind_pose(self):
        if cmds.ls(sl=1):
            mesh_list = []
            for item in cmds.ls(sl=1):
                if cmds.objectType(omu.get_dag_path(item, shape=1))=='mesh':
                    mesh_list.append(item)
        else:
            raise TypeError('Selected items are not of type mesh')

        if mesh_list:
            mesh_skin = []
            for item in mesh_list:
                skin_cluster = skn.get_skin_clusters(mesh_name=item)
                if skin_cluster:
                    mesh_skin.append(item)

        if mesh_skin != []:
            set_angle = self.ui.chk_bindPoseAngle.isChecked()
            for mesh in mesh_skin:
                skn.set_bind_pose(mesh_name=mesh, set_angle=set_angle)
        else:
            raise IndexError('Selection does not contain skinCluster(s)')

        print('DONE')

    def select_cluster_influences(self):
        joint_list = []
        for item in cmds.ls(sl=1):
            skin_cluster = skn.get_skin_clusters(mesh_name=item)
            if skin_cluster:
                joint_list.append(skn.get_skin_cluster_influences(skin_cluster=skin_cluster))
        cmds.select([jnt for jnt in joint_list for jnt in jnt])

    def select_by_suffix(self):
        if not cmds.ls(sl=1):
            raise IndexError('Nothing selected')

        suffix = self.ui.cbo_selSuffix.currentText()
        all_objects = [cmds.ls(sl=1), cmds.listRelatives(ad=True)]
        select_objects = []
        for lst in all_objects:
            for i in lst:
                if i.endswith('_'+suffix):
                    select_objects.append(i)

        cmds.select(select_objects, r=True)




if 'simpleWin' in locals():
    simpleWin.hide()

simpleWin = ControlMainWindow(parent=maya_main_window())
simpleWin.show()