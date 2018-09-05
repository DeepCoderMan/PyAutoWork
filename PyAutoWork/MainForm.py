#!/user/bin/env python
#-*- coding: UTF-8 -*-

# 主界面
# 2018/8/25 19:44
# 基于 Tkinter

from tkinter import *
from Operat.text_edit.write_log import write_log
from Operat.Keboard import KeyBoard

class MainForm(object):
    """description of class"""
    widgh = 0
    hight = 0
    Form = Tk()
    title = "form"
    ProjName = ["开始循环","结束循环","鼠标左击hah","图片定位"]
    log = write_log("MainForm")
    listItem = Listbox(Form)
    listScl = Scrollbar(Form)
    def __init__(self,title,w,h):
        self.log.Debug("Main Form Initial")
        self.widgh = w
        self.hight = h
        self.title = title

        self.InitMainForm()#设计窗口
        self.Form.mainloop()

    def InitMainForm(self):
        self.center_window(self.widgh,self.hight)#设置窗口在屏幕中心
        self.Form.title(self.title)#Set Form Title
        self.listScl.grid(row = 1,column = 3)#Set Scroll In Form
        self.listItem = Listbox(self.Form,yscrollcommand = self.listScl.set)#creat ListBox be related to listScl
        self.listItem.grid(row = 1,column = 2)#Set List Box
        self.SetProjectBtn();# Add Project Choose Button In Form
        pass

   
    def center_window(self,width, height):
        screenwidth = self.Form.winfo_screenwidth()
        screenheight = self.Form.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2 - 50)
        self.Form.geometry(size)

    #按照 ProjName  设置按钮
    def SetProjectBtn(self):
        for t in  range(len(self.ProjName)):
            self.MyBtn(self.ProjName[t]).grid(row = t + 1,column = 1,sticky=E+W)

    #设置一个基本按钮
    def MyBtn(self,text):
        return Button(self.Form,text = text)

    #往listItem里添加内容
    def SetProjectList(self,item):
        self.listItem.insert(EXTENDED,item)

    


    
    



