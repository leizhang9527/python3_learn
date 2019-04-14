# -*- coding: utf-8 -*-

import wave
import time
import json 
import pycurl
from datetime import datetime
from pyaudio import PyAudio, paInt16
import urllib.request as urllib2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

#from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
  
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        self.framerate=8000   #采样率
        self.NUM_SAMPLES=2000 #采样点
        self.channels=1  #一个声道
        self.sampwidth=2 #两个字节十六位
        self.TIME=2      #条件变量，可以设置定义录音的时间
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    def save_wave_file(self, filename, data):   #save the date to the wav file
        wf = wave.open(filename, 'wb')  #二进制写入模式
        wf.setnchannels(self.channels)  
        wf.setsampwidth(self.sampwidth)  #两个字节16位
        wf.setframerate(self.framerate)  #帧速率
        wf.writeframes(b"".join(data))  #把数据加进去，就会存到硬盘上去wf.writeframes(b"".join(data)) 
        wf.close()
        
    def my_record(self):
        pa = PyAudio()
        stream = pa.open(format = paInt16,channels = 1,
                          rate = self.framerate,input = True,
                         frames_per_buffer = self.NUM_SAMPLES)
        my_buf = []
        count = 0
        time.sleep(5)
        print('开始录音')
    #    time.sleep(10)
        while count < self.TIME*2:
            string_audio_data = stream.read(self.NUM_SAMPLES)
            my_buf.append(string_audio_data)
            count += 1
            print('.')
        filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+".wav"
        self.save_wave_file(filename, my_buf)
        stream.close()
        
    def dump_res(self, buf):  #dump_res即dump_result,buf是curl从网上返回来的缓存
        print(buf)
        my_temp=json.loads(buf)
        if my_temp['err_no'] :
            if my_temp['err_no'] == 3300:
                print('输入参数不正确')
            elif my_temp['err_no'] == 3301:
                print('音频质量过差')
            elif my_temp['err_no'] == 3302:
                print('鉴权失败')
            elif my_temp['err_no'] == 3303:
                print('语音服务器后端问题')
            elif my_temp['err_no'] == 3304:
                print('用户的请求QPS超限')
            elif my_temp['err_no'] == 3305:
                print('用户的日pv（日请求量）超限')
            elif my_temp['err_no'] == 3307:
                print('语音服务器后端识别出错问题')
            elif my_temp['err_no'] == 3308:
                print('音频过长')
            elif my_temp['err_no'] == 3309:
                print('音频数据问题')
            elif my_temp['err_no'] == 3310:
                print('输入的音频文件过大')
            elif my_temp['err_no'] == 3311:
                print('采样率rate参数不在选项里')
            elif my_temp['err_no'] == 3312:
                print('音频格式format参数不在选项里')
        else:
            my_list=my_temp['result']
            print(type(my_list))
            print(my_list[0])  #输出第一个
            print('dump_res函数调用成功！')
            
    def get_token(self):  #获取token
        apikey='tasNprtTUkhRQAMO2Cw3kwlU'
        secretkey='QoOlCFa0KGd1cYtMr4NSvyAIWPgLjXyG'
        auth_url='https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+apikey+'&client_secret=' +secretkey;
        
        res=urllib2.urlopen(auth_url) #获取服务器响应,res=urllib2.urlopen(auth_url) 
        json_data=res.read()         #读取到json_data中
        print(json_data,type(json_data))
        return json.loads(json_data)['access_token']
        
    def use_cloud(self, token):  #token类似一种访问权限等
        fp=wave.open(filename,'rb')             #打开wav文件
        nf=fp.getnframes()                     #获得文件的采样点数量
        print('sampwidth',fp.getsampwidth())
        print('framerate',fp.getframerate())
        print('channels',fp.getnchannels())
        f_len=nf*2                    #获取文件长度,文件长度计算，每个采样点2个字节
        audio_data=fp.readframes(nf)  #
        
        cuid="XXXXXXXXXX"   #硬件地址，my phone xiaomi MAC
        print(token)
        srv_url='http://vop.baidu.com/server_api'+'?cuid='+cuid+'&token='+token
        http_header=[
            'Content-Type:audio/pcm;rate=8000',  #音频,原先是pcm,可以改为wav
            'Content-length:%d:' % f_len
        ]
        
        c=pycurl.Curl()  #实例化curl
        c.setopt(pycurl.URL,str(srv_url))     #(网址)  
        
        c.setopt(c.HTTPHEADER, http_header)   #网址头部  
        c.setopt(c.POST, 1)                   #1表示调用post方法而不是get  
        c.setopt(c.CONNECTTIMEOUT,80)      #超时中断  
        c.setopt(c.TIMEOUT,80)             #下载超时  
        c.setopt(c.WRITEFUNCTION,self.dump_res) #返回数据，dump_res,进行回调  
        c.setopt(c.POSTFIELDS,audio_data)    #数据  
        c.setopt(c.POSTFIELDSIZE,f_len)      #文件大小
        c.perform()                           #提交， pycurl.perform()
        print('use_cloud函数over！')

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        print('OK!!!')
        self.my_record()
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError



#     my_record()
    print('录音结束！')
    token = get_token() 
    use_cloud(self.token)
    print('over！')

#if __name__ == "__main__":
#    import sys
##    MainWindow = QtWidgets.QMainWindow()
##    ui.setupUi(MainWindow)
#    ui = MainWindow()
#    ui.show()
#    sys.exit()
