
from PyQt4 import QtGui
from PyQt4.QtCore import QSize, QTimer, SIGNAL
from PyQt4.QtGui import *
import os, sys
import writepdf as wp

class PrettyWidget(QtGui.QWidget):
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.filePath = '' 
        self.initUI()
        self.args = ['','','']       
        
        
    def initUI(self):
        self.setGeometry(10,10,480,400)
        self.setWindowTitle('Create Receipts')    
        
        elabel = QLabel(self)
        elabel.move(20,20)
        elabel.setText("Name of Event")
        clabel = QLabel(self)
        clabel.move(20,90)
        clabel.setText("City")
        dlabel = QLabel(self)
        dlabel.move(20,160)
        dlabel.setText("Date")
        self.flabel = QLabel(self)
        self.flabel.move(110,260)
        self.flabel.setText('file not loaded')  

        self.eventbox = QLineEdit(self)
        self.eventbox.setPlaceholderText("Event")
        self.eventbox.move(20,40)
        self.eventbox.resize(280,30)
        self.citybox = QLineEdit(self)
        self.citybox.setPlaceholderText("City")
        self.citybox.move(20,110)
        self.citybox.resize(280,30)
        self.datebox = QLineEdit(self)
        self.datebox.setPlaceholderText("00/00")
        self.datebox.move(20,180)
        self.datebox.resize(280,30)

        self.eventbox.textChanged.connect(self.getevent)
        self.citybox.textChanged.connect(self.getcity)
        self.datebox.textChanged.connect(self.getdate)
        
        blabel = QLabel(self)
        blabel.move(20,230)
        blabel.setText("Load File")

        btn = QtGui.QPushButton('Browse', self)
        btn.move(20, 250)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.SingleBrowse)

        btn = QtGui.QPushButton('OK', self)
        btn.move(20, 300)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.onclicked)      

        self.show()

    def getevent(self):
    	self.args[0] = self.eventbox.text()

    def getcity(self):
    	self.args[1] = self.citybox.text()

    def getdate(self):
    	self.args[2] = self.datebox.text()

    def SingleBrowse(self):
        self.filePath = QtGui.QFileDialog.getOpenFileNames(self, 
                                                       'Single File',
                                                       "~/Desktop",
                                                      '*.csv*')[0]
        
        self.flabel.setText(self.filePath)
        self.flabel.resize(self.flabel.sizeHint())

    def onclicked(self):
    	print(self.args)
    	wp.fillout(self.filePath, self.args)
        
    
def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()


if __name__ == '__main__':
    main()