from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class MySleep(QWidget):
    def __init__(self):
        super(MySleep, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.move(20,20)
        self.setWindowTitle('SLEEP')
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
        	background-color: qlineargradient(x1: 0 ,y1: 0 ,x2: 1 ,y2: 1,
        						stop: 0 White, stop: 0.7 #558ed2);

         }
         """)
        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(0, 0, 300, 80)
        label_hours = QLabel(self.lcd)
        label_hours.setText("Hours last night")
        label_hours.setGeometry(10, 10, 200, 50)
        label_hours.setObjectName("hours")
        label_hours.setStyleSheet("""
         QLabel#hours {
            font-family: Helvetica;
            font-size: 15px;
        	color: white;
            font-weight: bold;
         }
         """)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 15)
        self.slider.setFixedWidth(290)
        self.slider.move(5, 80)
        self.slider.valueChanged.connect(self.sliderChanged)
        label_range = QLabel(self)
        label_range.setText("Hours per night on average ")
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(["3-5", "6-8", "9-12"])

        label_range.move(10, 140)
        self.dropdown.move(150, 135)
        self.button = QPushButton(self)
        self.button.setText("Submit")
        self.button.clicked.connect(self.submit)
        self.button.move(150, 160)
        self.show()

    def submit(self):  #secret thoughts of the app appear on the terminal
        if self.slider.value() <= 5:
            print "...Otherwise, you might get unproductive, which decreases your value as a citizen."
            quit_msg = "You should get more sleep."
            reply = QMessageBox.warning(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        elif 8 >= self.slider.value() > 5:
            print "...Apparently, our applied biopolitics on you were successful."
            quit_msg = "You sleep enough, that's good."
            reply = QMessageBox.information(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        elif 11 >= self.slider.value() > 8:
            print "...Sleeping too much decreases your productivity."
            quit_msg = "Somebody was really tired last night, hm?"
            reply = QMessageBox.question(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        else:
            print "...Don't you have work to do? If you sleep too much, you end up more sleepy than rested."
            quit_msg = "The optimal sleep range is 6-8 hours."
            reply = QMessageBox.warning(self, 'Notification',
                             quit_msg, QMessageBox.Yes)

        self.button.close()
        self.text1 = QLineEdit(self)
        self.text1.setText("Thank you for your submission.")
        self.text1.setGeometry(58, 160, 157, 20)
        self.text1.setStyleSheet("""
         QLineEdit {
            background-color: Gainsboro;
         }
         """)
        self.text1.show()

    def sliderChanged(self):
        newval = self.slider.value()
        self.lcd.display(newval)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sleepy = MySleep()
    sys.exit(app.exec_())
