# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Rotator import Ui_Form

class PyRotator(Ui_Form):

   def __init__(self, *args, **kwargs):
       super(Ui_Form, self).__init__(*args, **kwargs)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = PyRotator()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

