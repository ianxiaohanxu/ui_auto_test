#-*- coding: UTF-8 -*-
from distutils.core import setup

setup(
    name = 'ui_test',
    version = '1.0.0',
    package_dir = { '': '..' },
    packages = ['ui_test', 'ui_test.platform', 'ui_test.business', 'ui_test.business.android', 'ui_test.business.ios', 'ui_test.business.android.pages', 'ui_test.business.ios.pages'],
    author = 'AlexGao',
    author_email = 'alex.gao@uxin.com',
    url = 'http://',
    description = 'None',
    )