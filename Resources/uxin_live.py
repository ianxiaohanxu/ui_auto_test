# coding=utf-8

import commands
import json
import redis

class uxinliveclass(object):
    def __init__(self):
        pass

    def get_token(self, serverhost = '60.205.59.6', serverport = 8080, redishost = '60.205.59.6', redisport = 6321, redispwd = 'uxin001', mobile):
        cmd_code = "curl -s 'http://%s:%s/v1/user/sendValidateCode' -d 'mobile=%s'" % (serverhost, serverport, mobile)
        res_code = commands.getoutput(cmd_code)
        r = redis.Redis(host=redishost, port=redisport, db = 0, password = redispwd)
        value = r.get(mobile)
        code = json.loads(value)
        cmd_token = "curl -s -i -H '_c:1' 'http://%s:%s/v1/user/cellPhoneLogin' -d 'mobile=%s&code=%s'|grep 'x-auth-token'" % (serverhost, serverport, mobile, code)
        res_token = commands.getoutput(cmd_token)
        return res_token


if __name__ == '__main__':
    #token = uxinliveclass()
    #print token.get_token('127.0.0.1', 8080, '127.0.0.1', 6321, 'uxin001', 18612069260)
    pass
