//
//
$(document).ready(function(){

	$("button[name='commit']").bind("click",function(){
		var title = $("input[name='title']").val();
		var ip = $("input[name='ip']").val();
		var slave = $("input[name='slave']:checked").val();
		if(slave==undefined) slave=0;
		if(title == "" || title == undefined || ip == "" || ip == undefined){
			alert("请填写标题或主机");
			return false;
		}
		$.post("/dbMonitoring/",
			{title:title,ip:ip,slave:slave},
			function(data){
				if(data.status==1){
					alert("添加数据库信息成功");
				}else{
					alert("操作失败");
				}
			},
			"json"
			);
	});	
//del
	$("a.delDB").bind("click",function(){
		var id = $(this).attr("rel");
		$.post("/dbMonitoringDel/",
			{id:id},
			function(data){
				if(data.status==1){
					$("tr.db_"+id).hide();
				}else{
					alert("操作出错");
				}
			},
			"json"
			);
	});
	//cache
	$("button[name='initcache']").bind("click",function(){
		$.get("/initDBCache/",{},
			function(data){
				if(data.status==1){
					alert("缓存更新成功");
				}else{
					alert("操作失败");
				}
			},
			"json"
			);	
	});
	// create rrd
	$("a.createRRD").bind("click",function(){
		var id = $(this).attr("rel");
		$.post("/createDBrrd/",
			{id:id},
			function(data){
				alert(data);
			},
			"json"
			);
	});
})
