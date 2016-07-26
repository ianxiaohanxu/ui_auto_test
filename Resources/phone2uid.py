import sys
import pymysql

host = '113.31.82.189'
port = 3306
user = 'root'
passwd = 'uxin.com'
db = 'ams0'
uid = ''

if len(sys.argv) < 2:
    print "error input"
    sys.exit()
else:
    phone = sys.argv[1]
    db = 'ams' + str(eval(phone)%16)

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
c = conn.cursor()
c.execute("select uid from %s.t_phone_uid where phone = %s" % (db, str(sys.argv[1])))

for r in c:
    uid = str(r[0])

if not uid:
    print "error phone number or not exist"
else:
    print uid






