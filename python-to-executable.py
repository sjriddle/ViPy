import py2exe
import os
import sys
from distutils.core import setup

sys.argv.append("py3.exe")
setup(
    options={
        'py3exe': {
            'bundle_files':1
        }
    }
    windows=[{
        'script':"convert.py"
    }]
    zipfile=None,
)
