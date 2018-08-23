#!/user/bin/env python
#-*- coding: UTF-8 -*-
import time
import datetime
import tkinter
import tkinter.filedialog as filedialog
from Operat.text_edit.write_log import write_log
from Operat.Keboard import KeyBoard
from Operat.short_cut_picturn import ImageProcees

imagePro = ImageProcees()
pos = imagePro.GetCenter('D:/github/PyAutoWork/PyAutoWork/PyAutoWork/image/test/new.PNG','D:/github/PyAutoWork/PyAutoWork/PyAutoWork/image/test/old.PNG')
print(pos)


