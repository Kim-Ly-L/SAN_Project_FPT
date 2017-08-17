from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
import sys

class Calmative(QWidget):
    def __init__(self):
        super(Calmative, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(270)
        self.setFixedHeight(360)
        self.move(100,100)
        self.setWindowTitle('Advertisement')

        label = QLabel(self)
        pixmap = QPixmap('img/calmative.png')
        label.setPixmap(pixmap)
        self.show()

    def closeEvent(self, event):
        quit_msg = "Stressed out? This calmative might help you. BUY IT."
        reply = QMessageBox.information(self, 'I LOVE CALMATIVES!',
                         quit_msg, QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calmatives = Calmative()
    sys.exit(app.exec_())
