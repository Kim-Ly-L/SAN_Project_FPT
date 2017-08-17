from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
import sys

class Travelbox(QWidget):
    def __init__(self):
        super(Travelbox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.move(20,20)
        self.setWindowTitle('Travel')
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
        	background-color: qlineargradient(x1: 0 ,y1: 0 ,x2: 1 ,y2: 1,
        						stop: 0 White, stop: 0.7 #ffb681);
         }
         """)
        label = QLabel(self)
        pixmap = QPixmap('img/Travel.png')
        pixmap = pixmap.scaledToWidth(70)
        label.setPixmap(pixmap)
        label.move(112, 15)
        self.labelquestion = QLabel(self)
        self.labelquestion.setText("Where are you right now?")
        self.labelquestion.setStyleSheet("""
         QLabel {
        	font: 9pt;
            color: white;
            font-weight: bold;
         }
         """)
        self.labelquestion.move(72, 100)
        self.lineedit = QLineEdit("Type in your Destination...", self)
        self.lineedit.setGeometry(77, 130, 140, 20)
        self.button = QPushButton(self)
        self.button.setText("Submit")
        self.button.clicked.connect(self.submit)
        self.button.move(110, 160)
        self.show()

    def submit(self):
        self.button.close()
        self.lineedit.close()
        self.text1 = QLineEdit(self)
        self.text1.setText("Thank you for your submission.")
        self.text1.setGeometry(68, 160, 157, 25)
        self.text1.setStyleSheet("""
         QLineEdit {
            background-color: Gainsboro;
         }
         """)
        self.text1.show()
        quit_msg = "Thanks for the information. Now we can keep on observing you."
        reply = QMessageBox.information(self, 'Every day is April Fool\'s Day.',
                             quit_msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    travelling = Travelbox()
    sys.exit(app.exec_())
