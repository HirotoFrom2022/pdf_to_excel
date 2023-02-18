import PyPDF2
import pprint
import os

class PDF_READER:

    def __init__(self, proc):
        self.proc = proc

    def execute(self):
        self.proc.log(0, 'Reading pdf file.')
        strage_path = self.proc.config.get('STORAGE_PATH', 'pdf_folder')
        pdf_files = os.listdir(strage_path)
        pdf_full_path = os.path.join(strage_path, pdf_files[0])
        pprint.pprint(strage_path)
        pprint.pprint(pdf_files)
        pprint.pprint(os.path.join(strage_path, pdf_files[0]))
        with open(pdf_full_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            number_of_pages = len(reader.pages)
            for i in range(number_of_pages):
                page = reader.pages[i]
                print(page.extract_text())
