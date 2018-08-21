#  ===============================================================================
#  Project Name        :    Autowork
#  Project Description :
#  ===============================================================================
#  Class Name          :    Keyboard
#  Class Version       :    v1.0.0.0
#  Class Description   :    
#  Author              :    Administrator
#  Create Time         :    2018/8/18 15:33:50
#  Update Time         :    2014/8/18 13:51:50
#  ===============================================================================
#  Copyright ? peter 2018 . All rights reserved.
#  ===============================================================================


#coding=utf-8
from Operat.text_edit import write_log

class Keyboard(object):

	log = write_log.write_log("Keyboard")

	def __init__(self):
		log.Debug("keboard class instal")

	def _log(self,msg):
		log.Debug(msg)

	def __Error(self,error):
		log.Error(error)
