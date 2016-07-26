# coding=utf-8

import commands
import json
import redis

class uxin_live(object):
    def __init__(self):
        pass

    def get_token(self, mobile, serverhost = '60.205.59.6', serverport = 8080, redishost = '60.205.59.6', redisport = 6321, redispwd = 'uxin001'):
        cmd_code = "curl -s 'http://%s:%s/v1/user/sendValidateCode' -d 'mobile=%s'" % (serverhost, serverport, mobile)
        res_code = commands.getoutput(cmd_code)
        r = redis.Redis(host=redishost, port=redisport, db = 0, password = redispwd)
        value = r.get(mobile)
        code = json.loads(value)
        cmd_token = "curl -s -i -H '_c:1' 'http://%s:%s/v1/user/cellPhoneLogin' -d 'mobile=%s&code=%s'|grep 'x-auth-token'" % (serverhost, serverport, mobile, code)
        res_token = commands.getoutput(cmd_token)
        token_split = res_token[:-1].split(": ") # 不知道为啥有个换行符
        res = token_split[0] + "=" + token_split[1]
        print token_split
        return res


if __name__ == '__main__':
    token = uxin_live()
    print token.get_token(18688410526)
    pass
