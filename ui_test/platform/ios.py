#-*- coding: UTF-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

from mobile import Mobile
import constant
import keycode


class IOS(Mobile):

    def focus(self, what):
        '''
        Find an element, return webelement object.\n
        For 'what', you can use resource id, ios uiautomation. For IOS, id is 'name' on inspector, and we can write an uiautomation selector like "UIATarget.localTarget().frontMostApp().windows()[0].buttons()[0]"\n
        \n
        - what - element location info
        '''
        # id is IOS element's name
        try:
            item = self.driver.find_element_by_id(what)
            return item
        except NoSuchElementException:
            pass
        # It is a little slow when find by ios uiautomation
        try:
            item = self.driver.find_element_by_ios_uiautomation(what)
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
        items = self.driver.find_elements_by_ios_uiautomation(what)
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

    def swipe(self, start_x=None, start_y=None, end_x=None, end_y=None):
        '''
        Swip from somewhere to somewhere\n
        \n
        - start_x - coordinates on X axis for start point\n
        - start_y - coordinates on Y axis for start point\n
        - end_x - coordinates on X axis for end point\n
        - end_y - coordinates on Y axis for end point
        '''
        if (start_x == None) | (start_y == None) | \
            (start_x > self.X) | (start_y > self.Y) | \
            (end_x == None) | (end_y == None) | \
            (end_x > self.Y) | (end_y > self.Y):
                raise AssertionError('Please input a correct coordinate')
        action = TouchAction(self.driver)
        action\
            .press(x=start_x, y=start_y)\
            .wait()\
            .move_to(x=end_x - start_x, y=end_y - start_y)\
            .release()
        action.perform()

