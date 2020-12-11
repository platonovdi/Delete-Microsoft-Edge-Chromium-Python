import os
import re


PATH = 'C:\Program Files (x86)\Microsoft\Edge\Application\ '
os.chdir(PATH)
pattern = re.compile(r'\d\d\.\d\.\d\d\d\.\d\d')
list_dir = os.listdir('.')
for item in list_dir:
    if pattern.match(item):
        os.chdir(item)
os.chdir('Installer')
os.system('@echo off')
os.system('@chcp 65001')
os.system('''setup.exe --uninstall --system-level --verbose-logging 
    --force-uninstall''')
