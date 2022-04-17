# import Important modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic,QtGui
import lists as l 
import sys
import qdarkstyle


#_Welcom_page_########################################################################
class WelcomScreen(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('welcome.ui',self)
        






def main(WelcomScreen):
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    ###########################################################
    welcome = WelcomScreen()
    widget.addWidget(welcome)
   
    ##########################################################
    widget.setFixedHeight(510)
    widget.setFixedWidth(800)
    widget.setWindowIcon(QIcon('icon.png'))
    widget.setWindowTitle('  EsT Fes Inscription ')
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        pass



if __name__ == "__main__":
    main(WelcomScreen)