# coding=utf-8
import sys
import hashlib
import base64
import random
import uuid
import pymysql

import uxin_request
import global_config
from redis_library import *
#from couchbase_library import *

# def clear_accache(phone):
# 	"""
# 	清理下发短信上限的缓存，每天5次上限，每次有效时间30分钟
# 	eg:
# 	| clear_accache | 13798171764 |

# 	"""
# 	r = redis_library()
# 	return r.redis_update("set sm:uxin:number:%s 0" % phone, db=1)

# def send_ac(phone):
# 	"""
# 	发送登录验证码，直接调用，无返回
# 	"""
# 	r = uxin_request.uxin_request()
# 	params = {"phone":phone}
# 	r.get_general(global_config.ams_url, 'getauthcode.act', params=params)

# def get_login_ac(phone):
# 	""" 获取登录验证码，UI自动化用
# 	eg:
# 	| ${ac}= | get_login_ac | 13798171764 |

# 	${ac} 的值为4位数字

# 	"""
# 	r = redis_library()
# 	return r.redis_query("get user:reg:authcode:%s" % phone, db=1)

# def phone2uid(phone):
# 	""" 根据phone获取uid
# 	eg:
# 	| ${uid}= | phone2uid | 13798171764 |

# 	"""	
# 	uid = ''
# 	db = 'ams' + str((phone)%16)
# 	conn = pymysql.connect(host=global_config.db_url, port=3306, user=global_config.db_user, passwd=global_config.db_pwd, db=db, charset='utf8')
# 	c = conn.cursor()
# 	c.execute("select uid from %s.t_phone_uid where phone = %s" % (db, str(phone)))
# 	for r in c:
# 		uid = str(r[0])
# 	return uid

# def get_login_log(phone):
# 	"""
# 	根据手机号获取登录记录 t_login_log
# 	"""
# 	uid = phone2uid(phone)
# 	db = 'ams' + str(eval(uid)%16)
# 	conn = pymysql.connect(host=global_config.db_url, port=3306, user=global_config.db_user, passwd=global_config.db_pwd, db=db, charset='utf8')
# 	c = conn.cursor()
# 	c.execute("select * from %s.t_login_log where uid = %s" % (db, str(uid)))
# 	for r in c:
# 		return r

def get_bc_db(uid):
	"""
	根据uid返回balance库的库名
	"""
	if uid < 0:
		return None
	if uid%100 > 50:
		return 'bc_1'
	else: return 'bc_0'

def get_das_db(uid):
	"""
	根据uid返回das库U账簿记录的库名
	"""
	if uid < 0:
		return None
	sid = uid % 1000
	if sid <= 99:
		return 'das_0'
	elif sid <= 199:
		return 'das_1'
	elif sid <= 299:
		return 'das_2'
	elif sid <= 399:
		return 'das_3'
	elif sid <= 499:
		return 'das_4'
	elif sid <= 599:
		return 'das_5'
	elif sid <= 699:
		return 'das_6'
	elif sid <= 799:
		return 'das_7'
	elif sid <= 899:
		return 'das_8'
	else:
		return 'das_9'

def get_md5_pwd(pwd):
	"""
	获取md5后的密码
	eg:
	| ${pwd}= | get_md5_pwd | 123456 |
	"""
	return encrypt(str(pwd)+'~X!U@N#I$','md5')

def get_sendgoods_sign(uid, orderid, goodsid, nums):
	"""
	获取发货接口的sign
	"""
	return encrypt(str(uid)+str(orderid)+str(goodsid)+str(nums),'md5')

def get_neworder_sign(uid, paytype, goodsid, nums, bankid=''):
	"""
	获取新增订单接口的sign
	"""
	return encrypt(str(uid)+str(paytype)+str(goodsid)+str(nums)+str(bankid)+'uxin_order_key','md5')

def get_token1():
	"""
	生成token
	"""
	return str(uuid.uuid1()).replace('-','')

def sorted_values(params, type='keys'):
	"""
	按照英文字母大小排序query string parameters各值
	"""
	if type == 'keys':
		sorted_str = sorted(params.keys())
	else:
		values = params.values()
		for i in range(len(values)):
			values[i] = str(values[i])
		sorted_str = sorted(values, key=str.lower)
	str_v = ''
	if type == 'keys':
		for key in sorted_str:
			str_v = str_v + str(params[key])
	else:
		for value in sorted_str:
			str_v = str_v + value
	return str_v


def utf_to_unicode(content):
	"""Converts the utf-8 content to unicode 
	
	eg:
	| utf_to_unicode | ${resp.content} |
	"""
	CODEC = 'utf-8'
	str = content.decode(CODEC)
	return str	

def ch_to_unicode(content):
	"""converts chinese(unicode_escape) to unicode"""
	string = content.decode('unicode_escape')
	return string

def encrypt(str, enctype, bit=32):
	encrypttype = [
		'md5',
		'sha1',
		'sha512',
		'base64en',
		'base64de',
	]

	if enctype not in encrypttype:
		return ''

	if enctype == 'md5':
		encstr = hashlib.md5(str).hexdigest()
		if bit == 16:
			return encstr[8:-8]
		else:
			return encstr

	if enctype == 'sha1':
		return hashlib.sha1(str).hexdigest()

	if enctype == 'sha512':
		return hashlib.sha512(str).hexdigest()

	if enctype == 'base64en':
		return base64.b64encode(str)

	if enctype == 'base64de':
		return base64.b64decode(str)

def randomstr(bit=16):
	"""
	生成随机字符串
	"""
	intbit = int(bit)
	seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	l = []
	for i in range(intbit):
		l.append(random.choice(seed))
	str = string.join(l).replace(' ','')
	return str


def randomqq():
	"""
	生成qq号
	"""
	char_list1 = ["1","2","3","4","5","6","7","8","9","0"]
	char_list2 = ["1","2","3","4","5","6","7","8","9"]
	str = ''.join(random.sample(char_list1, random.randint(5,10))).replace(' ','')
	return random.choice(char_list2)+str

if __name__ == '__main__':
	#print phone2uid(15504578175)
	print get_neworder_sign(211636537,'weixinpay',535,1,'weixinpay')



