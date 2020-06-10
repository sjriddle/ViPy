import pyPdf
import optparse
from pyPdf import PdfFileReader

def printMeta(file_name):
    pdf_file = PdfFileReader(file(file_name, 'rb'))
    doc_info = pdf_file.getDocumentInfo()
    print(f'[*] PDF MetaData For: {file_name}')
    for meta_item in doc_info:
        print(f'[+] {meta_item}:{doc_info[meta_item]}')

        
def main():
    parser = optparse.OptionParser('usage %prog ' + '-F <PDF File Name>')
    parser.add_option('-F', dest='file_name', type='string', help='specify PDF File Name')
    (options, args) = parser.parse_args()
    file_name = options.file_name
    if not file_name:
        print(parser.usage)
        exit(0)
    else:
        printMeta(file_name)

        
if __name == '__main__':
    main()
