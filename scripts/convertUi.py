### Still only works in Maya 2022. ###

import sys
from pyside2uic import compileUi
pyfile = open("D:\\Working\\cmlib\\cmMayaWorkgroup2020\\cmSimpleSys\\scripts\\cmSimpleSys\\cmSimpleUi.py", 'w')
compileUi("D:\\Working\\cmlib\\cmMayaWorkgroup2020\\cmSimpleSys\\scripts\\cmSimpleSys\\cmSimpleUi.ui", pyfile, False, 4, False)
pyfile.close()

fullPath = r"D:\\Working\\cmlib\\cmMayaWorkgroup2020\\cmSimpleSys\\scripts\\cmSimpleSys\\cmSimpleQtUi.py"
exec(open(fullPath).read())
