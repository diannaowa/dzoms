from django.http import HttpResponse
from django.shortcuts import render_to_response
import time,json,os
from DZoms.models import Module,HostCategory,Host,User,Crontab,Script,BusinessMonitoring,dbInfo,dbStatusInfo

sysdir = os.path.abspath(os.path.dirname(__file__))

def index(request):
	return render_to_response("indexMgr.html")
def header(request):
	return render_to_response("frmHeader.html")
def content(request):
	return render_to_response("frmContent.html")
def nav(request):
	return render_to_response("frmNav.html")
def module(request):
	if request.method == "POST":
		moduleName = request.POST["moduleName"]
		moduleDes = request.POST["moduleDes"]
		pubDate = int(time.time())
		m = Module(title=moduleName,message=moduleDes,pubDate=pubDate)
		m.save()
		return HttpResponse(json.dumps({"status":1}))
	module = Module.objects.order_by("-id")
	return render_to_response("module.html",{"module":module})
#edit module
def moduleEdit(request):
	if request.method == "POST":
		id = request.POST["id"]
		m = Module.objects.get(id=id)
		m.title = request.POST["title"]
		m.message = request.POST["message"]
		m.save()
		return HttpResponse(json.dumps({"status":1}))
def moduledel(request):
	if request.method == "POST":
		id = request.POST["id"]
		m = Module.objects.get(id=id)
		m.delete()
		return HttpResponse(json.dumps({"status":1}))

# host category
def hostCategory(request):
	if request.method == "POST":
		title = request.POST["title"]
		cname = request.POST["cname"]
		pubDate = int(time.time())
		c = HostCategory(title=title,cname=cname,pubDate=pubDate)
		c.save()
		return HttpResponse(json.dumps({"status":1}))
	hostCategory = HostCategory.objects.order_by("-id")
	return render_to_response("hostCategory.html",{"category":hostCategory})
#edit category
def hostCategoryEdit(request):
	if request.method == "POST":
		id = request.POST["id"]
		c = HostCategory.objects.get(id=id)
		c.title = request.POST["title"]
		c.save()
		return HttpResponse(json.dumps({"status":1}))
#edit category2
def hostCategoryEdit2(request):
	if request.method == "POST":
		id = request.POST["id"]
		c = HostCategory.objects.get(id=id)
		c.cname = request.POST["cname"]
		c.save()
		return HttpResponse(json.dumps({"status":1}))
#delete category
def hostCategoryDel(request):
	if request.method == "POST":
		id = request.POST["id"]
		c = HostCategory.objects.get(id=id)
		c.delete()
		return HttpResponse(json.dumps({"status":1}))
#host
def host(request):
	if request.method == "POST":
		title = request.POST["title"]
		category = request.POST["category"]
		os = request.POST["os"]
		ip = request.POST["ip"]
		sudo = request.POST["sudo"]
		passwd = request.POST["passwd"]
		port = request.POST["port"]
		position = request.POST["position"]
		pubDate = int(time.time())
		h = Host(title=title,ip=ip,category=category,os=os,position=position,sudo=sudo,passwd=passwd,port=port,pubDate=pubDate)
		h.save()
		return HttpResponse(json.dumps({"status":1}))
	## get category list
	category = HostCategory.objects.order_by("-id")
	host = Host.objects.order_by("-id")
	return render_to_response("host.html",{"host":host,"category":category})
#delete host
def hostdel(request):
	if request.method == "POST":
		id = request.POST["id"]
		h = Host.objects.get(id=id)
		h.delete()
		return HttpResponse(json.dumps({"status":1}))
# edit host
def hostedit(request):
	if request.method == "POST":
		id = request.POST["id"]
		h = Host.objects.get(id=id)
		h.title = request.POST["title"]
		h.os = request.POST["os"]
		h.ip = request.POST["ip"]
		h.position = request.POST["position"]
		h.sudo = request.POST["sudo"]
		h.passwd = request.POST["passwd"]
		h.port = request.POST["port"]
		h.save()
		return HttpResponse(json.dumps({"status":1}))
# edit host category
def hosteditCategory(request):
	if request.method == "POST":
		id = request.POST["id"]
		h = Host.objects.get(id=id)
		h.category = request.POST["category"]
		h.save()
		return HttpResponse(json.dumps({"status":1}))
