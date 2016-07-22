# -*- coding: utf-8 -*-
from time import sleep, time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction

import constant


class Mobile(object):

    def teardown(self, DRIVER_QUIT=True):
        '''
        Close the session or not\n
        \n
        - DRIVER_QUIT - True or False, default is True.
        '''
        if DRIVER_QUIT == True:
            self.driver.quit()
        else:
            return

    def contexts(self):
        '''
        Returns the contexts within the current session
        '''
        return self.driver.contexts

    def context(self):
        '''
        Returns the current context of the current session
        '''
        return self.driver.context

    def reset(self):
        '''
        Resets the current application on the device\n
        It works like the scenario: Clear data for the app and then restart it
        '''
        self.driver.reset()

    def current_activity(self):
        '''
        Retrieves the current activity on the device
        '''
        return self.driver.current_activity

    def background_app(self, seconds):
        '''
        Puts the application in the background on the device for a certain seconds\n
        It works as the scenario: kill the process and restart it\n
        \n
        - seconds - The amount of seconds
        '''
        self.driver.background_app(seconds)

    def is_app_installed(self, bundle_id):
        '''
        Checks whether the application specified by `bundle_id` is installed on the device\n
        \n
        - bundle_id - the id of the application to query. On Android, it is the package name.
        '''
        return self.driver.is_app_installed(bundle_id)

    def install_app(self, app_path):
        '''
        Install the application found at `app_path` on the device\n
        \n
        - app_path - apk path on the device
        '''
        self.driver.install_app(app_path)

    def remove_app(self, bundle_id):
        '''
        Remove the specified application from the device\n
        \n
        - bundle_id - the id of the application to query. On Android, it is the package name.
        '''
        self.driver.remove_app(bundle_id)

    def get_settings(self):
        '''
        Returns the appium server Settings for the current session
        '''
        return self.driver.get_settings()

    def update_settings(self, settings):
        '''
        Set settings for the current session\n
        \n
        - settings - dictionary of settings to apply to the current test session
        '''
        self.driver.update_settings(settings)

    def click(self, what, count=1):
        '''
        Click an element, for double-click, just pass in count=2\n
        \n
        - what - element location info\n
        - count - times to click, default is 1
        '''
        item = self.focus(what)
        while count > 0:
            item.click()
            count -= 1
            sleep(constant.INTERVAL_1)

    def long_click(self, what, duration=1000):
        '''
        Long click an element\n
        \n
        - what - element location info\n
        - duration - how long time to long_click, default is 1000 ms
        '''
        item = self.focus(what)
        action = TouchAction(self.driver)
        action.long_press(el=item, duration=duration)
        action.release()
        action.perform()

    def tap(self, x=None, y=None, count=1):
        '''
        Tap a coordinates (x,y)\n
        \n
        - x - coordinates on X axis\n
        - y - coordinates on Y axis\n
        - count - times to tap, default is 1
        '''
        if (x == None) | (y == None) | (x > self.X) | (y > self.Y):
            raise AssertionError('Please input a correct coordinate')
        while count > 0:
            action = TouchAction(self.driver)
            action.press(x=x, y=y).release()
            action.perform()
            count -= 1
            sleep(constant.INTERVAL_1)

    def long_tap(self, x=None, y=None, duration=1000):
        '''
        Long tap a coordinates (x,y)\n
        \n
        - x - coordinates on X axis\n
        - y - coordinates on Y axis\n
        - duration - how long time to long_tap, default is 1000 ms
        '''
        if (x == None) | (y == None) | (x > self.X) | (y > self.Y):
            raise AssertionError('Please input correct coordinates')
        action = TouchAction(self.driver)
        action.long_press(x=x, y=y, duration=duration).release()
        action.perform()

    def enter(self, what, where):
        '''
        Input something into edit field\n
        \n
        - what - input text\n
        - where - element location info
        '''
        element = self.focus(where)
        if not isinstance(what, (str, unicode)):
            what = str(what)
        element.send_keys(what)

    def clear(self, where):
        '''
        Clear the edit field\n
        \n
        - where - element location info
        '''
        element = self.focus(where)
        element.clear()
        self.hide_keypad()

    def drag(self, origin_el=None, target_el=None, x=None, y=None):
        '''
        Drag something to somewhere\n
        \n
        - origin_el - source element\n
        - target_el - target element\n
        - x - target coordinates on X axis\n
        - y - target coordinates on Y axis
        '''
        if not (target_el is None):
            action = TouchAction(self.driver)
            action.\
                long_press(origin_el).\
                move_to(target_el).\
                release().\
                perform()
        elif (x == None) | (y == None) | (x > self.X) | (y > self.Y):
            raise AssertionError('Please input a correct coordinate')
        else:
            action = TouchAction(self.driver)
            action.\
                long_press(origin_el).\
                wait().\
                move_to(x=x, y=y).\
                release().\
                perform()

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
            .move_to(x=end_x, y=end_y)\
            .release()
        action.perform()

    def vswipe(self, start_y=None, end_y=None):
        '''
        Vertically swipe\n
        \n
        - start_y - coordinates on Y axis for start point\n
        - end_y - coordinates on Y axis for end point
        '''
        self.swipe(self.X/2, start_y, self.X/2, end_y)

    def hswipe(self, start_x=None, end_x=None):
        '''
        Horizontal swipe\n
        \n
        - start_x - coordinates on X axis for start point\n
        - end_x - coordinates on X axis for end point
        '''
        self.swipe(start_x, self.Y/2, end_x, self.Y/2)

    def swipe_up(self):
        '''
        Vertically swipe up
        '''
        start_y = self.Y/2 + self.Y/5
        end_y = self.Y/2 - self.Y/5
        self.vswipe(start_y, end_y)

    def swipe_down(self):
        '''
        Vertically swipe down
        '''
        start_y = self.Y/2 - self.Y/5
        end_y = self.Y/2 + self.Y/5
        self.vswipe(start_y, end_y)

    def swipe_left(self):
        '''
        Horizontal swipe left
        '''
        start_x = self.X/2 + self.X/3
        end_x = self.X/2 - self.X/3
        self.hswipe(start_x, end_x)

    def swipe_right(self):
        '''
        Horizontal swipe right
        '''
        start_x = self.X/2 - self.X/3
        end_x = self.X/2 + self.X/3
        self.hswipe(start_x, end_x)

    def zoom_in(self, element=None, percent=200, steps=50):
        '''
        Zoom in\n
        \n
        - element - the element to zoom\n
        - percent - amount to zoom. Defaults to 200%\n
        - steps - number of steps in the zoom action
        '''
        self.driver.zoom(element, percent, steps)

    def zoom_out(self, element=None, percent=200, steps=50):
        '''
        Zoom out\n
        \n
        - element - the element to pinch\n
        - percent - amount to pinch. Defaults to 200%\n
        - steps - number of steps in the pinch action
        '''
        self.driver.pinch(element, percent, steps)

    # def capture(self, what):
    #     # Capture a picture for an element
    #     begin = what.location
    #     size = what.size
    #     start_x = begin['x']
    #     start_y = begin['y']
    #     end_x = start_x + size['width']
    #     end_y = start_y + size['height']
    #     name = str(start_x)+'_'+str(start_y)+'_'+str(end_x)+'_'+str(end_y)
    #     box = (start_x, start_y, end_x, end_y)
    #     self.driver.get_screenshot_as_file(tmp + '/' + 'full_screen.png')
    #     image = Image.open(tmp + '/' + 'full_screen.png')
    #     newimage = image.crop(box)
    #     newimage.save(tmp + '/' + name + '.png')
    #     os.popen('rm %s/full_screen.png' %tmp)

    def verify(self, what, WAITTIME=10):
        '''
        Verify element shown on the screen\n
        \n
        - what - element location info\n
        - WAITTIME - amount of seconds for timeout, default is 10s
        '''
        end_time = time() + WAITTIME
        while time() < end_time:
            try:
                self.focus(what)
                return True
            except NoSuchElementException:
                pass
        raise NoSuchElementException('"%s" is not found' %what)

    def is_element_present(self, what, WAITTIME=1):
        '''
        Make a judgement, if the element is present or not\n
        \n
        - what - element location info\n
        - WAITTIME - amount of seconds for timeout, default is 1s
        '''
        end_time = time() + WAITTIME
        while time() < end_time:
            try:
                self.focus(what)
                return True
            except NoSuchElementException:
                pass
        return False

    def do_until_true(self, action, condition, times=5):
        '''
        Do 'action' until 'condition' is True, or try it for 'times' times\n
        \n
        - action - lambda statement for action\n
        - condition - lambda statement for condition\n
        - times - how many times to repeat, default is 5
        '''
        while(times):
            if condition():
                return
            action()
            times -= 1
        raise NoSuchElementException

    def do_until_false(self, action, condition, times=5):
        '''
        Do 'action' until 'condition' is True, or try it for 'times' times\n
        \n
        - action - lambda statement for action\n
        - condition - lambda statement for condition\n
        - times - how many times to repeat, default is 5
        '''
        while(times):
            if not condition():
                return
            action()
            times -= 1
        raise NoSuchElementException

    def text(self, where):
        '''
        Return text of an element.\n
        \n
        - where - element location info
        '''
        element = self.focus(where)
        text = element.text
        return text

    def wait_until(self, condition, WAITTIME=10):
        '''
        Wait until condition come true, default timeout is 10s.\n
        \n
        - condition - lambda statement for condition\n
        - WAITTIME - amount of seconds for timeout, default is 10s
        '''
        end_time = time() + WAITTIME
        while(time() < end_time):
            if condition():
                return
        raise TimeoutException

    def wait_until_not(self, condition, WAITTIME=10):
        '''
        Wait until condition comes false, default timeout is 10s.\n
        \n
        - condition - lambda statement for condition\n
        - WAITTIME - amount of seconds for timeout, default is 10s
        '''
        self.wait_until(lambda: not condition(), WAITTIME=WAITTIME)

    def wait_until_present(self, element, WAITTIME=10):
        '''
        Wait until element present\n
        \n
        - element - element location info
        - WAITTIME - seconds for timeout
        '''
        self.wait_until(lambda: self.is_element_present(element), WAITTIME)

    def wait_until_not_present(self, element, WAITTIME=10):
        '''
        Wait until element not present\n
        \n
        - element - element location info
        - WAITTIME - seconds for timeout
        '''
        self.wait_until_not(lambda: self.is_element_present(element), WAITTIME)

    def hide_keypad(self):
        '''
        If the keypad available, hide it
        '''
        try:
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    def launch_app(self):
        '''
        Launch test app
        '''
        self.driver.launch_app()

    def close_app(self):
        '''
        Close test app
        '''
        self.driver.close_app()

