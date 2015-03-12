<%@ page language="java"
	pageEncoding="utf-8"
	import="java.util.*"
	import="ac.ccpl.psymap.bo.*"
	import="ac.ccpl.psymap.util.*"
%>
<%@ include file="../_inc/header.jsp"%>
<%
	String _pageTitle = "连接成功！";
	
	String redirectURL = basePath+"./Home/Index.do";
	if(null!=prevURL)	redirectURL = prevURL;
%>

<html>
<%@ include file="../_inc/html-head.jsp"%>
  
<in-header-code>
	<style>
		.txt{
            color:#E21F03;
            font-size:1.4em;
            line-height:1.7em;
            margin:150px 0 0 180px;
        }
        #maincontent{
		    width:900px;
			height:520px;
			margin-left:32px;
			padding: 30px 30px 15px 30px;
		}
	</style>
</in-header-code>
  
<body>
	
	<%@ include file="/WEB-INF/jsp/_inc/html-navbar.jsp"%>

	<div class="container">
	
		<div id="maincontent">
			<div class="txt">
				<img src="./res/img/logo_<%=olU.getSiteType().toLowerCase()%>.jpg">
				<p>连接登录<%=SiteName%>>>>></p>

				<p>您已经成功用<%=SiteName%>账户连接心理地图，我们正在为您跳转页面！</p>

				正在为您进行页面跳转，请稍等……<br />
				如果页面没有及时跳转，请您点击<a href="<%=redirectURL%>">这里</a>进行跳转。
<script type="text/javascript">
 <!-- //
    function redirect() {
        window.location = "<%=redirectURL%>";
    }
    window.setTimeout("redirect()",1000 * 2);
 // -->
</script>
     </div>
     
            </div>

		
		
		<%@ include file="../_inc/html-footer.jsp"%>
	</div>
	
</body>

</html>