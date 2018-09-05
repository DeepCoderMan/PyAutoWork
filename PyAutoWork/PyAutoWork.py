#!/user/bin/env python
#-*- coding: utf-8 -*-
import time
import datetime
import tkinter
import tkinter.filedialog as filedialog
from MainForm import *
from Operat.text_edit.write_log import write_log
from Operat.Keboard import KeyBoard
from Operat.short_cut_picturn import ImageProcees
from Operat.short_cut_picturn import ShotCut

#主程序入口

if __name__=="__main__":  
        app = QApplication(sys.argv)  
        myWin = MyMainWindow()  
        myWin.show()  
        try:
            app.exec_()  
        except Exception as e:
            print(e.message)