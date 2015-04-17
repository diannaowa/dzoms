#!/usr/bin/env python
#author:duizhang
#email:570962906@qq.com
#date:20141210

from rpyc import Service
from rpyc.utils.server import ThreadedServer
import logging,os,json
sysdir = os.path.abspath(os.path.dirname(__file__))
class omsService(Service):
	'''
		rpc server for control remote host
	'''

	'''authentication'''
	def exposed_auth(self,name,passwd):
		if name == "root" and passwd == "123456":
			self.auth = True
		else:
			self.auth = False
	
	''' run command '''
	def exposed_run(self,cmdString):
		logging.basicConfig(level=logging.DEBUG,
				format='%(asctime)s [%(levelname)s] %(name)s : %(message)s',
				filename = sysdir+"/dzoms.log",
				filemode="a")
		if self.auth != True:
			return "Authentication failed"
		cmd = json.loads(cmdString)
		mod = "mid_"+str(cmd["module"])
		importString = "from module."+mod+" import moduleHandle"
		try:
			exec importString
		except:
			return mod+".py is not found"
		action = moduleHandle(cmd["hosts"])
		result = action.run()
		status = {"status":0,"hosts":{"dark":[],"contacted":[]}}
		if len(result["dark"])==0 and len(result["contacted"])==0:
			return json.dumps(status)
		status["status"] = 1
		for h in result["dark"]:
			status["hosts"]["dark"].append(h)
		for h in result["contacted"]:
			status["hosts"]["contacted"].append(h)
		return json.dumps(status)



s = ThreadedServer(omsService,port=2048,auto_register=False)
s.start()

