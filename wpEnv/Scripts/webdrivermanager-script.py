#!c:\users\mfurk\desktop\whatscomp\wpenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'webdrivermanager==0.9.0','console_scripts','webdrivermanager'
__requires__ = 'webdrivermanager==0.9.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('webdrivermanager==0.9.0', 'console_scripts', 'webdrivermanager')()
    )
