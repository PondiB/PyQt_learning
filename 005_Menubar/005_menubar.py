import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Creating the menu bar")
        self.setWindowIcon(QtGui.QIcon('pondilogo.jpg'))

        extractAction =QtGui.QAction("&LINK UP", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu =self.menuBar()
        fileMenu =mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu =mainMenu.addMenu('&Faith')
        fileMenu.addAction(extractAction)


        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
        self.show()

    def close_application(self):
        print ("Custom!!!")
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
run()