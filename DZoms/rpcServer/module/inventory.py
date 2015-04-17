#!/usr/bin/python
import MySQLdb,json
host = {}
try:
	conn = MySQLdb.connect(host='192.168.1.119',user='dzoms',passwd='123456',port=3306)
	cur = conn.cursor()
	conn.select_db('dzoms')
	cur.execute('SELECT a.title,a.ip,b.title,b.cname FROM DZoms_host a LEFT JOIN DZoms_hostcategory b ON a.category=b.id')
	result = cur.fetchall()
	for i in result:
		host[i[0]] = {}
	for i in result:
		host[i[0]] = {"hosts":[i[1]]}
		host[i[3]] = {"hosts":[]}
	for i in result:
		host[i[3]]["hosts"].append(i[1])
	print json.dumps(host)
except MySQLdb.Error,e:
	print e
