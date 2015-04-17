
$(document).ready(function(){
	$("button[name='commit']").bind("click",function(){
		var userName = $("input[name='userName']").val();
		var host = $("select[name='host']").val();
		if(userName=="" || host==""){
			alert("Plz input user name or host!~");
			return false;
		}
		$.post("/user/",
			{userName:userName,host:host},
			function(data){
				if(data.status==1){ 
					alert("用户添加成功");
				}
				return false;
			},
			"json"
			);
	});			
	$("button[name='reset']").bind("click",function(){
			$("input[name='userName']").val("");
			
		});
	$("a.del").bind("click",function(){
		var id = $(this).attr("ref");
		$.post("/userDel/",
			{id:id},
			function(data){
				if(data.status==1){
					$("#user_"+id).hide();
				}else{
					alert("删除失败");
				}
			},
			"json"
			);
	});
	//edit user
	$("font.edituser").bind("dblclick",function(){
		var text = $(this).text();
		var id = $(this).attr("name");
		$(this).html("<input name='userName' value='"+text+"'>");
		$("input[name='userName']").blur(function(){
			var title = $(this).val()
			$.post("/userEditName/",
				{id:id,userName:title}, 
				function(data){
					if(data.status==1 ){
						$("font.edituser[name='"+id+"']").text(title);
					}else{
						alert("操作失败");
					}
					return false;
				},
				"json"
				);
		});
	});
	$("select.edituser").change(function(){
		var id = $(this).attr("name");
		var host = $(this).val();
		$.post("/userEditHost/",
			{host:host,id:id},
			function(data){
				if(data.status==1){
					alert("修改主机成功");
				}else{
					alert("操作失败");
				}
				return false;
			},
			"json"
			);
	});
});
