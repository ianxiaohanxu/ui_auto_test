# coding:utf-8
from tools_library import *
from global_config import *
from redis_library import * 
from couchbase_library import *
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
print encrypt(signgc,'md5')


print "new order sign***************"
params_order = {
    "uid":"211636537",
    "payType":'weixinpay',
    "goodsId":551,
    "nums":1,
    "bankId":'',
    "key":"uxin_order_key",
}
signorder = str(params_order["uid"]) + str(params_order["payType"]) + str(params_order["goodsId"]) + str(params_order["nums"]) + str(params_order["bankId"]) + str(params_order["key"])
print encrypt(signorder,'md5')
signorder2 = str(params_order["uid"]) + str(params_order["key"])
print encrypt(signorder2,'md5')

print "\n\n\n\n"
print "send goods sign *************"
print encrypt('211636537'+'114727148325402116399992'+'506'+'1','md5')

print 200101079% 1000
print 200101079% 100

l = [1,2,3,4,5]
print l[10:]


r = redis_library()
print r.redis_query("get user:reg:authcode:13798171802",db=1)
#print r.redis_query("SELECT 1;get user:reg:authcode:13798171764")

print range(1,10)






