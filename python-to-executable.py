from distutils.core import setup
import py2exe
import os
import sys

sys.argv.appen("py3.exe")
setup(
    options={'py3exe':{'bundle_files':1}}
    windows=[{'script':"convert.py"}]
    zipfile=None,
)