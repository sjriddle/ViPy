import pyPdf
import optparse
from pyPdf import PdfFileReader

def printMeta(fileName):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print('[*] PDF MetaData For: ' + str(fileName))
    for metaItem in docInfo:
        print('[+] ' + metaItem + ':' + docInfo[metaItem])

def main():
    parser = optparse.OptionParser('usage %prog ' + '-F <PDF File Name>')
    parser.add_option('-F', dest='fileName', type='string', help='specify PDF File Name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print(parser.usage)
        exit(0)
    else:
        printMeta(fileName)

if __name == '__main__':
    main()
