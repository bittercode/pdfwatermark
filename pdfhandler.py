#This sample uses two third part modules for Python,
#pyPdf & ReportLab to achieve creating and placing
#watermark text at angle on an existing PDF file.
#This example was produced with Python 2.7
#See http://pybrary.net/pyPdf for more informaton about pyPdf.
#See http://www.reportlab.com for more information about ReportLab. 

#Import the needed external modules and functions from pyPdf and reportlab.
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
import os

class PyWatermark(object):
    
    def AddWatermark(self,watermark,pdffile):
        #Use reportlab to create a PDF that will be used
        #as a watermark on another PDF.
        fileout = "temp2_watermark.pdf"
        c= canvas.Canvas("temp_watermark.pdf")
        c.setFont("Courier", 60)
        c.setTitle("Stamped")
        #This next setting with make the text of our
        #watermark gray, nice touch for a watermark.
        c.setFillGray(0.5,0.5)
        #Set up our watermark document. Our watermark
        #will be rotated 45 degrees from the direction
        #of our underlying document.
        c.saveState()
        c.translate(500,100)
        c.rotate(45)
        c.drawCentredString(0, 0, watermark)
        c.drawCentredString(0, 150, watermark)
        c.drawCentredString(0, 400,  watermark)
        c.restoreState()
        c.save() 
        
        #Read in the PDF that will have the PDF applied to it.
        output = PdfFileWriter()
        input1 = PdfFileReader(file(pdffile, "rb"))
        
        #Read in the file created above by ReportLab for our watermark.
        twatermark = PdfFileReader(file("temp_watermark.pdf", "rb"))
        
        numPages = input1.getNumPages()
        for i in range(numPages):
        
            #Open up the orgininal PDF.
            page1 = input1.getPage(i)
        
            #Apply the watermark by merging the two PDF files.
            page1.mergePage(twatermark.getPage(0))
            #Send the resultant PDF to the output stream.
            output.addPage(page1)
        
        #write the output of our new, watermarked PDF.
        outputStream = file(fileout, "wb")
        output.write(outputStream)
        outputStream.close()
        os.remove("temp_watermark.pdf")
        #os.remove(filein)
        copyfile(fileout,pdffile)
        os.remove(fileout)
     
    def PrintInfo(self,watermark,pdffile):
        #Use reportlab to create a PDF that will be used
        #as a watermark on another PDF.
        fileout = "temp2_watermark.pdf"
        c= canvas.Canvas("temp_watermark.pdf")
        c.setFont("Courier", 60)
        c.setTitle("Stamped")
        #This next setting with make the text of our
        #watermark gray, nice touch for a watermark.
        c.setFillGray(0.5,0.5)
        #Set up our watermark document. Our watermark
        #will be rotated 45 degrees from the direction
        #of our underlying document.
        c.saveState()
        c.translate(500,100)
        c.rotate(315)
        c.drawCentredString(0, 0, watermark)
        c.drawCentredString(0, 300, watermark)
        c.drawCentredString(0, 600,  watermark)
        c.restoreState()
        c.save() 
        
        #Read in the PDF that will have the PDF applied to it.
        output = PdfFileWriter()
        input1 = PdfFileReader(file(pdffile, "rb"))
        
        print "pages:" + str(input1.getNumPages())
        print "title:" + str(input1.getDocumentInfo().title)
        
        #Open up the orgininal PDF.
        #page1 = input1.getPage(0)
        
        #Read in the file created above by ReportLab for our watermark.
        #twatermark = PdfFileReader(file("temp_watermark.pdf", "rb"))
        #Apply the watermark by merging the two PDF files.
        #page1.mergePage(twatermark.getPage(0))
        #Send the resultant PDF to the output stream.
        #output.addPage(page1)
        
        #write the output of our new, watermarked PDF.
        #outputStream = file(fileout, "wb")
        #output.write(outputStream)
        #outputStream.close()
        #os.remove("temp_watermark.pdf")
        #os.remove(filein)
        #copyfile(fileout,pdffile)
        #os.remove(fileout)
        