from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QRect
import sys

class SkyMoji2(QWidget):
    def __init__(self, imgpath, parent=None):
        super(SkyMoji2, self).__init__(parent)
        self.currentFrame = 0
        self.setPixmap(QPixmap(imgpath))
        self.startTimer(1000 / 15)

    def setPixmap(self, pix):
        self.pixmap = pix
        self.frameWidth = pix.rect().width()
        self.frameHeight = self.frameWidth
        self.numFrames = pix.rect().height() / self.frameHeight
        self.resize(self.frameWidth, self.frameHeight)

    def paintEvent(self, event):
        qp = QPainter(self)
        ypos = self.frameHeight * self.currentFrame
        sourceRect = QRect(0, ypos, self.frameWidth, self.frameHeight)
        qp.drawPixmap(self.rect(), self.pixmap, sourceRect)

    def timerEvent(self, event):
        self.currentFrame += 1
        if self.currentFrame == self.numFrames:
            self.currentFrame = 0
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    filepath = "img/sun_anim@2x.png"
    mywidget2 = SkyMoji2(filepath)
    mywidget2.setGeometry(50, 50, 200, 200)
    mywidget2.setWindowTitle("Protected Sex")
    mywidget2.show()
    sys.exit(app.exec_())
