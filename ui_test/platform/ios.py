#-*- coding: UTF-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from mobile import Mobile
import constant
import keycode


class IOS(Mobile):

    def lock(self, seconds):
        '''
        Lock the device for a certain period of time\n
        \n
        - seconds - amount of seconds
        '''
        self.driver.lock(seconds)
