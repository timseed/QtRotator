# -*- coding: utf-8 -*-
from QtRotator import Ui_Form
from PyQt5 import QtCore, QtWidgets, QtGui
from ham_dev.rotator import spid3,spid_serial3
from RumLogNG import RumLogNg

class PyRotator(Ui_Form):

    def __init__(self, *args, **kwargs):
        super(Ui_Form, self).__init__(*args, **kwargs)
        self.CheckHeading=1*1000   #in Milli Secs
        self.timer=QtCore.QTimer()
        self.firstTime=True
        self.oldHeading=-1
        self.Heading=-1
        self.RAK = spid3(port="/dev/tty.usbserial-A104FZJ8",speed=1200)
        self.rl=RumLogNg()


    def mysetup(self):
        self.cust_SP.clicked.connect(lambda: self.TurnTo(ShortPath=True, Logger=False))
        self.cust_LP.clicked.connect(lambda: self.TurnTo(ShortPath=False, Logger=False))
        self.rl_LP.clicked.connect(lambda: self.TurnTo(ShortPath=False, Logger=True))
        self.rl_SP.clicked.connect(lambda: self.TurnTo(ShortPath=True, Logger=True))
        self.left.clicked.connect(lambda: self.Turn(Offset=-20))
        self.right.clicked.connect(lambda: self.Turn(Offset=20))
        self.setup_timer()


    def setup_timer(self):
        self.timer.timeout.connect(self.OnTimer)
        self.timer.start(self.CheckHeading)

    def OnTimer(self):
        print("Timer has gone off")
        if self.autoRun.isChecked():
            heading = self.rl.get_heading()
            if self.firstTime:
                self.oldHeading=self.oldHeading
                self.firstTime=False
            else:
                if heading != -1:
                    print(str.format("Heading is {}", str(heading)))
                    self.lbHeading.setText(str(heading))
                    self.Heading=heading


                else:
                    print("Bad Heading ? Is the prograsm running ??")
        else:
            print("Not into Auto Mode only looking for Custom Headings")

    def TurnTo(self, ShortPath, Logger):

        print("Turn too is called ")
        if Logger:
            if ShortPath:
                print("Turn too Logger ShortPath")
                self.RAK.moveto(self.Heading)
            else:
                #Need to write
                print("Turn too Logger LongPath")
                self.RAK.moveto(self.Heading)
        else:
            try:
                cust_heading=int(self.custHead.text())
                print(str.format("Moving to Cusom heading {}", cust_heading))
                if ShortPath:
                    self.RAK.moveto(cust_heading)
                else:
                    #Need to write
                    self.RAK.moveto(cust_heading)
                print(str.format("Moving to Cusom heading {}",cust_heading))
            except Exception as err:
                print(str.format('Exception in custom heading {}',str(err)))

    def Turn(self,Offset):
        current=self.RAK.status()
        try:
            current=int(current)
            current=current+Offset
            if current < 0:
                current += 360
            if current > 360:
                current=current%360
            self.RAK.moveto(current)
            self.custHead.setText(str(current))
        except:
            print("Error getting heading from SPID")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = PyRotator()
    ui.setupUi(Form)
    ui.mysetup()
    Form.show()
    sys.exit(app.exec_())

