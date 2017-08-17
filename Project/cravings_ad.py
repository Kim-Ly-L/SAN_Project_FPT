from PyQt5.QtWidgets import QApplication, qApp, QWidget, QLabel
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtGui import QIcon, QPixmap
import sys

class Cravings_ad(QWidget):
    def __init__(self, xpos, ypos, title):
        super(Cravings_ad, self).__init__()
        self.acceleration = 5.0
        self.velocity = 0.0
        self.screenHeight = qApp.desktop().availableGeometry().height()
        self.makeWin(xpos, ypos, title)

    def makeWin(self, xpos, ypos, title):
        self.setGeometry(xpos, ypos, 400, 330)
        self.setWindowTitle(title)
        label = QLabel(self)
        pixmap = QPixmap('img/mcdonalds_ad.png')
        label.setPixmap(pixmap)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animateFrame)
        self.timer.start(1000 / 12)


    def animateFrame(self):
        xpos = self.pos().x()
        ypos = self.pos().y() + self.velocity
        if (ypos + self.height()) > self.screenHeight:
            ypos = self.screenHeight - self.height()
            if abs(self.velocity) <= self.acceleration:
                self.velocity = 0.0
            else:
                self.velocity *= -1.0
        self.move(xpos, ypos)
        self.velocity += self.acceleration


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win1 = Cravings_ad(630, 10, "Advertisement")
    win1.show()
    sys.exit(app.exec_())
