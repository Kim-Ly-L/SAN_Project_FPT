from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
import sys

class Sanitary(QWidget):
    def __init__(self):
        super(Sanitary, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(600)
        self.setFixedHeight(420)
        self.move(100,100)
        self.setWindowTitle('Advertisement')

        label = QLabel(self)
        pixmap = QPixmap('img/always.png')
        label.setPixmap(pixmap)
        self.show()

    def closeEvent(self, event):

        quit_msg = "This is the best brand for Sanitary Towels. BUY IT."
        reply = QMessageBox.information(self, 'I LOVE ALWAYS!',
                         quit_msg, QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sanitaryad = Sanitary()
    sys.exit(app.exec_())