# user
def user(request):
	if request.method == "POST":
		userName = request.POST["userName"]
		host = request.POST["host"]
		pubDate = int(time.time())
		u = User(userName=userName,host=host,pubDate=pubDate)
		u.save()
		return HttpResponse(json.dumps({"status":1}))
	user = User.objects.order_by("-id")
	host = Host.objects.order_by("-id").values("id","title")
	return render_to_response("user.html",{"user":user,"host":host})
# edit user name
def userEditName(request):
	if request.method == "POST":
		id = request.POST["id"]
		u = User.objects.get(id=id)
		u.userName = request.POST["userName"]
		u.save()
		return HttpResponse(json.dumps({"status":1}))
def userEditHost(request):
	if request.method == "POST":
		id = request.POST["id"]
		u = User.objects.get(id=id)
		u.host = request.POST["host"]
		u.save()
		return HttpResponse(json.dumps({"status":1}))
# user del
def userDel(request):
	if request.method == "POST":
		id = request.POST["id"]
		u = User.objects.get(id=id)
		u.delete()
		return HttpResponse(json.dumps({"status":1}))
#crontab
def crontab(request):
	import ansible.runner
	if request.method == "POST":
		title = request.POST["title"]
		min = request.POST["min"]
		hour = request.POST["hour"]
		day = request.POST["day"]
		month = request.POST["month"]
		week = request.POST["week"]
		job = request.POST["job"]
		host = request.POST["host"]
		user = request.POST["user"]
		pubDate = int(time.time())
		host = Host.objects.get(id=host)
		user = User.objects.get(id=user)
		runner = ansible.runner.Runner(
				module_name="cron",
				module_args="minute='"+min+"' hour='"+hour+"' day='"+day+"' month='"+month+"' weekday='"+week+"' name='"+title+"' user='"+user.userName+"' job='"+job+"'",
				host_list=sysdir+"/inventory.py",
				pattern=host.title,
				remote_user=host.sudo,
				remote_pass=host.passwd,
				remote_port=host.port,
				sudo=True,
				sudo_pass=host.passwd,
				forks=1
				)
		data=runner.run()
		if data["contacted"][host.ip]:
			cron = Crontab(title=title,min=min,hour=hour,day=day,month=month,week=week,job=job,host=host.id,user=user.userName,pubDate=pubDate)
			cron.save()
			return HttpResponse(json.dumps({"status":1}))
		else:	
			return HttpResponse(json.dumps({"status":0}))
	host = Host.objects.order_by("-id").values("id","title")
	#crontab = Crontab.objects.order_by("-id")[0:20]
	from django.db import connection
	cur = connection.cursor()
	cur.execute("SELECT a.*,b.title FROM DZoms_crontab a LEFT JOIN DZoms_host b ON a.host=b.id")
	crontab = cur.fetchall()
	crontabList = []
	cron = {}
	for c in crontab:
		cron["id"] = c[0]
		cron["title"] = c[1]
		cron["min"] = c[2]
		cron["hour"] = c[3]
		cron["day"] = c[4]
		cron["month"] = c[5]
		cron["week"] = c[6]
		cron["job"] = c[7]
		cron["host"] = c[8]
		cron["user"] = c[9]
		cron["pubDate"] = c[10]
		cron["hostName"] = c[11]
		crontabList.append(cron)
	return render_to_response("crontab.html",{"host":host,"crontab":crontabList})
#delete crontab
def crontabDel(request):
	import ansible.runner
	if request.method == "POST":
		id = request.POST["id"]
		c = Crontab.objects.get(id=id)
		host = Host.objects.get(id=c.host)
		runner = ansible.runner.Runner(
				module_name="cron",
				module_args="minute='"+c.min+"' hour='"+c.hour+"' day='"+c.day+"' month='"+c.month+"' weekday='"+c.week+"' name='"+c.title+"' user='"+c.user+"' job='"+c.job+"' state='absent'",
				host_list=sysdir+"/inventory.py",
				pattern=host.title,
				remote_user=host.sudo,
				remote_pass=host.passwd,
				remote_port=host.port,
				sudo=True,
				sudo_pass=host.passwd,
				forks=1
				)
		data=runner.run()
		if(data["contacted"][host.ip]):
			c.delete()
			return HttpResponse(json.dumps({"status":1}))
		else:
			return HttpResponse(json.dumps({"status":0}))

#get user by host
def getUserByHost(request):
	host = request.GET["host"]
	user = User.objects.filter(host=host)
	userList = []
	for u in user:
		userDic = {"userName":u.userName,"id":u.id}
		userList.append(userDic)
	return HttpResponse(json.dumps(userList))
