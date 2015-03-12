<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ include file="../_inc/header.jsp"%>
<%
	String _pageTitle = "连接失败……";
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
	
	<%@ include file="../_inc/html-navbar.jsp"%>

	<div class="container">
	
		<div id="maincontent">
			<div class="txt">
				<p>
					连接<%=SiteName%>登陆失败……
				</p>

				<p>请您稍后尝试，或者联系我们查找错误原因。</p>

<script type="text/javascript">
 <!-- //
    function redirect() {
        window.location = "<%=basePath%>";
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