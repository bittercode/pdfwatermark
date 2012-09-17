import sys
import PySide
import pdfhandler
from PySide import QtGui
from PySide import QtCore
from gui import Ui_MainWindow

class MyForm(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        self.btnFindFile.clicked.connect(self.getfile)
        self.btnGo.clicked.connect(self.applymark)
        
    def getfile(self):
        fileName,fltr = QtGui.QFileDialog.getOpenFileName(self,
            "Open Image", "/mnt/f002/jr/CON1301 N Journal Internal Transfers", "Email PDF (*.pdf)")
        print fileName
        
        self.lnFile.setText(fileName)
    
    def applymark(self):
        #Stop them if ref is empty
        ref = self.lnRef.text()
        fileName = self.lnFile.text()
        fpath = fileName.rsplit('/',1)
        
        fileout = fpath[0] + '/' + ref + '.pdf'
        print fileout
        #Otherwise send over file name and ref
        pdfh = pdfhandler.PyWatermark()
        pdfh.AddWatermark(ref, fileName,fileout)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    frame = MyForm()
    frame.show()
    app.exec_()
    