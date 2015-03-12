<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ include file="/WEB-INF/jsp/_inc/header.jsp"%>
<%
	String _pageTitle = "心理地图 - 请您登录";
%>

<html>
<%@ include file="/WEB-INF/jsp/_inc/html-head.jsp"%>

  
<body>
<in-header-code>
	<script language="javascript" type="text/javascript">
		function chk(){
			var login=$("#login").val();
			var pwd=$("#password").val();
			$.post("./Account/CommonLogin.do",{"login":login, "password":pwd},
			function(d){
				var msg=d.MSG;
				var sta=d.status;
				//alert(sta);
				switch(sta){
					case "f-login":
						alert(msg);
						
						break;
					case "s-login":
						alert(msg);
						break;
				}
			});
		}
	</script>
</in-header-code>
	<%@ include file="/WEB-INF/jsp/_inc/html-navbar.jsp"%>

	<div class="container">
		<div id="maincontent">
		
			<div class="container" style="padding-top:150px;">
				<div class="span3" style="padding:0 0px 0 50px;">
					<div style="margin:0 auto;display:table;">
						<h3>心理地图－登录</h3>
						<img class="img-circle" src="./res/img/c-a.png" style="width:140px; height:140px;margin-left:20px">
					</div>
					<hr/>
					<h4>欢迎您登录，登录之后您可以：</h4>
					<ul>
						<li>得到科学的的心理测评</li>
						<li>通过您的社交网络站点分析您与您的朋友的心理特征</li>
						<li>参与我们的心理学在线实验</li>
					</ul>
				</div>
								
				<div class="span7 container">
					<div class="hero-unit">
						<h4>使用您的社交网络账户连接登录<strong>心理地图</strong>。</h4>
<%if(null!=prevURL){%>
						<p>
							登录之后，您将跳转回到刚才的页面：<br/>
							<%=prevURL %>
						</p>
<%} %>	
					</div>
					
					<hr/>
					
					<div class="contianer" style="font-size:18px; line-height:30px; display:table; margin:0 auto;">
						<h2 class="form-signin-heading" align="center">请登录</h2>
						<div class="control-group">
							<div class="controls"> 
       							账号：<input id="login" type="text" class="input-large" placeholder="账号/邮箱" name="login">
       						</div>
       					</div>
       					<div class="control-group ">
       						<div class="controls">
								密码：<input id="password" type="password" class="input-large" placeholder="密码" name="password">
							</div>
						</div>
						<button class="btn btn-large btn-primary" onclick="chk()" type="submit">登录</button>
					</div>
					
					
					<hr/>
					
					<div>
						<br/><br/>我们遵照隐私条款保护您的隐私，您所填写的问卷、个人信息等，将只会用于进行科学研究。
					</div>
					
				</div>
     		</div>
     
        </div>
		
		<%@ include file="/WEB-INF/jsp/_inc/html-footer.jsp"%>
	</div>
	
</body>

</html>