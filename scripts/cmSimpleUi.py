# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Working\dev\git\simpleSys\simpleSysPy3\scripts\cmSimpleSys\cmSimpleUi.ui',
# licensing of 'D:\Working\dev\git\simpleSys\simpleSysPy3\scripts\cmSimpleSys\cmSimpleUi.ui' applies.
#
# Created: Thu Mar  6 07:29:28 2025
#      by: pyside2-uic  running on PySide2 5.15.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 607)
        MainWindow.setMinimumSize(QtCore.QSize(130, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(239, 182, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: -5 3px 0 3px;\n"
"    color:  rgb(239, 182, 0);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_70 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_70.setObjectName("gridLayout_70")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 220))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 7px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(255, 194, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: -5 3px 0 3px;\n"
"    color:  rgb(255, 194, 0);\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_56 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_56.setSpacing(3)
        self.gridLayout_56.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_56.setObjectName("gridLayout_56")
        spacerItem = QtWidgets.QSpacerItem(66, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_56.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSpacing(3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_17 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_17.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox_17.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_17)
        self.gridLayout_7.setSpacing(3)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lne_globCtlSuffix = QtWidgets.QLineEdit(self.groupBox_17)
        self.lne_globCtlSuffix.setMinimumSize(QtCore.QSize(0, 0))
        self.lne_globCtlSuffix.setAlignment(QtCore.Qt.AlignCenter)
        self.lne_globCtlSuffix.setObjectName("lne_globCtlSuffix")
        self.gridLayout_6.addWidget(self.lne_globCtlSuffix, 0, 0, 1, 1)
        self.lne_globJntSuffix = QtWidgets.QLineEdit(self.groupBox_17)
        self.lne_globJntSuffix.setMinimumSize(QtCore.QSize(0, 0))
        self.lne_globJntSuffix.setAlignment(QtCore.Qt.AlignCenter)
        self.lne_globJntSuffix.setObjectName("lne_globJntSuffix")
        self.gridLayout_6.addWidget(self.lne_globJntSuffix, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_globCtlShape = QtWidgets.QLabel(self.groupBox_17)
        self.lbl_globCtlShape.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_globCtlShape.setObjectName("lbl_globCtlShape")
        self.gridLayout_2.addWidget(self.lbl_globCtlShape, 0, 0, 1, 1)
        self.cbo_globCtlShape = QtWidgets.QComboBox(self.groupBox_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo_globCtlShape.sizePolicy().hasHeightForWidth())
        self.cbo_globCtlShape.setSizePolicy(sizePolicy)
        self.cbo_globCtlShape.setMinimumSize(QtCore.QSize(0, 0))
        self.cbo_globCtlShape.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbo_globCtlShape.setMaxVisibleItems(50)
        self.cbo_globCtlShape.setObjectName("cbo_globCtlShape")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.cbo_globCtlShape.addItem("")
        self.gridLayout_2.addWidget(self.cbo_globCtlShape, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_globCtlColor = QtWidgets.QLabel(self.groupBox_17)
        self.lbl_globCtlColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_globCtlColor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_globCtlColor.setObjectName("lbl_globCtlColor")
        self.gridLayout_4.addWidget(self.lbl_globCtlColor, 0, 0, 1, 1)
        self.cbo_globCtlColor = QtWidgets.QComboBox(self.groupBox_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo_globCtlColor.sizePolicy().hasHeightForWidth())
        self.cbo_globCtlColor.setSizePolicy(sizePolicy)
        self.cbo_globCtlColor.setMinimumSize(QtCore.QSize(0, 0))
        self.cbo_globCtlColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbo_globCtlColor.setMaxVisibleItems(50)
        self.cbo_globCtlColor.setObjectName("cbo_globCtlColor")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.cbo_globCtlColor.addItem("")
        self.gridLayout_4.addWidget(self.cbo_globCtlColor, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lbl_globCtlSize = QtWidgets.QLabel(self.groupBox_17)
        self.lbl_globCtlSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_globCtlSize.setObjectName("lbl_globCtlSize")
        self.gridLayout_5.addWidget(self.lbl_globCtlSize, 0, 0, 1, 1)
        self.spn_globCtlSize = QtWidgets.QDoubleSpinBox(self.groupBox_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spn_globCtlSize.sizePolicy().hasHeightForWidth())
        self.spn_globCtlSize.setSizePolicy(sizePolicy)
        self.spn_globCtlSize.setMinimumSize(QtCore.QSize(0, 0))
        self.spn_globCtlSize.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spn_globCtlSize.setDecimals(2)
        self.spn_globCtlSize.setMaximum(1000.0)
        self.spn_globCtlSize.setSingleStep(0.1)
        self.spn_globCtlSize.setProperty("value", 1.0)
        self.spn_globCtlSize.setObjectName("spn_globCtlSize")
        self.gridLayout_5.addWidget(self.spn_globCtlSize, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_globAutoColorMargin = QtWidgets.QLabel(self.groupBox_17)
        self.lbl_globAutoColorMargin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_globAutoColorMargin.setObjectName("lbl_globAutoColorMargin")
        self.gridLayout.addWidget(self.lbl_globAutoColorMargin, 0, 0, 1, 1)
        self.spn_globAutoColorMargin = QtWidgets.QDoubleSpinBox(self.groupBox_17)
        self.spn_globAutoColorMargin.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spn_globAutoColorMargin.setDecimals(3)
        self.spn_globAutoColorMargin.setProperty("value", 0.1)
        self.spn_globAutoColorMargin.setObjectName("spn_globAutoColorMargin")
        self.gridLayout.addWidget(self.spn_globAutoColorMargin, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 2, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_17, 0, 0, 1, 1)
        self.groupBox_31 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_31.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_31.sizePolicy().hasHeightForWidth())
        self.groupBox_31.setSizePolicy(sizePolicy)
        self.groupBox_31.setMinimumSize(QtCore.QSize(120, 0))
        self.groupBox_31.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_31.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_31.setObjectName("groupBox_31")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_31)
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_setCtlColor = QtWidgets.QPushButton(self.groupBox_31)
        self.btn_setCtlColor.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_setCtlColor.setMaximumSize(QtCore.QSize(16777215, 20))
        self.btn_setCtlColor.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(239, 182, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 195, 0);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_setCtlColor.setObjectName("btn_setCtlColor")
        self.gridLayout_3.addWidget(self.btn_setCtlColor, 0, 2, 1, 1)
        self.btn_setCtlSize = QtWidgets.QPushButton(self.groupBox_31)
        self.btn_setCtlSize.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_setCtlSize.setMaximumSize(QtCore.QSize(16777215, 20))
        self.btn_setCtlSize.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(239, 182, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 195, 0);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_setCtlSize.setObjectName("btn_setCtlSize")
        self.gridLayout_3.addWidget(self.btn_setCtlSize, 0, 0, 1, 1)
        self.btn_setCtlShape = QtWidgets.QPushButton(self.groupBox_31)
        self.btn_setCtlShape.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_setCtlShape.setMaximumSize(QtCore.QSize(16777215, 20))
        self.btn_setCtlShape.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(239, 182, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 195, 0);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_setCtlShape.setObjectName("btn_setCtlShape")
        self.gridLayout_3.addWidget(self.btn_setCtlShape, 0, 1, 1, 1)
        self.btn_setCtlVis = QtWidgets.QPushButton(self.groupBox_31)
        self.btn_setCtlVis.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_setCtlVis.setMaximumSize(QtCore.QSize(16777215, 20))
        self.btn_setCtlVis.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(239, 182, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 195, 0);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_setCtlVis.setObjectName("btn_setCtlVis")
        self.gridLayout_3.addWidget(self.btn_setCtlVis, 0, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_31, 1, 0, 1, 1)
        self.gridLayout_56.addLayout(self.gridLayout_9, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(67, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_56.addItem(spacerItem1, 0, 0, 1, 1)
        self.groupBox_35 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_35.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_35.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_35.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_35.setObjectName("groupBox_35")
        self.gridLayout_115 = QtWidgets.QGridLayout(self.groupBox_35)
        self.gridLayout_115.setSpacing(3)
        self.gridLayout_115.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_115.setObjectName("gridLayout_115")
        self.btn_selBySuffix = QtWidgets.QPushButton(self.groupBox_35)
        self.btn_selBySuffix.setMinimumSize(QtCore.QSize(180, 25))
        self.btn_selBySuffix.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(239, 182, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 195, 0);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_selBySuffix.setObjectName("btn_selBySuffix")
        self.gridLayout_115.addWidget(self.btn_selBySuffix, 0, 1, 1, 1)
        self.cbo_selSuffix = QtWidgets.QComboBox(self.groupBox_35)
        self.cbo_selSuffix.setStyleSheet("")
        self.cbo_selSuffix.setObjectName("cbo_selSuffix")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.cbo_selSuffix.addItem("")
        self.gridLayout_115.addWidget(self.cbo_selSuffix, 0, 0, 1, 1)
        self.gridLayout_56.addWidget(self.groupBox_35, 1, 1, 1, 1)
        self.gridLayout_70.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget_2.setStyleSheet("QTabBar::scroller {width: 90px; }\n"
"")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setMinimumSize(QtCore.QSize(290, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(290, 120))
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_19.setSpacing(6)
        self.gridLayout_19.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setSpacing(3)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.cbo_axisLockUnlock = QtWidgets.QComboBox(self.groupBox_3)
        self.cbo_axisLockUnlock.setObjectName("cbo_axisLockUnlock")
        self.cbo_axisLockUnlock.addItem("")
        self.cbo_axisLockUnlock.setItemText(0, "")
        self.cbo_axisLockUnlock.addItem("")
        self.cbo_axisLockUnlock.addItem("")
        self.gridLayout_17.addWidget(self.cbo_axisLockUnlock, 0, 0, 1, 1)
        self.cbo_hideUnhide = QtWidgets.QComboBox(self.groupBox_3)
        self.cbo_hideUnhide.setObjectName("cbo_hideUnhide")
        self.cbo_hideUnhide.addItem("")
        self.cbo_hideUnhide.setItemText(0, "")
        self.cbo_hideUnhide.addItem("")
        self.cbo_hideUnhide.addItem("")
        self.gridLayout_17.addWidget(self.cbo_hideUnhide, 0, 1, 1, 1)
        self.btn_axisGo = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_axisGo.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_axisGo.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_axisGo.setObjectName("btn_axisGo")
        self.gridLayout_17.addWidget(self.btn_axisGo, 1, 0, 1, 2)
        self.gridLayout_19.addLayout(self.gridLayout_17, 0, 1, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setSpacing(3)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.chk_axisTX = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_axisTX.setChecked(True)
        self.chk_axisTX.setObjectName("chk_axisTX")
        self.gridLayout_15.addWidget(self.chk_axisTX, 1, 0, 1, 1)
        self.chk_axisRZ = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_axisRZ.setChecked(True)
        self.chk_axisRZ.setObjectName("chk_axisRZ")
        self.gridLayout_15.addWidget(self.chk_axisRZ, 3, 1, 1, 1)
        self.chk_axisSY = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_axisSY.setChecked(True)
        self.chk_axisSY.setObjectName("chk_axisSY")
        self.gridLayout_15.addWidget(self.chk_axisSY, 2, 2, 1, 1)
        self.chk_axisTY = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_axisTY.setChecked(True)
        self.chk_axisTY.setObjectName("chk_axisTY")
        self.gridLayout_15.addWidget(self.chk_axisTY, 2, 0, 1, 1)
        self.chk_axisRX = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_axisRX.setChecked(True)
        self.chk_axisRX.setObjectName("chk_axisRX")
        self.gridLayout_15.addWidget(self.chk_axisRX, 1, 1, 1, 1)
        self.chk_axisSX = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_axisSX.setChecked(True)
        self.chk_axisSX.setObjectName("chk_axisSX")
        self.gridLayout_15.addWidget(self.chk_axisSX, 1, 2, 1, 1)
        self.chk_axisRY = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_axisRY.setChecked(True)
        self.chk_axisRY.setObjectName("chk_axisRY")
        self.gridLayout_15.addWidget(self.chk_axisRY, 2, 1, 1, 1)
        self.chk_axisSZ = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_axisSZ.setChecked(True)
        self.chk_axisSZ.setObjectName("chk_axisSZ")
        self.gridLayout_15.addWidget(self.chk_axisSZ, 3, 2, 1, 1)
        self.chk_axisTZ = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_axisTZ.setChecked(True)
        self.chk_axisTZ.setObjectName("chk_axisTZ")
        self.gridLayout_15.addWidget(self.chk_axisTZ, 3, 0, 1, 1)
        self.chk_T = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_T.setStyleSheet("QCheckBox { color: rgb(239, 182, 0) };")
        self.chk_T.setChecked(True)
        self.chk_T.setObjectName("chk_T")
        self.gridLayout_15.addWidget(self.chk_T, 0, 0, 1, 1)
        self.chk_R = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_R.setStyleSheet("QCheckBox { color: rgb(239, 182, 0) };")
        self.chk_R.setChecked(True)
        self.chk_R.setObjectName("chk_R")
        self.gridLayout_15.addWidget(self.chk_R, 0, 1, 1, 1)
        self.chk_S = QtWidgets.QCheckBox(self.groupBox_3)
        self.chk_S.setStyleSheet("QCheckBox { color: rgb(239, 182, 0) };")
        self.chk_S.setChecked(True)
        self.chk_S.setObjectName("chk_S")
        self.gridLayout_15.addWidget(self.chk_S, 0, 2, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_15, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_38 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_38.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_38.sizePolicy().hasHeightForWidth())
        self.groupBox_38.setSizePolicy(sizePolicy)
        self.groupBox_38.setMinimumSize(QtCore.QSize(290, 0))
        self.groupBox_38.setMaximumSize(QtCore.QSize(290, 94))
        self.groupBox_38.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_38.setObjectName("groupBox_38")
        self.gridLayout_111 = QtWidgets.QGridLayout(self.groupBox_38)
        self.gridLayout_111.setSpacing(3)
        self.gridLayout_111.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_111.setObjectName("gridLayout_111")
        self.gridLayout_112 = QtWidgets.QGridLayout()
        self.gridLayout_112.setObjectName("gridLayout_112")
        self.chk_maintainOffset = QtWidgets.QCheckBox(self.groupBox_38)
        self.chk_maintainOffset.setMaximumSize(QtCore.QSize(50, 16777215))
        self.chk_maintainOffset.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chk_maintainOffset.setChecked(True)
        self.chk_maintainOffset.setObjectName("chk_maintainOffset")
        self.gridLayout_112.addWidget(self.chk_maintainOffset, 0, 0, 1, 1)
        self.btn_createMatCon = QtWidgets.QPushButton(self.groupBox_38)
        self.btn_createMatCon.setMinimumSize(QtCore.QSize(120, 25))
        self.btn_createMatCon.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_createMatCon.setObjectName("btn_createMatCon")
        self.gridLayout_112.addWidget(self.btn_createMatCon, 0, 1, 1, 1)
        self.btn_delMatCon = QtWidgets.QPushButton(self.groupBox_38)
        self.btn_delMatCon.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_delMatCon.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_delMatCon.setObjectName("btn_delMatCon")
        self.gridLayout_112.addWidget(self.btn_delMatCon, 1, 0, 1, 2)
        self.gridLayout_111.addLayout(self.gridLayout_112, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_38, 1, 0, 1, 1)
        self.groupBox_36 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_36.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_36.sizePolicy().hasHeightForWidth())
        self.groupBox_36.setSizePolicy(sizePolicy)
        self.groupBox_36.setMinimumSize(QtCore.QSize(290, 0))
        self.groupBox_36.setMaximumSize(QtCore.QSize(290, 125))
        self.groupBox_36.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_36.setObjectName("groupBox_36")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_36)
        self.gridLayout_11.setSpacing(3)
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.btn_globalSclObj = QtWidgets.QPushButton(self.groupBox_36)
        self.btn_globalSclObj.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_globalSclObj.setObjectName("btn_globalSclObj")
        self.gridLayout_16.addWidget(self.btn_globalSclObj, 0, 1, 1, 1)
        self.btn_globalScaleConnect = QtWidgets.QPushButton(self.groupBox_36)
        self.btn_globalScaleConnect.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_globalScaleConnect.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_globalScaleConnect.setObjectName("btn_globalScaleConnect")
        self.gridLayout_16.addWidget(self.btn_globalScaleConnect, 2, 0, 1, 2)
        self.btn_directConnect = QtWidgets.QPushButton(self.groupBox_36)
        self.btn_directConnect.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_directConnect.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_directConnect.setObjectName("btn_directConnect")
        self.gridLayout_16.addWidget(self.btn_directConnect, 1, 0, 1, 2)
        self.lne_globalSclObj = QtWidgets.QLineEdit(self.groupBox_36)
        self.lne_globalSclObj.setObjectName("lne_globalSclObj")
        self.gridLayout_16.addWidget(self.lne_globalSclObj, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_36, 2, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 247, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.gridLayout_39 = QtWidgets.QGridLayout()
        self.gridLayout_39.setObjectName("gridLayout_39")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_39.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout_30 = QtWidgets.QGridLayout()
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.groupBox_22 = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox_22.setMinimumSize(QtCore.QSize(300, 75))
        self.groupBox_22.setMaximumSize(QtCore.QSize(300, 75))
        self.groupBox_22.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_22.setObjectName("groupBox_22")
        self.gridLayout_92 = QtWidgets.QGridLayout(self.groupBox_22)
        self.gridLayout_92.setSpacing(3)
        self.gridLayout_92.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_92.setObjectName("gridLayout_92")
        self.gridLayout_91 = QtWidgets.QGridLayout()
        self.gridLayout_91.setSpacing(3)
        self.gridLayout_91.setObjectName("gridLayout_91")
        self.btn_importWeights = QtWidgets.QPushButton(self.groupBox_22)
        self.btn_importWeights.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_importWeights.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_importWeights.setObjectName("btn_importWeights")
        self.gridLayout_91.addWidget(self.btn_importWeights, 0, 0, 1, 1)
        self.btn_exportWeights = QtWidgets.QPushButton(self.groupBox_22)
        self.btn_exportWeights.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_exportWeights.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_exportWeights.setObjectName("btn_exportWeights")
        self.gridLayout_91.addWidget(self.btn_exportWeights, 0, 1, 1, 1)
        self.gridLayout_92.addLayout(self.gridLayout_91, 0, 0, 1, 1)
        self.btn_selectClstrInfl = QtWidgets.QPushButton(self.groupBox_22)
        self.btn_selectClstrInfl.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_selectClstrInfl.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_selectClstrInfl.setObjectName("btn_selectClstrInfl")
        self.gridLayout_92.addWidget(self.btn_selectClstrInfl, 1, 0, 1, 1)
        self.gridLayout_30.addWidget(self.groupBox_22, 0, 0, 1, 1)
        self.groupBox_40 = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox_40.setMinimumSize(QtCore.QSize(300, 50))
        self.groupBox_40.setMaximumSize(QtCore.QSize(300, 50))
        self.groupBox_40.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_40.setObjectName("groupBox_40")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_40)
        self.gridLayout_14.setSpacing(3)
        self.gridLayout_14.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_47 = QtWidgets.QGridLayout()
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.btn_transferWeights = QtWidgets.QPushButton(self.groupBox_40)
        self.btn_transferWeights.setMinimumSize(QtCore.QSize(160, 25))
        self.btn_transferWeights.setMaximumSize(QtCore.QSize(160, 16777215))
        self.btn_transferWeights.setStatusTip("")
        self.btn_transferWeights.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_transferWeights.setObjectName("btn_transferWeights")
        self.gridLayout_47.addWidget(self.btn_transferWeights, 0, 0, 1, 1)
        self.chk_transferWeightsRemove = QtWidgets.QCheckBox(self.groupBox_40)
        self.chk_transferWeightsRemove.setObjectName("chk_transferWeightsRemove")
        self.gridLayout_47.addWidget(self.chk_transferWeightsRemove, 0, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_47, 0, 0, 1, 1)
        self.gridLayout_30.addWidget(self.groupBox_40, 1, 0, 1, 1)
        self.groupBox_20 = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox_20.setMinimumSize(QtCore.QSize(300, 80))
        self.groupBox_20.setMaximumSize(QtCore.QSize(300, 80))
        self.groupBox_20.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_71 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_71.setSpacing(3)
        self.gridLayout_71.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_71.setObjectName("gridLayout_71")
        self.gridLayout_68 = QtWidgets.QGridLayout()
        self.gridLayout_68.setObjectName("gridLayout_68")
        self.cbo_preBindJoint = QtWidgets.QComboBox(self.groupBox_20)
        self.cbo_preBindJoint.setObjectName("cbo_preBindJoint")
        self.cbo_preBindJoint.addItem("")
        self.cbo_preBindJoint.addItem("")
        self.gridLayout_68.addWidget(self.cbo_preBindJoint, 0, 0, 1, 1)
        self.cbo_preBindBfr = QtWidgets.QComboBox(self.groupBox_20)
        self.cbo_preBindBfr.setObjectName("cbo_preBindBfr")
        self.cbo_preBindBfr.addItem("")
        self.cbo_preBindBfr.addItem("")
        self.cbo_preBindBfr.addItem("")
        self.gridLayout_68.addWidget(self.cbo_preBindBfr, 0, 1, 1, 1)
        self.btn_ctlPreBindMat = QtWidgets.QPushButton(self.groupBox_20)
        self.btn_ctlPreBindMat.setEnabled(True)
        self.btn_ctlPreBindMat.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_ctlPreBindMat.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_ctlPreBindMat.setObjectName("btn_ctlPreBindMat")
        self.gridLayout_68.addWidget(self.btn_ctlPreBindMat, 1, 0, 1, 2)
        self.gridLayout_71.addLayout(self.gridLayout_68, 0, 0, 1, 1)
        self.gridLayout_30.addWidget(self.groupBox_20, 2, 0, 1, 1)
        self.groupBox_43 = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox_43.setMinimumSize(QtCore.QSize(300, 50))
        self.groupBox_43.setMaximumSize(QtCore.QSize(300, 50))
        self.groupBox_43.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_43.setObjectName("groupBox_43")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.groupBox_43)
        self.gridLayout_29.setSpacing(3)
        self.gridLayout_29.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.gridLayout_67 = QtWidgets.QGridLayout()
        self.gridLayout_67.setObjectName("gridLayout_67")
        self.btn_resetBindPose = QtWidgets.QPushButton(self.groupBox_43)
        self.btn_resetBindPose.setMinimumSize(QtCore.QSize(160, 25))
        self.btn_resetBindPose.setMaximumSize(QtCore.QSize(160, 16777215))
        self.btn_resetBindPose.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_resetBindPose.setObjectName("btn_resetBindPose")
        self.gridLayout_67.addWidget(self.btn_resetBindPose, 0, 0, 1, 1)
        self.chk_bindPoseAngle = QtWidgets.QCheckBox(self.groupBox_43)
        self.chk_bindPoseAngle.setObjectName("chk_bindPoseAngle")
        self.gridLayout_67.addWidget(self.chk_bindPoseAngle, 0, 1, 1, 1)
        self.gridLayout_29.addLayout(self.gridLayout_67, 0, 0, 1, 1)
        self.gridLayout_30.addWidget(self.groupBox_43, 3, 0, 1, 1)
        self.gridLayout_39.addLayout(self.gridLayout_30, 0, 0, 1, 1)
        self.gridLayout_42.addLayout(self.gridLayout_39, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.gridLayout_48 = QtWidgets.QGridLayout()
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.groupBox_39 = QtWidgets.QGroupBox(self.tab_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_39.sizePolicy().hasHeightForWidth())
        self.groupBox_39.setSizePolicy(sizePolicy)
        self.groupBox_39.setMinimumSize(QtCore.QSize(250, 80))
        self.groupBox_39.setMaximumSize(QtCore.QSize(250, 80))
        self.groupBox_39.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_39.setObjectName("groupBox_39")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.groupBox_39)
        self.gridLayout_31.setSpacing(3)
        self.gridLayout_31.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.gridLayout_28 = QtWidgets.QGridLayout()
        self.gridLayout_28.setSpacing(3)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.btn_meshUpdateOrig = QtWidgets.QPushButton(self.groupBox_39)
        self.btn_meshUpdateOrig.setMinimumSize(QtCore.QSize(110, 25))
        self.btn_meshUpdateOrig.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_meshUpdateOrig.setObjectName("btn_meshUpdateOrig")
        self.gridLayout_28.addWidget(self.btn_meshUpdateOrig, 0, 0, 1, 1)
        self.chk_updateAuto = QtWidgets.QCheckBox(self.groupBox_39)
        self.chk_updateAuto.setEnabled(True)
        self.chk_updateAuto.setMaximumSize(QtCore.QSize(70, 16777215))
        self.chk_updateAuto.setChecked(False)
        self.chk_updateAuto.setObjectName("chk_updateAuto")
        self.gridLayout_28.addWidget(self.chk_updateAuto, 0, 1, 1, 1)
        self.btn_meshMatchPoint = QtWidgets.QPushButton(self.groupBox_39)
        self.btn_meshMatchPoint.setMinimumSize(QtCore.QSize(110, 25))
        self.btn_meshMatchPoint.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_meshMatchPoint.setObjectName("btn_meshMatchPoint")
        self.gridLayout_28.addWidget(self.btn_meshMatchPoint, 1, 0, 1, 2)
        self.gridLayout_31.addLayout(self.gridLayout_28, 0, 0, 1, 1)
        self.gridLayout_48.addWidget(self.groupBox_39, 0, 0, 1, 1)
        self.groupBox_44 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_44.setMinimumSize(QtCore.QSize(250, 120))
        self.groupBox_44.setMaximumSize(QtCore.QSize(250, 120))
        self.groupBox_44.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_44.setObjectName("groupBox_44")
        self.gridLayout_121 = QtWidgets.QGridLayout(self.groupBox_44)
        self.gridLayout_121.setSpacing(3)
        self.gridLayout_121.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_121.setObjectName("gridLayout_121")
        self.gridLayout_32 = QtWidgets.QGridLayout()
        self.gridLayout_32.setSpacing(3)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.btn_delUnShp = QtWidgets.QPushButton(self.groupBox_44)
        self.btn_delUnShp.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_delUnShp.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_delUnShp.setObjectName("btn_delUnShp")
        self.gridLayout_32.addWidget(self.btn_delUnShp, 1, 0, 1, 1)
        self.btn_smoothEdges = QtWidgets.QPushButton(self.groupBox_44)
        self.btn_smoothEdges.setEnabled(True)
        self.btn_smoothEdges.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_smoothEdges.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_smoothEdges.setObjectName("btn_smoothEdges")
        self.gridLayout_32.addWidget(self.btn_smoothEdges, 0, 0, 1, 1)
        self.gridLayout_121.addLayout(self.gridLayout_32, 0, 0, 1, 1)
        self.gridLayout_48.addWidget(self.groupBox_44, 1, 0, 1, 1)
        self.gridLayout_50.addLayout(self.gridLayout_48, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 295, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_50.addItem(spacerItem4, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_51.setObjectName("gridLayout_51")
        spacerItem5 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_51.addItem(spacerItem5, 0, 0, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.grp_strapGuide = QtWidgets.QGroupBox(self.tab_5)
        self.grp_strapGuide.setEnabled(True)
        self.grp_strapGuide.setMinimumSize(QtCore.QSize(0, 0))
        self.grp_strapGuide.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.grp_strapGuide.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.grp_strapGuide.setObjectName("grp_strapGuide")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.grp_strapGuide)
        self.gridLayout_41.setSpacing(6)
        self.gridLayout_41.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.gridLayout_40 = QtWidgets.QGridLayout()
        self.gridLayout_40.setSpacing(3)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.btn_prepSrf = QtWidgets.QPushButton(self.grp_strapGuide)
        self.btn_prepSrf.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_prepSrf.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_prepSrf.setObjectName("btn_prepSrf")
        self.gridLayout_40.addWidget(self.btn_prepSrf, 0, 0, 1, 2)
        self.btn_swapUV = QtWidgets.QPushButton(self.grp_strapGuide)
        self.btn_swapUV.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_swapUV.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_swapUV.setObjectName("btn_swapUV")
        self.gridLayout_40.addWidget(self.btn_swapUV, 0, 2, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.grp_strapGuide)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_40.addWidget(self.line_3, 1, 0, 1, 4)
        self.spn_strapGuideRow = QtWidgets.QSpinBox(self.grp_strapGuide)
        self.spn_strapGuideRow.setMinimumSize(QtCore.QSize(75, 20))
        self.spn_strapGuideRow.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spn_strapGuideRow.setMinimum(1)
        self.spn_strapGuideRow.setProperty("value", 1)
        self.spn_strapGuideRow.setObjectName("spn_strapGuideRow")
        self.gridLayout_40.addWidget(self.spn_strapGuideRow, 2, 0, 1, 1)
        self.lbl_strapGuideRow = QtWidgets.QLabel(self.grp_strapGuide)
        self.lbl_strapGuideRow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_strapGuideRow.setObjectName("lbl_strapGuideRow")
        self.gridLayout_40.addWidget(self.lbl_strapGuideRow, 2, 1, 1, 1)
        self.spn_strapGuideColumn = QtWidgets.QSpinBox(self.grp_strapGuide)
        self.spn_strapGuideColumn.setMinimumSize(QtCore.QSize(75, 20))
        self.spn_strapGuideColumn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spn_strapGuideColumn.setMinimum(1)
        self.spn_strapGuideColumn.setProperty("value", 5)
        self.spn_strapGuideColumn.setObjectName("spn_strapGuideColumn")
        self.gridLayout_40.addWidget(self.spn_strapGuideColumn, 2, 2, 1, 1)
        self.lbl_strapGuideColumn = QtWidgets.QLabel(self.grp_strapGuide)
        self.lbl_strapGuideColumn.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_strapGuideColumn.setObjectName("lbl_strapGuideColumn")
        self.gridLayout_40.addWidget(self.lbl_strapGuideColumn, 2, 3, 1, 1)
        self.line_18 = QtWidgets.QFrame(self.grp_strapGuide)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.gridLayout_40.addWidget(self.line_18, 3, 0, 1, 4)
        self.chk_strapSkipLast = QtWidgets.QCheckBox(self.grp_strapGuide)
        self.chk_strapSkipLast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chk_strapSkipLast.setChecked(False)
        self.chk_strapSkipLast.setObjectName("chk_strapSkipLast")
        self.gridLayout_40.addWidget(self.chk_strapSkipLast, 4, 0, 1, 2)
        self.btn_goGuidesOnSrf = QtWidgets.QPushButton(self.grp_strapGuide)
        self.btn_goGuidesOnSrf.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_goGuidesOnSrf.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_goGuidesOnSrf.setObjectName("btn_goGuidesOnSrf")
        self.gridLayout_40.addWidget(self.btn_goGuidesOnSrf, 4, 2, 1, 2)
        self.gridLayout_41.addLayout(self.gridLayout_40, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.grp_strapGuide, 0, 0, 1, 1)
        self.grp_strapRig = QtWidgets.QGroupBox(self.tab_5)
        self.grp_strapRig.setEnabled(True)
        self.grp_strapRig.setMinimumSize(QtCore.QSize(0, 0))
        self.grp_strapRig.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.grp_strapRig.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.grp_strapRig.setAlignment(QtCore.Qt.AlignCenter)
        self.grp_strapRig.setObjectName("grp_strapRig")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.grp_strapRig)
        self.gridLayout_45.setSpacing(6)
        self.gridLayout_45.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.gridLayout_44 = QtWidgets.QGridLayout()
        self.gridLayout_44.setSpacing(3)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.spn_strapJntRow = QtWidgets.QSpinBox(self.grp_strapRig)
        self.spn_strapJntRow.setMinimumSize(QtCore.QSize(50, 20))
        self.spn_strapJntRow.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spn_strapJntRow.setMinimum(0)
        self.spn_strapJntRow.setMaximum(1000)
        self.spn_strapJntRow.setProperty("value", 0)
        self.spn_strapJntRow.setObjectName("spn_strapJntRow")
        self.gridLayout_44.addWidget(self.spn_strapJntRow, 0, 0, 1, 1)
        self.lbl_strapJntRow_3 = QtWidgets.QLabel(self.grp_strapRig)
        self.lbl_strapJntRow_3.setObjectName("lbl_strapJntRow_3")
        self.gridLayout_44.addWidget(self.lbl_strapJntRow_3, 0, 1, 1, 2)
        self.spn_strapJntColumn = QtWidgets.QSpinBox(self.grp_strapRig)
        self.spn_strapJntColumn.setMinimumSize(QtCore.QSize(50, 20))
        self.spn_strapJntColumn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spn_strapJntColumn.setMinimum(1)
        self.spn_strapJntColumn.setMaximum(1000)
        self.spn_strapJntColumn.setProperty("value", 10)
        self.spn_strapJntColumn.setObjectName("spn_strapJntColumn")
        self.gridLayout_44.addWidget(self.spn_strapJntColumn, 0, 3, 1, 1)
        self.lbl_strapJntColumn_2 = QtWidgets.QLabel(self.grp_strapRig)
        self.lbl_strapJntColumn_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_strapJntColumn_2.setObjectName("lbl_strapJntColumn_2")
        self.gridLayout_44.addWidget(self.lbl_strapJntColumn_2, 0, 4, 1, 1)
        self.line_23 = QtWidgets.QFrame(self.grp_strapRig)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.gridLayout_44.addWidget(self.line_23, 1, 0, 1, 5)
        self.spn_ikSplineNum = QtWidgets.QSpinBox(self.grp_strapRig)
        self.spn_ikSplineNum.setEnabled(False)
        self.spn_ikSplineNum.setMinimumSize(QtCore.QSize(50, 20))
        self.spn_ikSplineNum.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spn_ikSplineNum.setProperty("value", 10)
        self.spn_ikSplineNum.setObjectName("spn_ikSplineNum")
        self.gridLayout_44.addWidget(self.spn_ikSplineNum, 2, 3, 1, 1)
        self.lbl_ikSplineNo_2 = QtWidgets.QLabel(self.grp_strapRig)
        self.lbl_ikSplineNo_2.setEnabled(True)
        self.lbl_ikSplineNo_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_ikSplineNo_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_ikSplineNo_2.setObjectName("lbl_ikSplineNo_2")
        self.gridLayout_44.addWidget(self.lbl_ikSplineNo_2, 2, 4, 1, 1)
        self.line_24 = QtWidgets.QFrame(self.grp_strapRig)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.gridLayout_44.addWidget(self.line_24, 3, 0, 1, 5)
        self.chk_makeCtlFK = QtWidgets.QCheckBox(self.grp_strapRig)
        self.chk_makeCtlFK.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chk_makeCtlFK.setChecked(True)
        self.chk_makeCtlFK.setObjectName("chk_makeCtlFK")
        self.gridLayout_44.addWidget(self.chk_makeCtlFK, 4, 0, 1, 2)
        self.chk_lra = QtWidgets.QCheckBox(self.grp_strapRig)
        self.chk_lra.setChecked(False)
        self.chk_lra.setObjectName("chk_lra")
        self.gridLayout_44.addWidget(self.chk_lra, 4, 2, 1, 3)
        self.line_17 = QtWidgets.QFrame(self.grp_strapRig)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_44.addWidget(self.line_17, 5, 0, 1, 5)
        self.btn_goStrapRig = QtWidgets.QPushButton(self.grp_strapRig)
        self.btn_goStrapRig.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_goStrapRig.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_goStrapRig.setObjectName("btn_goStrapRig")
        self.gridLayout_44.addWidget(self.btn_goStrapRig, 6, 0, 1, 5)
        self.chk_ikSpline = QtWidgets.QCheckBox(self.grp_strapRig)
        self.chk_ikSpline.setObjectName("chk_ikSpline")
        self.gridLayout_44.addWidget(self.chk_ikSpline, 2, 0, 1, 3)
        self.gridLayout_45.addLayout(self.gridLayout_44, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.grp_strapRig, 0, 1, 1, 1)
        self.gridLayout_51.addLayout(self.gridLayout_18, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(27, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_51.addItem(spacerItem6, 0, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 449, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_51.addItem(spacerItem7, 1, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_52 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem8, 0, 0, 1, 1)
        self.groupBox_24 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_24.setEnabled(True)
        self.groupBox_24.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_24.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_24.setObjectName("groupBox_24")
        self.gridLayout_124 = QtWidgets.QGridLayout(self.groupBox_24)
        self.gridLayout_124.setSpacing(6)
        self.gridLayout_124.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_124.setObjectName("gridLayout_124")
        self.gridLayout_125 = QtWidgets.QGridLayout()
        self.gridLayout_125.setObjectName("gridLayout_125")
        self.spn_gdeOnCrv = QtWidgets.QSpinBox(self.groupBox_24)
        self.spn_gdeOnCrv.setMinimumSize(QtCore.QSize(75, 0))
        self.spn_gdeOnCrv.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spn_gdeOnCrv.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_gdeOnCrv.setMinimum(2)
        self.spn_gdeOnCrv.setMaximum(1000)
        self.spn_gdeOnCrv.setProperty("value", 2)
        self.spn_gdeOnCrv.setObjectName("spn_gdeOnCrv")
        self.gridLayout_125.addWidget(self.spn_gdeOnCrv, 0, 0, 1, 1)
        self.btn_gdeOnCrvGo = QtWidgets.QPushButton(self.groupBox_24)
        self.btn_gdeOnCrvGo.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_gdeOnCrvGo.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_gdeOnCrvGo.setObjectName("btn_gdeOnCrvGo")
        self.gridLayout_125.addWidget(self.btn_gdeOnCrvGo, 0, 1, 1, 1)
        self.gridLayout_124.addLayout(self.gridLayout_125, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_24, 0, 1, 1, 1)
        self.groupBox_27 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_27.setEnabled(True)
        self.groupBox_27.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_27.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_27.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_27.setObjectName("groupBox_27")
        self.gridLayout_126 = QtWidgets.QGridLayout(self.groupBox_27)
        self.gridLayout_126.setSpacing(6)
        self.gridLayout_126.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_126.setObjectName("gridLayout_126")
        self.gridLayout_127 = QtWidgets.QGridLayout()
        self.gridLayout_127.setObjectName("gridLayout_127")
        self.cbo_crvRigType = QtWidgets.QComboBox(self.groupBox_27)
        self.cbo_crvRigType.setEnabled(True)
        self.cbo_crvRigType.setAutoFillBackground(False)
        self.cbo_crvRigType.setObjectName("cbo_crvRigType")
        self.cbo_crvRigType.addItem("")
        self.cbo_crvRigType.addItem("")
        self.gridLayout_127.addWidget(self.cbo_crvRigType, 0, 0, 1, 1)
        self.btn_bldCrvRigGo = QtWidgets.QPushButton(self.groupBox_27)
        self.btn_bldCrvRigGo.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_bldCrvRigGo.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_bldCrvRigGo.setObjectName("btn_bldCrvRigGo")
        self.gridLayout_127.addWidget(self.btn_bldCrvRigGo, 0, 1, 1, 1)
        self.gridLayout_126.addLayout(self.gridLayout_127, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_27, 0, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem9, 0, 3, 1, 1)
        self.gridLayout_52.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 536, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_52.addItem(spacerItem10, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_13.setMinimumSize(QtCore.QSize(400, 90))
        self.groupBox_13.setMaximumSize(QtCore.QSize(400, 90))
        self.groupBox_13.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_65 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_65.setSpacing(5)
        self.gridLayout_65.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_65.setObjectName("gridLayout_65")
        self.gridLayout_77 = QtWidgets.QGridLayout()
        self.gridLayout_77.setSpacing(3)
        self.gridLayout_77.setObjectName("gridLayout_77")
        self.gridLayout_83 = QtWidgets.QGridLayout()
        self.gridLayout_83.setSpacing(3)
        self.gridLayout_83.setObjectName("gridLayout_83")
        self.btn_utilPrepSrf = QtWidgets.QPushButton(self.groupBox_13)
        self.btn_utilPrepSrf.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_utilPrepSrf.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_utilPrepSrf.setObjectName("btn_utilPrepSrf")
        self.gridLayout_83.addWidget(self.btn_utilPrepSrf, 0, 0, 1, 1)
        self.btn_utilSwapUV = QtWidgets.QPushButton(self.groupBox_13)
        self.btn_utilSwapUV.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_utilSwapUV.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_utilSwapUV.setObjectName("btn_utilSwapUV")
        self.gridLayout_83.addWidget(self.btn_utilSwapUV, 1, 0, 1, 1)
        self.gridLayout_77.addLayout(self.gridLayout_83, 0, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.groupBox_13)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_77.addWidget(self.line_6, 0, 1, 1, 1)
        self.gridLayout_86 = QtWidgets.QGridLayout()
        self.gridLayout_86.setObjectName("gridLayout_86")
        self.cbo_utilObjType = QtWidgets.QComboBox(self.groupBox_13)
        self.cbo_utilObjType.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbo_utilObjType.setObjectName("cbo_utilObjType")
        self.cbo_utilObjType.addItem("")
        self.cbo_utilObjType.addItem("")
        self.gridLayout_86.addWidget(self.cbo_utilObjType, 0, 0, 1, 1)
        self.gridLayout_88 = QtWidgets.QGridLayout()
        self.gridLayout_88.setSpacing(3)
        self.gridLayout_88.setObjectName("gridLayout_88")
        self.gridLayout_89 = QtWidgets.QGridLayout()
        self.gridLayout_89.setObjectName("gridLayout_89")
        self.spn_utilRow = QtWidgets.QSpinBox(self.groupBox_13)
        self.spn_utilRow.setMinimumSize(QtCore.QSize(75, 0))
        self.spn_utilRow.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spn_utilRow.setMinimum(1)
        self.spn_utilRow.setMaximum(500)
        self.spn_utilRow.setProperty("value", 1)
        self.spn_utilRow.setObjectName("spn_utilRow")
        self.gridLayout_89.addWidget(self.spn_utilRow, 0, 0, 1, 1)
        self.lbl_utilRow = QtWidgets.QLabel(self.groupBox_13)
        self.lbl_utilRow.setObjectName("lbl_utilRow")
        self.gridLayout_89.addWidget(self.lbl_utilRow, 0, 1, 1, 1)
        self.gridLayout_88.addLayout(self.gridLayout_89, 0, 0, 1, 1)
        self.gridLayout_94 = QtWidgets.QGridLayout()
        self.gridLayout_94.setObjectName("gridLayout_94")
        self.spn_utilColumn = QtWidgets.QSpinBox(self.groupBox_13)
        self.spn_utilColumn.setMinimumSize(QtCore.QSize(75, 0))
        self.spn_utilColumn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spn_utilColumn.setMinimum(1)
        self.spn_utilColumn.setMaximum(500)
        self.spn_utilColumn.setProperty("value", 1)
        self.spn_utilColumn.setObjectName("spn_utilColumn")
        self.gridLayout_94.addWidget(self.spn_utilColumn, 0, 0, 1, 1)
        self.lbl_utilColumn = QtWidgets.QLabel(self.groupBox_13)
        self.lbl_utilColumn.setObjectName("lbl_utilColumn")
        self.gridLayout_94.addWidget(self.lbl_utilColumn, 0, 1, 1, 1)
        self.gridLayout_88.addLayout(self.gridLayout_94, 1, 0, 1, 1)
        self.gridLayout_86.addLayout(self.gridLayout_88, 1, 0, 1, 1)
        self.gridLayout_77.addLayout(self.gridLayout_86, 0, 2, 1, 1)
        self.line_25 = QtWidgets.QFrame(self.groupBox_13)
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.gridLayout_77.addWidget(self.line_25, 0, 3, 1, 1)
        self.gridLayout_99 = QtWidgets.QGridLayout()
        self.gridLayout_99.setSpacing(3)
        self.gridLayout_99.setObjectName("gridLayout_99")
        self.chk_srfSkipLast = QtWidgets.QCheckBox(self.groupBox_13)
        self.chk_srfSkipLast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chk_srfSkipLast.setChecked(False)
        self.chk_srfSkipLast.setObjectName("chk_srfSkipLast")
        self.gridLayout_99.addWidget(self.chk_srfSkipLast, 0, 0, 1, 1)
        self.btn_utilCreateOnSrf = QtWidgets.QPushButton(self.groupBox_13)
        self.btn_utilCreateOnSrf.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_utilCreateOnSrf.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_utilCreateOnSrf.setObjectName("btn_utilCreateOnSrf")
        self.gridLayout_99.addWidget(self.btn_utilCreateOnSrf, 1, 0, 1, 1)
        self.gridLayout_77.addLayout(self.gridLayout_99, 0, 4, 1, 1)
        self.gridLayout_65.addLayout(self.gridLayout_77, 0, 0, 1, 1)
        self.gridLayout_21.addWidget(self.groupBox_13, 0, 0, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_14.setMinimumSize(QtCore.QSize(400, 80))
        self.groupBox_14.setMaximumSize(QtCore.QSize(400, 80))
        self.groupBox_14.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_100 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_100.setSpacing(5)
        self.gridLayout_100.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_100.setObjectName("gridLayout_100")
        self.gridLayout_101 = QtWidgets.QGridLayout()
        self.gridLayout_101.setSpacing(3)
        self.gridLayout_101.setObjectName("gridLayout_101")
        self.gridLayout_102 = QtWidgets.QGridLayout()
        self.gridLayout_102.setObjectName("gridLayout_102")
        self.spn_crvNumOf = QtWidgets.QSpinBox(self.groupBox_14)
        self.spn_crvNumOf.setMinimumSize(QtCore.QSize(75, 0))
        self.spn_crvNumOf.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spn_crvNumOf.setMinimum(1)
        self.spn_crvNumOf.setMaximum(1000)
        self.spn_crvNumOf.setProperty("value", 1)
        self.spn_crvNumOf.setObjectName("spn_crvNumOf")
        self.gridLayout_102.addWidget(self.spn_crvNumOf, 0, 0, 1, 1)
        self.lbl_crvNumOf = QtWidgets.QLabel(self.groupBox_14)
        self.lbl_crvNumOf.setObjectName("lbl_crvNumOf")
        self.gridLayout_102.addWidget(self.lbl_crvNumOf, 0, 1, 1, 1)
        self.cbo_crvNumOf = QtWidgets.QComboBox(self.groupBox_14)
        self.cbo_crvNumOf.setMinimumSize(QtCore.QSize(270, 0))
        self.cbo_crvNumOf.setMaximumSize(QtCore.QSize(260, 16777215))
        self.cbo_crvNumOf.setObjectName("cbo_crvNumOf")
        self.cbo_crvNumOf.addItem("")
        self.cbo_crvNumOf.addItem("")
        self.gridLayout_102.addWidget(self.cbo_crvNumOf, 0, 2, 1, 1)
        self.gridLayout_101.addLayout(self.gridLayout_102, 0, 0, 1, 1)
        self.gridLayout_108 = QtWidgets.QGridLayout()
        self.gridLayout_108.setObjectName("gridLayout_108")
        self.btn_crvGo = QtWidgets.QPushButton(self.groupBox_14)
        self.btn_crvGo.setMinimumSize(QtCore.QSize(300, 25))
        self.btn_crvGo.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_crvGo.setObjectName("btn_crvGo")
        self.gridLayout_108.addWidget(self.btn_crvGo, 0, 1, 1, 1)
        self.chk_crvJntAsChain = QtWidgets.QCheckBox(self.groupBox_14)
        self.chk_crvJntAsChain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chk_crvJntAsChain.setObjectName("chk_crvJntAsChain")
        self.gridLayout_108.addWidget(self.chk_crvJntAsChain, 0, 0, 1, 1)
        self.gridLayout_101.addLayout(self.gridLayout_108, 1, 0, 1, 1)
        self.gridLayout_100.addLayout(self.gridLayout_101, 0, 0, 1, 1)
        self.gridLayout_21.addWidget(self.groupBox_14, 1, 0, 1, 1)
        self.groupBox_41 = QtWidgets.QGroupBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_41.sizePolicy().hasHeightForWidth())
        self.groupBox_41.setSizePolicy(sizePolicy)
        self.groupBox_41.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_41.setMaximumSize(QtCore.QSize(16777215, 47))
        self.groupBox_41.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_41.setTitle("")
        self.groupBox_41.setObjectName("groupBox_41")
        self.gridLayout_131 = QtWidgets.QGridLayout(self.groupBox_41)
        self.gridLayout_131.setSpacing(5)
        self.gridLayout_131.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_131.setObjectName("gridLayout_131")
        self.btn_jntOnVtx = QtWidgets.QPushButton(self.groupBox_41)
        self.btn_jntOnVtx.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_jntOnVtx.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 249, 227);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 249, 227);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_jntOnVtx.setObjectName("btn_jntOnVtx")
        self.gridLayout_131.addWidget(self.btn_jntOnVtx, 0, 0, 1, 1)
        self.gridLayout_21.addWidget(self.groupBox_41, 2, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_21, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 295, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem11, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_54 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_54.setObjectName("gridLayout_54")
        spacerItem12 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_54.addItem(spacerItem12, 0, 0, 1, 1)
        self.gridLayout_53 = QtWidgets.QGridLayout()
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_15.setEnabled(True)
        self.groupBox_15.setMinimumSize(QtCore.QSize(330, 100))
        self.groupBox_15.setMaximumSize(QtCore.QSize(330, 100))
        self.groupBox_15.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_24.setSpacing(5)
        self.gridLayout_24.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setSpacing(3)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_15)
        self.checkBox.setEnabled(False)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_23.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_15)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_23.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.cbo_utilConsMethod = QtWidgets.QComboBox(self.groupBox_15)
        self.cbo_utilConsMethod.setMinimumSize(QtCore.QSize(100, 0))
        self.cbo_utilConsMethod.setObjectName("cbo_utilConsMethod")
        self.cbo_utilConsMethod.addItem("")
        self.cbo_utilConsMethod.addItem("")
        self.gridLayout_23.addWidget(self.cbo_utilConsMethod, 1, 0, 1, 2)
        self.btn_utilConstrainToSrf = QtWidgets.QPushButton(self.groupBox_15)
        self.btn_utilConstrainToSrf.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_utilConstrainToSrf.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_utilConstrainToSrf.setObjectName("btn_utilConstrainToSrf")
        self.gridLayout_23.addWidget(self.btn_utilConstrainToSrf, 2, 0, 1, 2)
        self.gridLayout_24.addLayout(self.gridLayout_23, 0, 0, 1, 1)
        self.gridLayout_53.addWidget(self.groupBox_15, 0, 0, 1, 1)
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_16.setMinimumSize(QtCore.QSize(330, 80))
        self.groupBox_16.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_16.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_118 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_118.setSpacing(5)
        self.gridLayout_118.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_118.setObjectName("gridLayout_118")
        self.gridLayout_119 = QtWidgets.QGridLayout()
        self.gridLayout_119.setObjectName("gridLayout_119")
        self.gridLayout_120 = QtWidgets.QGridLayout()
        self.gridLayout_120.setObjectName("gridLayout_120")
        self.cbo_crvConstType = QtWidgets.QComboBox(self.groupBox_16)
        self.cbo_crvConstType.setEnabled(True)
        self.cbo_crvConstType.setMinimumSize(QtCore.QSize(100, 0))
        self.cbo_crvConstType.setObjectName("cbo_crvConstType")
        self.cbo_crvConstType.addItem("")
        self.cbo_crvConstType.addItem("")
        self.cbo_crvConstType.addItem("")
        self.cbo_crvConstType.addItem("")
        self.cbo_crvConstType.addItem("")
        self.gridLayout_120.addWidget(self.cbo_crvConstType, 0, 0, 1, 1)
        self.lne_crvUpObj = QtWidgets.QLineEdit(self.groupBox_16)
        self.lne_crvUpObj.setEnabled(True)
        self.lne_crvUpObj.setMinimumSize(QtCore.QSize(120, 0))
        self.lne_crvUpObj.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lne_crvUpObj.setAlignment(QtCore.Qt.AlignCenter)
        self.lne_crvUpObj.setObjectName("lne_crvUpObj")
        self.gridLayout_120.addWidget(self.lne_crvUpObj, 0, 1, 1, 1)
        self.btn_crvUpObjGet = QtWidgets.QPushButton(self.groupBox_16)
        self.btn_crvUpObjGet.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_crvUpObjGet.setObjectName("btn_crvUpObjGet")
        self.gridLayout_120.addWidget(self.btn_crvUpObjGet, 0, 2, 1, 1)
        self.gridLayout_119.addLayout(self.gridLayout_120, 0, 0, 1, 1)
        self.gridLayout_122 = QtWidgets.QGridLayout()
        self.gridLayout_122.setObjectName("gridLayout_122")
        self.chk_crvPositionOnly = QtWidgets.QCheckBox(self.groupBox_16)
        self.chk_crvPositionOnly.setEnabled(True)
        self.chk_crvPositionOnly.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chk_crvPositionOnly.setCheckable(True)
        self.chk_crvPositionOnly.setChecked(False)
        self.chk_crvPositionOnly.setObjectName("chk_crvPositionOnly")
        self.gridLayout_122.addWidget(self.chk_crvPositionOnly, 0, 0, 1, 1)
        self.chk_crvParametric = QtWidgets.QCheckBox(self.groupBox_16)
        self.chk_crvParametric.setEnabled(True)
        self.chk_crvParametric.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chk_crvParametric.setCheckable(True)
        self.chk_crvParametric.setChecked(True)
        self.chk_crvParametric.setObjectName("chk_crvParametric")
        self.gridLayout_122.addWidget(self.chk_crvParametric, 0, 1, 1, 1)
        self.btn_crvConstGo = QtWidgets.QPushButton(self.groupBox_16)
        self.btn_crvConstGo.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_crvConstGo.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_crvConstGo.setObjectName("btn_crvConstGo")
        self.gridLayout_122.addWidget(self.btn_crvConstGo, 0, 2, 1, 1)
        self.gridLayout_119.addLayout(self.gridLayout_122, 1, 0, 1, 1)
        self.gridLayout_118.addLayout(self.gridLayout_119, 0, 0, 1, 1)
        self.gridLayout_53.addWidget(self.groupBox_16, 1, 0, 1, 1)
        self.gridLayout_54.addLayout(self.gridLayout_53, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_54.addItem(spacerItem13, 0, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 404, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_54.addItem(spacerItem14, 1, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_25.setObjectName("gridLayout_25")
        spacerItem15 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem15, 0, 0, 1, 1)
        self.groupBox_33 = QtWidgets.QGroupBox(self.tab_10)
        self.groupBox_33.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_33.sizePolicy().hasHeightForWidth())
        self.groupBox_33.setSizePolicy(sizePolicy)
        self.groupBox_33.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_33.setMaximumSize(QtCore.QSize(16777215, 47))
        self.groupBox_33.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_33.setObjectName("groupBox_33")
        self.gridLayout_60 = QtWidgets.QGridLayout(self.groupBox_33)
        self.gridLayout_60.setSpacing(5)
        self.gridLayout_60.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.gridLayout_132 = QtWidgets.QGridLayout()
        self.gridLayout_132.setSpacing(3)
        self.gridLayout_132.setObjectName("gridLayout_132")
        self.lne_singlesName = QtWidgets.QLineEdit(self.groupBox_33)
        self.lne_singlesName.setEnabled(True)
        self.lne_singlesName.setMinimumSize(QtCore.QSize(150, 0))
        self.lne_singlesName.setAlignment(QtCore.Qt.AlignCenter)
        self.lne_singlesName.setObjectName("lne_singlesName")
        self.gridLayout_132.addWidget(self.lne_singlesName, 0, 0, 1, 1)
        self.chk_singleJnt = QtWidgets.QCheckBox(self.groupBox_33)
        self.chk_singleJnt.setChecked(True)
        self.chk_singleJnt.setObjectName("chk_singleJnt")
        self.gridLayout_132.addWidget(self.chk_singleJnt, 0, 1, 1, 1)
        self.btn_singleCtl = QtWidgets.QPushButton(self.groupBox_33)
        self.btn_singleCtl.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_singleCtl.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_singleCtl.setObjectName("btn_singleCtl")
        self.gridLayout_132.addWidget(self.btn_singleCtl, 0, 2, 1, 1)
        self.btn_singlePatch = QtWidgets.QPushButton(self.groupBox_33)
        self.btn_singlePatch.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_singlePatch.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_singlePatch.setObjectName("btn_singlePatch")
        self.gridLayout_132.addWidget(self.btn_singlePatch, 0, 3, 1, 1)
        self.gridLayout_60.addLayout(self.gridLayout_132, 0, 0, 1, 1)
        self.gridLayout_25.addWidget(self.groupBox_33, 0, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(157, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem16, 0, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 320, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_25.addItem(spacerItem17, 1, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_26.setObjectName("gridLayout_26")
        spacerItem18 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem18, 0, 0, 1, 1)
        self.groupBox_42 = QtWidgets.QGroupBox(self.tab_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_42.sizePolicy().hasHeightForWidth())
        self.groupBox_42.setSizePolicy(sizePolicy)
        self.groupBox_42.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_42.setMaximumSize(QtCore.QSize(16777215, 47))
        self.groupBox_42.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"border-color:  rgb(150, 114, 0);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"    color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_42.setObjectName("groupBox_42")
        self.gridLayout_133 = QtWidgets.QGridLayout(self.groupBox_42)
        self.gridLayout_133.setSpacing(5)
        self.gridLayout_133.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_133.setObjectName("gridLayout_133")
        self.gridLayout_134 = QtWidgets.QGridLayout()
        self.gridLayout_134.setObjectName("gridLayout_134")
        self.chk_mmOrient = QtWidgets.QCheckBox(self.groupBox_42)
        self.chk_mmOrient.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chk_mmOrient.setObjectName("chk_mmOrient")
        self.gridLayout_134.addWidget(self.chk_mmOrient, 0, 0, 1, 1)
        self.chk_mmDorito = QtWidgets.QCheckBox(self.groupBox_42)
        self.chk_mmDorito.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chk_mmDorito.setObjectName("chk_mmDorito")
        self.gridLayout_134.addWidget(self.chk_mmDorito, 0, 1, 1, 1)
        self.btn_mmGo = QtWidgets.QPushButton(self.groupBox_42)
        self.btn_mmGo.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_mmGo.setStyleSheet("QPushButton{\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(253, 240, 197);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {   \n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240\n"
");\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.btn_mmGo.setObjectName("btn_mmGo")
        self.gridLayout_134.addWidget(self.btn_mmGo, 0, 2, 1, 1)
        self.gridLayout_133.addLayout(self.gridLayout_134, 0, 0, 1, 1)
        self.gridLayout_26.addWidget(self.groupBox_42, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem19, 0, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 320, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem20, 1, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_11, "")
        self.gridLayout_70.addWidget(self.tabWidget_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cbo_globCtlShape.setCurrentIndex(10)
        self.cbo_globCtlColor.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.cbo_crvConstType.setCurrentIndex(3)
        QtCore.QObject.connect(self.chk_ikSpline, QtCore.SIGNAL("clicked(bool)"), self.spn_ikSplineNum.setEnabled)
        QtCore.QObject.connect(self.chk_T, QtCore.SIGNAL("clicked(bool)"), self.chk_axisTY.setChecked)
        QtCore.QObject.connect(self.chk_T, QtCore.SIGNAL("clicked(bool)"), self.chk_axisTX.setChecked)
        QtCore.QObject.connect(self.chk_R, QtCore.SIGNAL("clicked(bool)"), self.chk_axisRZ.setChecked)
        QtCore.QObject.connect(self.chk_S, QtCore.SIGNAL("clicked(bool)"), self.chk_axisSX.setChecked)
        QtCore.QObject.connect(self.chk_R, QtCore.SIGNAL("clicked(bool)"), self.chk_axisRX.setChecked)
        QtCore.QObject.connect(self.chk_R, QtCore.SIGNAL("clicked(bool)"), self.chk_axisRY.setChecked)
        QtCore.QObject.connect(self.chk_T, QtCore.SIGNAL("clicked(bool)"), self.chk_axisTZ.setChecked)
        QtCore.QObject.connect(self.chk_S, QtCore.SIGNAL("clicked(bool)"), self.chk_axisSY.setChecked)
        QtCore.QObject.connect(self.chk_S, QtCore.SIGNAL("clicked(bool)"), self.chk_axisSZ.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_setCtlSize, self.btn_setCtlShape)
        MainWindow.setTabOrder(self.btn_setCtlShape, self.btn_setCtlColor)
        MainWindow.setTabOrder(self.btn_setCtlColor, self.spn_globCtlSize)
        MainWindow.setTabOrder(self.spn_globCtlSize, self.cbo_globCtlShape)
        MainWindow.setTabOrder(self.cbo_globCtlShape, self.cbo_globCtlColor)
        MainWindow.setTabOrder(self.cbo_globCtlColor, self.lne_globCtlSuffix)
        MainWindow.setTabOrder(self.lne_globCtlSuffix, self.lne_globJntSuffix)
        MainWindow.setTabOrder(self.lne_globJntSuffix, self.spn_globAutoColorMargin)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "cmSimpleSys", None, -1))
        self.groupBox_17.setTitle(QtWidgets.QApplication.translate("MainWindow", "Pre Build", None, -1))
        self.lne_globCtlSuffix.setText(QtWidgets.QApplication.translate("MainWindow", "ctl", None, -1))
        self.lne_globCtlSuffix.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Ctl Suffix (optional)", None, -1))
        self.lne_globJntSuffix.setText(QtWidgets.QApplication.translate("MainWindow", "jnt", None, -1))
        self.lne_globJntSuffix.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Joint Suffix (optional)", None, -1))
        self.lbl_globCtlShape.setText(QtWidgets.QApplication.translate("MainWindow", "Ctl Shape", None, -1))
        self.cbo_globCtlShape.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "sphere", None, -1))
        self.cbo_globCtlShape.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "arrow", None, -1))
        self.cbo_globCtlShape.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "arrowCurved", None, -1))
        self.cbo_globCtlShape.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "arrowDouble", None, -1))
        self.cbo_globCtlShape.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "arrowDoubleCurved", None, -1))
        self.cbo_globCtlShape.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "arrowFour", None, -1))
        self.cbo_globCtlShape.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "arrowFourCurved", None, -1))
        self.cbo_globCtlShape.setItemText(7, QtWidgets.QApplication.translate("MainWindow", "arrowStrike", None, -1))
        self.cbo_globCtlShape.setItemText(8, QtWidgets.QApplication.translate("MainWindow", "circle", None, -1))
        self.cbo_globCtlShape.setItemText(9, QtWidgets.QApplication.translate("MainWindow", "circleH", None, -1))
        self.cbo_globCtlShape.setItemText(10, QtWidgets.QApplication.translate("MainWindow", "circleV", None, -1))
        self.cbo_globCtlShape.setItemText(11, QtWidgets.QApplication.translate("MainWindow", "circularArrow", None, -1))
        self.cbo_globCtlShape.setItemText(12, QtWidgets.QApplication.translate("MainWindow", "chevron", None, -1))
        self.cbo_globCtlShape.setItemText(13, QtWidgets.QApplication.translate("MainWindow", "cross", None, -1))
        self.cbo_globCtlShape.setItemText(14, QtWidgets.QApplication.translate("MainWindow", "crossX", None, -1))
        self.cbo_globCtlShape.setItemText(15, QtWidgets.QApplication.translate("MainWindow", "cube", None, -1))
        self.cbo_globCtlShape.setItemText(16, QtWidgets.QApplication.translate("MainWindow", "diamond", None, -1))
        self.cbo_globCtlShape.setItemText(17, QtWidgets.QApplication.translate("MainWindow", "star", None, -1))
        self.cbo_globCtlShape.setItemText(18, QtWidgets.QApplication.translate("MainWindow", "star_8", None, -1))
        self.cbo_globCtlShape.setItemText(19, QtWidgets.QApplication.translate("MainWindow", "fourArrowCircle", None, -1))
        self.cbo_globCtlShape.setItemText(20, QtWidgets.QApplication.translate("MainWindow", "googleSign", None, -1))
        self.cbo_globCtlShape.setItemText(21, QtWidgets.QApplication.translate("MainWindow", "googleSignSharp", None, -1))
        self.cbo_globCtlShape.setItemText(22, QtWidgets.QApplication.translate("MainWindow", "joint", None, -1))
        self.cbo_globCtlShape.setItemText(23, QtWidgets.QApplication.translate("MainWindow", "locator", None, -1))
        self.cbo_globCtlShape.setItemText(24, QtWidgets.QApplication.translate("MainWindow", "locatorVolume", None, -1))
        self.cbo_globCtlShape.setItemText(25, QtWidgets.QApplication.translate("MainWindow", "lollipopCircle", None, -1))
        self.cbo_globCtlShape.setItemText(26, QtWidgets.QApplication.translate("MainWindow", "lollipopDouble", None, -1))
        self.cbo_globCtlShape.setItemText(27, QtWidgets.QApplication.translate("MainWindow", "lollipopFour", None, -1))
        self.cbo_globCtlShape.setItemText(28, QtWidgets.QApplication.translate("MainWindow", "lollipopSquare", None, -1))
        self.cbo_globCtlShape.setItemText(29, QtWidgets.QApplication.translate("MainWindow", "square", None, -1))
        self.cbo_globCtlShape.setItemText(30, QtWidgets.QApplication.translate("MainWindow", "triangle", None, -1))
        self.lbl_globCtlColor.setText(QtWidgets.QApplication.translate("MainWindow", "Ctl Color", None, -1))
        self.cbo_globCtlColor.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "primary", None, -1))
        self.cbo_globCtlColor.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "secondary", None, -1))
        self.cbo_globCtlColor.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "tertiary", None, -1))
        self.cbo_globCtlColor.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "blue", None, -1))
        self.cbo_globCtlColor.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "darkBlue", None, -1))
        self.cbo_globCtlColor.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "lightBlue", None, -1))
        self.cbo_globCtlColor.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "softBlue", None, -1))
        self.cbo_globCtlColor.setItemText(7, QtWidgets.QApplication.translate("MainWindow", "pastelBlue", None, -1))
        self.cbo_globCtlColor.setItemText(8, QtWidgets.QApplication.translate("MainWindow", "red", None, -1))
        self.cbo_globCtlColor.setItemText(9, QtWidgets.QApplication.translate("MainWindow", "darkRed", None, -1))
        self.cbo_globCtlColor.setItemText(10, QtWidgets.QApplication.translate("MainWindow", "lightRed", None, -1))
        self.cbo_globCtlColor.setItemText(11, QtWidgets.QApplication.translate("MainWindow", "pastelRed", None, -1))
        self.cbo_globCtlColor.setItemText(12, QtWidgets.QApplication.translate("MainWindow", "green", None, -1))
        self.cbo_globCtlColor.setItemText(13, QtWidgets.QApplication.translate("MainWindow", "darkGreen", None, -1))
        self.cbo_globCtlColor.setItemText(14, QtWidgets.QApplication.translate("MainWindow", "lightGreen", None, -1))
        self.cbo_globCtlColor.setItemText(15, QtWidgets.QApplication.translate("MainWindow", "blueGreen", None, -1))
        self.cbo_globCtlColor.setItemText(16, QtWidgets.QApplication.translate("MainWindow", "turquoise", None, -1))
        self.cbo_globCtlColor.setItemText(17, QtWidgets.QApplication.translate("MainWindow", "yellow", None, -1))
        self.cbo_globCtlColor.setItemText(18, QtWidgets.QApplication.translate("MainWindow", "yellowGreen", None, -1))
        self.cbo_globCtlColor.setItemText(19, QtWidgets.QApplication.translate("MainWindow", "lightYellow", None, -1))
        self.cbo_globCtlColor.setItemText(20, QtWidgets.QApplication.translate("MainWindow", "pastelYellow", None, -1))
        self.cbo_globCtlColor.setItemText(21, QtWidgets.QApplication.translate("MainWindow", "pink", None, -1))
        self.cbo_globCtlColor.setItemText(22, QtWidgets.QApplication.translate("MainWindow", "darkPink", None, -1))
        self.cbo_globCtlColor.setItemText(23, QtWidgets.QApplication.translate("MainWindow", "greyPink", None, -1))
        self.cbo_globCtlColor.setItemText(24, QtWidgets.QApplication.translate("MainWindow", "brown", None, -1))
        self.cbo_globCtlColor.setItemText(25, QtWidgets.QApplication.translate("MainWindow", "darkBrown", None, -1))
        self.cbo_globCtlColor.setItemText(26, QtWidgets.QApplication.translate("MainWindow", "lightBrown", None, -1))
        self.cbo_globCtlColor.setItemText(27, QtWidgets.QApplication.translate("MainWindow", "redBrown", None, -1))
        self.cbo_globCtlColor.setItemText(28, QtWidgets.QApplication.translate("MainWindow", "pastelBrown", None, -1))
        self.cbo_globCtlColor.setItemText(29, QtWidgets.QApplication.translate("MainWindow", "white", None, -1))
        self.cbo_globCtlColor.setItemText(30, QtWidgets.QApplication.translate("MainWindow", "black", None, -1))
        self.cbo_globCtlColor.setItemText(31, QtWidgets.QApplication.translate("MainWindow", "darkGrey", None, -1))
        self.cbo_globCtlColor.setItemText(32, QtWidgets.QApplication.translate("MainWindow", "lightGrey", None, -1))
        self.lbl_globCtlSize.setText(QtWidgets.QApplication.translate("MainWindow", "Ctl Size", None, -1))
        self.lbl_globAutoColorMargin.setText(QtWidgets.QApplication.translate("MainWindow", "Color Margin", None, -1))
        self.spn_globAutoColorMargin.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Distance +/- along global X", None, -1))
        self.groupBox_31.setTitle(QtWidgets.QApplication.translate("MainWindow", "Post Build", None, -1))
        self.btn_setCtlColor.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Set selected ctrl(s) color from Global setting", None, -1))
        self.btn_setCtlColor.setText(QtWidgets.QApplication.translate("MainWindow", "Set Color", None, -1))
        self.btn_setCtlSize.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Set selected ctrl(s) size from Global setting", None, -1))
        self.btn_setCtlSize.setText(QtWidgets.QApplication.translate("MainWindow", "Set Size", None, -1))
        self.btn_setCtlShape.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Set selected ctrl(s) shape from Global setting", None, -1))
        self.btn_setCtlShape.setText(QtWidgets.QApplication.translate("MainWindow", "Set Shape", None, -1))
        self.btn_setCtlVis.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Set ctrl(s) visibility to Head UI Host attrs", None, -1))
        self.btn_setCtlVis.setText(QtWidgets.QApplication.translate("MainWindow", "Set Vis", None, -1))
        self.groupBox_35.setTitle(QtWidgets.QApplication.translate("MainWindow", "Select Child by Suffix", None, -1))
        self.btn_selBySuffix.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Select edge loop on headCut mesh to create deformers for Lashes. Or select old Lash curve to rebuild.", None, -1))
        self.btn_selBySuffix.setText(QtWidgets.QApplication.translate("MainWindow", "Select Children By Suffix", None, -1))
        self.cbo_selSuffix.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "jnt", None, -1))
        self.cbo_selSuffix.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "ctl", None, -1))
        self.cbo_selSuffix.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "bfr", None, -1))
        self.cbo_selSuffix.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "ctlRef", None, -1))
        self.cbo_selSuffix.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "spljnt", None, -1))
        self.cbo_selSuffix.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "bind", None, -1))
        self.cbo_selSuffix.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "anim", None, -1))
        self.cbo_selSuffix.setItemText(7, QtWidgets.QApplication.translate("MainWindow", "cns", None, -1))
        self.cbo_selSuffix.setItemText(8, QtWidgets.QApplication.translate("MainWindow", "off", None, -1))
        self.cbo_selSuffix.setItemText(9, QtWidgets.QApplication.translate("MainWindow", "root", None, -1))
        self.cbo_selSuffix.setItemText(10, QtWidgets.QApplication.translate("MainWindow", "grp", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "(un)Lock/(un)Hide", None, -1))
        self.cbo_axisLockUnlock.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Locks / Unlocks selected", None, -1))
        self.cbo_axisLockUnlock.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Unlock", None, -1))
        self.cbo_axisLockUnlock.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Lock", None, -1))
        self.cbo_hideUnhide.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Hide", None, -1))
        self.cbo_hideUnhide.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Unhide", None, -1))
        self.btn_axisGo.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.chk_axisTX.setText(QtWidgets.QApplication.translate("MainWindow", "tx", None, -1))
        self.chk_axisRZ.setText(QtWidgets.QApplication.translate("MainWindow", "rz", None, -1))
        self.chk_axisSY.setText(QtWidgets.QApplication.translate("MainWindow", "sy", None, -1))
        self.chk_axisTY.setText(QtWidgets.QApplication.translate("MainWindow", "ty", None, -1))
        self.chk_axisRX.setText(QtWidgets.QApplication.translate("MainWindow", "rx", None, -1))
        self.chk_axisSX.setText(QtWidgets.QApplication.translate("MainWindow", "sx", None, -1))
        self.chk_axisRY.setText(QtWidgets.QApplication.translate("MainWindow", "ry", None, -1))
        self.chk_axisSZ.setText(QtWidgets.QApplication.translate("MainWindow", "sz", None, -1))
        self.chk_axisTZ.setText(QtWidgets.QApplication.translate("MainWindow", "tz", None, -1))
        self.chk_T.setText(QtWidgets.QApplication.translate("MainWindow", "T", None, -1))
        self.chk_R.setText(QtWidgets.QApplication.translate("MainWindow", "R", None, -1))
        self.chk_S.setText(QtWidgets.QApplication.translate("MainWindow", "S", None, -1))
        self.groupBox_38.setTitle(QtWidgets.QApplication.translate("MainWindow", "Parent Constraint", None, -1))
        self.chk_maintainOffset.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Maintain Offset", None, -1))
        self.chk_maintainOffset.setText(QtWidgets.QApplication.translate("MainWindow", "MO", None, -1))
        self.btn_createMatCon.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Creates Matrix Constraint using checked attrs. Select Parent, then Child", None, -1))
        self.btn_createMatCon.setText(QtWidgets.QApplication.translate("MainWindow", "Create Constraint", None, -1))
        self.btn_delMatCon.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Deletes Matrix Constraint", None, -1))
        self.btn_delMatCon.setText(QtWidgets.QApplication.translate("MainWindow", "Delete Constraint", None, -1))
        self.groupBox_36.setTitle(QtWidgets.QApplication.translate("MainWindow", "Connect", None, -1))
        self.btn_globalSclObj.setText(QtWidgets.QApplication.translate("MainWindow", "<<", None, -1))
        self.btn_globalScaleConnect.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Connects rig global scale to transform scale attrs", None, -1))
        self.btn_globalScaleConnect.setText(QtWidgets.QApplication.translate("MainWindow", "Global Scale", None, -1))
        self.btn_directConnect.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Connects selected SRT attr(s). Select SOURCE then TARGET. Multiple Targets allowed.", None, -1))
        self.btn_directConnect.setText(QtWidgets.QApplication.translate("MainWindow", "Direct Connect", None, -1))
        self.lne_globalSclObj.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Object that contains globalScale attr", None, -1))
        self.lne_globalSclObj.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "global_C0_ctl", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "Attr Control", None, -1))
        self.groupBox_22.setTitle(QtWidgets.QApplication.translate("MainWindow", "Import / Export", None, -1))
        self.btn_importWeights.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Import XML weight file.", None, -1))
        self.btn_importWeights.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Import weight(s) from directory", None, -1))
        self.btn_importWeights.setText(QtWidgets.QApplication.translate("MainWindow", "Import Weight(s)", None, -1))
        self.btn_exportWeights.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Export XML weight file.", None, -1))
        self.btn_exportWeights.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Export weight(s) to directory", None, -1))
        self.btn_exportWeights.setText(QtWidgets.QApplication.translate("MainWindow", "Export Weight(s)", None, -1))
        self.btn_selectClstrInfl.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Select joints in objects skinCluster", None, -1))
        self.btn_selectClstrInfl.setText(QtWidgets.QApplication.translate("MainWindow", "Select Clstr Jts", None, -1))
        self.groupBox_40.setTitle(QtWidgets.QApplication.translate("MainWindow", "Transfer", None, -1))
        self.btn_transferWeights.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Select SOURCE then TARGET(S).  Poly to Nurbs IS supported. Method is Closest Point, Closest Joint, One to One", None, -1))
        self.btn_transferWeights.setText(QtWidgets.QApplication.translate("MainWindow", "Transfer Weights", None, -1))
        self.chk_transferWeightsRemove.setText(QtWidgets.QApplication.translate("MainWindow", "Remove Unused", None, -1))
        self.groupBox_20.setTitle(QtWidgets.QApplication.translate("MainWindow", "Joint Pre-Bind Matrix", None, -1))
        self.cbo_preBindJoint.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Joint suffix", None, -1))
        self.cbo_preBindJoint.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "jnt", None, -1))
        self.cbo_preBindJoint.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "bind", None, -1))
        self.cbo_preBindBfr.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Buffer suffix", None, -1))
        self.cbo_preBindBfr.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "ctlRef (Strap Rig)", None, -1))
        self.cbo_preBindBfr.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "cns (mGear Jnt)", None, -1))
        self.cbo_preBindBfr.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "bfr (Face Rig)", None, -1))
        self.btn_ctlPreBindMat.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Connects the joints bfr.wm as bindpose prematrix. Select joints, then object with skinCluster", None, -1))
        self.btn_ctlPreBindMat.setText(QtWidgets.QApplication.translate("MainWindow", "Connect .wm", None, -1))
        self.groupBox_43.setTitle(QtWidgets.QApplication.translate("MainWindow", "BindPose", None, -1))
        self.btn_resetBindPose.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Sets new bindPose, and sets Prefered Angle (option) for all joints in selected mesh skinCluster", None, -1))
        self.btn_resetBindPose.setText(QtWidgets.QApplication.translate("MainWindow", "Set BindPose", None, -1))
        self.chk_bindPoseAngle.setToolTip(QtWidgets.QApplication.translate("MainWindow", "If checked, joints preferred angle will be set to its current angle when BindPose is run", None, -1))
        self.chk_bindPoseAngle.setText(QtWidgets.QApplication.translate("MainWindow", "Set Preferred Angle", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QtWidgets.QApplication.translate("MainWindow", "Skin Tools", None, -1))
        self.groupBox_39.setTitle(QtWidgets.QApplication.translate("MainWindow", "Points", None, -1))
        self.btn_meshUpdateOrig.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Updates Target mesh to shape of Source mesh. Works on Mesh, Select SOURCE then TARGET. Auto option for multi mesh updates.", None, -1))
        self.btn_meshUpdateOrig.setText(QtWidgets.QApplication.translate("MainWindow", "Update Shape", None, -1))
        self.chk_updateAuto.setToolTip(QtWidgets.QApplication.translate("MainWindow", "If checked, select the newly imported mdl alembic objects in the outliner. If NOT checked. Select SOURCE then TARGET for individual shape updates.", None, -1))
        self.chk_updateAuto.setText(QtWidgets.QApplication.translate("MainWindow", "Auto", None, -1))
        self.btn_meshMatchPoint.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Target to follow source mesh transformation, and deformation. Works on Mesh, Nurbs, Curves. Select DRIVER then DRIVEN", None, -1))
        self.btn_meshMatchPoint.setText(QtWidgets.QApplication.translate("MainWindow", "Match Point Pos", None, -1))
        self.groupBox_44.setTitle(QtWidgets.QApplication.translate("MainWindow", "Published Geo", None, -1))
        self.btn_delUnShp.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Delete unused shape nodes from the scene.", None, -1))
        self.btn_delUnShp.setText(QtWidgets.QApplication.translate("MainWindow", "Del Unused Shapes", None, -1))
        self.btn_smoothEdges.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Smooth polygon edges", None, -1))
        self.btn_smoothEdges.setText(QtWidgets.QApplication.translate("MainWindow", "Smooth Edges", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QtWidgets.QApplication.translate("MainWindow", "Mesh Control", None, -1))
        self.grp_strapGuide.setTitle(QtWidgets.QApplication.translate("MainWindow", "Guides on Surface", None, -1))
        self.btn_prepSrf.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Create new surface, or rebuild selected nurbs 0,1 Parameterization. Displays UV border.", None, -1))
        self.btn_prepSrf.setText(QtWidgets.QApplication.translate("MainWindow", "Prep Srf", None, -1))
        self.btn_swapUV.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Spin nurbs surface border edges", None, -1))
        self.btn_swapUV.setText(QtWidgets.QApplication.translate("MainWindow", "Swap U,V", None, -1))
        self.spn_strapGuideRow.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Number or guide rows to create", None, -1))
        self.lbl_strapGuideRow.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Number or guide rows to create (U Param Red)", None, -1))
        self.lbl_strapGuideRow.setText(QtWidgets.QApplication.translate("MainWindow", "Gde Row", None, -1))
        self.spn_strapGuideColumn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Number or guide columns to create", None, -1))
        self.lbl_strapGuideColumn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Number or guide columns to create (V Param Green)", None, -1))
        self.lbl_strapGuideColumn.setText(QtWidgets.QApplication.translate("MainWindow", "Gde Column", None, -1))
        self.chk_strapSkipLast.setText(QtWidgets.QApplication.translate("MainWindow", "Closed Srf (cylinder)", None, -1))
        self.btn_goGuidesOnSrf.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Create guide locators on nurb surface", None, -1))
        self.btn_goGuidesOnSrf.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.grp_strapRig.setTitle(QtWidgets.QApplication.translate("MainWindow", "Rig From Guides", None, -1))
        self.spn_strapJntRow.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Number or joint rows to create on dorito mesh", None, -1))
        self.lbl_strapJntRow_3.setToolTip(QtWidgets.QApplication.translate("MainWindow", "If 0, no dorito joints will be created.", None, -1))
        self.lbl_strapJntRow_3.setText(QtWidgets.QApplication.translate("MainWindow", "*Jnt Row", None, -1))
        self.spn_strapJntColumn.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Number or joint columns to create on dorito mesh", None, -1))
        self.lbl_strapJntColumn_2.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Number or joint columns to create on dorito mesh", None, -1))
        self.lbl_strapJntColumn_2.setText(QtWidgets.QApplication.translate("MainWindow", "Jnt Column", None, -1))
        self.spn_ikSplineNum.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Number of joints in IK Spline", None, -1))
        self.lbl_ikSplineNo_2.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Number of joints in IK Spline", None, -1))
        self.lbl_ikSplineNo_2.setText(QtWidgets.QApplication.translate("MainWindow", "Spl. Column", None, -1))
        self.chk_makeCtlFK.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Builds ctls in FK mode, with IK option", None, -1))
        self.chk_makeCtlFK.setText(QtWidgets.QApplication.translate("MainWindow", "Make Ctls FK", None, -1))
        self.chk_lra.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Turn on Local Rotation Axis for deformer joints", None, -1))
        self.chk_lra.setText(QtWidgets.QApplication.translate("MainWindow", "Display Local Rot Axis", None, -1))
        self.btn_goStrapRig.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Build rig from Guides on Surface, or current selected nurbs surface with _ctlGde children", None, -1))
        self.btn_goStrapRig.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.chk_ikSpline.setText(QtWidgets.QApplication.translate("MainWindow", "IK Spline", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QtWidgets.QApplication.translate("MainWindow", "Strap Rigs", None, -1))
        self.groupBox_24.setTitle(QtWidgets.QApplication.translate("MainWindow", "Guides on Curve", None, -1))
        self.btn_gdeOnCrvGo.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Create guides evenly along curve. Position guides as needed. Yellow guide defines curve direction.", None, -1))
        self.btn_gdeOnCrvGo.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.groupBox_27.setTitle(QtWidgets.QApplication.translate("MainWindow", "Rig From Guides", None, -1))
        self.cbo_crvRigType.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "IK/FK", None, -1))
        self.cbo_crvRigType.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "FK", None, -1))
        self.btn_bldCrvRigGo.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Build rig from Guides on Curve, or current selected nurbs curve with _ctlGde children", None, -1))
        self.btn_bldCrvRigGo.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QtWidgets.QApplication.translate("MainWindow", "Curve Rigs", None, -1))
        self.groupBox_13.setTitle(QtWidgets.QApplication.translate("MainWindow", "Create on Surface", None, -1))
        self.btn_utilPrepSrf.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Create new surface, or rebuild selected nurbs 0,1 Parameterization. Displays UV border.", None, -1))
        self.btn_utilPrepSrf.setText(QtWidgets.QApplication.translate("MainWindow", "Prep Srf", None, -1))
        self.btn_utilSwapUV.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Spin nurbs surface border edges", None, -1))
        self.btn_utilSwapUV.setText(QtWidgets.QApplication.translate("MainWindow", "Swap U,V", None, -1))
        self.cbo_utilObjType.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "Joint", None, -1))
        self.cbo_utilObjType.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Joint", None, -1))
        self.cbo_utilObjType.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Locator", None, -1))
        self.lbl_utilRow.setText(QtWidgets.QApplication.translate("MainWindow", "Row Num.", None, -1))
        self.lbl_utilColumn.setText(QtWidgets.QApplication.translate("MainWindow", "Column Num", None, -1))
        self.chk_srfSkipLast.setToolTip(QtWidgets.QApplication.translate("MainWindow", "For closed surfaces", None, -1))
        self.chk_srfSkipLast.setText(QtWidgets.QApplication.translate("MainWindow", "Skip Last", None, -1))
        self.btn_utilCreateOnSrf.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Creates the selected items evenly along nurbs surface", None, -1))
        self.btn_utilCreateOnSrf.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.groupBox_14.setTitle(QtWidgets.QApplication.translate("MainWindow", "Create On Curve", None, -1))
        self.lbl_crvNumOf.setText(QtWidgets.QApplication.translate("MainWindow", "No. of", None, -1))
        self.cbo_crvNumOf.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "Joints", None, -1))
        self.cbo_crvNumOf.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Joints", None, -1))
        self.cbo_crvNumOf.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Locators", None, -1))
        self.btn_crvGo.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Create items evenly along curve. Select curve and run", None, -1))
        self.btn_crvGo.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.chk_crvJntAsChain.setText(QtWidgets.QApplication.translate("MainWindow", "Chain", None, -1))
        self.btn_jntOnVtx.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Creates joints attached to mesh vertex. UV\'s are required on the mesh. And the mesh have transforms frozen.", None, -1))
        self.btn_jntOnVtx.setText(QtWidgets.QApplication.translate("MainWindow", "Jnt on Mesh Vert", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QtWidgets.QApplication.translate("MainWindow", "Create On", None, -1))
        self.groupBox_15.setTitle(QtWidgets.QApplication.translate("MainWindow", "Constrain To Surface", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("MainWindow", "Translate", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("MainWindow", "Rotate", None, -1))
        self.cbo_utilConsMethod.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Matrix", None, -1))
        self.cbo_utilConsMethod.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Follicle", None, -1))
        self.btn_utilConstrainToSrf.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Constrain selected items to nurbs surface by closest point. Select nurbs surface last", None, -1))
        self.btn_utilConstrainToSrf.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.groupBox_16.setTitle(QtWidgets.QApplication.translate("MainWindow", "Constrain to Curve", None, -1))
        self.cbo_crvConstType.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Scene Up", None, -1))
        self.cbo_crvConstType.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Obj Up", None, -1))
        self.cbo_crvConstType.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Obj Rot Up", None, -1))
        self.cbo_crvConstType.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Vector", None, -1))
        self.cbo_crvConstType.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "Normal", None, -1))
        self.lne_crvUpObj.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Up Object", None, -1))
        self.btn_crvUpObjGet.setText(QtWidgets.QApplication.translate("MainWindow", "<<", None, -1))
        self.chk_crvPositionOnly.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Position Only is Parametric placement (no sliding)", None, -1))
        self.chk_crvPositionOnly.setText(QtWidgets.QApplication.translate("MainWindow", "Position Only", None, -1))
        self.chk_crvParametric.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Sticks to curve. Non-Parametric will slide on crv length is changed.", None, -1))
        self.chk_crvParametric.setText(QtWidgets.QApplication.translate("MainWindow", "Parametric", None, -1))
        self.btn_crvConstGo.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Constrain items to closest point on curve. Select curve last", None, -1))
        self.btn_crvConstGo.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QtWidgets.QApplication.translate("MainWindow", "Constrain To", None, -1))
        self.groupBox_33.setTitle(QtWidgets.QApplication.translate("MainWindow", "Singles", None, -1))
        self.lne_singlesName.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Ctl Name", None, -1))
        self.chk_singleJnt.setText(QtWidgets.QApplication.translate("MainWindow", "Jnt", None, -1))
        self.btn_singleCtl.setText(QtWidgets.QApplication.translate("MainWindow", "Single Ctl", None, -1))
        self.btn_singlePatch.setText(QtWidgets.QApplication.translate("MainWindow", "Single Patch", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QtWidgets.QApplication.translate("MainWindow", "Single Ctl", None, -1))
        self.groupBox_42.setTitle(QtWidgets.QApplication.translate("MainWindow", "MM Ctl(s) from Vtx", None, -1))
        self.chk_mmOrient.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Orient ctls to vertex normal", None, -1))
        self.chk_mmOrient.setText(QtWidgets.QApplication.translate("MainWindow", "Orient to Mesh", None, -1))
        self.chk_mmDorito.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Creates decondary dorito mesh, that is deformed by ctls", None, -1))
        self.chk_mmDorito.setText(QtWidgets.QApplication.translate("MainWindow", "Dorito Mesh", None, -1))
        self.btn_mmGo.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Creates Match Move controllers on selected vetex(s), Selected mesh needs to be deformed on vertex level for ctls to follow.", None, -1))
        self.btn_mmGo.setText(QtWidgets.QApplication.translate("MainWindow", "Go", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), QtWidgets.QApplication.translate("MainWindow", "Match Move Ctl", None, -1))

