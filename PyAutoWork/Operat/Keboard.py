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
import win32api
import win32con
import win32gui
import pythoncom
import pyHook
import time
from ctypes import *
from Operat.text_edit.write_log import write_log

class KeyBoard(object):
    _log = write_log("keyboad")
    _KeyCode_strKey = {'None':0,'LButton':1,'RButton':2,'Cancel':3,'MButton':4,'XButton1':5,'XButton2':6,'Back':8,'Tab':9,'LineFeed':10,'Clear':12,'Return':13,'Return':13,'ShiftKey':16,'ControlKey':17,'Menu':18,'Pause':19,'Capital':20,'Capital':20,'KanaMode':21,'KanaMode':21,'KanaMode':21,'JunjaMode':23,'FinalMode':24,'HanjaMode':25,'HanjaMode':25,'Escape':27,'IMEConvert':28,'IMENonconvert':29,'IMEAceept':30,'IMEAceept':30,'IMEModeChange':31,'Space':32,'PageUp':33,'PageUp':33,'Next':34,'Next':34,'End':35,'Home':36,'Left':37,'Up':38,'Right':39,'Down':40,'Select':41,'Print':42,'Execute':43,'PrintScreen':44,'PrintScreen':44,'Insert':45,'Delete':46,'Help':47,'D0':48,'D1':49,'D2':50,'D3':51,'D4':52,'D5':53,'D6':54,'D7':55,'D8':56,'D9':57,'A':65,'B':66,'C':67,'D':68,'E':69,'F':70,'G':71,'H':72,'I':73,'J':74,'K':75,'L':76,'M':77,'N':78,'O':79,'P':80,'Q':81,'R':82,'S':83,'T':84,'U':85,'V':86,'W':87,'X':88,'Y':89,'Z':90,'LWin':91,'RWin':92,'Apps':93,'Sleep':95,'NumPad0':96,'NumPad1':97,'NumPad2':98,'NumPad3':99,'NumPad4':100,'NumPad5':101,'NumPad6':102,'NumPad7':103,'NumPad8':104,'NumPad9':105,'Multiply':106,'Add':107,'Separator':108,'Subtract':109,'Decimal':110,'Divide':111,'F1':112,'F2':113,'F3':114,'F4':115,'F5':116,'F6':117,'F7':118,'F8':119,'F9':120,'F10':121,'F11':122,'F12':123,'F13':124,'F14':125,'F15':126,'F16':127,'F17':128,'F18':129,'F19':130,'F20':131,'F21':132,'F22':133,'F23':134,'F24':135,'NumLock':144,'Scroll':145,'LShiftKey':160,'RShiftKey':161,'LControlKey':162,'RControlKey':163,'LMenu':164,'RMenu':165,'BrowserBack':166,'BrowserForward':167,'BrowserRefresh':168,'BrowserStop':169,'BrowserSearch':170,'BrowserFavorites':171,'BrowserHome':172,'VolumeMute':173,'VolumeDown':174,'VolumeUp':175,'MediaNextTrack':176,'MediaPreviousTrack':177,'MediaStop':178,'MediaPlayPause':179,'LaunchMail':180,'SelectMedia':181,'LaunchApplication1':182,'LaunchApplication2':183,'Oem1':186,'Oem1':186,'Oemplus':187,'Oemcomma':188,'OemMinus':189,'OemPeriod':190,'OemQuestion':191,'OemQuestion':191,'Oemtilde':192,'Oemtilde':192,'OemOpenBrackets':219,'OemOpenBrackets':219,'Oem5':220,'Oem5':220,'Oem6':221,'Oem6':221,'Oem7':222,'Oem7':222,'Oem8':223,'OemBackslash':226,'OemBackslash':226,'ProcessKey':229,'Packet':231,'Attn':246,'Crsel':247,'Exsel':248,'EraseEof':249,'Play':250,'Zoom':251,'NoName':252,'Pa1':253,'OemClear':254,'KeyCode':65535,'Shift':65536,'Control':131072,'Alt':262144,'Modifiers':-65536}

    _KeyCode_numKey = {0:'None',1:'LButton',2:'RButton',3:'Cancel',4:'MButton',5:'XButton1',6:'XButton2',8:'Back',9:'Tab',10:'LineFeed',12:'Clear',13:'Return',13:'Return',16:'ShiftKey',17:'ControlKey',18:'Menu',19:'Pause',20:'Capital',20:'Capital',21:'KanaMode',21:'KanaMode',21:'KanaMode',23:'JunjaMode',24:'FinalMode',25:'HanjaMode',25:'HanjaMode',27:'Escape',28:'IMEConvert',29:'IMENonconvert',30:'IMEAceept',30:'IMEAceept',31:'IMEModeChange',32:'Space',33:'PageUp',33:'PageUp',34:'Next',34:'Next',35:'End',36:'Home',37:'Left',38:'Up',39:'Right',40:'Down',41:'Select',42:'Print',43:'Execute',44:'PrintScreen',44:'PrintScreen',45:'Insert',46:'Delete',47:'Help',48:'D0',49:'D1',50:'D2',51:'D3',52:'D4',53:'D5',54:'D6',55:'D7',56:'D8',57:'D9',65:'A',66:'B',67:'C',68:'D',69:'E',70:'F',71:'G',72:'H',73:'I',74:'J',75:'K',76:'L',77:'M',78:'N',79:'O',80:'P',81:'Q',82:'R',83:'S',84:'T',85:'U',86:'V',87:'W',88:'X',89:'Y',90:'Z',91:'LWin',92:'RWin',93:'Apps',95:'Sleep',96:'NumPad0',97:'NumPad1',98:'NumPad2',99:'NumPad3',100:'NumPad4',101:'NumPad5',102:'NumPad6',103:'NumPad7',104:'NumPad8',105:'NumPad9',106:'Multiply',107:'Add',108:'Separator',109:'Subtract',110:'Decimal',111:'Divide',112:'F1',113:'F2',114:'F3',115:'F4',116:'F5',117:'F6',118:'F7',119:'F8',120:'F9',121:'F10',122:'F11',123:'F12',124:'F13',125:'F14',126:'F15',127:'F16',128:'F17',129:'F18',130:'F19',131:'F20',132:'F21',133:'F22',134:'F23',135:'F24',144:'NumLock',145:'Scroll',160:'LShiftKey',161:'RShiftKey',162:'LControlKey',163:'RControlKey',164:'LMenu',165:'RMenu',166:'BrowserBack',167:'BrowserForward',168:'BrowserRefresh',169:'BrowserStop',170:'BrowserSearch',171:'BrowserFavorites',172:'BrowserHome',173:'VolumeMute',174:'VolumeDown',175:'VolumeUp',176:'MediaNextTrack',177:'MediaPreviousTrack',178:'MediaStop',179:'MediaPlayPause',180:'LaunchMail',181:'SelectMedia',182:'LaunchApplication1',183:'LaunchApplication2',186:'Oem1',186:'Oem1',187:'Oemplus',188:'Oemcomma',189:'OemMinus',190:'OemPeriod',191:'OemQuestion',191:'OemQuestion',192:'Oemtilde',192:'Oemtilde',219:'OemOpenBrackets',219:'OemOpenBrackets',220:'Oem5',220:'Oem5',221:'Oem6',221:'Oem6',222:'Oem7',222:'Oem7',223:'Oem8',226:'OemBackslash',226:'OemBackslash',229:'ProcessKey',231:'Packet',246:'Attn',247:'Crsel',248:'Exsel',249:'EraseEof',250:'Play',251:'Zoom',252:'NoName',253:'Pa1',254:'OemClear',65535:'KeyCode',65536:'Shift',131072:'Control',262144:'Alt',-65536:'Modifiers'}

    def __init__(self):
        self._log.Debug("keyboard init")

    def Clicked(self,key):
        win32api.keybd_event(key,0,0,0)
        time.sleep(0.02)
        win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)
        self._log.Debug(str(key) + " Cliecked")

    def KeyDown(self,key):
        win32api.keybd_event(key,0,0,0)
        self._log.Debug(str(key) + " Down")

    def KeyUp(self,key):
        win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0)
        self._log.Debug(str(key) + " Up")

    def Key_NumToStr(self,num):
        return self._KeyCode_numKey[num]

    def Key_StrToNum(self,str):
        return self._KeyCode_strKey[str]

    #获取鼠标位置
    def cursor_point(self):
        pos = win32api.GetCursorPos()
        return int(pos[0]), int(pos[1])

    #移动鼠标位置
    def mouse_move(self, new_x, new_y):
        if new_y is not None and new_x is not None:
            point = (new_x, new_y)
            win32api.SetCursorPos(point)

    #键盘输入文本
    def key_input(self, input_words=''):
        for word in input_words:
            win32api.keybd_event(self.Key_StrToNum(word), 0, 0, 0)
            win32api.keybd_event(self.Key_StrToNum(word), 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.1)

     # 鼠标右击事件
     # :param new_x: 新移动的坐标x轴坐标
     # :param new_y: 新移动的坐标y轴坐标
    def mouse_right_click(self, new_x=None, new_y=None):
        self.mouse_move(new_x, new_y)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    #鼠标左击事件
    #:param new_x: 新移动的坐标x轴坐标
    #:param new_y: 新移动的坐标y轴坐标1506240215
    #:param times: 点击次数
    def mouse_left_click(self, new_x=None, new_y=None, times=1):
        self.mouse_move(new_x, new_y)
        time.sleep(0.05)
        while times:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            times -= 1

    #键盘输入事件
    def key_even(self, input_key):
        win32api.keybd_event(VK_CODE[input_key], 0, 0, 0)
        win32api.keybd_event(VK_CODE[input_key], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)