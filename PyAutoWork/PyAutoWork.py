#!/user/bin/env python
#-*- coding: UTF-8 -*-
from tkinter import *
root = Tk()
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  ���������б����
listb2 = Listbox(root)
for item in li:                 # ��һ��С������������
    listb.insert(0,item)
 
for item in movie:              # �ڶ���С������������
    listb2.insert(1,item)
 
listb.pack()                    # ��С�������õ���������
listb2.pack()
root.mainloop()                 # ������Ϣѭ��
