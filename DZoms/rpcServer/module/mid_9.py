#!/usr/bin/env python
import ansible.runner
import os
sysdir = os.path.abspath(os.path.dirname(__file__))
class moduleHandle():
	def __init__(self,hosts):
		self.hosts = hosts
		self.result = ""
	
	def run(self):
		try:	
			runner = ansible.runner.Runner(
				module_name="command",
				module_args="find /data/nginx/1youku/ -name '*.cache.php' -type f -exec rm -rf {} \;",
				host_list=sysdir+"/inventory.py",
				pattern=self.hosts,
				forks=10
				)
			self.result = runner.run()
			#if len(self.result["dark"])==0 and len(self.result["contacted"])==0:
			#	return "No hosts found"
		except Exception,e:
			return str(e)
		return self.result

#if __name__ == "__main__":
#	d = moduleHandle("test")
#	print d.run()

