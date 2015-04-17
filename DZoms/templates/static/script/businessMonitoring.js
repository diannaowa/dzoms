$(document).ready(function(){
	$("button[name='commit']").bind("click",function(){
		var title = $("input[name='title']").val();
		var url = $("input[name='url']").val();
		var code200 = $("input[name='code200']:checked").val();
		var returnMsg = "";
		if(code200==undefined){
			code200=0;
			returnMsg = $("input[name='returnMsg']").val();
		}
		if(title==""||title==undefined||url==""||url==undefined){
			alert("请填写完整业务名称和链接");
			return false;
		}
		if(code200==0 && returnMsg==""){
			alert("请指定检测规则");
			return false;
		}
		$.post("/businessMonitoring/",
			{title:title,url:url,code200:code200,returnMsg:returnMsg},
			function(data){
				if(data.status==1){
					alert("业务添加成功");
				}else{
					alert("操作失败");
				}
			},
			"json"
			);
	});	

	// delete
	$("a.delBusiness").bind("click",function(){
		var id = $(this).attr("rel");
		$.post("/businessMonitoringDel/",
			{id:id},
			function(data){
				if(data.status==1){
					$("tr.business_"+id).hide();
				}else{
					alert("操作失败");
				}
			},
			"json"
			);
	});
  // init cache
  $("button[name='initcache']").bind("click",function(){
		var obj = $(this);
		obj.text("操作中....");	  
		$.get("/initBusinessCache/",
			{},
			function(data){
		 		if(data.status==1){
					obj.text("操作成功");
				}else{
					obj.text("操作失败");
				}
			},
			"json"
			);
	});
  //create rrd
  $("a.createRRD").bind("click",function(){
		var id = $(this).attr("rel");		  
		$.post("/createBusinessMrrd/",
			{id:id},
			function(data){
				if(data.status==1){
					alert("成功创建RRD文件");
				}else{
					alert("操作失败");
				}
			},
			"json"
			);
	});
})
