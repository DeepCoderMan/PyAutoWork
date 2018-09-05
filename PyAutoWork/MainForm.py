#!/user/bin/env python
#-*- coding: utf-8 -*-

# 主界面
# 2018/8/25 19:44
# PyQt

import sys
from pyForm_form import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QImage,QPixmap

class MyMainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self, parent=None):   
            super(MyMainWindow, self).__init__(parent)
            self.setupUi(self)

    


    
    



