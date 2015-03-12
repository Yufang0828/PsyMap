<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<%@ include file="../_inc/header.jsp"%>

<%
    Integer statusCode = (Integer) request.getAttribute("javax.servlet.error.status_code");
    String message = (String) request.getAttribute("javax.servlet.error.message");
    String servletName = (String) request.getAttribute("javax.servlet.error.servlet_name");
    String uri = (String) request.getAttribute("javax.servlet.error.request_uri");
    Throwable t = (Throwable) request.getAttribute("javax.servlet.error.exception");
    if(t == null) {
        t = (Throwable) request.getAttribute("exception");
    }
    Class<?> exception = (Class<?>) request.getAttribute("javax.servlet.error.exception_type");
    String exceptionName = "";
    if (exception != null) {
        exceptionName = exception.getName();
    }
    if (statusCode == null) {
        statusCode = 0;
    }
    if (statusCode == 500) {
        LOGGER.error(statusCode + "|" + message + "|" + servletName + "|" + uri + "|" + exceptionName + "|" + request.getRemoteAddr(), t);
    }
    else if (statusCode == 404) {
        LOGGER.error(statusCode + "|" + message + "|" + servletName + "|" + uri + "|" + request.getRemoteAddr());
    }

    String queryString = request.getQueryString();
    String url = uri + (queryString == null || queryString.length() == 0 ? "" : "?" + queryString);
    url = url.replaceAll("&amp;", "&").replaceAll("&", "&amp;");

    if(t != null) {
        LOGGER.error("error", t);
    }
    
    String _pageTitle = "出错了~ 页面错误:" + statusCode;
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
			<%
		        if (statusCode == 404) {
		            out.println("对不起,暂时没有找到您所访问的页面地址,请联系管理员解决此问题.<br/><br/>");
		            out.println("<a href=\"" + url + "\">刷新,看看是否能访问了</a><br/>");
		        }
		        else {
		            out.println("对不起,您访问的页面出了一点内部小问题,请<a href=\"" + url + "\">刷新一下</a>重新访问,</br>或者先去别的页面转转,过会再来吧~<br/><br/>");
		        }
		    %>
		    <a href="javascript:void(0);" onclick="history.go(-1)">返回刚才页面</a><br/><br/>
		    </div>
     	</div>
     
		<%@ include file="../_inc/html-footer.jsp"%>
	</div>
	
</body>

</html>

<%!
    private static final org.slf4j.Logger LOGGER = org.slf4j.LoggerFactory.getLogger("DAILY_ALL");
%>