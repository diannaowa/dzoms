#!/usr/bin/env python
import cPickle as pickle
import sys,pycurl,os,rrdtool
import multiprocessing
import time

class businessMonitor():
	def __init__(self,url,code="",returnMsg=""):
		self.url = str(url)
		self.code = code
		self.returnMsg = str(returnMsg)
		self.result = {}
	def runMonitor(self):
		c = pycurl.Curl()
		c.setopt(pycurl.URL,self.url)
		c.setopt(pycurl.CONNECTTIMEOUT,5)
		c.setopt(pycurl.TIMEOUT,5)
		c.setopt(pycurl.NOPROGRESS,5)
		c.setopt(pycurl.FORBID_REUSE,1)
		c.setopt(pycurl.MAXREDIRS,1)
		c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
		body = open(os.path.dirname(os.path.realpath(__file__))+"/index.txt","wb")
		c.setopt(pycurl.WRITEHEADER,body)
		c.setopt(pycurl.WRITEDATA,body)
		try:
			c.perform()
		except Exception,e:
			print "error:"+str(e)
			body.close()
			c.close()
			sys.exit()

		self.result["namelookupTime"] = round(c.getinfo(c.NAMELOOKUP_TIME)*1000,2)#dns resolve time ms
		self.result["connectTime"] = round(c.getinfo(c.CONNECT_TIME)*1000,2)# connect time ms
		self.result["totalTime"] = round(c.getinfo(c.TOTAL_TIME)*1000,2)#total time
		self.result["httpCode"] = c.getinfo(c.HTTP_CODE)#http code
		self.result["startTransferTime"] = round(c.getinfo(c.STARTTRANSFER_TIME)*1000,2)#ms
		body.close()
		c.close()
		return self.result

def runMonitor(id,url,code,returnMsg):
	b = businessMonitor(url,code,returnMsg)
	data = b.runMonitor()
	curTime = str(int(time.time()))
	rrdPath = os.path.dirname(os.path.realpath(__file__))+"/rrd/businessMonitoring_"+id+".rrd"
	#update rrd
	namelookupTime = str(round(data["namelookupTime"],2))
	startTransferTime = str(round(data["startTransferTime"],2))
	totalTime = str(round(data["totalTime"],2))
	connectTime = str(round(data["connectTime"],2))
	if data["httpCode"]==200 or data["httpCode"]==302:
		try:
			rrdtool.updatev(rrdPath,"%s:%s:%s:%s:%s"%(curTime,namelookupTime,startTransferTime,totalTime,connectTime))
		except Exception,e:
			print str(e)

if __name__ == "__main__":
	maxThread = 10
	maxPool = 10
	result = []
	fp = file("/root/DZoms/DZoms/monitorServer/businessData.pkl","rb")
	data = pickle.load(fp)
	fp.close()
	p = multiprocessing.Pool(processes=maxPool)
	for i in range(maxThread):
		try:
			result.append(p.apply_async(runMonitor,("%d"%data[i]["id"],"%s"%data[i]["url"],"%s"%data[i]["code200"],"%s"%data[i]["returnMsg"],)))
		except IndexError:
			break
	for rs in result:
		rs.get(timeout=30)
