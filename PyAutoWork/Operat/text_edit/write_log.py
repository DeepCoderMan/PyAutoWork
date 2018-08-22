#  ===============================================================================
#  Project Name        :    Autowork
#  Project Description :
#  ===============================================================================
#  Class Name          :    write_log
#  Class Version       :    v1.0.0.0
#  Class Description   :    
#  Author              :    peter
#  Create Time         :    2018/8/18 15:33:50
#  Update Time         :    2014/8/18 13:51:50
#  ===============================================================================
#  Copyright © peter 2018 . All rights reserved.
#  ===============================================================================


"""
    日志模块，单线程测试ok
"""

#coding=utf-8
import unittest
import os
import datetime

class write_log(object):
    
    _fileName = ""
    _filePath = ""
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
    nowLog = datetime.datetime.now().strftime('%Y-%m-%d')

    def __init__(self,str_filename = "log"):

        self._fileName = "logs/%s/%s.txt"%(str_filename,self.nowLog)
        self._filePath = "logs/%s"%(str_filename)
        self.__OpenCreatLog()

    def __OpenCreatLog(self):
        if os.path.isfile(self._fileName + "/" + self.nowLog + ".txt") == False:
            if os.path.exists(self._filePath) == False:
                os.makedirs(self._filePath)

            fp = open(self._fileName,'a+')

            fp.write("---- Creat log now! -------\n")

            fp.close()

    def Debug(self,str_msg):
        self.__writeLog("Debug",str_msg)

    def Error(self,str_error):
        self.__writeLog("Error",str_msg)
    def Info(self,str_info):
        self.__writeLog("Info",str_msg)
    def Warnning(self,str_warnning):
        self.__writeLog("Warning",str_msg)
    def __writeLog(self,mode,msg):
            str = "%s [%s]:%s"%(self.nowTime,mode,msg)

            fp = open(self._fileName,'a+')

            fp.write(str + "\n")

            fp.close()

    

