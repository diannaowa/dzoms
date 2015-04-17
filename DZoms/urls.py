from django.conf.urls import patterns, include, url
from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from django.conf import settings
# admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DZoms.views.home', name='home'),
    # url(r'^DZoms/', include('DZoms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^$',index),
	url(r'^header/$',header),
	url(r'^content/$',content),
	url(r'^nav/$',nav),
	url(r'^module/$',module),
	url(r'^moduledel/$',moduledel),
	url(r'^moduleEdit/$',moduleEdit),
	url(r'^hostCategory/$',hostCategory),
	url(r'^hostCategoryDel/$',hostCategoryDel),
	url(r'^host/$',host),
	url(r'^hostdel/$',hostdel),
	url(r'^hostedit/$',hostedit),
	url(r'^hosteditc/$',hosteditCategory),
	url(r'^hostCategoryEdit/$',hostCategoryEdit),
	url(r'^hostCategoryEdit2/$',hostCategoryEdit2),
	url(r'^user/$',user),
	url(r'^userDel/$',userDel),
	url(r'^userEditName/$',userEditName),
	url(r'^userEditHost/$',userEditHost),
	url(r'^crontab/$',crontab),
	url(r'^crontabDel/$',crontabDel),
	url(r'^getUserByHost/$',getUserByHost),
	url(r'^createScript/$',createScript),
	url(r'^scriptDel/$',scriptDel),
	url(r'^remoteControl/$',remoteControl),
	url(r'^businessMonitoring/$',businessMonitoring),
	url(r'^businessMonitoringDel/$',businessMonitoringDel),
	url(r'^initBusinessCache/$',initBusinessCache),
	url(r'^createBusinessMrrd/$',createBusinessMrrd),
	url(r'^businessGraph/$',businessGraph),
	url(r'^dbMonitoring/$',dbMonitoring),
	url(r'^dbMonitoringDel/$',dbMonitoringDel),
	url(r'^initDBCache/$',initDBCache),
	url(r'^dbGraph/$',dbGraph),
	url(r'^hostM/$',hostM),

)
urlpatterns += staticfiles_urlpatterns() 
