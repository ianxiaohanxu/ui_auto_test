#-*- coding: UTF-8 -*-

import requests

import testdata


def get_account(stype):
    '''
    Get a random account from accounts pool
    '''
    account = requests.post(testdata.url_get_account, json={"special_type": stype})
    return account.json()

def free_account(cellnum):
    '''
    Free an account according to "cellnum"
    '''
    requests.post(testdata.url_free_account, json={"cell": cellnum})
