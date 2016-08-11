#-*- coding: UTF-8 -*-

import requests

from ui_test.business import testdata


def get_account():
    '''
    Get a random account from accounts pool
    '''
    account = requests.post(testdata.url_get_account)
    return account.json()

def free_account(cellnum):
    '''
    Free an account according to "cellnum"
    '''
    requests.post(testdata.url_free_account, json={"cell": cellnum})
