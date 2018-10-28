# -*- coding: utf-8 -*-
# 微信给好友数羊小程序
# author: liuwenjiajia
import itchat
import time
import sys


reload(sys)
sys.setdefaultencoding('utf8')
itchat.auto_login() #login pages
itchat.get_friends(True)
users = itchat.search_friends(name='Laura')
userName = users[0]['UserName']
print userName
for i in range(10086000):
    # print str(i) + " sheep"
    msg = str(i) + " 只羊"
    itchat.send(msg=msg, toUserName=userName)
    time.sleep(2)