#delete script
def scriptDel(request):
	if request.method == "POST":
		id = request.POST["id"]
		s = Script.objects.get(id=id)
		s.delete()
		return HttpResponse(json.dumps({"status":1}))
#create script
def createScript(request):
	if request.method == "POST":
		title = request.POST["title"]
		path = request.POST["path"]
		user = request.POST["user"]
		host = request.POST["host"]
		content = request.POST["content"]
		pubDate = int(time.time())
		#save the script file
		#sysdir = os.path.abspath(os.path.dirname(__file__))
		try:
			fp = open(sysdir+"/script/"+title,"w")
			fp.write(content)
		except:
			return HttpResponse(json.dumps({"status":0}))
		finally:
			fp.close()
		#copy the file to the remote server
		import ansible.runner
		user = User.objects.get(id=user)
		host = Host.objects.get(id=host)
		runner = ansible.runner.Runner(
				module_name="copy",
				module_args="group='"+user.userName+"' owner='"+user.userName+"' mode='0755' dest='"+path+"/"+title+"' src="+sysdir+"/script/"+title,
				host_list=sysdir+"/inventory.py",
				pattern=host.title,
				remote_user=host.sudo,
				remote_pass=host.passwd,
				remote_port=host.port,
				sudo=True,
				sudo_pass=host.passwd,
				forks=1
				)
		data = runner.run()
		if data['contacted'][host.ip]:
			script = Script(title=title,path=path,user=user.userName,host=host.id,pubDate=pubDate)
			script.save()
			return HttpResponse(json.dumps({"status":1}))
		else:
			return HttpResponse(json.dumps({"status":0}))

	host = Host.objects.order_by("-id").values("id","title")
	script = Script.objects.order_by("-id")[0:20]
	return render_to_response("script.html",{"host":host,"script":script})

# remote control center
def remoteControl(request):
	import rpyc
	from config import configSettings
	rpc = configSettings.RPC
	if request.method == "POST":
		cmdDic = {}
		hid = request.POST["hid"]
		mid = request.POST["mid"]
		#host = Host.objects.filter(category=hid).values("ip","sudo","passwd","port")
		hosts = HostCategory.objects.get(id=hid)
		cmdDic["module"] = mid
		cmdDic["hosts"] = hosts.cname
		c = rpyc.connect(rpc["host"],rpc["port"])
		c.root.auth("root","123456")
		string = c.root.run(json.dumps(cmdDic))
		return HttpResponse(string)
	module = Module.objects.values("id","title")
	hostCategory = HostCategory.objects.values("id","title")
	return render_to_response("remoteControl.html",{"module":module,"hostCategory":hostCategory})

# business monitoring
def businessMonitoring(request):
	if request.method == "POST":
		title = request.POST["title"]
		url = request.POST["url"]
		code200 = request.POST["code200"]
		returnMsg = request.POST["returnMsg"]
		pubDate = int(time.time())
		b = BusinessMonitoring(title=title,url=url,code200=code200,returnMsg=returnMsg,pubDate=pubDate)
		b.save()
		return HttpResponse(json.dumps({"status":1}))
	businessMonitoring = BusinessMonitoring.objects.order_by("-id")
	return render_to_response("businessMonitoring.html",{"business":businessMonitoring})
# delete business monitoring
def businessMonitoringDel(request):
	if request.method == "POST":
		id = request.POST["id"]
		b = BusinessMonitoring.objects.get(id=id)
		b.delete()
		return HttpResponse(json.dumps({"status":1}))
#init business cache
def initBusinessCache(request):
	business = BusinessMonitoring.objects.order_by("-id")
	bList = []
	for b in business:
		t = {"id":b.id,"title":b.title,"url":b.url,"code200":b.code200,"returnMsg":b.returnMsg}
		bList.append(t)
	import cPickle as pickle
	fp = file(sysdir+"/monitorServer/businessData.pkl","wb")
	pickle.dump(bList,fp,True)
	fp.close()
	return HttpResponse(json.dumps({"status":1}))
