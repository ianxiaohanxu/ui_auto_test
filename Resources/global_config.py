# coding=utf-8

uxin_dev = {#---server url
            'ams_url': 'http://60.205.150.134:8046/ams2',
            'das_url': 'http://60.205.150.90:9090',
            'rms_url': 'http://60.205.150.90:9880/rateManager',
            'goodscenter_umember_url': 'http://60.205.150.90:8015/goodscenter/umember',
            'goodscenter_url': 'http://60.205.150.90:8015/goodscenter',
            'order_url': 'http://60.205.150.90:8036/order',
            'epay_url': 'http://113.31.82.174:7793/epay',
            'offiaccount_url': 'http://113.31.82.189:8887/v3/im/offiaccount',
            'bc_url': 'http://60.205.150.90:8052',
            'rcserver_url': 'http://60.205.150.90:8058/rcserver'
}

uxin_test = {#---server url
            'ams_url': 'http://101.200.175.73:8046/ams2',
            'das_url': 'http://101.200.175.73:6002',
            'rms_url': 'http://101.200.175.73:6000/rateManager',
            'goodscenter_umember_url': 'http://101.200.175.73:8015/goodscenter/umember',
            'goodscenter_url': 'http://101.200.175.73:8015/goodscenter',
            'order_url': 'http://101.200.175.73:8036/order',
            'epay_url': 'http://101.200.175.73:8038/epay',
            'offiaccount_url': 'http://101.200.175.73:8887/v3/im/offiaccount',
            'bc_url': 'http://101.200.175.73:6001',
            'rcserver_url': 'http://101.200.175.73:8056/rcserver'
}

uxin_basic = {# pwd salt 
            'salt': '~X!U@N#I$',
            'signkey': 'sdvb753!@&*qpaltrko#$%^159plmokn',
            'rcserverkey': '#!rcserver@2014',
            #db url
            'db_url': '101.201.74.42',
            'db_user': 'root',
            'db_pwd': 'uxin.com',
            #redis
            'uxin_redis_url': '101.201.74.42',
            'uxin_redis_port': '6322',
}

def get_variables(arg=''):
    if arg == 'uxin_dev':
        uxin_dev.update(uxin_basic)
        return uxin_dev
    else:
        uxin_test.update(uxin_basic)
        return uxin_test

##----直播
live_user_url = "http://60.205.59.6:8080/api/v1/user"
live_userrelation_url = "http://60.205.59.6:8080/api/v1/userrelation"
live_goods_url = "http://60.205.59.6:8080/api/v1/goods"
live_room_url = "http://60.205.59.6:8080/api/v1/room"
live_account_url = "http://60.205.59.6:8080/api/v1/account"
live_configuration_url = "http://60.205.59.6:8080/api/v1/configuration"

