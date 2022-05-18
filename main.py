from bilibili_api import live,sync
import time
import yaml,os
import requests

#读配置文件
with open(os.path.join(os.path.dirname(__file__),'config.yml'),encoding='UTF-8') as conf:
    config = yaml.load(conf.read(),Loader = yaml.Loader)
    room_id = config['roomid']
    key = config['pushkey']
    content = config['pushcontent']

roomid = room_id
url = 'https://api2.pushdeer.com/message/push?pushkey='+key+'&text='
binfo = 0
pers = 1 #持久化参量
pstat = 0 #开播后推送状态

#获取直播间状态
def get_live_status():    
    global binfo
    room = live.LiveRoom(roomid)
    rinfo = sync(room.get_room_play_info())
    binfo = rinfo['live_status']
    #print(rinfo) #DEBUG
    #print(binfo) #DEBUG
    #time.sleep(20) #alter
    return binfo

#开播通知
def live_start_push():
    purl = url + '开播！'
    req = requests.get(purl)

#下播通知
def live_end_push():
    purl = url + '下播！'
    req = requests.get(purl)

#get_live_status()

while(pers == 1): #写个死循环皮一下2333
    get_live_status()
    if(binfo == 1): #明天写一下开播通知的逻辑
        if(pstat != 1):
            #req = requests.get(url)
            live_start_push()
            #print('start') #debug
            pstat = 1
            time.sleep(3)
            while(pers == 1):
                get_live_status()
                print('in')
                time.sleep(20)
                if(binfo == 0 or binfo ==2):
                    live_end_push()
                    #print('end') #debug
                    pstat = 0
    time.sleep(20)
                


        

#print(rinfo) #DEBUG
#print(binfo) #DEBUG