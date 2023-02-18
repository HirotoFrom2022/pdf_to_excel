import os
import sys
import time
import datetime
import pprint
import math
import traceback

from libs import risk
from libs import automate

def main():
    curDir = os.path.dirname(__file__)
    os.chdir(curDir)
    sys.path.append(os.path.join(curDir, 'libs'))
    import process
    import pdf_reader

    proc = process.Base()

    try:
        reader = pdf_reader.PDF_READER(proc)
        reader.execute()

    except:
        proc.log(0, traceback.format_exc())
    finally:
        print('done')

if __name__ == '__main__':
    main()