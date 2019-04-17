# -*- coding: utf-8 -*-

'''
1.录音
2.读取wav文件
3.获取token
4.生成url4
5.调用云端api
6.打印识别结果
'''

import wave, time, json, pycurl
import urllib.request as urllib2
from datetime import datetime
from pyaudio import PyAudio, paInt16


chunk = 1024
framerate = 8000   #采样率
NUM_SAMPLES = 2000 #采样点
channels = 1  #一个声道
sampwidth = 2 #两个字节十六位
TIME = 20     #条件变量，可以设置定义录音的时间
filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+".wav"
 
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
    print('\n开始录音')
    time.sleep(2)
#    time.sleep(10)
    while count < TIME*1:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1
        print('...')
    save_wave_file(filename, my_buf)
    stream.close()

def read_file():
    wf = wave.open(filename, 'rb')
    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),rate = wf.getframerate(),output = True,)
    time.sleep(2)
    print('开始放音')
    while True:
        data = wf.readframes(chunk)
        if data == b'':break
        stream.write(data)
        print('...')
    wf.close()
    stream.close()
    p.terminate()
    
def dump_res(buf):  #dump_res即dump_result,buf是curl从网上返回来的缓存
    print(buf)
    my_temp = json.loads(buf)
    if my_temp['err_no']:
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
        elif my_temp['err_no'] == 3313:
            print('语音服务器解析超时')
        elif my_temp['err_no'] == 3314:
            print('音频长度过短')
        elif my_temp['err_no'] == 3315:
            print('语音服务器处理超时')
        elif my_temp['err_no'] == 3316:
            print('音频转为pcm失败')
    else:
        my_list = my_temp['result']
        print(type(my_list))
        print(my_list[0])  # 输出第一个
        print('dump_res函数调用成功！')
    
def get_token():  #获取token
    apikey = 'tasNprtTUkhRQAMO2Cw3kwlU'
    secretkey = 'QoOlCFa0KGd1cYtMr4NSvyAIWPgLjXyG'
    auth_url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=' +apikey+'&client_secret=' +secretkey

    print(auth_url)
    res = urllib2.urlopen(auth_url) #获取服务器响应,res=urllib2.urlopen(auth_url)

    print(res)
    json_data = res.read()         #读取到json_data中

    print(json_data,type(json_data))
    return json.loads(json_data)['access_token']
    
def use_cloud(token):                       #token类似一种访问权限等
    fp = wave.open(filename,'rb')             #打开wav文件
    nf = fp.getnframes()                      #获得文件的采样点数量
    print('sampwidth',fp.getsampwidth())
    print('framerate',fp.getframerate())
    print('channels',fp.getnchannels())
    f_len = nf*2                    #获取文件长度,文件长度计算，每个采样点2个字节
    audio_data = fp.readframes(nf)  #
    
    cuid = '74-70-FD-3A-42-74 '   #硬件地址，my phone xiaomi MAC

    print(token)
    srv_url = 'http://vop.baidu.com/server_api?dev_pid=1536&cuid='+cuid+'&token='+token

    print(srv_url)
    http_header = [
        'Content-Type:audio/pcm;rate=8000',  #音频,原先是pcm,可以改为wav
        'Content-length: %d' % f_len
    ]
    print(http_header)
    
    c = pycurl.Curl()                       #实例化curl
    c.setopt(pycurl.URL,str(srv_url))       #(网址)
    c.setopt(c.HTTPHEADER, http_header)     #网址头部 
    c.setopt(c.POST, 1)                     #1表示调用post方法而不是get
    c.setopt(c.CONNECTTIMEOUT,80)           #超时中断
    c.setopt(c.TIMEOUT,600)                  #下载超时
    c.setopt(c.WRITEFUNCTION,dump_res)      #返回数据，dump_res,进行回调
    c.setopt(c.POSTFIELDS,audio_data)
    c.setopt(c.POSTFIELDSIZE,f_len)         #文件大小
    c.getinfo(c.HTTP_CODE)                 #返回的HTTP状态码
    c.getinfo(c.TOTAL_TIME)                 #传输结束所消耗的总时间
    c.perform()                             #提交， pycurl.perform()

def main():
    import sys
    # my_record()
    # print('录音完成')
    # read_file()
    # print('放音完成')
    use_cloud(get_token())
    print('识别完成')
    # #    sys.exit()

    
if __name__ == "__main__":
    main()
