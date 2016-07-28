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
from ui_test.business.testdata import *


class Scenario(Android):

    def __init__(self, port="4723", package="com.yx", activity="com.yx.activity.welcome.Splash"):
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
            self.logout()
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

    def go_to_login(self):
        '''
        Go to login page, if "welcome" page shown, skip it.
        '''
        try:
            self.verify(verify_code_login_location_use_password, 5)
        except NoSuchElementException:
            self.verify(welcome_location_launch_btn)
            self.click(welcome_location_launch_btn)
        self.verify(verify_code_login_location_use_password)

    def login_with_password(self, username, password):
        '''
        Login with username and password\n
        - username - username\n
        - password - password
        '''
        self.go_to_login()
        self.click(verify_code_login_location_use_password)
        self.verify(password_login_location_phone_number)
        assert self.text(password_login_location_country_code_text) == password_login_verification_country_code_china, \
                "Country code is not for China."
        assert not self.is_clickable(password_login_location_login_btn)
        self.enter(username, password_login_location_phone_number)
        assert not self.is_clickable(password_login_location_login_btn)
        self.enter(password, password_login_location_password)
        assert self.is_clickable(password_login_location_login_btn)
        self.click(password_login_location_login_btn)
        try:
            self.verify(bottom_location_me, 7)
            return
        except:
            self.verify(auth_location_contact_permission)
            self.click(auth_location_contact_permission)
            self.verify(auth_location_contact_permission_enabled)
            self.verify(auth_location_contact_permission_accept)
            self.verify(auth_location_calllog_permission)
            self.click(auth_location_calllog_permission)
            self.verify(auth_location_calllog_permission_enabled)
            self.verify(auth_location_calllog_permission_accept)
            self.verify(auth_location_mic_permission)
            self.click(auth_location_mic_permission)
        self.verify(bottom_location_me, 5)

    def unbind_system(self):
        '''
        Turn off the settings for binding dial pad and contact
        '''
        status, output = commands.getstatusoutput("adb shell getprop ro.build.version.release") 
        if status != 0:
            raise Exception("Command execute fail")
        elif output[0] > "4":
            return
        else:
            self.login_with_password(phone1_number, phone1_password)
            self.click(bottom_location_me)
            self.verify(me_location_settings)
            self.click(me_location_settings)
            self.verify(settings_location_take_over)
            self.click(settings_location_take_over)
            self.verify(settings_take_over_location_bind_dial_btn)
            if self.is_checked(settings_take_over_location_bind_dial_btn):
                self.click(settings_take_over_location_bind_dial_btn)
                assert not self.is_checked(settings_take_over_location_bind_dial_btn)
            if self.is_checked(settings_take_over_location_bind_contact_btn):
                self.click(settings_take_over_location_bind_contact_btn)
                assert not self.is_checked(settings_take_over_location_bind_contact_btn)
            self.click(settings_take_over_location_back)
            self.verify(settings_location_take_over)


    def skip_ad(self):
        '''
        Skip AD page
        '''
        self.wait_until_present(ad_location_skip, 3)
        self.click(ad_location_skip)
        self.verify(bottom_location_me)

    def logout(self):
        '''
        Log out unless already log out
        '''
        self.close_app()
        self.launch_app()
        try:
            self.skip_ad()
        except TimeoutException:
            if self.is_element_present(verify_code_login_location_agreement_title):
                return
            else:
                raise TimeoutException
        self.click(bottom_location_me)
        self.verify(me_location_settings)
        self.click(me_location_settings)
        self.verify(settings_location_exit)
        self.click(settings_location_exit)
        self.verify(settings_logout_confirmation_location_dialog)
        assert self.text(settings_logout_confirmation_location_text) == settings_logout_confirmation_verification_text
        self.click(settings_logout_confirmation_location_ok)
        self.verify(verify_code_login_location_agreement_title)




# if __name__ == "__main__":
#     test = Scenario()
#     import pdb;pdb.set_trace()     #Debug code
#     test.teardown()

