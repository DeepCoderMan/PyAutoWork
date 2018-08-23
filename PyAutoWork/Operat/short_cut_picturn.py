#!/user/bin/env python
# coding=utf-8
import cv2
import os
import numpy as np
import aircv as ac
from Operat.text_edit.write_log import write_log
class ImageProcees(object):

    _log = write_log("ImageProcees")

    def __init(self):
        self._log.Debug("ImageProcees init")

    def __draw_circle(self,img, pos, circle_radius, color, line_width):
        cv2.circle(img, pos, circle_radius, color, line_width)
        cv2.imshow('objDetect', img) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()

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

