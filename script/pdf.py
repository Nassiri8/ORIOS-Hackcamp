import pdfkit
import os
def html_to_pdf():

    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    cwd = os.getcwd()
    htmlFile = 'test.html'
    outFile = 'result.pdf'

    pdfkit.from_file(htmlFile, outFile, configuration=config)