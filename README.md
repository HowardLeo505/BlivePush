# B站开播推送组件 
## 测试中... 
本组件是我拿来练手写Python的小程序，顺便学习一个.gitignore和GitHub Action的用法。 

当然，大的也在规划当中了，暑假就会开搞。 

## ————————————分割线————————————  

大体功能已经完成了，使用方法就是在程序目录底下创建一个config.yml，然后按如下格式写文件： 

roomid: xxxxxx #B站直播间号（live.bilibili.com/） 后面跟的纯数字   
pushkey:  #pushdeer的pushkey，因为我平时用的pushdeer，后面会加入pushplus、bark、Server酱的支持，key获取方式：[pushdeer官网](https://www.pushdeer.com/official.html)   
pushcontent:    #推送消息的内容  

目前不保证推送服务完全可用，初步测试下来功能没问题，没时间做深入测试和联调，有问题去issue提...6月21考完试回来处理...

## 画大饼  
后续会使用Github Action自动打包传Releases（包括源码和Linux、Windows可执行文件）推送平台，加入远程热部署...反正会很摩登...
