#
# txt2tags CJK wrapping tester (http://txt2tags.org)
# See also: ../run.py ../lib.py
#

import glob
import os
import re
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.dirname(DIR)
sys.path.insert(0, TEST_DIR)
import lib

os.chdir(DIR)

# sux
lib.OK = lib.FAILED = 0
lib.ERROR_FILES = []

def run():
    # test all OK files found
    # Note: txt target is to test the table-to-verbatim mapping
    for outfile in glob.glob("ok/*"):
        stderr = 0
        basename = re.sub('\..*?$', '', outfile.replace('ok/', ''))
        target = re.sub('.*\.', '', outfile)
        if target == 'out':
            target = 'txt'
            stderr = 1
        infile = basename + ".t2t"
        outfile = outfile.replace('ok/', '')

        if lib.initTest(basename, infile, outfile):
            cmdline = ['-t', target]
            cmdline.extend(['-i', infile])
            if stderr:
                cmdline.extend(['-o', '-'])
                cmdline.append('>' + outfile)
                cmdline.append('2>&1')
            lib.test(cmdline, outfile)
    # clean up
    if os.path.isfile(lib.CONFIG_FILE):
        os.remove(lib.CONFIG_FILE)

    return lib.OK, lib.FAILED, lib.ERROR_FILES

if __name__ == '__main__':
    print lib.MSG_RUN_ALONE