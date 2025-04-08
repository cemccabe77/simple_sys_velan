TO INSTALL QTDESIGNER:
Install python

pip located in : C:\Users\USERNAME\AppData\Local\Programs\Python\PYTHONVERSION\Lib

Command Prompt: py -m pip install PyQt5Designer

installs to:
C:\Users\USERNAME\AppData\Local\Programs\Python\PYTHONVERSION\Lib\site-packages\QtDesigner



TO COMPILE UI:
Install pySide6:  py -m pip install pySide6

pyside6-uic.exe located in:  C:\Users\USERNAME\AppData\Local\Programs\Python\PYTHONVERSION\Scripts

Command Prompt: pyside6-uic.exe "path\to\mainwindow.ui" > "path\to\ui_mainwindow.py"



# Modify import modules in cmSimpleUi.py after compiling
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