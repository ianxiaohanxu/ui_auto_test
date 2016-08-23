# coding=utf-8

import hashlib
import base64
import random
import uuid
from redis_library import *
#from couchbase_library import *

def get_login_ac(phone):
	r = redis_library()
	return r.redis_query("get user:reg:authcode:%s" % phone, db=1)

def get_vc(phone):
	pass

def get_token1():
	"""
	生成token
	"""
	return str(uuid.uuid1()).replace('-','')

def sorted_values(params):
	"""
	按照英文字母大小排序query string parameters各值
	"""
	sortedkeys = sorted(params.keys())
	str_v = ''
	for key in sortedkeys:
		str_v = str_v + str(params[key])
	return str_v


def utf_to_unicode(content):
	"""Converts the utf-8 content to unicode 
	
	ex:
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
	print get_login_ac(13798171764)




