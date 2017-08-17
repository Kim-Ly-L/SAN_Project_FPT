from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class MyWeight(QWidget):
    def __init__(self):
        super(MyWeight, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(300)  #U SHALL NOT RESIZE ME!!!!!!
        self.setFixedHeight(200) #RHHHHHAAAAWWWW
        self.move(20,20)
        self.setWindowTitle('Scales')
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
        	background-color: qlineargradient(x1: 0 ,y1: 0 ,x2: 1 ,y2: 1,
        						stop: 0 White, stop: 0.7 #558ed2);

         }
         """)
        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(0, 0, 300, 80) 
        label_weight = QLabel(self.lcd)
        label_weight.setText("Weight in kg")
        label_weight.setGeometry(10, 10, 200, 50)
        label_weight.setObjectName("weight")
        label_weight.setStyleSheet("""
         QLabel#weight {
            font-family: Helvetica;
            font-size: 15px;
        	color: white;
            font-weight: bold;
         }
         """)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(30, 50)
        self.slider.setFixedWidth(290)
        self.slider.move(5, 80)
        self.slider.valueChanged.connect(self.sliderChanged)
        label_range = QLabel(self)
        label_range.setText("Weight Category: ")
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(["30-50", "50-100", "100-200"])
        self.dropdown.currentIndexChanged.connect(self.rangeChanged)
        label_range.move(60, 140)
        self.dropdown.move(150, 135)
        self.button = QPushButton(self)
        self.button.setText("Submit")
        self.button.clicked.connect(self.submit)
        self.button.move(150, 160)
        self.show()

    def submit(self):  #secret thoughts of the app appear on the terminal
        if self.slider.value() <= 45:
            print "...You are clearly underweight or really small. Latter one would indicate a Napoleon complex. Interesting."
            quit_msg = "Warning: You could be underweight."
            reply = QMessageBox.warning(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        elif 60 >= self.slider.value() > 45:
            print "...Apparently, our applied biopolitics on you were successful."
            quit_msg = "Your weight is optimal."
            reply = QMessageBox.information(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        elif 85 >= self.slider.value() > 60:
            print "...Either you are chubby or tall. Hm. In any case, we could advertise and sell you snacks."
            quit_msg = "Depending on your height, you might need to take care of your weight as you could be already overweight."
            reply = QMessageBox.information(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        elif 100 >= self.slider.value() > 85:
            print "...Oooh, somebody wants Groupons for McDonalds."
            quit_msg = "Depending on your height, you must take care of your weight as you could be already overweight."
            reply = QMessageBox.warning(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        else:
            print "...Let's arrange some proper gym ads. This is getting out of our control."
            quit_msg = "Warning: You are heading towards obesity and should do some sports."
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

    def rangeChanged(self):
        item = self.dropdown.currentText()
        if item == "30-50":
            self.slider.setRange(30, 50)
        elif item == "50-100":
            self.slider.setRange(50, 100)
        elif item == "100-200":
            self.slider.setRange(100, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weighty = MyWeight()
    sys.exit(app.exec_())
