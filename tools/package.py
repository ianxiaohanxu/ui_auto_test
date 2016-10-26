#-*- coding: UTF-8 -*-
from distutils.core import setup

setup(
    name = 'ui_test',
    version = '1.0.0',
    package_dir = { '': '..' },
    packages = [
        'ui_test',
        'ui_test.platform',
        'ui_test.business_uxin',
        'ui_test.business_uxin.android',
        'ui_test.business_uxin.ios',
        'ui_test.business_uxin.android.pages',
        'ui_test.business_uxin.ios.pages',
        'ui_test.business_redbeans',
        'ui_test.business_redbeans.android',
        'ui_test.business_redbeans.ios',
        'ui_test.business_redbeans.android.pages',
        'ui_test.business_redbeans.ios.pages'
        ],
    author = 'AlexGao',
    author_email = 'alex.gao@uxin.com',
    url = 'http://',
    description = 'None',
    )