# create business monitoring rrd
def createBusinessMrrd(request):
	import rrdtool
	if request.method == "POST":
		id = request.POST["id"]
		curTime = str(int(time.time()))
		try:
			rrdTime = rrdtool.create(sysdir+"/monitorServer/rrd/businessMonitoring_"+str(id)+".rrd","--step","300","--start",curTime,
					"DS:namelookupTime:GAUGE:600:0:U",
					"DS:startTransferTime:GAUGE:600:0:U",
					"DS:totalTime:GAUGE:600:0:U",
					"DS:connectTime:GAUGE:600:0:U",
					"RRA:AVERAGE:0.5:1:600",
					"RRA:AVERAGE:0.5:6:700",
					"RRA:AVERAGE:0.5:24:775",
					"RRA:AVERAGE:0.5:288:797",
					"RRA:MAX:0.5:1:600",
					"RRA:MAX:0.5:6:700",
					"RRA:MAX:0.5:24:775",
					"RRA:MAX:0.5:444:797",
					"RRA:MIN:0.5:1:600",
					"RRA:MIN:0.5:6:700",
					"RRA:MIN:0.5:24:775",
					"RRA:MIN:0.5:444:797")
			if rrdTime:
				return HttpResponse(json.dumps({"status":0}))
		except Exception,e:
			return HttpResponse(json.dumps({"status":0}))

		return HttpResponse(json.dumps({"status":1}))
# list business rrd png
def businessGraph(request):
	import cPickle as pickle
	fp = file(sysdir+"/monitorServer/businessData.pkl","rb")
	data = pickle.load(fp)
	fp.close()
	graphList=[]
	for d in data:
		graphList.append("/static/rrdpng/businessMonitoring_"+str(d["id"])+".png")
	return render_to_response("businessGraph.html",{"graph":graphList})

#db monitoring
def dbMonitoring(request):
	if request.method == "POST":
		title = request.POST["title"]
		host = request.POST["ip"]
		slave = request.POST["slave"]
		pubDate = int(time.time())
		d = dbInfo(title=title,host=host,slave=slave,pubDate=pubDate)
		d.save()
		return HttpResponse(json.dumps({"status":1}))
	dbList = dbInfo.objects.order_by("-id")
	return render_to_response("dbMonitoring.html",{"db":dbList})
#del db monitoring
def dbMonitoringDel(request):
	if request.method == "POST":
		id = request.POST["id"]
		d = dbInfo.objects.get(id=id)
		d.delete()
		return HttpResponse(json.dumps({"status":1}))
	return HttpResponse(json.dumps({"status":0}))
# db cache
def initDBCache(request):
	db = dbInfo.objects.order_by("-id")
	bList = []
	for b in db:
		t = {"id":b.id,"title":b.title,"host":b.host,"slave":b.slave}
		bList.append(t)
	import cPickle as pickle
	fp = file(sysdir+"/monitorServer/dbData.pkl","wb")
	pickle.dump(bList,fp,True)
	fp.close()
	return HttpResponse(json.dumps({"status":1}))
#create db rrd
def dbGraph(request):
	import pygal,time
	#get host list
	import cPickle as pickle
	fp = file(sysdir+"/monitorServer/dbData.pkl","rb")
	data = pickle.load(fp)
	fp.close()
	for d in data:
		status = dbStatusInfo.objects.filter(host=d["id"]).order_by("-id")[0:10] 
		select = []
		update = []
		delete = []
		times = []
		img = []
		for s in status:
			select.append(s.select)
			update.append(s.update)
			delete.append(s.delete)
			times.append(s.pubDate)
		sel = [select[i]-select[i+1] for i in range(len(select)-1)]
		select = map(lambda x:x>0 and x or 0,sel)
		up = [update[i]-update[i+1] for i in range(len(update)-1)]
		update = map(lambda x:x>0 and x or 0,up)
		de = [delete[i]-delete[i+1] for i in range(len(delete)-1)]
		delete = map(lambda x:x>0 and x or 0,de)
		times = map(lambda t:time.strftime('%H:%M',time.localtime(float(t))),times)
		times.pop()
		lineChart = pygal.Line()
		#lineChart = pygal.StackedLine(fill=True,interpolate='cubic',style=pygal.style.NeonStyle)
		lineChart.title = d["title"]
		lineChart.x_labels = map(str,times)
		lineChart.add("Select",select)
		lineChart.add("Update",update)
		lineChart.add("Delete",delete)
		imgName = sysdir+"/templates/static/dbsvg/db_"+str(d["id"])+".svg"
		lineChart.render_to_file(imgName)
		img.append(imgName)
	return render_to_response("dbGraph.html",{"host":data})

#if monitor hos
def hostM(request):
	if request.method == "POST":
		id = request.POST["id"]
		val = request.POST["val"]
		h = Host.objects.get(id=id)
		h.hostm = val
		h.save()
		return HttpResponse(json.dumps({"status":1}))

