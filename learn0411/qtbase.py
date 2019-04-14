# -*- coding: utf-8 -*-

import wave
import time
import json 
import pycurl
from pyaudio import PyAudio, paInt16
import urllib.request as urllib2

framerate=8000   #采样率
NUM_SAMPLES=2000 #采样点
channels=1  #一个声道
sampwidth=2 #两个字节十六位
TIME=2      #条件变量，可以设置定义录音的时间
 
def save_wave_file(filename, data):   #save the date to the wav file
    wf = wave.open(filename, 'wb')  #二进制写入模式
    wf.setnchannels(channels)  
    wf.setsampwidth(sampwidth)  #两个字节16位
    wf.setframerate(framerate)  #帧速率
    wf.writeframes(b"".join(data))  #把数据加进去，就会存到硬盘上去wf.writeframes(b"".join(data)) 
    wf.close()

    
def my_record():
    pa = PyAudio()
    stream = pa.open(format = paInt16,channels = 1,
                     rate = framerate,input = True,
                     frames_per_buffer = NUM_SAMPLES)
    my_buf = []
    count = 0
    time.sleep(5)
    print('开始录音')
#    time.sleep(10)
    while count < TIME*2:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1
    save_wave_file('01.wav', my_buf)
    stream.close()

def read_file():
    wf = wave.open(r"01.wav", 'rb')
    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),rate = wf.getframerate(),output = True,)
    while True:
        data = wf.readframes(chunk)
        if data == "":break
        stream.write(data)
    stream.close()
    p.terminate()
    
def dump_res(buf):  #dump_res即dump_result,buf是curl从网上返回来的缓存
    print(buf)
    my_temp=json.loads(buf)
    my_list=my_temp['result']
    print(type(my_list))
    print(my_list[0])  #输出第一个
    print('dump_res函数调用成功！')
    
def get_token():  #获取token
    apikey='tasNprtTUkhRQAMO2Cw3kwlU'
    secretkey='QoOlCFa0KGd1cYtMr4NSvyAIWPgLjXyG'
    auth_url='https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+apikey+'&client_secret=' +secretkey;
    
    res=urllib2.urlopen(auth_url) #获取服务器响应,res=urllib2.urlopen(auth_url) 
    json_data=res.read()         #读取到json_data中
    print(json_data,type(json_data))
    return json.loads(json_data)['access_token']
    
def use_cloud(token):  #token类似一种访问权限等
    fp=wave.open(u'01.wav','rb')             #打开wav文件
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
    c.setopt(c.WRITEFUNCTION,dump_res) #返回数据，dump_res,进行回调  
    c.setopt(c.POSTFIELDS,audio_data)    #数据  
    c.setopt(c.POSTFIELDSIZE,f_len)      #文件大小
    c.perform()                           #提交， pycurl.perform()
    print('use_cloud函数over！')


if __name__ == "__main__":
    import sys
    my_record()
    print('录音完毕')
    use_cloud(get_token())
    
#    read_file()
    print('转换完毕')
    sys.exit()

    
    
