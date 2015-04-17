
$(document).ready(function(){
	$("button[name='commit']").bind("click",function(){
		var category = $("input[name='category']").val();
		var cname = $("input[name='cname']").val();
		if(category==""||cname==""){
			alert("Plz input category name!~");
			return false;
		}
		$.post("/hostCategory/",
			{title:category,cname:cname},
			function(data){
				if(data.status==1){
					alert("分类添加成功");
				}
				return false;
			},
			"json"
			);
	});			
	$("button[name='reset']").bind("click",function(){
			$("input[name='category']").val("");
			$("input[name='cname']").val("");
			
		});
	$("a.del").bind("click",function(){
		var id = $(this).attr("ref");
		$.post("/hostCategoryDel/",
			{id:id},
			function(data){
				if(data.status==1){
					$("#category_"+id).hide();
				}else{
					alert("删除失败");
				}
			},
			"json"
			);
	});
	//host
	$("button[name='hostcommit']").bind("click",function(){
		var title = $("input[name='hosttitle']").val();
		var ip = $("input[name='ip']").val();
		var position = $("input[name='position']").val();
		var os = $("input[name='os']").val();
		var sudo = $("input[name='sudo']").val();
		var passwd = $("input[name='passwd']").val();
		var port = $("input[name='port']").val();
		var category = $("select[name='category']").val();
		if(ip == ""){
			alert("情输入主机IP!");
			return false;
		}
		if(category == ""){
			alert("请选择主机所属分类");
			return false;
		}
		$.post("/host/",
			{title:title,ip:ip,position:position,os:os,category:category,sudo:sudo,passwd:passwd,port:port},
			function(data){
				if(data.status==1){
					alert("主机添加成功");
				}else{
					alert("操作失败");
				}
				return false;
			},
			"json"
			);
	});
	$("a.hostdel").bind("click",function(){
		var id = $(this).attr("ref");
		alert(id);
		$.post("/hostdel/",
			{id:id},
			function(data){
				if(data.status==1){
					$("#host_"+id).hide();
				}else{
					alert("删除失败");
				}
			},
			"json"
			);
	});
	$("font.hostedit").bind("dblclick",function(){
		var id = $(this).attr("id");
		var text = $(this).text();
		var name = $(this).attr("name")
		$("input[name='"+name+"_"+id+"']").remove();
		$(this).html("<input style='height:22px; border:1px #ccc; width:100px;' name='"+name+"_"+id+"' value='"+text+"'/>");
		$("input[name='"+name+"_"+id+"']").focus();
		$("input[name='"+name+"_"+id+"']").blur(function(){
			var title = $("input[name='title_"+id+"']").val();
			var ip = $("input[name='ip_"+id+"']").val();
			var os = $("input[name='os_"+id+"']").val();
			var position = $("input[name='position_"+id+"']").val();
			var sudo = $("input[name='sudo_"+id+"']").val();
			var passwd = $("input[name='passwd_"+id+"']").val();
			var port = $("input[name='port_"+id+"']").val();
			var text2 = $(this).val()
			$.post("/hostedit/",
				{id:id,title:title,ip:ip,os:os,position:position,sudo:sudo,passwd:passwd,port:port},
				function(data){
					if(data.status==1){
						$("font.hostedit[name='"+name+"'][id='"+id+"']").html(text2).append("<input type='hidden' value='"+text2+"' name='"+name+"_"+id+"' >");
					}
				},
				"json"
				);
		});
	});
	$("select.editcategory").change(function(){
		var id = $(this).attr("name");
		var category = $(this).val();
		$.post("/hosteditc/",
			{id:id,category:category},
			function(data){
				if(data.status==1){
					alert("修改分类成功");
				}else{
					alert("失败");
				}
				return false;
			},
			"json"
			);
	});
	//edit category
	$("font.editcategory").bind("dblclick",function(){
		var text = $(this).text();
		var id = $(this).attr("name");
		$(this).html("<input name='title' value='"+text+"'>");
		$("input[name='title']").blur(function(){
			var title = $(this).val()
			$.post("/hostCategoryEdit/",
				{id:id,title:title},
				function(data){
					if(data.status==1){
						$("font.editcategory[name='"+id+"']").text(title);
					}else{
						alert("操作失败");
					}
					return false;
				},
				"json"
				);
		});
	});
	//edit category2
	$("font.editcname").bind("dblclick",function(){
		var text = $(this).text();
		var id = $(this).attr("name");
		$(this).html("<input name='cname' value='"+text+"'>");
		$("input[name='cname']").blur(function(){
			var cname = $(this).val()
			$.post("/hostCategoryEdit2/",
				{id:id,cname:cname},
				function(data){
					if(data.status==1){
						$("font.editcname[name='"+id+"']").text(cname);
					}else{
						alert("操作失败");
					}
					return false;
				},
				"json"
				);
		});
	});
	//host monitoring
	$("input[name='hostM']").bind("click",function(){
		var val = 0;
		var id = $(this).attr("id");
		if($(this).attr("checked")=="checked"){val=1;}
		$.post("/hostM/",
			{id:id,val:val},
			function(data){
				if(data.status == 1){
					alert("操作成功");
				}else{
					alert("操作失败");
				}
				return false;
			},
			"json"
			);
	});
});
