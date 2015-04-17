#!/usr/bin/env python
#author:duizhang
#email:570962906@qq.com
#date:2014-12-19
#desc:mysql monitor client
import MySQLdb
import time

def getMysqlInfo():
	data = {}
	data["id"] = 1
	con = MySQLdb.connect(host="localhost",user="monitoruser",passwd="123456",db="",port=3306)
	cursor = con.cursor(cursorclass = MySQLdb.cursors.DictCursor)
	cursor.execute("SHOW GLOBAL STATUS LIKE 'Com_select'")
	result = cursor.fetchall()
	myisamSelect = result[0]["Value"]
	cursor.execute("SHOW GLOBAL STATUS LIKE 'Com_delete'")
	result = cursor.fetchall()
	myisamDelete = result[0]["Value"]
	cursor.execute("SHOW GLOBAL STATUS LIKE 'Com_update'")
	result = cursor.fetchall()
	myisamUpdate = result[0]["Value"]
#	cursor.execute("SHOW GLOBAL STATUS LIKE 'Innodb_rows_read'")
#	result = cursor.fetchall()
#	key,innodbSelect = result[0]
#	cursor.execute("SHOW GLOBAL STATUS LIKE 'Innodb_rows_deleted'")
#	result = cursor.fetchall()
#	key,innodbDelete = result[0]
#	cursor.execute("SHOW GLOBAL STATUS LIKE 'Innodb_rows_updated'")
#	result = cursor.fetchall()
#	key,innodbUpdate = result[0]
	data["select"] = int(myisamSelect)
	data["delete"] = int(myisamDelete)
	data["update"] = int(myisamUpdate)
	##slave status
	cursor.execute("SHOW SLAVE STATUS;")
	result = cursor.fetchall()
	try:
		data["slaveIO"] = result[0]["Slave_IO_Running"]
		data["slaveSQL"] = result[0]["Slave_SQL_Running"]
	except:
		data["slaveIO"] = "None"
		data["slaveSQL"] = "None"
	cursor.close()
	con.close()
	return data
# inert into database
def saveInfo():
	data = getMysqlInfo()
	con = MySQLdb.connect(host="192.168.1.109",user="getinfo",passwd="123456",db="dzoms",port=3306)
	cursor = con.cursor(cursorclass = MySQLdb.cursors.DictCursor)
	sql = "INSERT INTO DZoms_dbstatusinfo (`host`,`select`,`delete`,`update`,`slaveIO`,`slaveSQL`,`pubDate`) VALUES(%d,%d,%d,%d,'%s','%s',%d)"%(data["id"],data["select"],data["delete"],data["update"],data["slaveIO"],data["slaveSQL"],int(time.time()))
	cursor.execute(sql)
	con.commit()
	cursor.close()
	con.close()	

if __name__ == "__main__":
	saveInfo()
