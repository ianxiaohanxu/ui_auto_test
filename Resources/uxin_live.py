# coding=utf-8

import commands
import json
import redis
import sys  
import time

reload(sys)  
sys.setdefaultencoding('utf8')


class uxin_live(object):
    def __init__(self):
        pass

    def get_token(self, mobile, serverhost = '60.205.59.6', serverport = 8080, redishost = '60.205.59.6', redisport = 6321, redispwd = 'uxin001'):
        cmd_code = "curl -s 'http://%s:%s/v1/user/sendValidateCode' -d 'mobile=%s'" % (serverhost, serverport, mobile)
        res_code = commands.getoutput(cmd_code)
        r = redis.Redis(host=redishost, port=redisport, db = 0, password = redispwd)
	key = "sms_item_businesstype_mobile__0_" + str(mobile)
        value = r.get(key)
	cmd_code = "echo '%s'|awk -F 'contents\":' '{print $2}'|cut -b 3-6" % (value)
	code = commands.getoutput(cmd_code)
        cmd_token = "curl -s -i -H '_c:1' 'http://%s:%s/v1/user/cellPhoneLogin' -d 'mobile=%s&code=%s'|grep 'x-auth-token'" % (serverhost, serverport, mobile, code)
        res_token = commands.getoutput(cmd_token)
        token_split = res_token[:-1].split(": ") # 不知道为啥有个换行符
        res = token_split[0] + "=" + token_split[1]
        print token_split
        return res

    def get_uid(self, mobile, serverhost = '60.205.59.6', serverport = 8080, redishost = '60.205.59.6', redisport = 6321, redispwd = 'uxin001'):
	cmd_code = "curl -s 'http://%s:%s/v1/user/sendValidateCode' -d 'mobile=%s'" % (serverhost, serverport, mobile)
        res_code = commands.getoutput(cmd_code)
        r = redis.Redis(host=redishost, port=redisport, db = 0, password = redispwd)
        key = "sms_item_businesstype_mobile__0_" + str(mobile)
        value = r.get(key)
        cmd_code = "echo '%s'|awk -F 'contents\":' '{print $2}'|cut -b 3-6" % (value)
        code = commands.getoutput(cmd_code)
        cmd_uid = "curl -s -H '_c:1' 'http://%s:%s/v1/user/cellPhoneLogin' -d 'mobile=%s&code=%s'|awk -F 'id\":' '{print $2}'|awk -F ',' '{print $1}'" % (serverhost, serverport, mobile, code)
        res_uid = commands.getoutput(cmd_uid)
	return res_uid

    def get_code(self, mobile, serverhost = '60.205.59.6', serverport = 8080, redishost = '60.205.59.6', redisport = 6321, redispwd = 'uxin001'):
        cmd_code = "curl -s 'http://%s:%s/v1/user/sendValidateCode' -d 'mobile=%s'" % (serverhost, serverport, mobile)
        res_code = commands.getoutput(cmd_code)
        r = redis.Redis(host=redishost, port=redisport, db = 0, password = redispwd)
        key = "sms_item_businesstype_mobile__0_" + str(mobile)
        value = r.get(key)
        cmd_code = "echo '%s'|awk -F 'contents\":' '{print $2}'|cut -b 3-6" % (value)
        code = commands.getoutput(cmd_code)
        return code

    def upload_file(self, token, params= None, files = None, serverhost = '60.205.59.6', serverport = 8080, url = 'user/setUserInfo', mode = 1):
	token = token.replace('=',':')
	if mode == 1:
	    cmd = "curl -s -F'%s' -H'_c:1' -H'%s' 'http://%s:%s/v1/%s?%s'" % (files, token, serverhost, serverport, url, params)
	else :
	    cmd = "curl -s -H'_c:1' -H'%s' 'http://%s:%s/v1/%s' -d ''" % (token, serverhost, serverport, url)
	res = commands.getoutput(cmd)
	return res

    def get_datetime(self, time_dur=0):
	#返回13位时间戳， time_dur 单位：小时
        now = time.time()
	res_time = now*1000 + int(time_dur)*60*60*1000
	return '%d'%res_time

    def get_url_split(self, str_url, c = '/', pos = 3):
	arr1 = str_url.split(c)
	str_tmp = arr1[pos]
	if '?' in str_tmp:
	    arr2 = str_tmp.split('?')
	    return arr2[0]
	else :
	    return str_tmp

if __name__ == '__main__':
    user = uxin_live()
    #print user.get_token(18612069260)
    #print user.get_uid(18612069260)
    #print user.upload_file('x-auth-token:559d0efc-d91d-48ae-aead-bcd9f61a72fd', params='introduction=test1352245782&nickname=test1352245782&gender=1', files = 'multipartFile=@/Users/douqianxin/work/robot/auto_test/scripts/interface_test/uxinlive/user/1.png')
    #print user.get_datetime(-1)
    #print user.get_url_split('http://uxin-zb-picture.img-cn-shenzhen.aliyuncs.com/p201607306751932937015699373.png?124fsadf')
    pass
