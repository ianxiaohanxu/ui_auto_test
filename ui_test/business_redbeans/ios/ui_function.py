#-*- coding: UTF-8 -*-
from time import time, sleep
import datetime
import commands

import simplejson as json
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from pages.all_pages import *
from ui_test.platform import constant
from ui_test.platform import keycode
from ui_test.platform.ios import IOS
from ui_test.business_redbeans import api_function
from ui_test.business_redbeans.testdata import *


class Scenario(IOS):

    def __init__(self, port="4723", bundleID="com.uxin.live"):
        '''
        Set parameters for webdriver session\n
        \n
        - port - Webdriver listenning port\n
        - bundleID - Tested app bundleID\n
        '''
        self.bundleid = bundleID
        self._address = 'http://localhost:' + port + '/wd/hub'
        self._caps = {
                "deviceName": "Nameless",
                "platformName": "IOS",
                "automationName": "Appium",
                "platformVersion": "",
                "newCommandTimeout": 300,
                "bundleId": self.bundleid
        }

    def teardown(self, DRIVER_QUIT=True):
        '''
        Close the session or not\n
        \n
        - DRIVER_QUIT - True or False, default is True.
        '''
        try:
            self.reset()
        finally:
            super(Scenario, self).teardown(DRIVER_QUIT)

    def ready(self):
        '''
        Create a new webdriver session
        '''
        self.driver = webdriver.Remote(self._address, self._caps)

        # Set resolution for current device
        self.X = self.driver.get_window_size()["width"]
        self.Y = self.driver.get_window_size()["height"]

    def get_account(self):
        '''
        Get a random account from accounts pool
        '''
        return api_function.get_account()

    def free_account(self, cellnum):
        '''
        Free an account according to "cellnum"\n
        - cellnum - Cell number as a string
        '''
        api_function.free_account(cellnum)

