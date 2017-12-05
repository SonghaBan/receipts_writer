from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
import csv
import os

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
font_chinese = 'STSong-Light' # from Adobe's Asian Language Packs
#font_chinese = 'HYGothic-Medium'
pdfmetrics.registerFont(UnicodeCIDFont(font_chinese))



def get_data(data, i, args):
	can = canvas.Canvas('text{}.pdf'.format(i), pagesize = (841,595))
	# create a new PDF with Reportlab	
	can.setFont(font_chinese, 12)
	can.drawString(100, 480, data[2])
	can.drawString(550, 480, args[0])
	can.drawString(740, 475, args[2])
	can.drawString(550, 380, data[0])
	can.drawString(740, 300, data[3])
	can.drawString(490, 160, args[2])
	can.drawString(620, 160, args[1])
	can.save()

	new_pdf = PdfFileReader(open('text{}.pdf'.format(i),"rb"))
	newpage = new_pdf.getPage(0)
	return newpage

def readcsv(csvfile):
	with open('list2.csv','r') as csvfile:
		contents = csv.reader(csvfile)
		return [c for c in contents][1:]

def fillout(csvfile, args):
	output = PdfFileWriter()
	data = readcsv(csvfile)

	for i,d in enumerate(data):
		existing_pdf = PdfFileReader(open("rr.pdf", "rb"))
		page = existing_pdf.getPage(0)
		newpage = get_data(d,i,args)
		page.mergeRotatedTranslatedPage(newpage,180,newpage.mediaBox.getWidth()/2, newpage.mediaBox.getHeight()/2,expand=True)
		output.addPage(page)
		os.remove('text{}.pdf'.format(i))

	outputStream = open("receipts.pdf", "wb")
	output.write(outputStream)
	outputStream.close()

	

	
	

