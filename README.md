
#QtPt Interface to the rotator

At this point you must have installed 

  - createed a pyqt virtual environment && are using it
  - qt the dmg package
  - sip bolt on
  - pyqt

We have run designer and saved a UI file.



#Test the UI

First build the Python code using **pyuic** as we are running QT5 this is

    pyuic5 -x Rotator.ui > Rotator.py


I then can test the file by

   python Rotator.py
   
Asssuming it works...


#Make a Class of the UI

The UI will be overwritten by the pyuic command - so we need to create a class code that came from the pyuic command


##Original Header of Rotator

This is what the rotator file originally looked like

```python
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
```


Note the Warnings about loosing changes.


##Create a new Python File

With an editor create a new python file that looks like this

I am calling this file RotClass.py

```python
# -*- coding: utf-8 -*-
#RotClass.py
from PyQt5 import QtCore, QtGui, QtWidgets
from Rotator import Ui_Form

class PyRotator(Ui_Form):

   def __init__(self, *args, **kwargs):
       super(Ui_Form, self).__init__(*args, **kwargs)

```

And in theory you are done - you now can add your methods and new classes - and carry on.

If you want to test this then add this at the bottom of the RotClass.py file


```python
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = PyRotator()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
```


And run with

    python RotClass.py
    
    
#Adding Functionality

I now want to add some custom functionality - but remember I can not alter the UI generated file, I am having trouble **super** the setupUi so I do currently in 2 steps

by using my custom setup called **mysetup** I do not see why it is not callable like this

```
    def setupUi(self, *args, **kwargs):
        super(Ui_Form, self).setupUi(*args, **kwargs)
        self.cust_SP.clicked.connect(lambda: self.MyClicked("cust_SP"))
        self.cust_LP.clicked.connect(lambda: self.MyClicked("cust_LP"))
        self.rl_LP.clicked.connect(lambda: self.MyClicked("rl_LP"))
        self.rl_SP.clicked.connect(lambda: self.MyClicked("rl_SP"))
```

But at the moment I can not get this to work - hence the code now looks like this.


```python
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
```
