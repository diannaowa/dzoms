from django.db import models

# Create your models here.
class Module(models.Model):
	title = models.CharField(max_length=30)
	message = models.CharField(max_length=255)
	pubDate = models.IntegerField(max_length=11)

# host category
class HostCategory(models.Model):
	title = models.CharField(max_length=30)
	cname = models.CharField(max_length=30)
	pubDate = models.IntegerField(max_length=11)

# host
class Host(models.Model):
	title = models.CharField(max_length=30)
	ip = models.CharField(max_length=16)
	os = models.CharField(max_length=10)
	position = models.CharField(max_length=20)
	category = models.IntegerField(max_length=5)
	sudo = models.CharField(max_length=30)
	passwd = models.CharField(max_length=50)
	port = models.IntegerField(max_length=5)
	hostm = models.IntegerField(max_length=1)
	pubDate = models.IntegerField(max_length=11)
# host user
class User(models.Model):
	userName = models.CharField(max_length=30)
	host = models.IntegerField(max_length=11)#host id
	pubDate = models.IntegerField(max_length=11)
#crontab
class Crontab(models.Model):
	title = models.CharField(max_length=100)
	min = models.CharField(max_length=30)
	hour = models.CharField(max_length=30)
	day = models.CharField(max_length=30)
	month = models.CharField(max_length=30)
	week = models.CharField(max_length=30)
	job = models.CharField(max_length=200)
	host = models.IntegerField(max_length=11)#host id
	user = models.CharField(max_length=30)
	pubDate = models.IntegerField(max_length=11)
#create script
class Script(models.Model):
	title = models.CharField(max_length=30)
	host = models.IntegerField(max_length=11)
	user = models.CharField(max_length=30)
	path = models.CharField(max_length=100)
	#content = models.TextField(blank=True)
	pubDate = models.IntegerField(max_length=11)
#business monitoring
class BusinessMonitoring(models.Model):
	title = models.CharField(max_length=50)
	url = models.CharField(max_length=200)
	code200 = models.IntegerField(max_length=1)
	returnMsg = models.CharField(max_length=100)
	pubDate = models.IntegerField(max_length=11)

#db list
class dbInfo(models.Model):
	title = models.CharField(max_length=50)
	host = models.CharField(max_length=20)
	slave = models.IntegerField(max_length=1)
	pubDate = models.IntegerField(max_length=11)
#db status info
class dbStatusInfo(models.Model):
	host = models.IntegerField(max_length=11)#db id
	select = models.IntegerField(max_length=11)
	update = models.IntegerField(max_length=11)
	delete = models.IntegerField(max_length=11)
	slaveIO = models.CharField(max_length=10)
	slaveSQL = models.CharField(max_length=10)
	pubDate = models.IntegerField(max_length=11)
#performance
#class performanceHost(models.Model):
#	host = models.IntegerField(max_length=11)#host id
#	pubDate = models.IntegerField(max_length=11)
