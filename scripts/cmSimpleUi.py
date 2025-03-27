# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cmSimpleUi.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

try: # Maya 2025
    from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
        QFrame, QGridLayout, QGroupBox, QLabel,
        QLineEdit, QMainWindow, QPushButton, QSizePolicy,
        QSpacerItem, QSpinBox, QTabWidget, QWidget)
except: # Maya 2024
    from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide2.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
        QFrame, QGridLayout, QGroupBox, QLabel,
        QLineEdit, QMainWindow, QPushButton, QSizePolicy,
        QSpacerItem, QSpinBox, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(883, 627)
        MainWindow.setMinimumSize(QSize(130, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(239, 182, 0);\n"
"}")
        self.gridLayout_70 = QGridLayout(self.centralwidget)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 220))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(255, 194, 0);\n"
"}")
        self.gridLayout_56 = QGridLayout(self.groupBox)
        self.gridLayout_56.setSpacing(3)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_2 = QSpacerItem(66, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setSpacing(3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_17 = QGroupBox(self.groupBox)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setMinimumSize(QSize(500, 0))
        self.groupBox_17.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_7 = QGridLayout(self.groupBox_17)
        self.gridLayout_7.setSpacing(3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lne_globCtlSuffix = QLineEdit(self.groupBox_17)
        self.lne_globCtlSuffix.setObjectName(u"lne_globCtlSuffix")
        self.lne_globCtlSuffix.setMinimumSize(QSize(0, 0))
        self.lne_globCtlSuffix.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lne_globCtlSuffix, 0, 0, 1, 1)

        self.lne_globJntSuffix = QLineEdit(self.groupBox_17)
        self.lne_globJntSuffix.setObjectName(u"lne_globJntSuffix")
        self.lne_globJntSuffix.setMinimumSize(QSize(0, 0))
        self.lne_globJntSuffix.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lne_globJntSuffix, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_globCtlShape = QLabel(self.groupBox_17)
        self.lbl_globCtlShape.setObjectName(u"lbl_globCtlShape")
        self.lbl_globCtlShape.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_globCtlShape, 0, 0, 1, 1)

        self.cbo_globCtlShape = QComboBox(self.groupBox_17)
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
        self.cbo_globCtlShape.setObjectName(u"cbo_globCtlShape")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo_globCtlShape.sizePolicy().hasHeightForWidth())
        self.cbo_globCtlShape.setSizePolicy(sizePolicy)
        self.cbo_globCtlShape.setMinimumSize(QSize(0, 0))
        self.cbo_globCtlShape.setMaximumSize(QSize(16777215, 16777215))
        self.cbo_globCtlShape.setMaxVisibleItems(50)

        self.gridLayout_2.addWidget(self.cbo_globCtlShape, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lbl_globCtlColor = QLabel(self.groupBox_17)
        self.lbl_globCtlColor.setObjectName(u"lbl_globCtlColor")
        self.lbl_globCtlColor.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_globCtlColor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lbl_globCtlColor, 0, 0, 1, 1)

        self.cbo_globCtlColor = QComboBox(self.groupBox_17)
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
        self.cbo_globCtlColor.setObjectName(u"cbo_globCtlColor")
        sizePolicy.setHeightForWidth(self.cbo_globCtlColor.sizePolicy().hasHeightForWidth())
        self.cbo_globCtlColor.setSizePolicy(sizePolicy)
        self.cbo_globCtlColor.setMinimumSize(QSize(0, 0))
        self.cbo_globCtlColor.setMaximumSize(QSize(16777215, 16777215))
        self.cbo_globCtlColor.setMaxVisibleItems(50)

        self.gridLayout_4.addWidget(self.cbo_globCtlColor, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lbl_globCtlSize = QLabel(self.groupBox_17)
        self.lbl_globCtlSize.setObjectName(u"lbl_globCtlSize")
        self.lbl_globCtlSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.lbl_globCtlSize, 0, 0, 1, 1)

        self.spn_globCtlSize = QDoubleSpinBox(self.groupBox_17)
        self.spn_globCtlSize.setObjectName(u"spn_globCtlSize")
        sizePolicy.setHeightForWidth(self.spn_globCtlSize.sizePolicy().hasHeightForWidth())
        self.spn_globCtlSize.setSizePolicy(sizePolicy)
        self.spn_globCtlSize.setMinimumSize(QSize(0, 0))
        self.spn_globCtlSize.setMaximumSize(QSize(75, 16777215))
        self.spn_globCtlSize.setDecimals(2)
        self.spn_globCtlSize.setMaximum(1000.000000000000000)
        self.spn_globCtlSize.setSingleStep(0.100000000000000)
        self.spn_globCtlSize.setValue(1.000000000000000)

        self.gridLayout_5.addWidget(self.spn_globCtlSize, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_globAutoColorMargin = QLabel(self.groupBox_17)
        self.lbl_globAutoColorMargin.setObjectName(u"lbl_globAutoColorMargin")
        self.lbl_globAutoColorMargin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_globAutoColorMargin, 0, 0, 1, 1)

        self.spn_globAutoColorMargin = QDoubleSpinBox(self.groupBox_17)
        self.spn_globAutoColorMargin.setObjectName(u"spn_globAutoColorMargin")
        self.spn_globAutoColorMargin.setMaximumSize(QSize(75, 16777215))
        self.spn_globAutoColorMargin.setDecimals(3)
        self.spn_globAutoColorMargin.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.spn_globAutoColorMargin, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 2, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_17, 0, 0, 1, 1)

        self.groupBox_31 = QGroupBox(self.groupBox)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_31.sizePolicy().hasHeightForWidth())
        self.groupBox_31.setSizePolicy(sizePolicy1)
        self.groupBox_31.setMinimumSize(QSize(120, 0))
        self.groupBox_31.setMaximumSize(QSize(16777215, 50))
        self.groupBox_31.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_8 = QGridLayout(self.groupBox_31)
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_setCtlColor = QPushButton(self.groupBox_31)
        self.btn_setCtlColor.setObjectName(u"btn_setCtlColor")
        self.btn_setCtlColor.setMinimumSize(QSize(0, 25))
        self.btn_setCtlColor.setMaximumSize(QSize(16777215, 20))
        self.btn_setCtlColor.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_3.addWidget(self.btn_setCtlColor, 0, 2, 1, 1)

        self.btn_setCtlSize = QPushButton(self.groupBox_31)
        self.btn_setCtlSize.setObjectName(u"btn_setCtlSize")
        self.btn_setCtlSize.setMinimumSize(QSize(0, 25))
        self.btn_setCtlSize.setMaximumSize(QSize(16777215, 20))
        self.btn_setCtlSize.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_3.addWidget(self.btn_setCtlSize, 0, 0, 1, 1)

        self.btn_setCtlShape = QPushButton(self.groupBox_31)
        self.btn_setCtlShape.setObjectName(u"btn_setCtlShape")
        self.btn_setCtlShape.setMinimumSize(QSize(0, 25))
        self.btn_setCtlShape.setMaximumSize(QSize(16777215, 20))
        self.btn_setCtlShape.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_3.addWidget(self.btn_setCtlShape, 0, 1, 1, 1)

        self.btn_setCtlVis = QPushButton(self.groupBox_31)
        self.btn_setCtlVis.setObjectName(u"btn_setCtlVis")
        self.btn_setCtlVis.setMinimumSize(QSize(0, 25))
        self.btn_setCtlVis.setMaximumSize(QSize(16777215, 20))
        self.btn_setCtlVis.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_3.addWidget(self.btn_setCtlVis, 0, 3, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_31, 1, 0, 1, 1)


        self.gridLayout_56.addLayout(self.gridLayout_9, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(67, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.groupBox_35 = QGroupBox(self.groupBox)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.groupBox_35.setMinimumSize(QSize(150, 0))
        self.groupBox_35.setMaximumSize(QSize(16777215, 50))
        self.groupBox_35.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_115 = QGridLayout(self.groupBox_35)
        self.gridLayout_115.setSpacing(3)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.gridLayout_115.setContentsMargins(5, 5, 5, 5)
        self.btn_selBySuffix = QPushButton(self.groupBox_35)
        self.btn_selBySuffix.setObjectName(u"btn_selBySuffix")
        self.btn_selBySuffix.setMinimumSize(QSize(180, 25))
        self.btn_selBySuffix.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_115.addWidget(self.btn_selBySuffix, 0, 1, 1, 1)

        self.cbo_selSuffix = QComboBox(self.groupBox_35)
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
        self.cbo_selSuffix.setObjectName(u"cbo_selSuffix")
        self.cbo_selSuffix.setStyleSheet(u"")

        self.gridLayout_115.addWidget(self.cbo_selSuffix, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_56.addWidget(self.groupBox_35, 1, 1, 1, 1)


        self.gridLayout_70.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(0, 0))
        self.tabWidget_2.setStyleSheet(u"QTabBar::scroller {width: 90px; }\n"
"")
        self.tabWidget_2.setTabPosition(QTabWidget.North)
        self.tabWidget_2.setIconSize(QSize(16, 16))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_13 = QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(290, 0))
        self.groupBox_3.setMaximumSize(QSize(290, 120))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_19 = QGridLayout(self.groupBox_3)
        self.gridLayout_19.setSpacing(6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setSpacing(3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.cbo_axisLockUnlock = QComboBox(self.groupBox_3)
        self.cbo_axisLockUnlock.addItem("")
        self.cbo_axisLockUnlock.addItem("")
        self.cbo_axisLockUnlock.addItem("")
        self.cbo_axisLockUnlock.setObjectName(u"cbo_axisLockUnlock")

        self.gridLayout_17.addWidget(self.cbo_axisLockUnlock, 0, 0, 1, 1)

        self.cbo_hideUnhide = QComboBox(self.groupBox_3)
        self.cbo_hideUnhide.addItem("")
        self.cbo_hideUnhide.addItem("")
        self.cbo_hideUnhide.addItem("")
        self.cbo_hideUnhide.setObjectName(u"cbo_hideUnhide")

        self.gridLayout_17.addWidget(self.cbo_hideUnhide, 0, 1, 1, 1)

        self.btn_axisGo = QPushButton(self.groupBox_3)
        self.btn_axisGo.setObjectName(u"btn_axisGo")
        self.btn_axisGo.setMinimumSize(QSize(0, 25))
        self.btn_axisGo.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_17.addWidget(self.btn_axisGo, 1, 0, 1, 2)


        self.gridLayout_19.addLayout(self.gridLayout_17, 0, 1, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setSpacing(3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.chk_axisTX = QCheckBox(self.groupBox_3)
        self.chk_axisTX.setObjectName(u"chk_axisTX")
        self.chk_axisTX.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_axisTX, 1, 0, 1, 1)

        self.chk_axisRZ = QCheckBox(self.groupBox_3)
        self.chk_axisRZ.setObjectName(u"chk_axisRZ")
        self.chk_axisRZ.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_axisRZ, 3, 1, 1, 1)

        self.chk_axisSY = QCheckBox(self.groupBox_3)
        self.chk_axisSY.setObjectName(u"chk_axisSY")
        self.chk_axisSY.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_axisSY, 2, 2, 1, 1)

        self.chk_axisTY = QCheckBox(self.groupBox_3)
        self.chk_axisTY.setObjectName(u"chk_axisTY")
        self.chk_axisTY.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_axisTY, 2, 0, 1, 1)

        self.chk_axisRX = QCheckBox(self.groupBox_3)
        self.chk_axisRX.setObjectName(u"chk_axisRX")
        self.chk_axisRX.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_axisRX, 1, 1, 1, 1)

        self.chk_axisSX = QCheckBox(self.groupBox_3)
        self.chk_axisSX.setObjectName(u"chk_axisSX")
        self.chk_axisSX.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_axisSX, 1, 2, 1, 1)

        self.chk_axisRY = QCheckBox(self.groupBox_3)
        self.chk_axisRY.setObjectName(u"chk_axisRY")
        self.chk_axisRY.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_axisRY, 2, 1, 1, 1)

        self.chk_axisSZ = QCheckBox(self.groupBox_3)
        self.chk_axisSZ.setObjectName(u"chk_axisSZ")
        self.chk_axisSZ.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_axisSZ, 3, 2, 1, 1)

        self.chk_axisTZ = QCheckBox(self.groupBox_3)
        self.chk_axisTZ.setObjectName(u"chk_axisTZ")
        self.chk_axisTZ.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_axisTZ, 3, 0, 1, 1)

        self.chk_T = QCheckBox(self.groupBox_3)
        self.chk_T.setObjectName(u"chk_T")
        self.chk_T.setStyleSheet(u"QCheckBox { color: rgb(239, 182, 0) };")
        self.chk_T.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_T, 0, 0, 1, 1)

        self.chk_R = QCheckBox(self.groupBox_3)
        self.chk_R.setObjectName(u"chk_R")
        self.chk_R.setStyleSheet(u"QCheckBox { color: rgb(239, 182, 0) };")
        self.chk_R.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_R, 0, 1, 1, 1)

        self.chk_S = QCheckBox(self.groupBox_3)
        self.chk_S.setObjectName(u"chk_S")
        self.chk_S.setStyleSheet(u"QCheckBox { color: rgb(239, 182, 0) };")
        self.chk_S.setChecked(True)

        self.gridLayout_15.addWidget(self.chk_S, 0, 2, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_38 = QGroupBox(self.tab_3)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.groupBox_38.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.groupBox_38.sizePolicy().hasHeightForWidth())
        self.groupBox_38.setSizePolicy(sizePolicy1)
        self.groupBox_38.setMinimumSize(QSize(290, 0))
        self.groupBox_38.setMaximumSize(QSize(290, 94))
        self.groupBox_38.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_111 = QGridLayout(self.groupBox_38)
        self.gridLayout_111.setSpacing(3)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.gridLayout_111.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_112 = QGridLayout()
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.chk_maintainOffset = QCheckBox(self.groupBox_38)
        self.chk_maintainOffset.setObjectName(u"chk_maintainOffset")
        self.chk_maintainOffset.setMaximumSize(QSize(50, 16777215))
        self.chk_maintainOffset.setLayoutDirection(Qt.RightToLeft)
        self.chk_maintainOffset.setChecked(True)

        self.gridLayout_112.addWidget(self.chk_maintainOffset, 0, 0, 1, 1)

        self.btn_createMatCon = QPushButton(self.groupBox_38)
        self.btn_createMatCon.setObjectName(u"btn_createMatCon")
        self.btn_createMatCon.setMinimumSize(QSize(120, 25))
        self.btn_createMatCon.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_112.addWidget(self.btn_createMatCon, 0, 1, 1, 1)

        self.btn_delMatCon = QPushButton(self.groupBox_38)
        self.btn_delMatCon.setObjectName(u"btn_delMatCon")
        self.btn_delMatCon.setMinimumSize(QSize(100, 25))
        self.btn_delMatCon.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_112.addWidget(self.btn_delMatCon, 1, 0, 1, 2)


        self.gridLayout_111.addLayout(self.gridLayout_112, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_38, 1, 0, 1, 1)

        self.groupBox_36 = QGroupBox(self.tab_3)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.groupBox_36.sizePolicy().hasHeightForWidth())
        self.groupBox_36.setSizePolicy(sizePolicy1)
        self.groupBox_36.setMinimumSize(QSize(290, 0))
        self.groupBox_36.setMaximumSize(QSize(290, 125))
        self.groupBox_36.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_11 = QGridLayout(self.groupBox_36)
        self.gridLayout_11.setSpacing(3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.btn_globalSclObj = QPushButton(self.groupBox_36)
        self.btn_globalSclObj.setObjectName(u"btn_globalSclObj")
        self.btn_globalSclObj.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_16.addWidget(self.btn_globalSclObj, 0, 1, 1, 1)

        self.btn_globalScaleConnect = QPushButton(self.groupBox_36)
        self.btn_globalScaleConnect.setObjectName(u"btn_globalScaleConnect")
        self.btn_globalScaleConnect.setMinimumSize(QSize(100, 25))
        self.btn_globalScaleConnect.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_16.addWidget(self.btn_globalScaleConnect, 2, 0, 1, 2)

        self.btn_directConnect = QPushButton(self.groupBox_36)
        self.btn_directConnect.setObjectName(u"btn_directConnect")
        self.btn_directConnect.setMinimumSize(QSize(100, 25))
        self.btn_directConnect.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_16.addWidget(self.btn_directConnect, 1, 0, 1, 2)

        self.lne_globalSclObj = QLineEdit(self.groupBox_36)
        self.lne_globalSclObj.setObjectName(u"lne_globalSclObj")

        self.gridLayout_16.addWidget(self.lne_globalSclObj, 0, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_16, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_36, 2, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 247, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_8, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_42 = QGridLayout(self.tab_12)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_39.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.groupBox_22 = QGroupBox(self.tab_12)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setMinimumSize(QSize(300, 75))
        self.groupBox_22.setMaximumSize(QSize(300, 75))
        self.groupBox_22.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_92 = QGridLayout(self.groupBox_22)
        self.gridLayout_92.setSpacing(3)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.gridLayout_92.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_91 = QGridLayout()
        self.gridLayout_91.setSpacing(3)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.btn_importWeights = QPushButton(self.groupBox_22)
        self.btn_importWeights.setObjectName(u"btn_importWeights")
        self.btn_importWeights.setMinimumSize(QSize(0, 25))
        self.btn_importWeights.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_91.addWidget(self.btn_importWeights, 0, 0, 1, 1)

        self.btn_exportWeights = QPushButton(self.groupBox_22)
        self.btn_exportWeights.setObjectName(u"btn_exportWeights")
        self.btn_exportWeights.setMinimumSize(QSize(0, 25))
        self.btn_exportWeights.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_91.addWidget(self.btn_exportWeights, 0, 1, 1, 1)


        self.gridLayout_92.addLayout(self.gridLayout_91, 0, 0, 1, 1)

        self.btn_selectClstrInfl = QPushButton(self.groupBox_22)
        self.btn_selectClstrInfl.setObjectName(u"btn_selectClstrInfl")
        self.btn_selectClstrInfl.setMinimumSize(QSize(100, 25))
        self.btn_selectClstrInfl.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_92.addWidget(self.btn_selectClstrInfl, 1, 0, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_22, 0, 0, 1, 1)

        self.groupBox_40 = QGroupBox(self.tab_12)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.groupBox_40.setMinimumSize(QSize(300, 50))
        self.groupBox_40.setMaximumSize(QSize(300, 50))
        self.groupBox_40.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_14 = QGridLayout(self.groupBox_40)
        self.gridLayout_14.setSpacing(3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_47 = QGridLayout()
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.btn_transferWeights = QPushButton(self.groupBox_40)
        self.btn_transferWeights.setObjectName(u"btn_transferWeights")
        self.btn_transferWeights.setMinimumSize(QSize(160, 25))
        self.btn_transferWeights.setMaximumSize(QSize(160, 16777215))
        self.btn_transferWeights.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_47.addWidget(self.btn_transferWeights, 0, 0, 1, 1)

        self.chk_transferWeightsRemove = QCheckBox(self.groupBox_40)
        self.chk_transferWeightsRemove.setObjectName(u"chk_transferWeightsRemove")

        self.gridLayout_47.addWidget(self.chk_transferWeightsRemove, 0, 1, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_47, 0, 0, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_40, 1, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.tab_12)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setMinimumSize(QSize(300, 80))
        self.groupBox_20.setMaximumSize(QSize(300, 80))
        self.groupBox_20.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_71 = QGridLayout(self.groupBox_20)
        self.gridLayout_71.setSpacing(3)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_71.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_68 = QGridLayout()
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.cbo_preBindJoint = QComboBox(self.groupBox_20)
        self.cbo_preBindJoint.addItem("")
        self.cbo_preBindJoint.addItem("")
        self.cbo_preBindJoint.setObjectName(u"cbo_preBindJoint")

        self.gridLayout_68.addWidget(self.cbo_preBindJoint, 0, 0, 1, 1)

        self.cbo_preBindBfr = QComboBox(self.groupBox_20)
        self.cbo_preBindBfr.addItem("")
        self.cbo_preBindBfr.addItem("")
        self.cbo_preBindBfr.addItem("")
        self.cbo_preBindBfr.setObjectName(u"cbo_preBindBfr")

        self.gridLayout_68.addWidget(self.cbo_preBindBfr, 0, 1, 1, 1)

        self.btn_ctlPreBindMat = QPushButton(self.groupBox_20)
        self.btn_ctlPreBindMat.setObjectName(u"btn_ctlPreBindMat")
        self.btn_ctlPreBindMat.setEnabled(True)
        self.btn_ctlPreBindMat.setMinimumSize(QSize(100, 25))
        self.btn_ctlPreBindMat.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_68.addWidget(self.btn_ctlPreBindMat, 1, 0, 1, 2)


        self.gridLayout_71.addLayout(self.gridLayout_68, 0, 0, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_20, 2, 0, 1, 1)

        self.groupBox_43 = QGroupBox(self.tab_12)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.groupBox_43.setMinimumSize(QSize(300, 50))
        self.groupBox_43.setMaximumSize(QSize(300, 50))
        self.groupBox_43.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_29 = QGridLayout(self.groupBox_43)
        self.gridLayout_29.setSpacing(3)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_67 = QGridLayout()
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.btn_resetBindPose = QPushButton(self.groupBox_43)
        self.btn_resetBindPose.setObjectName(u"btn_resetBindPose")
        self.btn_resetBindPose.setMinimumSize(QSize(160, 25))
        self.btn_resetBindPose.setMaximumSize(QSize(160, 16777215))
        self.btn_resetBindPose.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_67.addWidget(self.btn_resetBindPose, 0, 0, 1, 1)

        self.chk_bindPoseAngle = QCheckBox(self.groupBox_43)
        self.chk_bindPoseAngle.setObjectName(u"chk_bindPoseAngle")

        self.gridLayout_67.addWidget(self.chk_bindPoseAngle, 0, 1, 1, 1)


        self.gridLayout_29.addLayout(self.gridLayout_67, 0, 0, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_43, 3, 0, 1, 1)


        self.gridLayout_39.addLayout(self.gridLayout_30, 0, 0, 1, 1)


        self.gridLayout_42.addLayout(self.gridLayout_39, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_50 = QGridLayout(self.tab_7)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_48 = QGridLayout()
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.groupBox_39 = QGroupBox(self.tab_7)
        self.groupBox_39.setObjectName(u"groupBox_39")
        sizePolicy1.setHeightForWidth(self.groupBox_39.sizePolicy().hasHeightForWidth())
        self.groupBox_39.setSizePolicy(sizePolicy1)
        self.groupBox_39.setMinimumSize(QSize(250, 80))
        self.groupBox_39.setMaximumSize(QSize(250, 80))
        self.groupBox_39.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_31 = QGridLayout(self.groupBox_39)
        self.gridLayout_31.setSpacing(3)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setSpacing(3)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.btn_meshUpdateOrig = QPushButton(self.groupBox_39)
        self.btn_meshUpdateOrig.setObjectName(u"btn_meshUpdateOrig")
        self.btn_meshUpdateOrig.setMinimumSize(QSize(110, 25))
        self.btn_meshUpdateOrig.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_28.addWidget(self.btn_meshUpdateOrig, 0, 0, 1, 1)

        self.chk_updateAuto = QCheckBox(self.groupBox_39)
        self.chk_updateAuto.setObjectName(u"chk_updateAuto")
        self.chk_updateAuto.setEnabled(True)
        self.chk_updateAuto.setMaximumSize(QSize(70, 16777215))
        self.chk_updateAuto.setChecked(False)

        self.gridLayout_28.addWidget(self.chk_updateAuto, 0, 1, 1, 1)

        self.btn_meshMatchPoint = QPushButton(self.groupBox_39)
        self.btn_meshMatchPoint.setObjectName(u"btn_meshMatchPoint")
        self.btn_meshMatchPoint.setMinimumSize(QSize(110, 25))
        self.btn_meshMatchPoint.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_28.addWidget(self.btn_meshMatchPoint, 1, 0, 1, 2)


        self.gridLayout_31.addLayout(self.gridLayout_28, 0, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_39, 0, 0, 1, 1)

        self.groupBox_44 = QGroupBox(self.tab_7)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.groupBox_44.setMinimumSize(QSize(250, 120))
        self.groupBox_44.setMaximumSize(QSize(250, 120))
        self.groupBox_44.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_121 = QGridLayout(self.groupBox_44)
        self.gridLayout_121.setSpacing(3)
        self.gridLayout_121.setObjectName(u"gridLayout_121")
        self.gridLayout_121.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setSpacing(3)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.btn_smoothEdges = QPushButton(self.groupBox_44)
        self.btn_smoothEdges.setObjectName(u"btn_smoothEdges")
        self.btn_smoothEdges.setEnabled(True)
        self.btn_smoothEdges.setMinimumSize(QSize(0, 25))
        self.btn_smoothEdges.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_32.addWidget(self.btn_smoothEdges, 0, 0, 1, 1)

        self.btn_delUnShp = QPushButton(self.groupBox_44)
        self.btn_delUnShp.setObjectName(u"btn_delUnShp")
        self.btn_delUnShp.setMinimumSize(QSize(0, 25))
        self.btn_delUnShp.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_32.addWidget(self.btn_delUnShp, 1, 0, 1, 1)


        self.gridLayout_121.addLayout(self.gridLayout_32, 0, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_44, 1, 0, 1, 1)


        self.gridLayout_50.addLayout(self.gridLayout_48, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 295, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_50.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_51 = QGridLayout(self.tab_5)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.horizontalSpacer_11 = QSpacerItem(26, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_51.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.grp_strapGuide = QGroupBox(self.tab_5)
        self.grp_strapGuide.setObjectName(u"grp_strapGuide")
        self.grp_strapGuide.setEnabled(True)
        self.grp_strapGuide.setMinimumSize(QSize(0, 0))
        self.grp_strapGuide.setMaximumSize(QSize(16777215, 16777215))
        self.grp_strapGuide.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_41 = QGridLayout(self.grp_strapGuide)
        self.gridLayout_41.setSpacing(6)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_40 = QGridLayout()
        self.gridLayout_40.setSpacing(3)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.btn_prepSrf = QPushButton(self.grp_strapGuide)
        self.btn_prepSrf.setObjectName(u"btn_prepSrf")
        self.btn_prepSrf.setMinimumSize(QSize(0, 25))
        self.btn_prepSrf.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_40.addWidget(self.btn_prepSrf, 0, 0, 1, 2)

        self.btn_swapUV = QPushButton(self.grp_strapGuide)
        self.btn_swapUV.setObjectName(u"btn_swapUV")
        self.btn_swapUV.setMinimumSize(QSize(0, 25))
        self.btn_swapUV.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_40.addWidget(self.btn_swapUV, 0, 2, 1, 2)

        self.line_3 = QFrame(self.grp_strapGuide)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_40.addWidget(self.line_3, 1, 0, 1, 4)

        self.spn_strapGuideRow = QSpinBox(self.grp_strapGuide)
        self.spn_strapGuideRow.setObjectName(u"spn_strapGuideRow")
        self.spn_strapGuideRow.setMinimumSize(QSize(75, 20))
        self.spn_strapGuideRow.setMaximumSize(QSize(75, 16777215))
        self.spn_strapGuideRow.setMinimum(1)
        self.spn_strapGuideRow.setValue(1)

        self.gridLayout_40.addWidget(self.spn_strapGuideRow, 2, 0, 1, 1)

        self.lbl_strapGuideRow = QLabel(self.grp_strapGuide)
        self.lbl_strapGuideRow.setObjectName(u"lbl_strapGuideRow")
        self.lbl_strapGuideRow.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.lbl_strapGuideRow, 2, 1, 1, 1)

        self.spn_strapGuideColumn = QSpinBox(self.grp_strapGuide)
        self.spn_strapGuideColumn.setObjectName(u"spn_strapGuideColumn")
        self.spn_strapGuideColumn.setMinimumSize(QSize(75, 20))
        self.spn_strapGuideColumn.setMaximumSize(QSize(75, 16777215))
        self.spn_strapGuideColumn.setMinimum(1)
        self.spn_strapGuideColumn.setValue(5)

        self.gridLayout_40.addWidget(self.spn_strapGuideColumn, 2, 2, 1, 1)

        self.lbl_strapGuideColumn = QLabel(self.grp_strapGuide)
        self.lbl_strapGuideColumn.setObjectName(u"lbl_strapGuideColumn")
        self.lbl_strapGuideColumn.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.lbl_strapGuideColumn, 2, 3, 1, 1)

        self.line_18 = QFrame(self.grp_strapGuide)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_40.addWidget(self.line_18, 3, 0, 1, 4)

        self.chk_strapSkipLast = QCheckBox(self.grp_strapGuide)
        self.chk_strapSkipLast.setObjectName(u"chk_strapSkipLast")
        self.chk_strapSkipLast.setLayoutDirection(Qt.LeftToRight)
        self.chk_strapSkipLast.setChecked(False)

        self.gridLayout_40.addWidget(self.chk_strapSkipLast, 4, 0, 1, 2)

        self.btn_goGuidesOnSrf = QPushButton(self.grp_strapGuide)
        self.btn_goGuidesOnSrf.setObjectName(u"btn_goGuidesOnSrf")
        self.btn_goGuidesOnSrf.setMinimumSize(QSize(0, 25))
        self.btn_goGuidesOnSrf.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_40.addWidget(self.btn_goGuidesOnSrf, 4, 2, 1, 2)


        self.gridLayout_41.addLayout(self.gridLayout_40, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.grp_strapGuide, 0, 0, 1, 1)

        self.grp_strapRig = QGroupBox(self.tab_5)
        self.grp_strapRig.setObjectName(u"grp_strapRig")
        self.grp_strapRig.setEnabled(True)
        self.grp_strapRig.setMinimumSize(QSize(0, 0))
        self.grp_strapRig.setMaximumSize(QSize(16777215, 16777215))
        self.grp_strapRig.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.grp_strapRig.setAlignment(Qt.AlignCenter)
        self.gridLayout_45 = QGridLayout(self.grp_strapRig)
        self.gridLayout_45.setSpacing(6)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_44 = QGridLayout()
        self.gridLayout_44.setSpacing(3)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.spn_strapJntRow = QSpinBox(self.grp_strapRig)
        self.spn_strapJntRow.setObjectName(u"spn_strapJntRow")
        self.spn_strapJntRow.setMinimumSize(QSize(50, 20))
        self.spn_strapJntRow.setMaximumSize(QSize(50, 16777215))
        self.spn_strapJntRow.setMinimum(0)
        self.spn_strapJntRow.setMaximum(1000)
        self.spn_strapJntRow.setValue(0)

        self.gridLayout_44.addWidget(self.spn_strapJntRow, 0, 0, 1, 1)

        self.lbl_strapJntRow_3 = QLabel(self.grp_strapRig)
        self.lbl_strapJntRow_3.setObjectName(u"lbl_strapJntRow_3")

        self.gridLayout_44.addWidget(self.lbl_strapJntRow_3, 0, 1, 1, 2)

        self.spn_strapJntColumn = QSpinBox(self.grp_strapRig)
        self.spn_strapJntColumn.setObjectName(u"spn_strapJntColumn")
        self.spn_strapJntColumn.setMinimumSize(QSize(50, 20))
        self.spn_strapJntColumn.setMaximumSize(QSize(50, 16777215))
        self.spn_strapJntColumn.setMinimum(1)
        self.spn_strapJntColumn.setMaximum(1000)
        self.spn_strapJntColumn.setValue(10)

        self.gridLayout_44.addWidget(self.spn_strapJntColumn, 0, 3, 1, 1)

        self.lbl_strapJntColumn_2 = QLabel(self.grp_strapRig)
        self.lbl_strapJntColumn_2.setObjectName(u"lbl_strapJntColumn_2")
        self.lbl_strapJntColumn_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_44.addWidget(self.lbl_strapJntColumn_2, 0, 4, 1, 1)

        self.line_23 = QFrame(self.grp_strapRig)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_44.addWidget(self.line_23, 1, 0, 1, 5)

        self.spn_ikSplineNum = QSpinBox(self.grp_strapRig)
        self.spn_ikSplineNum.setObjectName(u"spn_ikSplineNum")
        self.spn_ikSplineNum.setEnabled(False)
        self.spn_ikSplineNum.setMinimumSize(QSize(50, 20))
        self.spn_ikSplineNum.setMaximumSize(QSize(50, 16777215))
        self.spn_ikSplineNum.setValue(10)

        self.gridLayout_44.addWidget(self.spn_ikSplineNum, 2, 3, 1, 1)

        self.lbl_ikSplineNo_2 = QLabel(self.grp_strapRig)
        self.lbl_ikSplineNo_2.setObjectName(u"lbl_ikSplineNo_2")
        self.lbl_ikSplineNo_2.setEnabled(True)
        self.lbl_ikSplineNo_2.setLayoutDirection(Qt.LeftToRight)
        self.lbl_ikSplineNo_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_44.addWidget(self.lbl_ikSplineNo_2, 2, 4, 1, 1)

        self.line_24 = QFrame(self.grp_strapRig)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.HLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_44.addWidget(self.line_24, 3, 0, 1, 5)

        self.chk_makeCtlFK = QCheckBox(self.grp_strapRig)
        self.chk_makeCtlFK.setObjectName(u"chk_makeCtlFK")
        self.chk_makeCtlFK.setLayoutDirection(Qt.LeftToRight)
        self.chk_makeCtlFK.setChecked(True)

        self.gridLayout_44.addWidget(self.chk_makeCtlFK, 4, 0, 1, 2)

        self.chk_lra = QCheckBox(self.grp_strapRig)
        self.chk_lra.setObjectName(u"chk_lra")
        self.chk_lra.setChecked(False)

        self.gridLayout_44.addWidget(self.chk_lra, 4, 2, 1, 3)

        self.line_17 = QFrame(self.grp_strapRig)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_44.addWidget(self.line_17, 5, 0, 1, 5)

        self.btn_goStrapRig = QPushButton(self.grp_strapRig)
        self.btn_goStrapRig.setObjectName(u"btn_goStrapRig")
        self.btn_goStrapRig.setMinimumSize(QSize(0, 25))
        self.btn_goStrapRig.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_44.addWidget(self.btn_goStrapRig, 6, 0, 1, 5)

        self.chk_ikSpline = QCheckBox(self.grp_strapRig)
        self.chk_ikSpline.setObjectName(u"chk_ikSpline")

        self.gridLayout_44.addWidget(self.chk_ikSpline, 2, 0, 1, 3)


        self.gridLayout_45.addLayout(self.gridLayout_44, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.grp_strapRig, 0, 1, 1, 1)


        self.gridLayout_51.addLayout(self.gridLayout_18, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_51.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 449, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_51.addItem(self.verticalSpacer_4, 1, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_52 = QGridLayout(self.tab_6)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.groupBox_24 = QGroupBox(self.tab_6)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setEnabled(True)
        self.groupBox_24.setMinimumSize(QSize(200, 0))
        self.groupBox_24.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_24.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_124 = QGridLayout(self.groupBox_24)
        self.gridLayout_124.setSpacing(6)
        self.gridLayout_124.setObjectName(u"gridLayout_124")
        self.gridLayout_124.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_125 = QGridLayout()
        self.gridLayout_125.setObjectName(u"gridLayout_125")
        self.spn_gdeOnCrv = QSpinBox(self.groupBox_24)
        self.spn_gdeOnCrv.setObjectName(u"spn_gdeOnCrv")
        self.spn_gdeOnCrv.setMinimumSize(QSize(75, 0))
        self.spn_gdeOnCrv.setMaximumSize(QSize(75, 16777215))
        self.spn_gdeOnCrv.setAlignment(Qt.AlignCenter)
        self.spn_gdeOnCrv.setMinimum(2)
        self.spn_gdeOnCrv.setMaximum(1000)
        self.spn_gdeOnCrv.setValue(2)

        self.gridLayout_125.addWidget(self.spn_gdeOnCrv, 0, 0, 1, 1)

        self.btn_gdeOnCrvGo = QPushButton(self.groupBox_24)
        self.btn_gdeOnCrvGo.setObjectName(u"btn_gdeOnCrvGo")
        self.btn_gdeOnCrvGo.setMinimumSize(QSize(100, 25))
        self.btn_gdeOnCrvGo.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_125.addWidget(self.btn_gdeOnCrvGo, 0, 1, 1, 1)


        self.gridLayout_124.addLayout(self.gridLayout_125, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.groupBox_24, 0, 1, 1, 1)

        self.groupBox_27 = QGroupBox(self.tab_6)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setEnabled(True)
        self.groupBox_27.setMinimumSize(QSize(200, 0))
        self.groupBox_27.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_27.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_126 = QGridLayout(self.groupBox_27)
        self.gridLayout_126.setSpacing(6)
        self.gridLayout_126.setObjectName(u"gridLayout_126")
        self.gridLayout_126.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_127 = QGridLayout()
        self.gridLayout_127.setObjectName(u"gridLayout_127")
        self.cbo_crvRigType = QComboBox(self.groupBox_27)
        self.cbo_crvRigType.addItem("")
        self.cbo_crvRigType.addItem("")
        self.cbo_crvRigType.setObjectName(u"cbo_crvRigType")
        self.cbo_crvRigType.setEnabled(True)
        self.cbo_crvRigType.setAutoFillBackground(False)

        self.gridLayout_127.addWidget(self.cbo_crvRigType, 0, 0, 1, 1)

        self.btn_bldCrvRigGo = QPushButton(self.groupBox_27)
        self.btn_bldCrvRigGo.setObjectName(u"btn_bldCrvRigGo")
        self.btn_bldCrvRigGo.setMinimumSize(QSize(100, 25))
        self.btn_bldCrvRigGo.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_127.addWidget(self.btn_bldCrvRigGo, 0, 1, 1, 1)


        self.gridLayout_126.addLayout(self.gridLayout_127, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.groupBox_27, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)


        self.gridLayout_52.addLayout(self.gridLayout_20, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 536, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_52.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_22 = QGridLayout(self.tab_8)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.groupBox_13 = QGroupBox(self.tab_8)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(400, 90))
        self.groupBox_13.setMaximumSize(QSize(400, 90))
        self.groupBox_13.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_65 = QGridLayout(self.groupBox_13)
        self.gridLayout_65.setSpacing(5)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_77 = QGridLayout()
        self.gridLayout_77.setSpacing(3)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.gridLayout_83 = QGridLayout()
        self.gridLayout_83.setSpacing(3)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.btn_utilPrepSrf = QPushButton(self.groupBox_13)
        self.btn_utilPrepSrf.setObjectName(u"btn_utilPrepSrf")
        self.btn_utilPrepSrf.setMinimumSize(QSize(100, 25))
        self.btn_utilPrepSrf.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_83.addWidget(self.btn_utilPrepSrf, 0, 0, 1, 1)

        self.btn_utilSwapUV = QPushButton(self.groupBox_13)
        self.btn_utilSwapUV.setObjectName(u"btn_utilSwapUV")
        self.btn_utilSwapUV.setMinimumSize(QSize(0, 25))
        self.btn_utilSwapUV.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_83.addWidget(self.btn_utilSwapUV, 1, 0, 1, 1)


        self.gridLayout_77.addLayout(self.gridLayout_83, 0, 0, 1, 1)

        self.line_6 = QFrame(self.groupBox_13)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_77.addWidget(self.line_6, 0, 1, 1, 1)

        self.gridLayout_86 = QGridLayout()
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.cbo_utilObjType = QComboBox(self.groupBox_13)
        self.cbo_utilObjType.addItem("")
        self.cbo_utilObjType.addItem("")
        self.cbo_utilObjType.setObjectName(u"cbo_utilObjType")
        self.cbo_utilObjType.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_86.addWidget(self.cbo_utilObjType, 0, 0, 1, 1)

        self.gridLayout_88 = QGridLayout()
        self.gridLayout_88.setSpacing(3)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.gridLayout_89 = QGridLayout()
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.spn_utilRow = QSpinBox(self.groupBox_13)
        self.spn_utilRow.setObjectName(u"spn_utilRow")
        self.spn_utilRow.setMinimumSize(QSize(75, 0))
        self.spn_utilRow.setMaximumSize(QSize(75, 16777215))
        self.spn_utilRow.setMinimum(1)
        self.spn_utilRow.setMaximum(500)
        self.spn_utilRow.setValue(1)

        self.gridLayout_89.addWidget(self.spn_utilRow, 0, 0, 1, 1)

        self.lbl_utilRow = QLabel(self.groupBox_13)
        self.lbl_utilRow.setObjectName(u"lbl_utilRow")

        self.gridLayout_89.addWidget(self.lbl_utilRow, 0, 1, 1, 1)


        self.gridLayout_88.addLayout(self.gridLayout_89, 0, 0, 1, 1)

        self.gridLayout_94 = QGridLayout()
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.spn_utilColumn = QSpinBox(self.groupBox_13)
        self.spn_utilColumn.setObjectName(u"spn_utilColumn")
        self.spn_utilColumn.setMinimumSize(QSize(75, 0))
        self.spn_utilColumn.setMaximumSize(QSize(75, 16777215))
        self.spn_utilColumn.setMinimum(1)
        self.spn_utilColumn.setMaximum(500)
        self.spn_utilColumn.setValue(1)

        self.gridLayout_94.addWidget(self.spn_utilColumn, 0, 0, 1, 1)

        self.lbl_utilColumn = QLabel(self.groupBox_13)
        self.lbl_utilColumn.setObjectName(u"lbl_utilColumn")

        self.gridLayout_94.addWidget(self.lbl_utilColumn, 0, 1, 1, 1)


        self.gridLayout_88.addLayout(self.gridLayout_94, 1, 0, 1, 1)


        self.gridLayout_86.addLayout(self.gridLayout_88, 1, 0, 1, 1)


        self.gridLayout_77.addLayout(self.gridLayout_86, 0, 2, 1, 1)

        self.line_25 = QFrame(self.groupBox_13)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_77.addWidget(self.line_25, 0, 3, 1, 1)

        self.gridLayout_99 = QGridLayout()
        self.gridLayout_99.setSpacing(3)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.chk_srfSkipLast = QCheckBox(self.groupBox_13)
        self.chk_srfSkipLast.setObjectName(u"chk_srfSkipLast")
        self.chk_srfSkipLast.setLayoutDirection(Qt.LeftToRight)
        self.chk_srfSkipLast.setChecked(False)

        self.gridLayout_99.addWidget(self.chk_srfSkipLast, 0, 0, 1, 1)

        self.btn_utilCreateOnSrf = QPushButton(self.groupBox_13)
        self.btn_utilCreateOnSrf.setObjectName(u"btn_utilCreateOnSrf")
        self.btn_utilCreateOnSrf.setMinimumSize(QSize(100, 25))
        self.btn_utilCreateOnSrf.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_99.addWidget(self.btn_utilCreateOnSrf, 1, 0, 1, 1)


        self.gridLayout_77.addLayout(self.gridLayout_99, 0, 4, 1, 1)


        self.gridLayout_65.addLayout(self.gridLayout_77, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_13, 0, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_8)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(400, 80))
        self.groupBox_14.setMaximumSize(QSize(400, 80))
        self.groupBox_14.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_100 = QGridLayout(self.groupBox_14)
        self.gridLayout_100.setSpacing(5)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.gridLayout_100.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_101 = QGridLayout()
        self.gridLayout_101.setSpacing(3)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.gridLayout_102 = QGridLayout()
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.spn_crvNumOf = QSpinBox(self.groupBox_14)
        self.spn_crvNumOf.setObjectName(u"spn_crvNumOf")
        self.spn_crvNumOf.setMinimumSize(QSize(75, 0))
        self.spn_crvNumOf.setMaximumSize(QSize(75, 16777215))
        self.spn_crvNumOf.setMinimum(1)
        self.spn_crvNumOf.setMaximum(1000)
        self.spn_crvNumOf.setValue(1)

        self.gridLayout_102.addWidget(self.spn_crvNumOf, 0, 0, 1, 1)

        self.lbl_crvNumOf = QLabel(self.groupBox_14)
        self.lbl_crvNumOf.setObjectName(u"lbl_crvNumOf")

        self.gridLayout_102.addWidget(self.lbl_crvNumOf, 0, 1, 1, 1, Qt.AlignRight)

        self.cbo_crvNumOf = QComboBox(self.groupBox_14)
        self.cbo_crvNumOf.addItem("")
        self.cbo_crvNumOf.addItem("")
        self.cbo_crvNumOf.setObjectName(u"cbo_crvNumOf")
        self.cbo_crvNumOf.setMinimumSize(QSize(270, 0))
        self.cbo_crvNumOf.setMaximumSize(QSize(260, 16777215))

        self.gridLayout_102.addWidget(self.cbo_crvNumOf, 0, 2, 1, 1)


        self.gridLayout_101.addLayout(self.gridLayout_102, 0, 0, 1, 1)

        self.gridLayout_108 = QGridLayout()
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.btn_crvGo = QPushButton(self.groupBox_14)
        self.btn_crvGo.setObjectName(u"btn_crvGo")
        self.btn_crvGo.setMinimumSize(QSize(300, 25))
        self.btn_crvGo.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_108.addWidget(self.btn_crvGo, 0, 1, 1, 1)

        self.chk_crvJntAsChain = QCheckBox(self.groupBox_14)
        self.chk_crvJntAsChain.setObjectName(u"chk_crvJntAsChain")
        self.chk_crvJntAsChain.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_108.addWidget(self.chk_crvJntAsChain, 0, 0, 1, 1)


        self.gridLayout_101.addLayout(self.gridLayout_108, 1, 0, 1, 1)


        self.gridLayout_100.addLayout(self.gridLayout_101, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_14, 1, 0, 1, 1)

        self.groupBox_41 = QGroupBox(self.tab_8)
        self.groupBox_41.setObjectName(u"groupBox_41")
        sizePolicy1.setHeightForWidth(self.groupBox_41.sizePolicy().hasHeightForWidth())
        self.groupBox_41.setSizePolicy(sizePolicy1)
        self.groupBox_41.setMinimumSize(QSize(0, 0))
        self.groupBox_41.setMaximumSize(QSize(16777215, 47))
        self.groupBox_41.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_131 = QGridLayout(self.groupBox_41)
        self.gridLayout_131.setSpacing(5)
        self.gridLayout_131.setObjectName(u"gridLayout_131")
        self.gridLayout_131.setContentsMargins(5, 5, 5, 5)
        self.btn_jntOnVtx = QPushButton(self.groupBox_41)
        self.btn_jntOnVtx.setObjectName(u"btn_jntOnVtx")
        self.btn_jntOnVtx.setMinimumSize(QSize(100, 25))
        self.btn_jntOnVtx.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_131.addWidget(self.btn_jntOnVtx, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_41, 2, 0, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_21, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 295, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_54 = QGridLayout(self.tab_9)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.horizontalSpacer_10 = QSpacerItem(161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_10, 0, 0, 1, 1)

        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setHorizontalSpacing(6)
        self.groupBox_16 = QGroupBox(self.tab_9)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMinimumSize(QSize(330, 80))
        self.groupBox_16.setMaximumSize(QSize(16777215, 80))
        self.groupBox_16.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_118 = QGridLayout(self.groupBox_16)
        self.gridLayout_118.setSpacing(5)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.gridLayout_118.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_119 = QGridLayout()
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.gridLayout_120 = QGridLayout()
        self.gridLayout_120.setObjectName(u"gridLayout_120")
        self.cbo_crvConstType = QComboBox(self.groupBox_16)
        self.cbo_crvConstType.addItem("")
        self.cbo_crvConstType.addItem("")
        self.cbo_crvConstType.addItem("")
        self.cbo_crvConstType.addItem("")
        self.cbo_crvConstType.addItem("")
        self.cbo_crvConstType.setObjectName(u"cbo_crvConstType")
        self.cbo_crvConstType.setEnabled(True)
        self.cbo_crvConstType.setMinimumSize(QSize(100, 0))

        self.gridLayout_120.addWidget(self.cbo_crvConstType, 0, 0, 1, 1)

        self.lne_crvUpObj = QLineEdit(self.groupBox_16)
        self.lne_crvUpObj.setObjectName(u"lne_crvUpObj")
        self.lne_crvUpObj.setEnabled(True)
        self.lne_crvUpObj.setMinimumSize(QSize(120, 0))
        self.lne_crvUpObj.setMaximumSize(QSize(150, 16777215))
        self.lne_crvUpObj.setAlignment(Qt.AlignCenter)

        self.gridLayout_120.addWidget(self.lne_crvUpObj, 0, 1, 1, 1)

        self.btn_crvUpObjGet = QPushButton(self.groupBox_16)
        self.btn_crvUpObjGet.setObjectName(u"btn_crvUpObjGet")
        self.btn_crvUpObjGet.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_120.addWidget(self.btn_crvUpObjGet, 0, 2, 1, 1)


        self.gridLayout_119.addLayout(self.gridLayout_120, 0, 0, 1, 1)

        self.gridLayout_122 = QGridLayout()
        self.gridLayout_122.setObjectName(u"gridLayout_122")
        self.chk_crvPositionOnly = QCheckBox(self.groupBox_16)
        self.chk_crvPositionOnly.setObjectName(u"chk_crvPositionOnly")
        self.chk_crvPositionOnly.setEnabled(True)
        self.chk_crvPositionOnly.setLayoutDirection(Qt.LeftToRight)
        self.chk_crvPositionOnly.setCheckable(True)
        self.chk_crvPositionOnly.setChecked(False)

        self.gridLayout_122.addWidget(self.chk_crvPositionOnly, 0, 0, 1, 1)

        self.btn_crvConstGo = QPushButton(self.groupBox_16)
        self.btn_crvConstGo.setObjectName(u"btn_crvConstGo")
        self.btn_crvConstGo.setMinimumSize(QSize(100, 25))
        self.btn_crvConstGo.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_122.addWidget(self.btn_crvConstGo, 0, 3, 1, 1)

        self.chk_crvParametric = QCheckBox(self.groupBox_16)
        self.chk_crvParametric.setObjectName(u"chk_crvParametric")
        self.chk_crvParametric.setEnabled(True)
        self.chk_crvParametric.setLayoutDirection(Qt.LeftToRight)
        self.chk_crvParametric.setCheckable(True)
        self.chk_crvParametric.setChecked(False)

        self.gridLayout_122.addWidget(self.chk_crvParametric, 0, 1, 1, 1)

        self.chk_crvPositionOffset = QCheckBox(self.groupBox_16)
        self.chk_crvPositionOffset.setObjectName(u"chk_crvPositionOffset")
        self.chk_crvPositionOffset.setEnabled(True)
        self.chk_crvPositionOffset.setLayoutDirection(Qt.LeftToRight)
        self.chk_crvPositionOffset.setCheckable(True)
        self.chk_crvPositionOffset.setChecked(False)

        self.gridLayout_122.addWidget(self.chk_crvPositionOffset, 0, 2, 1, 1)


        self.gridLayout_119.addLayout(self.gridLayout_122, 1, 0, 1, 1)


        self.gridLayout_118.addLayout(self.gridLayout_119, 0, 0, 1, 1)


        self.gridLayout_53.addWidget(self.groupBox_16, 1, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.tab_9)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setEnabled(True)
        self.groupBox_15.setMinimumSize(QSize(384, 100))
        self.groupBox_15.setMaximumSize(QSize(330, 100))
        self.groupBox_15.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.groupBox_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_24 = QGridLayout(self.groupBox_15)
        self.gridLayout_24.setSpacing(5)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setSpacing(3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.chk_srfConTra = QCheckBox(self.groupBox_15)
        self.chk_srfConTra.setObjectName(u"chk_srfConTra")
        self.chk_srfConTra.setEnabled(True)
        self.chk_srfConTra.setChecked(True)

        self.gridLayout_23.addWidget(self.chk_srfConTra, 4, 0, 1, 1)

        self.chk_srfConRot = QCheckBox(self.groupBox_15)
        self.chk_srfConRot.setObjectName(u"chk_srfConRot")
        self.chk_srfConRot.setEnabled(True)
        self.chk_srfConRot.setChecked(True)

        self.gridLayout_23.addWidget(self.chk_srfConRot, 4, 1, 1, 1)

        self.cbo_utilConsMethod = QComboBox(self.groupBox_15)
        self.cbo_utilConsMethod.addItem("")
        self.cbo_utilConsMethod.addItem("")
        self.cbo_utilConsMethod.setObjectName(u"cbo_utilConsMethod")
        self.cbo_utilConsMethod.setMinimumSize(QSize(100, 0))

        self.gridLayout_23.addWidget(self.cbo_utilConsMethod, 1, 0, 1, 4)

        self.btn_utilConstrainToSrf = QPushButton(self.groupBox_15)
        self.btn_utilConstrainToSrf.setObjectName(u"btn_utilConstrainToSrf")
        self.btn_utilConstrainToSrf.setMinimumSize(QSize(100, 25))
        self.btn_utilConstrainToSrf.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_23.addWidget(self.btn_utilConstrainToSrf, 4, 3, 1, 1)

        self.chk_srfPositionOffset = QCheckBox(self.groupBox_15)
        self.chk_srfPositionOffset.setObjectName(u"chk_srfPositionOffset")
        self.chk_srfPositionOffset.setEnabled(True)
        self.chk_srfPositionOffset.setLayoutDirection(Qt.LeftToRight)
        self.chk_srfPositionOffset.setCheckable(True)
        self.chk_srfPositionOffset.setChecked(False)

        self.gridLayout_23.addWidget(self.chk_srfPositionOffset, 4, 2, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_23, 0, 0, 1, 1)


        self.gridLayout_53.addWidget(self.groupBox_15, 0, 0, 1, 1)


        self.gridLayout_54.addLayout(self.gridLayout_53, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(160, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 404, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_54.addItem(self.verticalSpacer_9, 1, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_25 = QGridLayout(self.tab_10)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalSpacer_26 = QSpacerItem(158, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_26, 0, 0, 1, 1)

        self.groupBox_33 = QGroupBox(self.tab_10)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.groupBox_33.sizePolicy().hasHeightForWidth())
        self.groupBox_33.setSizePolicy(sizePolicy1)
        self.groupBox_33.setMinimumSize(QSize(0, 0))
        self.groupBox_33.setMaximumSize(QSize(16777215, 47))
        self.groupBox_33.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_60 = QGridLayout(self.groupBox_33)
        self.gridLayout_60.setSpacing(5)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_132 = QGridLayout()
        self.gridLayout_132.setSpacing(3)
        self.gridLayout_132.setObjectName(u"gridLayout_132")
        self.lne_singlesName = QLineEdit(self.groupBox_33)
        self.lne_singlesName.setObjectName(u"lne_singlesName")
        self.lne_singlesName.setEnabled(True)
        self.lne_singlesName.setMinimumSize(QSize(150, 0))
        self.lne_singlesName.setAlignment(Qt.AlignCenter)

        self.gridLayout_132.addWidget(self.lne_singlesName, 0, 0, 1, 1)

        self.chk_singleJnt = QCheckBox(self.groupBox_33)
        self.chk_singleJnt.setObjectName(u"chk_singleJnt")
        self.chk_singleJnt.setChecked(True)

        self.gridLayout_132.addWidget(self.chk_singleJnt, 0, 1, 1, 1)

        self.btn_singleCtl = QPushButton(self.groupBox_33)
        self.btn_singleCtl.setObjectName(u"btn_singleCtl")
        self.btn_singleCtl.setMinimumSize(QSize(100, 25))
        self.btn_singleCtl.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_132.addWidget(self.btn_singleCtl, 0, 2, 1, 1)

        self.btn_singlePatch = QPushButton(self.groupBox_33)
        self.btn_singlePatch.setObjectName(u"btn_singlePatch")
        self.btn_singlePatch.setMinimumSize(QSize(100, 25))
        self.btn_singlePatch.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_132.addWidget(self.btn_singlePatch, 0, 3, 1, 1)


        self.gridLayout_60.addLayout(self.gridLayout_132, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox_33, 0, 1, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(157, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_27, 0, 2, 1, 1)

        self.verticalSpacer_39 = QSpacerItem(20, 320, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer_39, 1, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_26 = QGridLayout(self.tab_11)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.horizontalSpacer_30 = QSpacerItem(213, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_30, 0, 0, 1, 1)

        self.groupBox_42 = QGroupBox(self.tab_11)
        self.groupBox_42.setObjectName(u"groupBox_42")
        sizePolicy1.setHeightForWidth(self.groupBox_42.sizePolicy().hasHeightForWidth())
        self.groupBox_42.setSizePolicy(sizePolicy1)
        self.groupBox_42.setMinimumSize(QSize(0, 0))
        self.groupBox_42.setMaximumSize(QSize(16777215, 47))
        self.groupBox_42.setStyleSheet(u"QGroupBox {\n"
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
"	color:  rgb(150, 114, 0);\n"
"}")
        self.gridLayout_133 = QGridLayout(self.groupBox_42)
        self.gridLayout_133.setSpacing(5)
        self.gridLayout_133.setObjectName(u"gridLayout_133")
        self.gridLayout_133.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_134 = QGridLayout()
        self.gridLayout_134.setObjectName(u"gridLayout_134")
        self.chk_mmOrient = QCheckBox(self.groupBox_42)
        self.chk_mmOrient.setObjectName(u"chk_mmOrient")
        self.chk_mmOrient.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_134.addWidget(self.chk_mmOrient, 0, 0, 1, 1)

        self.chk_mmDorito = QCheckBox(self.groupBox_42)
        self.chk_mmDorito.setObjectName(u"chk_mmDorito")
        self.chk_mmDorito.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_134.addWidget(self.chk_mmDorito, 0, 1, 1, 1)

        self.btn_mmGo = QPushButton(self.groupBox_42)
        self.btn_mmGo.setObjectName(u"btn_mmGo")
        self.btn_mmGo.setMinimumSize(QSize(100, 25))
        self.btn_mmGo.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_134.addWidget(self.btn_mmGo, 0, 2, 1, 1)


        self.gridLayout_133.addLayout(self.gridLayout_134, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_42, 0, 1, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(213, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_31, 0, 2, 1, 1)

        self.verticalSpacer_42 = QSpacerItem(20, 320, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_42, 1, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_11, "")

        self.gridLayout_70.addWidget(self.tabWidget_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_setCtlSize, self.btn_setCtlShape)
        QWidget.setTabOrder(self.btn_setCtlShape, self.btn_setCtlColor)
        QWidget.setTabOrder(self.btn_setCtlColor, self.spn_globCtlSize)
        QWidget.setTabOrder(self.spn_globCtlSize, self.cbo_globCtlShape)
        QWidget.setTabOrder(self.cbo_globCtlShape, self.cbo_globCtlColor)
        QWidget.setTabOrder(self.cbo_globCtlColor, self.lne_globCtlSuffix)
        QWidget.setTabOrder(self.lne_globCtlSuffix, self.lne_globJntSuffix)
        QWidget.setTabOrder(self.lne_globJntSuffix, self.spn_globAutoColorMargin)

        self.retranslateUi(MainWindow)
        self.chk_ikSpline.clicked["bool"].connect(self.spn_ikSplineNum.setEnabled)
        self.chk_T.clicked["bool"].connect(self.chk_axisTX.setChecked)
        self.chk_T.clicked["bool"].connect(self.chk_axisTY.setChecked)
        self.chk_T.clicked["bool"].connect(self.chk_axisTZ.setChecked)
        self.chk_R.clicked["bool"].connect(self.chk_axisRX.setChecked)
        self.chk_R.clicked["bool"].connect(self.chk_axisRY.setChecked)
        self.chk_R.clicked["bool"].connect(self.chk_axisRZ.setChecked)
        self.chk_S.clicked["bool"].connect(self.chk_axisSX.setChecked)
        self.chk_S.clicked["bool"].connect(self.chk_axisSY.setChecked)
        self.chk_S.clicked["bool"].connect(self.chk_axisSZ.setChecked)

        self.cbo_globCtlShape.setCurrentIndex(10)
        self.cbo_globCtlColor.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.cbo_crvConstType.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"cmSimpleSys", None))
        self.groupBox.setTitle("")
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Pre Build", None))
        self.lne_globCtlSuffix.setText(QCoreApplication.translate("MainWindow", u"ctl", None))
        self.lne_globCtlSuffix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ctl Suffix (optional)", None))
        self.lne_globJntSuffix.setText(QCoreApplication.translate("MainWindow", u"jnt", None))
        self.lne_globJntSuffix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Joint Suffix (optional)", None))
        self.lbl_globCtlShape.setText(QCoreApplication.translate("MainWindow", u"Ctl Shape", None))
        self.cbo_globCtlShape.setItemText(0, QCoreApplication.translate("MainWindow", u"sphere", None))
        self.cbo_globCtlShape.setItemText(1, QCoreApplication.translate("MainWindow", u"arrow", None))
        self.cbo_globCtlShape.setItemText(2, QCoreApplication.translate("MainWindow", u"arrowCurved", None))
        self.cbo_globCtlShape.setItemText(3, QCoreApplication.translate("MainWindow", u"arrowDouble", None))
        self.cbo_globCtlShape.setItemText(4, QCoreApplication.translate("MainWindow", u"arrowDoubleCurved", None))
        self.cbo_globCtlShape.setItemText(5, QCoreApplication.translate("MainWindow", u"arrowFour", None))
        self.cbo_globCtlShape.setItemText(6, QCoreApplication.translate("MainWindow", u"arrowFourCurved", None))
        self.cbo_globCtlShape.setItemText(7, QCoreApplication.translate("MainWindow", u"arrowStrike", None))
        self.cbo_globCtlShape.setItemText(8, QCoreApplication.translate("MainWindow", u"circle", None))
        self.cbo_globCtlShape.setItemText(9, QCoreApplication.translate("MainWindow", u"circleH", None))
        self.cbo_globCtlShape.setItemText(10, QCoreApplication.translate("MainWindow", u"circleV", None))
        self.cbo_globCtlShape.setItemText(11, QCoreApplication.translate("MainWindow", u"circularArrow", None))
        self.cbo_globCtlShape.setItemText(12, QCoreApplication.translate("MainWindow", u"chevron", None))
        self.cbo_globCtlShape.setItemText(13, QCoreApplication.translate("MainWindow", u"cross", None))
        self.cbo_globCtlShape.setItemText(14, QCoreApplication.translate("MainWindow", u"crossX", None))
        self.cbo_globCtlShape.setItemText(15, QCoreApplication.translate("MainWindow", u"cube", None))
        self.cbo_globCtlShape.setItemText(16, QCoreApplication.translate("MainWindow", u"diamond", None))
        self.cbo_globCtlShape.setItemText(17, QCoreApplication.translate("MainWindow", u"star", None))
        self.cbo_globCtlShape.setItemText(18, QCoreApplication.translate("MainWindow", u"star_8", None))
        self.cbo_globCtlShape.setItemText(19, QCoreApplication.translate("MainWindow", u"fourArrowCircle", None))
        self.cbo_globCtlShape.setItemText(20, QCoreApplication.translate("MainWindow", u"googleSign", None))
        self.cbo_globCtlShape.setItemText(21, QCoreApplication.translate("MainWindow", u"googleSignSharp", None))
        self.cbo_globCtlShape.setItemText(22, QCoreApplication.translate("MainWindow", u"joint", None))
        self.cbo_globCtlShape.setItemText(23, QCoreApplication.translate("MainWindow", u"locator", None))
        self.cbo_globCtlShape.setItemText(24, QCoreApplication.translate("MainWindow", u"locatorVolume", None))
        self.cbo_globCtlShape.setItemText(25, QCoreApplication.translate("MainWindow", u"lollipopCircle", None))
        self.cbo_globCtlShape.setItemText(26, QCoreApplication.translate("MainWindow", u"lollipopDouble", None))
        self.cbo_globCtlShape.setItemText(27, QCoreApplication.translate("MainWindow", u"lollipopFour", None))
        self.cbo_globCtlShape.setItemText(28, QCoreApplication.translate("MainWindow", u"lollipopSquare", None))
        self.cbo_globCtlShape.setItemText(29, QCoreApplication.translate("MainWindow", u"square", None))
        self.cbo_globCtlShape.setItemText(30, QCoreApplication.translate("MainWindow", u"triangle", None))

        self.lbl_globCtlColor.setText(QCoreApplication.translate("MainWindow", u"Ctl Color", None))
        self.cbo_globCtlColor.setItemText(0, QCoreApplication.translate("MainWindow", u"primary", None))
        self.cbo_globCtlColor.setItemText(1, QCoreApplication.translate("MainWindow", u"secondary", None))
        self.cbo_globCtlColor.setItemText(2, QCoreApplication.translate("MainWindow", u"tertiary", None))
        self.cbo_globCtlColor.setItemText(3, QCoreApplication.translate("MainWindow", u"blue", None))
        self.cbo_globCtlColor.setItemText(4, QCoreApplication.translate("MainWindow", u"darkBlue", None))
        self.cbo_globCtlColor.setItemText(5, QCoreApplication.translate("MainWindow", u"lightBlue", None))
        self.cbo_globCtlColor.setItemText(6, QCoreApplication.translate("MainWindow", u"softBlue", None))
        self.cbo_globCtlColor.setItemText(7, QCoreApplication.translate("MainWindow", u"pastelBlue", None))
        self.cbo_globCtlColor.setItemText(8, QCoreApplication.translate("MainWindow", u"red", None))
        self.cbo_globCtlColor.setItemText(9, QCoreApplication.translate("MainWindow", u"darkRed", None))
        self.cbo_globCtlColor.setItemText(10, QCoreApplication.translate("MainWindow", u"lightRed", None))
        self.cbo_globCtlColor.setItemText(11, QCoreApplication.translate("MainWindow", u"pastelRed", None))
        self.cbo_globCtlColor.setItemText(12, QCoreApplication.translate("MainWindow", u"green", None))
        self.cbo_globCtlColor.setItemText(13, QCoreApplication.translate("MainWindow", u"darkGreen", None))
        self.cbo_globCtlColor.setItemText(14, QCoreApplication.translate("MainWindow", u"lightGreen", None))
        self.cbo_globCtlColor.setItemText(15, QCoreApplication.translate("MainWindow", u"blueGreen", None))
        self.cbo_globCtlColor.setItemText(16, QCoreApplication.translate("MainWindow", u"turquoise", None))
        self.cbo_globCtlColor.setItemText(17, QCoreApplication.translate("MainWindow", u"yellow", None))
        self.cbo_globCtlColor.setItemText(18, QCoreApplication.translate("MainWindow", u"yellowGreen", None))
        self.cbo_globCtlColor.setItemText(19, QCoreApplication.translate("MainWindow", u"lightYellow", None))
        self.cbo_globCtlColor.setItemText(20, QCoreApplication.translate("MainWindow", u"pastelYellow", None))
        self.cbo_globCtlColor.setItemText(21, QCoreApplication.translate("MainWindow", u"pink", None))
        self.cbo_globCtlColor.setItemText(22, QCoreApplication.translate("MainWindow", u"darkPink", None))
        self.cbo_globCtlColor.setItemText(23, QCoreApplication.translate("MainWindow", u"greyPink", None))
        self.cbo_globCtlColor.setItemText(24, QCoreApplication.translate("MainWindow", u"brown", None))
        self.cbo_globCtlColor.setItemText(25, QCoreApplication.translate("MainWindow", u"darkBrown", None))
        self.cbo_globCtlColor.setItemText(26, QCoreApplication.translate("MainWindow", u"lightBrown", None))
        self.cbo_globCtlColor.setItemText(27, QCoreApplication.translate("MainWindow", u"redBrown", None))
        self.cbo_globCtlColor.setItemText(28, QCoreApplication.translate("MainWindow", u"pastelBrown", None))
        self.cbo_globCtlColor.setItemText(29, QCoreApplication.translate("MainWindow", u"white", None))
        self.cbo_globCtlColor.setItemText(30, QCoreApplication.translate("MainWindow", u"black", None))
        self.cbo_globCtlColor.setItemText(31, QCoreApplication.translate("MainWindow", u"darkGrey", None))
        self.cbo_globCtlColor.setItemText(32, QCoreApplication.translate("MainWindow", u"lightGrey", None))

        self.lbl_globCtlSize.setText(QCoreApplication.translate("MainWindow", u"Ctl Size", None))
        self.lbl_globAutoColorMargin.setText(QCoreApplication.translate("MainWindow", u"Color Margin", None))
#if QT_CONFIG(tooltip)
        self.spn_globAutoColorMargin.setToolTip(QCoreApplication.translate("MainWindow", u"Distance +/- along global X", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_31.setTitle(QCoreApplication.translate("MainWindow", u"Post Build", None))
#if QT_CONFIG(tooltip)
        self.btn_setCtlColor.setToolTip(QCoreApplication.translate("MainWindow", u"Set selected ctrl(s) color from Global setting", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setCtlColor.setText(QCoreApplication.translate("MainWindow", u"Set Color", None))
#if QT_CONFIG(tooltip)
        self.btn_setCtlSize.setToolTip(QCoreApplication.translate("MainWindow", u"Set selected ctrl(s) size from Global setting", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setCtlSize.setText(QCoreApplication.translate("MainWindow", u"Set Size", None))
#if QT_CONFIG(tooltip)
        self.btn_setCtlShape.setToolTip(QCoreApplication.translate("MainWindow", u"Set selected ctrl(s) shape from Global setting", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setCtlShape.setText(QCoreApplication.translate("MainWindow", u"Set Shape", None))
#if QT_CONFIG(tooltip)
        self.btn_setCtlVis.setToolTip(QCoreApplication.translate("MainWindow", u"Set ctrl(s) visibility to Head UI Host attrs", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setCtlVis.setText(QCoreApplication.translate("MainWindow", u"Set Vis", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("MainWindow", u"Select Child by Suffix", None))
#if QT_CONFIG(tooltip)
        self.btn_selBySuffix.setToolTip(QCoreApplication.translate("MainWindow", u"Select edge loop on headCut mesh to create deformers for Lashes. Or select old Lash curve to rebuild.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_selBySuffix.setText(QCoreApplication.translate("MainWindow", u"Select Children By Suffix", None))
        self.cbo_selSuffix.setItemText(0, QCoreApplication.translate("MainWindow", u"jnt", None))
        self.cbo_selSuffix.setItemText(1, QCoreApplication.translate("MainWindow", u"ctl", None))
        self.cbo_selSuffix.setItemText(2, QCoreApplication.translate("MainWindow", u"bfr", None))
        self.cbo_selSuffix.setItemText(3, QCoreApplication.translate("MainWindow", u"ctlRef", None))
        self.cbo_selSuffix.setItemText(4, QCoreApplication.translate("MainWindow", u"spljnt", None))
        self.cbo_selSuffix.setItemText(5, QCoreApplication.translate("MainWindow", u"bind", None))
        self.cbo_selSuffix.setItemText(6, QCoreApplication.translate("MainWindow", u"anim", None))
        self.cbo_selSuffix.setItemText(7, QCoreApplication.translate("MainWindow", u"cns", None))
        self.cbo_selSuffix.setItemText(8, QCoreApplication.translate("MainWindow", u"off", None))
        self.cbo_selSuffix.setItemText(9, QCoreApplication.translate("MainWindow", u"root", None))
        self.cbo_selSuffix.setItemText(10, QCoreApplication.translate("MainWindow", u"grp", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"(un)Lock/(un)Hide", None))
        self.cbo_axisLockUnlock.setItemText(0, "")
        self.cbo_axisLockUnlock.setItemText(1, QCoreApplication.translate("MainWindow", u"Unlock", None))
        self.cbo_axisLockUnlock.setItemText(2, QCoreApplication.translate("MainWindow", u"Lock", None))

#if QT_CONFIG(tooltip)
        self.cbo_axisLockUnlock.setToolTip(QCoreApplication.translate("MainWindow", u"Locks / Unlocks selected", None))
#endif // QT_CONFIG(tooltip)
        self.cbo_hideUnhide.setItemText(0, "")
        self.cbo_hideUnhide.setItemText(1, QCoreApplication.translate("MainWindow", u"Hide", None))
        self.cbo_hideUnhide.setItemText(2, QCoreApplication.translate("MainWindow", u"Unhide", None))

        self.btn_axisGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.chk_axisTX.setText(QCoreApplication.translate("MainWindow", u"tx", None))
        self.chk_axisRZ.setText(QCoreApplication.translate("MainWindow", u"rz", None))
        self.chk_axisSY.setText(QCoreApplication.translate("MainWindow", u"sy", None))
        self.chk_axisTY.setText(QCoreApplication.translate("MainWindow", u"ty", None))
        self.chk_axisRX.setText(QCoreApplication.translate("MainWindow", u"rx", None))
        self.chk_axisSX.setText(QCoreApplication.translate("MainWindow", u"sx", None))
        self.chk_axisRY.setText(QCoreApplication.translate("MainWindow", u"ry", None))
        self.chk_axisSZ.setText(QCoreApplication.translate("MainWindow", u"sz", None))
        self.chk_axisTZ.setText(QCoreApplication.translate("MainWindow", u"tz", None))
        self.chk_T.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.chk_R.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.chk_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("MainWindow", u"Parent Constraint", None))
#if QT_CONFIG(tooltip)
        self.chk_maintainOffset.setToolTip(QCoreApplication.translate("MainWindow", u"Maintain Offset", None))
#endif // QT_CONFIG(tooltip)
        self.chk_maintainOffset.setText(QCoreApplication.translate("MainWindow", u"MO", None))
#if QT_CONFIG(tooltip)
        self.btn_createMatCon.setToolTip(QCoreApplication.translate("MainWindow", u"Creates Matrix Constraint using checked attrs. Select Parent, then Child", None))
#endif // QT_CONFIG(tooltip)
        self.btn_createMatCon.setText(QCoreApplication.translate("MainWindow", u"Create Constraint", None))
#if QT_CONFIG(tooltip)
        self.btn_delMatCon.setToolTip(QCoreApplication.translate("MainWindow", u"Deletes Matrix Constraint", None))
#endif // QT_CONFIG(tooltip)
        self.btn_delMatCon.setText(QCoreApplication.translate("MainWindow", u"Delete Constraint", None))
        self.groupBox_36.setTitle(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btn_globalSclObj.setText(QCoreApplication.translate("MainWindow", u"<<", None))
#if QT_CONFIG(tooltip)
        self.btn_globalScaleConnect.setToolTip(QCoreApplication.translate("MainWindow", u"Connects rig global scale to transform scale attrs", None))
#endif // QT_CONFIG(tooltip)
        self.btn_globalScaleConnect.setText(QCoreApplication.translate("MainWindow", u"Global Scale", None))
#if QT_CONFIG(tooltip)
        self.btn_directConnect.setToolTip(QCoreApplication.translate("MainWindow", u"Connects selected SRT attr(s). Select SOURCE then TARGET. Multiple Targets allowed.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_directConnect.setText(QCoreApplication.translate("MainWindow", u"Direct Connect", None))
#if QT_CONFIG(tooltip)
        self.lne_globalSclObj.setToolTip(QCoreApplication.translate("MainWindow", u"Object that contains globalScale attr", None))
#endif // QT_CONFIG(tooltip)
        self.lne_globalSclObj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"global_C0_ctl", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Attr Control", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Import / Export", None))
#if QT_CONFIG(tooltip)
        self.btn_importWeights.setToolTip(QCoreApplication.translate("MainWindow", u"Import XML weight file.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_importWeights.setStatusTip(QCoreApplication.translate("MainWindow", u"Import weight(s) from directory", None))
#endif // QT_CONFIG(statustip)
        self.btn_importWeights.setText(QCoreApplication.translate("MainWindow", u"Import Weight(s)", None))
#if QT_CONFIG(tooltip)
        self.btn_exportWeights.setToolTip(QCoreApplication.translate("MainWindow", u"Export XML weight file.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_exportWeights.setStatusTip(QCoreApplication.translate("MainWindow", u"Export weight(s) to directory", None))
#endif // QT_CONFIG(statustip)
        self.btn_exportWeights.setText(QCoreApplication.translate("MainWindow", u"Export Weight(s)", None))
#if QT_CONFIG(tooltip)
        self.btn_selectClstrInfl.setToolTip(QCoreApplication.translate("MainWindow", u"Select joints in objects skinCluster", None))
#endif // QT_CONFIG(tooltip)
        self.btn_selectClstrInfl.setText(QCoreApplication.translate("MainWindow", u"Select Clstr Jts", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("MainWindow", u"Transfer", None))
#if QT_CONFIG(tooltip)
        self.btn_transferWeights.setToolTip(QCoreApplication.translate("MainWindow", u"Select SOURCE then TARGET(S).  Poly to Nurbs IS supported. Method is Closest Point, Closest Joint, One to One", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_transferWeights.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_transferWeights.setText(QCoreApplication.translate("MainWindow", u"Transfer Weights", None))
        self.chk_transferWeightsRemove.setText(QCoreApplication.translate("MainWindow", u"Remove Unused", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Joint Pre-Bind Matrix", None))
        self.cbo_preBindJoint.setItemText(0, QCoreApplication.translate("MainWindow", u"jnt", None))
        self.cbo_preBindJoint.setItemText(1, QCoreApplication.translate("MainWindow", u"bind", None))

#if QT_CONFIG(tooltip)
        self.cbo_preBindJoint.setToolTip(QCoreApplication.translate("MainWindow", u"Joint suffix", None))
#endif // QT_CONFIG(tooltip)
        self.cbo_preBindBfr.setItemText(0, QCoreApplication.translate("MainWindow", u"ctlRef (Strap Rig)", None))
        self.cbo_preBindBfr.setItemText(1, QCoreApplication.translate("MainWindow", u"cns (mGear Jnt)", None))
        self.cbo_preBindBfr.setItemText(2, QCoreApplication.translate("MainWindow", u"bfr (Face Rig)", None))

#if QT_CONFIG(tooltip)
        self.cbo_preBindBfr.setToolTip(QCoreApplication.translate("MainWindow", u"Buffer suffix", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_ctlPreBindMat.setToolTip(QCoreApplication.translate("MainWindow", u"Connects the joints bfr.wm as bindpose prematrix. Select joints, then object with skinCluster", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ctlPreBindMat.setText(QCoreApplication.translate("MainWindow", u"Connect .wm", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("MainWindow", u"BindPose", None))
#if QT_CONFIG(tooltip)
        self.btn_resetBindPose.setToolTip(QCoreApplication.translate("MainWindow", u"Sets new bindPose, and sets Prefered Angle (option) for all joints in selected mesh skinCluster", None))
#endif // QT_CONFIG(tooltip)
        self.btn_resetBindPose.setText(QCoreApplication.translate("MainWindow", u"Set BindPose", None))
#if QT_CONFIG(tooltip)
        self.chk_bindPoseAngle.setToolTip(QCoreApplication.translate("MainWindow", u"If checked, joints preferred angle will be set to its current angle when BindPose is run", None))
#endif // QT_CONFIG(tooltip)
        self.chk_bindPoseAngle.setText(QCoreApplication.translate("MainWindow", u"Set Preferred Angle", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Skin Tools", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("MainWindow", u"Points", None))
#if QT_CONFIG(tooltip)
        self.btn_meshUpdateOrig.setToolTip(QCoreApplication.translate("MainWindow", u"Updates Target mesh to shape of Source mesh. Works on Mesh, Select SOURCE then TARGET. Auto option for multi mesh updates.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_meshUpdateOrig.setText(QCoreApplication.translate("MainWindow", u"Update Shape", None))
#if QT_CONFIG(tooltip)
        self.chk_updateAuto.setToolTip(QCoreApplication.translate("MainWindow", u"If checked, select the newly imported mdl alembic objects in the outliner. If NOT checked. Select SOURCE then TARGET for individual shape updates.", None))
#endif // QT_CONFIG(tooltip)
        self.chk_updateAuto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
#if QT_CONFIG(tooltip)
        self.btn_meshMatchPoint.setToolTip(QCoreApplication.translate("MainWindow", u"Target to follow source mesh transformation, and deformation. Works on Mesh, Nurbs, Curves. Select DRIVER then DRIVEN", None))
#endif // QT_CONFIG(tooltip)
        self.btn_meshMatchPoint.setText(QCoreApplication.translate("MainWindow", u"Match Point Pos", None))
        self.groupBox_44.setTitle(QCoreApplication.translate("MainWindow", u"Scale Published Geo", None))
#if QT_CONFIG(tooltip)
        self.btn_smoothEdges.setToolTip(QCoreApplication.translate("MainWindow", u"Smooth polygon edges", None))
#endif // QT_CONFIG(tooltip)
        self.btn_smoothEdges.setText(QCoreApplication.translate("MainWindow", u"Smooth Edges", None))
#if QT_CONFIG(tooltip)
        self.btn_delUnShp.setToolTip(QCoreApplication.translate("MainWindow", u"Delete unused shape nodes from the scene.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_delUnShp.setText(QCoreApplication.translate("MainWindow", u"Del Unused Shapes", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Mesh Control", None))
        self.grp_strapGuide.setTitle(QCoreApplication.translate("MainWindow", u"Guides on Surface", None))
#if QT_CONFIG(tooltip)
        self.btn_prepSrf.setToolTip(QCoreApplication.translate("MainWindow", u"Create new surface, or rebuild selected nurbs 0,1 Parameterization. Displays UV border.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_prepSrf.setText(QCoreApplication.translate("MainWindow", u"Prep Srf", None))
#if QT_CONFIG(tooltip)
        self.btn_swapUV.setToolTip(QCoreApplication.translate("MainWindow", u"Spin nurbs surface border edges", None))
#endif // QT_CONFIG(tooltip)
        self.btn_swapUV.setText(QCoreApplication.translate("MainWindow", u"Swap U,V", None))
#if QT_CONFIG(tooltip)
        self.spn_strapGuideRow.setToolTip(QCoreApplication.translate("MainWindow", u"Number or guide rows to create", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbl_strapGuideRow.setToolTip(QCoreApplication.translate("MainWindow", u"Number or guide rows to create (U Param Red)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_strapGuideRow.setText(QCoreApplication.translate("MainWindow", u"Gde Row", None))
#if QT_CONFIG(tooltip)
        self.spn_strapGuideColumn.setToolTip(QCoreApplication.translate("MainWindow", u"Number or guide columns to create", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbl_strapGuideColumn.setToolTip(QCoreApplication.translate("MainWindow", u"Number or guide columns to create (V Param Green)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_strapGuideColumn.setText(QCoreApplication.translate("MainWindow", u"Gde Column", None))
        self.chk_strapSkipLast.setText(QCoreApplication.translate("MainWindow", u"Closed Srf (cylinder)", None))
#if QT_CONFIG(tooltip)
        self.btn_goGuidesOnSrf.setToolTip(QCoreApplication.translate("MainWindow", u"Create guide locators on nurb surface", None))
#endif // QT_CONFIG(tooltip)
        self.btn_goGuidesOnSrf.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.grp_strapRig.setTitle(QCoreApplication.translate("MainWindow", u"Rig From Guides", None))
#if QT_CONFIG(tooltip)
        self.spn_strapJntRow.setToolTip(QCoreApplication.translate("MainWindow", u"Number or joint rows to create on dorito mesh", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbl_strapJntRow_3.setToolTip(QCoreApplication.translate("MainWindow", u"If 0, no dorito joints will be created.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_strapJntRow_3.setText(QCoreApplication.translate("MainWindow", u"*Jnt Row", None))
#if QT_CONFIG(tooltip)
        self.spn_strapJntColumn.setToolTip(QCoreApplication.translate("MainWindow", u"Number or joint columns to create on dorito mesh", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbl_strapJntColumn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Number or joint columns to create on dorito mesh", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_strapJntColumn_2.setText(QCoreApplication.translate("MainWindow", u"Jnt Column", None))
#if QT_CONFIG(tooltip)
        self.spn_ikSplineNum.setToolTip(QCoreApplication.translate("MainWindow", u"Number of joints in IK Spline", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbl_ikSplineNo_2.setToolTip(QCoreApplication.translate("MainWindow", u"Number of joints in IK Spline", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_ikSplineNo_2.setText(QCoreApplication.translate("MainWindow", u"Spl. Column", None))
#if QT_CONFIG(tooltip)
        self.chk_makeCtlFK.setToolTip(QCoreApplication.translate("MainWindow", u"Builds ctls in FK mode, with IK option", None))
#endif // QT_CONFIG(tooltip)
        self.chk_makeCtlFK.setText(QCoreApplication.translate("MainWindow", u"Make Ctls FK", None))
#if QT_CONFIG(tooltip)
        self.chk_lra.setToolTip(QCoreApplication.translate("MainWindow", u"Turn on Local Rotation Axis for deformer joints", None))
#endif // QT_CONFIG(tooltip)
        self.chk_lra.setText(QCoreApplication.translate("MainWindow", u"Display Local Rot Axis", None))
#if QT_CONFIG(tooltip)
        self.btn_goStrapRig.setToolTip(QCoreApplication.translate("MainWindow", u"Build rig from Guides on Surface, or current selected nurbs surface with _ctlGde children", None))
#endif // QT_CONFIG(tooltip)
        self.btn_goStrapRig.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.chk_ikSpline.setText(QCoreApplication.translate("MainWindow", u"IK Spline", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Strap Rigs", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Guides on Curve", None))
#if QT_CONFIG(tooltip)
        self.btn_gdeOnCrvGo.setToolTip(QCoreApplication.translate("MainWindow", u"Create guides evenly along curve. Position guides as needed. Yellow guide defines curve direction.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_gdeOnCrvGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Rig From Guides", None))
        self.cbo_crvRigType.setItemText(0, QCoreApplication.translate("MainWindow", u"IK/FK", None))
        self.cbo_crvRigType.setItemText(1, QCoreApplication.translate("MainWindow", u"FK", None))

#if QT_CONFIG(tooltip)
        self.btn_bldCrvRigGo.setToolTip(QCoreApplication.translate("MainWindow", u"Build rig from Guides on Curve, or current selected nurbs curve with _ctlGde children", None))
#endif // QT_CONFIG(tooltip)
        self.btn_bldCrvRigGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Curve Rigs", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Create on Surface", None))
#if QT_CONFIG(tooltip)
        self.btn_utilPrepSrf.setToolTip(QCoreApplication.translate("MainWindow", u"Create new surface, or rebuild selected nurbs 0,1 Parameterization. Displays UV border.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_utilPrepSrf.setText(QCoreApplication.translate("MainWindow", u"Prep Srf", None))
#if QT_CONFIG(tooltip)
        self.btn_utilSwapUV.setToolTip(QCoreApplication.translate("MainWindow", u"Spin nurbs surface border edges", None))
#endif // QT_CONFIG(tooltip)
        self.btn_utilSwapUV.setText(QCoreApplication.translate("MainWindow", u"Swap U,V", None))
        self.cbo_utilObjType.setItemText(0, QCoreApplication.translate("MainWindow", u"Joint", None))
        self.cbo_utilObjType.setItemText(1, QCoreApplication.translate("MainWindow", u"Locator", None))

        self.cbo_utilObjType.setCurrentText(QCoreApplication.translate("MainWindow", u"Joint", None))
        self.lbl_utilRow.setText(QCoreApplication.translate("MainWindow", u"Row Num.", None))
        self.lbl_utilColumn.setText(QCoreApplication.translate("MainWindow", u"Column Num", None))
#if QT_CONFIG(tooltip)
        self.chk_srfSkipLast.setToolTip(QCoreApplication.translate("MainWindow", u"For closed surfaces", None))
#endif // QT_CONFIG(tooltip)
        self.chk_srfSkipLast.setText(QCoreApplication.translate("MainWindow", u"Skip Last", None))
#if QT_CONFIG(tooltip)
        self.btn_utilCreateOnSrf.setToolTip(QCoreApplication.translate("MainWindow", u"Creates the selected items evenly along nurbs surface", None))
#endif // QT_CONFIG(tooltip)
        self.btn_utilCreateOnSrf.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Create On Curve", None))
        self.lbl_crvNumOf.setText(QCoreApplication.translate("MainWindow", u"No. of", None))
        self.cbo_crvNumOf.setItemText(0, QCoreApplication.translate("MainWindow", u"Joints", None))
        self.cbo_crvNumOf.setItemText(1, QCoreApplication.translate("MainWindow", u"Locators", None))

        self.cbo_crvNumOf.setCurrentText(QCoreApplication.translate("MainWindow", u"Joints", None))
#if QT_CONFIG(tooltip)
        self.btn_crvGo.setToolTip(QCoreApplication.translate("MainWindow", u"Create items evenly along curve. Select curve and run", None))
#endif // QT_CONFIG(tooltip)
        self.btn_crvGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.chk_crvJntAsChain.setText(QCoreApplication.translate("MainWindow", u"Chain", None))
        self.groupBox_41.setTitle("")
#if QT_CONFIG(tooltip)
        self.btn_jntOnVtx.setToolTip(QCoreApplication.translate("MainWindow", u"Creates joints attached to mesh vertex. UV's are required on the mesh. And the mesh have transforms frozen.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_jntOnVtx.setText(QCoreApplication.translate("MainWindow", u"Jnt on Mesh Vert", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Create On", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Constrain to Curve", None))
        self.cbo_crvConstType.setItemText(0, QCoreApplication.translate("MainWindow", u"Scene Up", None))
        self.cbo_crvConstType.setItemText(1, QCoreApplication.translate("MainWindow", u"Obj Up", None))
        self.cbo_crvConstType.setItemText(2, QCoreApplication.translate("MainWindow", u"Obj Rot Up", None))
        self.cbo_crvConstType.setItemText(3, QCoreApplication.translate("MainWindow", u"Vector", None))
        self.cbo_crvConstType.setItemText(4, QCoreApplication.translate("MainWindow", u"Normal", None))

        self.lne_crvUpObj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Up Object", None))
        self.btn_crvUpObjGet.setText(QCoreApplication.translate("MainWindow", u"<<", None))
#if QT_CONFIG(tooltip)
        self.chk_crvPositionOnly.setToolTip(QCoreApplication.translate("MainWindow", u"Ignores rotation when constraining to curve.", None))
#endif // QT_CONFIG(tooltip)
        self.chk_crvPositionOnly.setText(QCoreApplication.translate("MainWindow", u"Position Only", None))
#if QT_CONFIG(tooltip)
        self.btn_crvConstGo.setToolTip(QCoreApplication.translate("MainWindow", u"Constrain items to closest point on curve. Select curve last", None))
#endif // QT_CONFIG(tooltip)
        self.btn_crvConstGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
#if QT_CONFIG(tooltip)
        self.chk_crvParametric.setToolTip(QCoreApplication.translate("MainWindow", u"(OFF) objects will slide on curve. (ON) objects do not slide on curve.", None))
#endif // QT_CONFIG(tooltip)
        self.chk_crvParametric.setText(QCoreApplication.translate("MainWindow", u"Parametric", None))
#if QT_CONFIG(tooltip)
        self.chk_crvPositionOffset.setToolTip(QCoreApplication.translate("MainWindow", u"Constrains objects to curve using offset matrix.", None))
#endif // QT_CONFIG(tooltip)
        self.chk_crvPositionOffset.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Constrain To Surface", None))
#if QT_CONFIG(tooltip)
        self.chk_srfConTra.setToolTip(QCoreApplication.translate("MainWindow", u"Constrain object translation", None))
#endif // QT_CONFIG(tooltip)
        self.chk_srfConTra.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
#if QT_CONFIG(tooltip)
        self.chk_srfConRot.setToolTip(QCoreApplication.translate("MainWindow", u"Constrain object rotation", None))
#endif // QT_CONFIG(tooltip)
        self.chk_srfConRot.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.cbo_utilConsMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Matrix", None))
        self.cbo_utilConsMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"Follicle", None))

#if QT_CONFIG(tooltip)
        self.cbo_utilConsMethod.setToolTip(QCoreApplication.translate("MainWindow", u"Follicle constraint will only follow vertex deformations, not object transformations. Parent nurbs surface needs to be skinned", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_utilConstrainToSrf.setToolTip(QCoreApplication.translate("MainWindow", u"Constrain selected items to nurbs surface by closest point. Select nurbs surface last", None))
#endif // QT_CONFIG(tooltip)
        self.btn_utilConstrainToSrf.setText(QCoreApplication.translate("MainWindow", u"Go", None))
#if QT_CONFIG(tooltip)
        self.chk_srfPositionOffset.setToolTip(QCoreApplication.translate("MainWindow", u"Constrains objects to surface using offset matrix.", None))
#endif // QT_CONFIG(tooltip)
        self.chk_srfPositionOffset.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Constrain To", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"Singles", None))
        self.lne_singlesName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ctl Name", None))
        self.chk_singleJnt.setText(QCoreApplication.translate("MainWindow", u"Jnt", None))
        self.btn_singleCtl.setText(QCoreApplication.translate("MainWindow", u"Single Ctl", None))
        self.btn_singlePatch.setText(QCoreApplication.translate("MainWindow", u"Single Patch", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Single Ctl", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("MainWindow", u"MM Ctl(s) from Vtx", None))
#if QT_CONFIG(tooltip)
        self.chk_mmOrient.setToolTip(QCoreApplication.translate("MainWindow", u"Orient ctls to vertex normal", None))
#endif // QT_CONFIG(tooltip)
        self.chk_mmOrient.setText(QCoreApplication.translate("MainWindow", u"Orient to Mesh", None))
#if QT_CONFIG(tooltip)
        self.chk_mmDorito.setToolTip(QCoreApplication.translate("MainWindow", u"Creates decondary dorito mesh, that is deformed by ctls", None))
#endif // QT_CONFIG(tooltip)
        self.chk_mmDorito.setText(QCoreApplication.translate("MainWindow", u"Dorito Mesh", None))
#if QT_CONFIG(tooltip)
        self.btn_mmGo.setToolTip(QCoreApplication.translate("MainWindow", u"Creates Match Move controllers on selected vetex(s), Selected mesh needs to be deformed on vertex level for ctls to follow.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mmGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Match Move Ctl", None))
    # retranslateUi

