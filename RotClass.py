# -*- coding: utf-8 -*-
from Rotator import Ui_Form
from PyQt5 import QtCore, QtWidgets, QtGui


class PyRotator(Ui_Form):

    def __init__(self, *args, **kwargs):
        super(Ui_Form, self).__init__(*args, **kwargs)

    def mysetup(self):
        self.cust_SP.clicked.connect(lambda: self.MyClicked("cust_SP"))
        self.cust_LP.clicked.connect(lambda: self.MyClicked("cust_LP"))
        self.rl_LP.clicked.connect(lambda: self.MyClicked("rl_LP"))
        self.rl_SP.clicked.connect(lambda: self.MyClicked("rl_SP"))

    def MyClicked(self,btname=""):
        print(str.format('Button {} was clicked',btname))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = PyRotator()
    ui.setupUi(Form)
    ui.mysetup()
    Form.show()
    sys.exit(app.exec_())

