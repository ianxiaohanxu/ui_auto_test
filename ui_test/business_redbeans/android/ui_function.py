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
from ui_test.platform.android import Android
from ui_test.business_redbeans import api_function
from ui_test.business_redbeans.testdata import *


class Scenario(Android):

    def __init__(self, port="4723", package="com.uxin.live", activity="notSure"):
        '''
        Set parameters for webdriver session\n
        \n
        - port - Webdriver listenning port\n
        - package - Tested app package name\n
        - activity - Tested app launched activity
        '''
        self._package = package
        self._activity = activity
        self._address = 'http://localhost:' + port + '/wd/hub'
        self._caps = {
                "deviceName": "Nameless",
                "platformName": "Android",
                "appPackage": self._package,
                "appActivity": self._activity,
                "automationName": "Appium",
                "platformVersion": "",
                "newCommandTimeout": 300,
                "unicodeKeyboard": True,
                "resetKeyboard": True,
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

