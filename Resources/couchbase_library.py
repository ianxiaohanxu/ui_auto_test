#!/usr/bin/env python
# encoding: utf-8

from couchbase import Couchbase
import time
import sys

#cb = Couchbase.connect(host='10.10.85.4',port=8091,bucket='ywz_star_clock')
#cb = Couchbase.connect(host='10.10.82.188',port=8091,bucket='ywz_otps_friendfree')
cb = Couchbase.connect(host='10.10.82.188',port=8091,bucket='ywz_star_clock')

key2 = 'custom:themes:iphone:4.4.0'


def test_set():
    #cb.set('f:f:daily:140006465', 7200)
    cb.set('f:f:daily:200109752', 7260)

def test_set_multi():
    cb.set_multi({'key4': 'val4', 'key5': 'val5'})
def test_add():
    cb.add('key2', 'val12')
def test_replace():
    cb.replace('key3', 'val3')

def test_get():
    try:
        res = cb.get('key2', quiet = True)
    except:
        res = cb.get("key2", replica=True, quiet=True)

    print res

def test_get_multi():
    res = cb.get_multi(['key1', 'key2', 'key3'],quiet=True)
    print res

def test_delete():
    key = sys.argv[1]
    res = cb.delete(key)
    print res

def test_delete_multi():
    res = cb.delete_multi(['key1', 'key2'])
    print res

def test_set_1000():
    pass
    start = time.time()
    for x in xrange(0, 10000):
      cb.set(str(x),x)
    end = time.time()
    print end - start

def test_set_multi_1000():
    pass
    start= time.time()
    tmp ={}
    for x in xrange(0, 100000):
      tmp[str(x)] = x
      if len(tmp) == 1000:
        cb.set_multi(tmp)
        tmp = {}
    if tmp:
        cb.set_multi(tmp)
        tmp ={}
    end = time.time()
    print end - start

def main():
    #test_set()
    #test_set_multi()
    #test_add()
    test_get()
    #test_get_multi()
    #test_set_1000()
    #test_set_multi_1000()
    #test_delete()

if __name__ == '__main__':
    main()