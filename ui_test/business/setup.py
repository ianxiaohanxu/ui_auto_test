#-*- coding: UTF-8 -*-

from ui_test.business.android.ui_function import Scenario

pre_session = Scenario()
pre_session.ready()
try:
    pre_session.unbind_system()
finally:
    pre_session.teardown()
