#!/usr/bin/env python
# encoding: utf-8
from couchbase import Couchbase
import time
import sys

class couchbase_library(object):

    def __init__(self):
        pass
        #self.cb = Couchbase.connect(host='10.10.82.188',port=8091,bucket='ywz_star_clock')

    def cb_set(self, bucket, key, value, host='113.31.82.188', port=8091):
        cb = Couchbase.connect(host=host, port=port, bucket=bucket)
        cb.set(key, value)

    def cb_set_multi(self, bucket, setdict, host='113.31.82.188', port=8091):
        cb = Couchbase.connect(host=host, port=port, bucket=bucket)        
        cb.set_multi(setdict)

    def cb_add(self, bucket, key, value, host='113.31.82.188', port=8091):
        cb = Couchbase.connect(host=host, port=port, bucket=bucket)  
        cb.add(key, value)

    def cb_replace(self, bucket, key, value, host='113.31.82.188', port=8091):
        cb = Couchbase.connect(host=host, port=port, bucket=bucket)  
        cb.replace(key, value)

    def cb_get(self, bucket, key, host='113.31.82.188', port=8091):
        cb = Couchbase.connect(host=host, port=port, bucket=bucket) 
        try:
            res = cb.get(key, quiet = True)
        except:
            res = cb.get(key, replica=True, quiet=True)
        return res

    def cb_get_multi(self, bucket, list_key, host='113.31.82.188', port=8091):
        cb = Couchbase.connect(host=host, port=port, bucket=bucket) 
        res = cb.get_multi(list_key, quiet=True)
        return res

    def cb_delete(self, bucket, key, host='113.31.82.188', port=8091):
        cb = Couchbase.connect(host=host, port=port, bucket=bucket) 
        res = cb.delete(key)
        return res

    def cb_delete_multi(self, bucket, list_key, host='113.31.82.188', port=8091):
        cb = Couchbase.connect(host=host, port=port, bucket=bucket) 
        res = cb.delete_multi(list_key)
        return res

    # def test_set_1000(self):
    #     pass
    #     start = time.time()
    #     for x in xrange(0, 10000):
    #       cb.set(str(x),x)
    #     end = time.time()
    #     print end - start

    # def test_set_multi_1000(self):
    #     pass
    #     start= time.time()
    #     tmp ={}
    #     for x in xrange(0, 100000):
    #       tmp[str(x)] = x
    #       if len(tmp) == 1000:
    #         cb.set_multi(tmp)
    #         tmp = {}
    #     if tmp:
    #         cb.set_multi(tmp)
    #         tmp ={}
    #     end = time.time()
    #     print end - start

def main():
    #test_set()
    #test_set_multi()
    #test_add()
    cb = couchbase_library()
    cb.cb_get()
    #test_get_multi()
    #test_set_1000()
    #test_set_multi_1000()
    #test_delete()

if __name__ == '__main__':
    main()