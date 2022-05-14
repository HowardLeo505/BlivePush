from bilibili_api import live,sync
import time
import requests

roomid = *
url = 'https://api2.pushdeer.com/message/push?pushkey=*&text=*'

pers = 1

room = live.LiveRoom(roomid)
rinfo = sync(room.get_room_play_info())
binfo = rinfo['live_status']

#while(pers == 1): #写个死循环皮一下2333
#    if(binfo == 1): #明天写一下开播通知的逻辑
        

print(rinfo)
print(binfo)