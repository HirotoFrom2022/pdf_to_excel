import os
import sys
import time
import datetime
import pprint
import math
import traceback

def main():
    curDir = os.path.dirname(__file__)
    os.chdir(curDir)
    sys.path.append(os.path.join(curDir, 'libs'))
    import process
    import pdf_reader
    import excel_maker
    import handle

    try:
        proc = process.Base()

        input_handler = handle.INPUT_HANDLE(proc)
        input = input_handler.ask_input()

        # 7,8,9,10,13

        reader = pdf_reader.PDF_READER(proc)
        content_dict = reader.execute(input)

        excel = excel_maker.EXCEL_MAKER(proc)
        excel.create_book()
        excel.load_book()

        if(input == ''):
            for i in range(len(content_dict)):
                excel.write_content_without_p(i, content_dict[i])
        else:
            for i in range(len(content_dict)):
                excel.write_content_with_p(i, input, content_dict[input[i]])

        excel.save_book()

    except:
        proc.log(0, traceback.format_exc())
    finally:
        print('done')

if __name__ == '__main__':
    main()