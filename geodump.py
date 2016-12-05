import sqlite3
import json
import codecs

conn = sqlite3.connect("geodata.db")
cur = conn.cursor()
cur.execute('SELECT * FROM Locations')
fw = codecs.open('where.js','w','utf-8')
fw.write("myData = [\n")
count =0
for row in cur:
    data = str(row[1])
    try: js=json.loads(str(data))
    except:continue

    if not ('status' in js and js['status'] == 'OK') : continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    where = js['results'][0]['formatted_address']
    print "first where is ", where
    where = where.replace("'", "")
    print "second where is", where
    count = count + 1
    if count > 1 : fw.write(",\n")
    output = "["+str(lat)+","+str(lng)+",'"+where+"']"
    fw.write(output)
fw.write("\n];\n")
fw.close()
cur.close()
print count, "records written to where.js"
