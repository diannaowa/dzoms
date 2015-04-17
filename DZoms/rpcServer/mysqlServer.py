#!/usr/bin/env python
#author:duizhang
#email:570962906@qq.com
#date:2014-12-19
#desc: mysql rpc server,get info from rpc client,and update rrd
from rpyc import Service
from rpyc.utils.server import ThreadedServer
import logging,os,json
sysdir = os.path.abspath(os.path.dirname(__file__))

class mysqlService(Service):

	'''authentication'''

	def exposed_auth(self,name,passwd):
		if name == "root" and passwd == "123456":
			self.auth = True
		else:
			self.auth = False
	
	'''get mysql info from client and update rrd'''

	def exposed_run(self,infoString):
		logging.basicConfig(level=logging.DEBUG,
				format="%(asctime)s [%(levelname)s] %(name)s :%(message)s",
				filename=sysdir+"/mysql.log",
				filemode="a")
		if self.auth != True:
			return "Authentication failed"
		return infoString

if __name__ == "__main__":
	s = ThreadedServer(mysqlService,port=2049,auto_register=False)
	s.start()
