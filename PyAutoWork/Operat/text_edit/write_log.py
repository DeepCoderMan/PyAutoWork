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
#  Copyright ? peter 2018 . All rights reserved.
#  ===============================================================================


#coding=utf-8
import logging
import unittest


class Keyboard:
    
    _fileName = ""

    def __init__(self,str_filename):

        _fileName = str_filena

        logging.basicConfig(filename='../LOG/'+_fileName+'.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level = logging.DEBUG,filemode='a',datefmt='%Y-%m-%d%I:%M:%S %p')

    def Debug(self,str_msg):
        logging.debug(str_msg)

    def Error(self,str_error):
        logging.debug(str_error)
    
    def Info(self,str_info):
        logging.info(str_info)

    def Warnning(self,str_warnning):
        logging.warning(str_warnning)

        

    

