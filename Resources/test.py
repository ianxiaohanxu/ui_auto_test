# coding:utf-8
from tools_library import *
from global_config import *
from redis_library import * 
from couchbase_library import *
from uxin_slive import *
import time

signkey = "sdvb753!@&*qpaltrko#$%^159plmokn"
params = {
    "uid":200101079,
    "orderid":120160809143332200101079,
    "goodsid":532,
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

print "gc sign***************"
params_gc = {
    "uid":"211636537",
    "time":1464210000,
    "key":"goodscenter$%^456",
}
print str(params_gc["time"])

signgc = str(params_gc["uid"]) + str(params_gc["time"]) + str(params_gc["key"])
print "******************aaaaaaaa"
print encrypt('211636537goodscenter$%^456','md5')
print encrypt(signgc,'md5')


print "new order sign***************"
params_order = {
    "uid":"200384192",
    "payType":'sp_pay',
    "goodsId":535,
    "nums":1,
    "bankId":'sp_pay',
    "key":"uxin_order_key",
}
signorder = str(params_order["uid"]) + str(params_order["payType"]) + str(params_order["goodsId"]) + str(params_order["nums"]) + str(params_order["bankId"]) + str(params_order["key"])
print encrypt(signorder,'md5')
signorder2 = str(params_order["uid"]) + str(params_order["key"])
print encrypt(signorder2,'md5')

print "\n\n\n\n"
print "send goods sign *************"
print encrypt('211636537'+'20161209173420211636537'+'551'+'1','md5')


print "\n\n\n\n"
print "order sign *************"
print encrypt('211636537'+'uxin_order_key','md5')



print "\n\n\n\n"
print "user_wallet *************"
print encrypt('ordersn=1473167028554&'+'uid=10031405&'+'key=guoling!@#456','md5')


print 200101079% 1000
print 200101079% 100


slive = uxin_slive()

xxxx = slive.get_token(18618318916, 984781916, 'SDKdemo', '0ulivexxx', 'xxx.jpg')
print xxxx









