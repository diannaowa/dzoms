
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
			var min = $("input[name='min']").val();
			var hour = $("input[name='hour']").val();
			var day = $("input[name='day']").val();
			var month = $("input[name='month']").val();
			var week = $("input[name='week']").val();
			var title = $("input[name='title']").val();
			var job = $("input[name='job']").val()
			var user = $("select[name='user']").val();
			var host = $("select[name='host']").val();
			if(min==""||hour==""||day==""||month==""||week==""||title==""||job==""||user==""||host==""){
				alert("请输入所有选项");
				return false;
			}
			$.post("/crontab/",
				{title:title,min:min,hour:hour,day:day,month:month,week:week,title:title,job:job,user:user,host:host},
				function(data){
					if(data.status==1){
						alert("计划任务添加成功");
					}else{
						alert("操作失败");
					}
					return false;
				},
				"json"
				);
		});
		$("a.del").bind("click",function(){
			var id = $(this).attr("ref");
			$.post("/crontabDel/",
				{id:id},
				function(data){
					alert(data.status);
				},
				"json"
				);
		});
});
