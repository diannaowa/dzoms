
$(document).ready(function(){
		$("select[name='host']").change(function(){
			var host = $(this).val();
			if(host!=""){
				$.get("/getUserByHost/",
					{host:host},
					function(data){
						var html = "<option value=''>选择用户</option>";
						$.each(data,function(k,v){
							html += "<option value='"+v.id+"'>"+v.userName+"</option>";
							$("select[name='user']").html(html);
						});
					},
					"json"
					);
			}
		});
		$("button[name='commit']").bind("click",function(){
			var title = $("input[name='title']").val();
			var path = $("input[name='path']").val();
			var host = $("select[name='host']").val();
			var user = $("select[name='user']").val();
			var content = $("textarea[name='content']").val();
			if(title=="" || path=="" || host=="" || user=="" || content==""){
				alert("请输入完整信息");
				return false;
			}
			$.post("/createScript/",
				{title:title,path:path,host:host,user:user,content:content},
				function(data){
					if(data.status==1){
						alert("脚本添加并上传至远程机");
					}
					else{
						alert("操作失败");
					}
					return false;
				},
				"json"
				);
		});

		$("a.del").bind("click",function(){
			var id = $(this).attr("ref");
			$.post("/scriptDel/",
				{id:id},
				function(data){
					if(data.status==1){
						$("#script_"+id).hide();
					}
					else{
						alert('操作失败');
					}
				},
				"json"
				);
			return false;		
		});
});
