#-*- coding: UTF-8 -*-
from time import time, sleep
import datetime
import simplejson as json

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

import pages
from ui_test.platform import constant
from ui_test.platform import keycode
from ui_test.platform.android import Android
from ui_test.business import setup
from ui_test.business import testdata


class Scenario(Android):

    def __init__(self, port="4723", package="com.yx", activity="com.yx.activity.welcome.Splash"):
        '''
        Create a new webdriver session

        port: Webdriver listenning port
        package: Tested app package name
        activity: Tested app launched activity
        '''
        self._package = package
        self._activity = activity
        address = 'http://localhost:' + port + '/wd/hub'
        caps = {
                "deviceName": "Nameless",
                "platformName": "Android",
                "appPackage": self._package,
                "appActivity": self._activity,
                "automationName": "Selendroid",
                "platformVersion": "",
        }
        self.driver = webdriver.Remote(address, caps)

        # Set resolution for current device
        self.X = self.driver.get_window_size()["width"]
        self.Y = self.driver.get_windwo_size()["height"]


if __name__ == "__main__":
    test = Scenario()
    import pdb;pdb.set_trace()     #Debug code
    test.teardown()

