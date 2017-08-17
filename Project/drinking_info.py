from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
import sys

class Alcohol(QWidget):
    def __init__(self):
        super(Alcohol, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(600)
        self.setFixedHeight(520)
        self.move(100,100)
        self.setWindowTitle('Information on Alcohol Consumption')

        label = QLabel(self)
        pixmap = QPixmap('img/Alcohol_diagram.png')
        label.setPixmap(pixmap)
        self.show()

    def closeEvent(self, event):

        quit_msg = "Don't drink. It makes you become unproductive, which decreases your optimization potential."
        reply = QMessageBox.critical(self, 'Don\'t drink!',
                         quit_msg, QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    alc_info = Alcohol()
    sys.exit(app.exec_())
