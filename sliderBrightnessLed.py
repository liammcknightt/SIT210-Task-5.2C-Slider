import sys
import RPI.GPIO as GPIO
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 263)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(140, 100, 160, 22))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(190, 150, 64, 23))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.onButton = QtWidgets.QRadioButton(self.centralwidget)
        self.onButton.setGeometry(QtCore.QRect(170, 60, 82, 17))
        self.onButton.setObjectName("onButton")
        self.offButton = QtWidgets.QRadioButton(self.centralwidget)
        self.offButton.setGeometry(QtCore.QRect(240, 60, 82, 17))
        self.offButton.setObjectName("offButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.onButton.setText(_translate("MainWindow", "On"))
        self.offButton.setText(_translate("MainWindow", "Off"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.led = 10

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.led, GPIO.OUT)

        self.onButton.toggled.connect(self.checkled)

        self.ledPwm = GPIO.PWM(self.lef, 100)

        self.ledPwm.start(0)

        self.lcdNumber.display(0)

        self.slider.valueChanged.connect(self.changeLedIntensity)

    def checkLed(self):
        if self.onButton.isChecked():
            GPIO.output(self.led, GPIO.HIGH)
            self.ledPwm.ChangeDutyCycle(100)
            self.slider.setValue(100)
            self.lcdNumber.display(100)
            print("LED ON")
            print("LED Intensity: 100%")
        else:
            GPIO.output(self.led, GPIO.LOW)
            self.ledPwm.ChangeDutyCycle(0)
            self.slider.setValue(0)
            self.lcdNumber.display(0)
            print("LED ON")
            print("LED Intensity: 0%")
  
    def changeLedIntensity(self, value):
        if self.onButton.isChecked():
            self.ledPwm.ChangeDutyCycle(value)
            self.lcdNumber.display(value)
            print("Led Intensity:" value)

    def closeEvent(self, event):
        GPIO.output(self.led, GPIO.LOW)
        self.ledPwm.stop()
        GPIO.cleanup()

        super().closeEvent(event)

if __name__ == "__main__"
    GPIO.setwarnings(False)

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
