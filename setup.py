import cx_Freeze
import sys
import os
import matplotlib
os.environ['TCL_LIBRARY']="c:\\LOCAL_TO_PYTHON\\Python38-32\\tcl8.6"
os.environ['TK_LIBRARY']="c:\\LOCAL_TO_PYTHON\\Python38-32\\tk8.6"
base=None
if sys.platform=='win32':
    base='Win32GUI'
executables=[cx_Freeze.Executable("coronavirus.py",base=None)]
cx_Freeze.setup(
    name="this is a tes",
    options={"build_exe":{"packages":["numpy"]}},
    version="0.01",
    description="Trying to get this to work",
    executables=executables
)
