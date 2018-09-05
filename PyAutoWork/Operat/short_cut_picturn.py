#!/user/bin/env python
# coding=utf-8
import cv2
import os
import win32api #pyWin32
import win32con
import win32gui
import pythoncom
import pyHook
import numpy as np
import aircv as ac
import time
from PIL import Image,ImageGrab
from Operat.text_edit.write_log import write_log
from Operat.Keboard import KeyBoard

class ShotCut(object):

    _log = write_log("ShotCut")
    pos1 = [0,0]
    pos2 = [0,0]
    bCaptureSuc = False
    KeyB = KeyBoard()

    def __ini__(self):
         self._log.Debug("ShotCut init")

    def Capture(self,pos1,pos2,path = None):
        image = ImageGrab.grab((pos1[0], pos1[1], pos2[0], pos2[1]))
        if path != None :
            image.save(path)
        return image

    # 六秒截图法，缺点是不太人性化，
    # path = 截图保存路径，bshow 截图是否显示
    def MouseCapture(self,path,bShwo):
        print("3 秒后获取截图第一个位置")
        for count in range(3):
            print(count)
            time.sleep(1)
        self.pos1 = self.KeyB.cursor_point()
        print("获取到鼠标位置:%d,%d"%(self.pos1[0],self.pos1[1]))

        print("3 秒后获取截图第二个位置")
        for count in range(3):
            print(count)
            time.sleep(1)
        self.pos2 = self.KeyB.cursor_point()
        print("获取到鼠标位置:%d,%d"%(self.pos2[0],self.pos2[1]))

        image = self.Capture(self.pos1,self.pos2,path)
        if bShwo:
            image.show()


class ImageProcees(object):

    _log = write_log("ImageProcees")

    def __init__(self):
        self._log.Debug("ImageProcees init")

    def __draw_circle(self,img, pos, circle_radius, color, line_width):
        cv2.circle(img, pos, circle_radius, color, line_width)
        cv2.imshow('objDetect', img) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 大图及需要定位的图，小图即去大图中定位的图片，是否显示出来
    def GetCenter(self,bigImage,smallImage,Show = False):
        #ab = bigImage.split("\\")
        imsrc = ac.imread(bigImage)
        imobj = ac.imread(smallImage)

        # find the match position
        pos = ac.find_template(imsrc, imobj)

        circle_center_pos = pos['result']
        x = int(circle_center_pos[0])  
        y = int(circle_center_pos[1])  
        position = (x,y) 

        circle_radius = 50
        color = (0, 255, 0)
        line_width = 10
        #print(position)
        # draw circle
        if(Show):
            self.__draw_circle(imsrc, position, circle_radius, color, line_width)

        self._log.Debug("Big Image: " + bigImage)
        self._log.Debug("Small Image: " + smallImage)
        str1 = "Get Center pos: %d,%d"% (position[0],position[1])
        self._log.Debug(str1)
        return position

