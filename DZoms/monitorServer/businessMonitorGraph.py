#!/usr/bin/env python
#coding:utf-8
#business monitor graph

import rrdtool,time,multiprocessing
import cPickle as pickle

def rrdGraph(id,title):
	nowTime = time.strftime("%H\:%M")
	startTime = "-6h"
	endTime = str(int(time.time()))
	alarm = "500"
	rrdfile = "/root/DZoms/DZoms/monitorServer/rrd/businessMonitoring_"+str(id)+".rrd"
	title = title.encode("utf-8")
	ymax = "500"
	pngPath = "/root/DZoms/DZoms/templates/static/rrdpng/businessMonitoring_"+str(id)+".png"
	rrdtool.graph(pngPath,"--start",startTime,"--end",endTime,"--width","480","--height","207px",
		"--color","SHADEA#808080","--color","SHADEB#808080","--color","FRAME#006600","--color","ARROW#FF0000",
		"--color","FONT#000000","--color","CANVAS#EEFFFF","--color","BACK#FFFFFF",
		"--title",title,"--lower-limit","0","--base","1024","--upper-limit",ymax,
		"DEF:namelookupTime="+rrdfile+":namelookupTime:AVERAGE",
		"DEF:connectTime="+rrdfile+":connectTime:AVERAGE",
		"DEF:startTransferTime1="+rrdfile+":startTransferTime:AVERAGE",
		"DEF:totalTime="+rrdfile+":totalTime:AVERAGE",
		"COMMENT:\\r",
		"AREA:totalTime#0011FF:总共时间",
		"GPRINT:totalTime:LAST:当前\:%6.2lf %Sms",
		"GPRINT:totalTime:AVERAGE:平均\:%6.2lf %Sms",
		"GPRINT:totalTime:MAX:最大\:%6.2lf %Sms",
		"GPRINT:totalTime:MIN:最小\:%6.2lf %Sms",
		"COMMENT:\\r",
		"LINE1:namelookupTime#EEEE00:域名解析",
		"GPRINT:namelookupTime:LAST:当前\:%6.2lf %Sms",
		"GPRINT:namelookupTime:AVERAGE:平均\:%6.2lf %Sms",
		"GPRINT:namelookupTime:MAX:最大\:%6.2lf %Sms",
		"GPRINT:namelookupTime:MIN:最小\:%6.2lf %Sms",
		"COMMENT:\\r",
		"LINE1:startTransferTime1#EE00FF:开始传输",
		"GPRINT:startTransferTime1:LAST:当前\:%6.2lf %Sms",
		"GPRINT:startTransferTime1:AVERAGE:平均\:%6.2lf %Sms",
		"GPRINT:startTransferTime1:MAX:最大\:%6.2lf %Sms",
		"GPRINT:startTransferTime1:MIN:最小\:%6.2lf %Sms",
		"COMMENT:\\r",
		"LINE1:connectTime#99CFEE:连接时间",
		"GPRINT:connectTime:LAST:当前\:%6.2lf %Sms",
		"GPRINT:connectTime:AVERAGE:平均\:%6.2lf %Sms",
		"GPRINT:connectTime:MAX:最大\:%6.2lf %Sms",
		"GPRINT:connectTime:MIN:最小\:%6.2lf %Sms",
		"COMMENT:\\r",
		"HRULE:"+alarm+"#FF0000:告警值",
		"COMMENT:\\r",
		"COMMENT:\\r",
		"COMMENT:最后更新时间\:"+nowTime
		)

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
			rrdGraph(data[i]["id"],data[i]["title"])
			#result.append(p.apply_async(rrdGraph,("%d"%data[i]["id"],"%s"%data[i]["title"])))
		except IndexError:
			break
	#for rs in result:
	#	rs.get(timeout=30)
