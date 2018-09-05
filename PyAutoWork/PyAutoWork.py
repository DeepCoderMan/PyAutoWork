#!/user/bin/env python
#-*- coding: UTF-8 -*-
import time
import datetime
import tkinter
import tkinter.filedialog as filedialog
import MainForm
from Operat.text_edit.write_log import write_log
from Operat.Keboard import KeyBoard
from Operat.short_cut_picturn import ImageProcees
from Operat.short_cut_picturn import ShotCut

#主程序入口

mainForm = MainForm.MainForm("PyAutoWork",800,600)