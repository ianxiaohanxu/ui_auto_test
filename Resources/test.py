# coding:utf-8
from tools_library import *
from global_config import *
from redis_library import * 
import time

signkey = "sdvb753!@&*qpaltrko#$%^159plmokn"
params = {
    "uid":203202223,
    "orderid":20160530123,
    "goodsid":361,
    "nums":1,
}
signstr = sorted_values(params)
#--goodscenter
#--sendgoods    
signstr = str(params["uid"]) + str(params["orderid"]) + str(params["goodsid"]) + str(params["nums"])
print encrypt(signstr,'md5')

#-- 根据手机号查找对应的uid
print  13798171764%16


params_chat = {
    "uid":"1400060481",
    "time":1464210000,
    "key":"#!rcserver@2014",
}
print str(params_chat["time"])

signchat = str(params_chat["uid"]) + str(params_chat["time"]) + str(params_chat["key"])
print encrypt(signchat,'md5')

print 200101079% 1000
print 200101079% 100

l = [1,2,3,4,5]
print l[10:]




