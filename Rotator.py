# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtRotator.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(298, 204)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 301, 211))
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(90, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 59, 16))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 70, 291, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(10, 100, 291, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 80, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 120, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(10, 140, 291, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 150, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 150, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(10, 170, 291, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Rotator Control"))
        self.label_2.setText(_translate("Form", "RumLogNG"))
        self.pushButton.setText(_translate("Form", "SP"))
        self.pushButton_2.setText(_translate("Form", "LP"))
        self.label_4.setText(_translate("Form", "Custom Heading"))
        self.pushButton_3.setText(_translate("Form", "SP"))
        self.pushButton_4.setText(_translate("Form", "LP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

