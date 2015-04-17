
$(document).ready(function(){
	$("button[name='commit']").bind("click",function(){
		var moduleName = $("input[name='moduleName']").val();
		var moduleDes = $("textarea[name='moduleDes']").val();
		if(moduleName==""){
			alert("Plz input module name!~");
			return false;
		}
		$.post("/module/",
			{moduleName:moduleName,moduleDes:moduleDes},
			function(data){
				if(data.status==1){
					alert("模块添加成功，请自定义开发后端模块");
				}
				return false;
			},
			"json"
			);
	});			
	$("button[name='reset']").bind("click",function(){
			$("input[name='moduleName']").val("");
			$("textarea[name='moduleDes']").val("");
			
		});
	$("a.del").bind("click",function(){
		var id = $(this).attr("ref");
		$.post("/moduledel/",
			{id:id},
			function(data){
				if(data.status==1){
					$("#module_"+id).hide();
				}else{
					alert("删除失败");
				}
			},
			"json"
			);
	});
});
