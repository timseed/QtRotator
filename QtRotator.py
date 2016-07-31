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
        Form.resize(298, 192)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 301, 191))
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lbHeading = QtWidgets.QLabel(self.widget)
        self.lbHeading.setGeometry(QtCore.QRect(150, 40, 59, 16))
        self.lbHeading.setAutoFillBackground(True)
        self.lbHeading.setFrameShape(QtWidgets.QFrame.Box)
        self.lbHeading.setLineWidth(2)
        self.lbHeading.setText("")
        self.lbHeading.setObjectName("lbHeading")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(10, 90, 291, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.rl_SP = QtWidgets.QPushButton(self.widget)
        self.rl_SP.setGeometry(QtCore.QRect(120, 60, 51, 32))
        self.rl_SP.setObjectName("rl_SP")
        self.rl_LP = QtWidgets.QPushButton(self.widget)
        self.rl_LP.setGeometry(QtCore.QRect(180, 60, 51, 32))
        self.rl_LP.setObjectName("rl_LP")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.label_4.setObjectName("label_4")
        self.custHead = QtWidgets.QLineEdit(self.widget)
        self.custHead.setGeometry(QtCore.QRect(140, 110, 41, 21))
        self.custHead.setObjectName("custHead")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(10, 140, 291, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.cust_SP = QtWidgets.QPushButton(self.widget)
        self.cust_SP.setGeometry(QtCore.QRect(90, 150, 51, 32))
        self.cust_SP.setObjectName("cust_SP")
        self.cust_LP = QtWidgets.QPushButton(self.widget)
        self.cust_LP.setGeometry(QtCore.QRect(160, 150, 51, 32))
        self.cust_LP.setObjectName("cust_LP")
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(10, 170, 291, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.autoRun = QtWidgets.QCheckBox(self.widget)
        self.autoRun.setGeometry(QtCore.QRect(130, 10, 86, 20))
        self.autoRun.setObjectName("autoRun")
        self.left = QtWidgets.QPushButton(self.widget)
        self.left.setGeometry(QtCore.QRect(190, 110, 51, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.left.setFont(font)
        self.left.setObjectName("left")
        self.right = QtWidgets.QPushButton(self.widget)
        self.right.setGeometry(QtCore.QRect(240, 110, 51, 32))
        self.right.setObjectName("right")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Rotator Control"))
        self.label_2.setText(_translate("Form", "RumLogNG"))
        self.rl_SP.setText(_translate("Form", "SP"))
        self.rl_LP.setText(_translate("Form", "LP"))
        self.label_4.setText(_translate("Form", "Custom Heading"))
        self.cust_SP.setText(_translate("Form", "SP"))
        self.cust_LP.setText(_translate("Form", "LP"))
        self.autoRun.setText(_translate("Form", "CheckBox"))
        self.left.setText(_translate("Form", "-20"))
        self.right.setText(_translate("Form", "+20"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

