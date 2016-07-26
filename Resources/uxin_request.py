# coding=utf-8

import os
import sys
import glob
import random
import global_config
import tools_library
from RequestsLibrary import *

exedir = os.path.abspath('.')
sys.path.insert(0,glob.glob(exedir)[0])

class uxin_request(object):
    def __init__(self):
        #固定参数
        self.uid = 0
        self.sn = tools_library.get_sn()
        self.pv = 'android'
        self.v = '4.4.0'
        self.p = 'com.yx'
        self.u = 5
        self.sign = ''
        #http参数
        self.url = 'http://113.31.82.189:8887'
        self.alias = 'uxin'
        self.param = {}
        self.uri = 'v3/im/getTmpUid?pv=android&v=4.4.0&sn='+str(self.sn)+'&sign='+self.sign+'&p=uxin.com&u=884'
        self.header = {}

    #def _getSign(self,params):
    def getac(self, account, pwd):
        #获取登录凭证方法 authCode
        r = RequestsLibrary()
        r.create_session(self.alias, self.url, '')
        params = {
            #'p':'youxin7',
            'securityver':'1',
            'sn':self.sn,
            'brand':'iPhone',
            'osv':'9.3.1',
            'spn':'1',
            'u':'4852',
            'token_type':'1',
            'v':'2',
            'netmode':'1',
            'unionid':'4852',
            'model':'iPhone8,2',
            'accounttype':'iPhone',
            'fgflag':'1',
            'pv':'iphone',#
            'product':'youxin7'
        }
        params['account'] = account
        params['pwd'] = tools_library.encrypt(pwd+global_config.salt,'md5')
        params['token'] = '2e145b038c420ded04c825856bc0c06683edeff1b629130cbc461ff507386049' # how 
        #params['token'] = ''
        params['idfv'] = '547e8abb06b6471f941c7dfd7b127c63'
        params['adid'] = 'e966c076597e4250b3ead30cbb6979c1'
        params['openudid'] = '363141e9bc35c843397780babc72932af2320a7a'
        signstr = tools_library.sorted_values(params)
        sign = tools_library.encrypt(signstr+global_config.signkey,'sha1')
        params['sign'] = sign
        #acuri = '/v3/im/login?p=youxin7&account=18688410526&securityver=1&pv=iphone&sn=f2320a7a483437080159075&brand=iPhone&osv=9.3.1&span=1&u=4852&token_type=1&v=4.4.0&netmode=1&sign=f49659ac6f2c7f3bc42d1d1767c7e2f62faf02bb&unionid=4852&openudid=363141e9bc35c843397780babc72932af2320a7a&token=2e145b038c420ded04c825856bc0c06683edeff1b629130cbc461ff507386049&pwd=9e51869ba2733b231e1995738490663f&idfv=547e8abb06b6471f941c7dfd7b127c63&model=iPhone8%2C2&product=youxin7&adid=e966c076597e4250b3ead30cbb6979c1&accounttype=phone&fgflag=1'
        acuri = '/v3/im/login'
        resp = r.get_request(self.alias, acuri, self.header, params)
        return resp

    def get_general(self, url, uri=None, header='', params=None, ac=None):
        r = RequestsLibrary()
        r.create_session(self.alias, url, '')
        resp = r.get_request(self.alias, uri, header, params)
        return resp

    def post_general(self, url, uri=None, headers='', datas=None, params=None, ac=None):
        urilist = None
        if params == None:
            urilist = uri
        else:
            urilist = uri+'?'+params
        print urilist
        headerlist = {}
        for  header in headers.split(';'):
            if header == '':
                break
            header_split = header.split('=')
            headerlist[header_split[0]] = header_split[1]
        r = RequestsLibrary()
        r.create_session(self.alias, url, '')
        resp = r.post_request(self.alias, urilist, datas, params, headerlist)
        return resp

if __name__ == '__main__':
    u = uxin_request()
    resp = u.getac('18688410526','111222')
    print resp.content