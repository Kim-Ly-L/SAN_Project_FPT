from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
import sys

class Ironman(QWidget):
    def __init__(self):
        super(Ironman, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(280)
        self.setFixedHeight(380)
        self.move(100,100)
        self.setWindowTitle('Advertisement')

        label = QLabel(self)
        pixmap = QPixmap('img/iron_ad.png')
        label.setPixmap(pixmap)
        self.show()

    def closeEvent(self, event):
        quit_msg = "TIP: Limited Edition only for a short time. BUY IT."
        reply = QMessageBox.information(self, 'You logged in \'Masturbation\'',
                         quit_msg, QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ironman = Ironman()
    sys.exit(app.exec_())
