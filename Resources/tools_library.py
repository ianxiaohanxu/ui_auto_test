# coding=utf-8

import hashlib
import base64
import random
import uuid

def get_sn():
	"""
	生成sn
	"""
	return str(random.randrange(1000000000000, 9999999999999))

def get_token():
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
	print randomqq()




