import PyPDF2
import pprint
import os

class PDF_READER:

    def __init__(self, proc):
        self.proc = proc

    def execute(self, request_pages):
        self.proc.log(0, 'Reading pdf file.')

        strage_path = self.proc.config.get('STORAGE_PATH', 'pdf_folder')
        pdf_files = os.listdir(strage_path)
        pdf_full_path = os.path.join(strage_path, pdf_files[0])

        contentDict = {}
        number_of_pages = ''
        with open(pdf_full_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            number_of_pages = len(reader.pages)

            if(request_pages == ''):
                for i in range(number_of_pages):
                    page = reader.pages[i]
                    # print('------------------' + str(i+1) + '/' + str(number_of_pages) + '------------------\n')
                    # pprint.pprint(page.extract_text().split('\n'))
                    contentDict[i] = page.extract_text().split('\n')
            else:
                for i in range(number_of_pages):
                    if i in request_pages:
                        page = reader.pages[i]
                        # print('------------------' + str(i+1) + '/' + str(number_of_pages) + '------------------\n')
                        # pprint.pprint(page.extract_text().split('\n'))
                        contentDict[i] = page.extract_text().split('\n')

        return contentDict
