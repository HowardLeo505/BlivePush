from bilibili_api import live,sync
import time
import yaml,os
import requests

#好吧大晚上闲的蛋疼写了个读文件以后直接用配置文件了
with open(os.path.join(os.path.dirname(__file__),'config.yml'),encoding='UTF-8') as conf:
    config = yaml.load(conf.read(),Loader = yaml.Loader)
    room_id = config['roomid']
    key = config['pushkey']
    content = config['pushcontent']

roomid = room_id
url = 'https://api2.pushdeer.com/message/push?pushkey=*&text=*'
pers = 1

room = live.LiveRoom(roomid)
rinfo = sync(room.get_room_play_info())
binfo = rinfo['live_status']

#while(pers == 1): #写个死循环皮一下2333
#    if(binfo == 1): #明天写一下开播通知的逻辑
        

print(rinfo)
print(binfo)