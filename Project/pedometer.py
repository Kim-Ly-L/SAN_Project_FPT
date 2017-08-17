from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class MyPedometer(QWidget):
    def __init__(self):
        super(MyPedometer, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.move(20,20)
        self.setWindowTitle('Pedometer')
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
        	background-color: qlineargradient(x1: 0 ,y1: 0 ,x2: 1 ,y2: 1,
        						stop: 0 White, stop: 0.7 #558ed2);

         }
         """)
        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(0, 0, 300, 80)
        label_pedo = QLabel(self.lcd)
        label_pedo.setText("Walking: km")
        label_pedo.setGeometry(10, 10, 200, 50)
        label_pedo.setObjectName("pedo")
        label_pedo.setStyleSheet("""
         QLabel#pedo {
            font-family: Helvetica;
            font-size: 15px;
        	color: white;
            font-weight: bold;
         }
         """)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 60)
        self.slider.setFixedWidth(290)
        self.slider.move(5, 80)
        self.slider.valueChanged.connect(self.sliderChanged)
        label_range = QLabel(self)
        label_range.setText("How often do you go for a walk? ")
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(["Not very often.", "1-2 days/week", "3-5 days/week", "Every day!"])

        label_range.move(10, 140)
        self.dropdown.move(180, 135)
        self.button = QPushButton(self)
        self.button.setText("Submit")
        self.button.clicked.connect(self.submit)
        self.button.move(180, 160)
        self.show()

    def submit(self):  #secret thoughts of the app appear on the terminal
        if self.slider.value() <= 1:
            print "...You are not sportive enough and thus, no productive citizen. "
            quit_msg = "Warning: It is unhealthy to stay at home all day long."
            reply = QMessageBox.warning(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        elif 3 >= self.slider.value() > 1:
            print "...Let's apply some biopolitics in form of advice."
            quit_msg = "Tip: Going more often for a walk can increase your health and looks."
            reply = QMessageBox.information(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        elif 6 >= self.slider.value() > 3:
            print "...That's a fair amount."
            quit_msg = "Thumbs up!"
            reply = QMessageBox.information(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        elif 12 >= self.slider.value() > 6:
            print "...Looks like somebody is trying to get more sportive. Maybe we can help you to stay motivated with the proper ads."
            quit_msg = "Tip: The proper products and the right gym can increase your success in sports!"
            reply = QMessageBox.information(self, 'Notification',
                             quit_msg, QMessageBox.Yes)
        elif 30 >= self.slider.value() > 12:
            print "Wow! Trying to do a marathon or practicing for hiking? Some ads for outdoor sports and diet plans might help."
            quit_msg = "Are you practicing for any special occasion?"
            reply = QMessageBox.question(self, 'Notification',
                             quit_msg, QMessageBox.Yes, QMessageBox.No)
        else:
            print "Maybe you are a potential candidate for bigger events and responsibilities like the Federal Armed Forces."
            quit_msg = "Amazing! But make sure to get some rest."
            reply = QMessageBox.information(self, 'Notification',
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
    pedy = MyPedometer()
    sys.exit(app.exec_())
