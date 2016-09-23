#-*- coding: UTF-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from mobile import Mobile
import constant
import keycode


class IOS(Mobile):

    def focus(self, what):
        '''
        Find an element, return webelement object.\n
        For 'what', you can use resource id, text, partial text and xpath.\n
        \n
        - what - element location info
        '''
        # id is IOS element's name
        try:
            item = self.driver.find_element_by_id(what)
            return item
        except NoSuchElementException:
            pass
        try:
            item = self.driver.find_element_by_xpath(what)
            return item
        except NoSuchElementException:
            raise NoSuchElementException('Element not found by "%s"' %what)

    def find(self, what):
        '''
        Find elements by what\n
        \n
        - what - element location info
        '''
        items = self.driver.find_elements_by_id(what)
        if not len(items) == 0:
            return items
        items = self.driver.find_elements_by_xpath(what)
        if not len(items) == 0:
            return items
        raise NoSuchElementException('Element not found by "%s"' %what)

    def lock(self, seconds):
        '''
        Lock the device for a certain period of time\n
        \n
        - seconds - amount of seconds
        '''
        self.driver.lock(seconds)
