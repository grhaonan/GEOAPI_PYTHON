import urllib
import sqlite3
import json
import time

serviceurl = "http://maps.google.cn/maps/api/geocode/json?"
conndb = sqlite3.connect('geodata.db')
cur = conndb.cursor()

uni_list = open("where.data")
count=0
for ln in uni_list:
    if count > 100 : break
    uni_name = ln.strip()
    print "Retriving", uni_name
    url = serviceurl+ urllib.urlencode({"sensor":"false","address":uni_name})
    print "Retriving", url
    temp = urllib.urlopen(url, context=None)
    data = temp.read()
    count= count+1
    js=json.loads(str(data))

    if "status" not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print "----Failure To Retrieve----"
        print data
        break
    cur.execute('''INSERT INTO Locations VALUES (?,? )''', (buffer(uni_name), buffer(data)))
    conndb.commit()
    uni_list.close()
    time.sleep(1)




