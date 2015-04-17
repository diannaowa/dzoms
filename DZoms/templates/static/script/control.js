/*
 * */
$(document).ready(function(){
	$("button[name='execute']").bind("click",function(){
		var mid = $("select[name='module']").val();
		var hid = $("select[name='host']").val();
		var mtext = $("select[name='module']").find("option:selected").text();
		var htext = $("select[name='host']").find("option:selected").text();
		if (mid==""||mid==null||hid==""||hid==null){
			alert("请选择模块或主机");
			return false;
		}
		$("ul.cmdLine").append("<li>[root@localhost ~]# 正在 "+htext+" 上执行 "+mtext+"......</li>");
		$.post("/remoteControl/",
			{mid:mid,hid:hid},
			function(data){
				if(data.status!=1){
					$("ul.cmdLine").append("<li>[root@localhost ~]# 服务器内部出错......</li>");	
				}else{
					$.each(data.hosts.dark,function(k,v){
						$("ul.cmdLine").append("<li>[root@localhost ~]# "+v+" 执行<font color=red>失败</font>......</li>");	
					});
					$.each(data.hosts.contacted,function(kk,vv){
						$("ul.cmdLine").append("<li>[root@localhost ~]# "+vv+" 执行<font color=green>成功</font>......</li>");	
					});
				}
			},
			"json"
			);
	});	
		
});
