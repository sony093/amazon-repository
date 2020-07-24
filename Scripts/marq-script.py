#!C:\Users\Abinash\PycharmProjects\AMAZON\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'mark==0.2','console_scripts','marq'
__requires__ = 'mark==0.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('mark==0.2', 'console_scripts', 'marq')()
    )
