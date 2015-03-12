<%@ page language="java" pageEncoding="utf-8"
import="java.util.*" 
import="java.lang.reflect.*"
%>
<%@ include file="../_inc/header.jsp"%>
<%
	String _pageTitle = "心理地图 - 后台管理";
%>

<html>
<%@ include file="/WEB-INF/jsp/_inc/html-head.jsp"%>

<body>
<in-header-code>
	<style>
		.table *{
			white-space:normal;
			word-break:break-all;
			word-wrap:break-word;
		}
	</style>
</in-header-code>
	<%@ include file="/WEB-INF/jsp/_inc/html-navbar.jsp"%>

	<div class="container">
		<div id="maincontent">
		
			<div class="container" style="padding-top:150px;">
			
				<div class="page-header">
  					<img class="pull-right" src="./res/ico/logo_57by57.png"/>
  					<h1>心理地图后台管理</h1>
				</div>
				
				<div class="container">
  					<h3>参数查看</h3>
  					<hr/>
  					
  					<table class="table table-striped table-bordered table-hover table-condensed">
  						<caption>参数</caption>
						<thead>
							<tr>
								<th>参数名称</th>
								<th>参数值</th>
							</tr>
						</thead>
						
						<tbody>
						
<% Field[] ff = Constants.class.getFields();
for (Field f : ff){%>
							<tr>
								<td><%=f.getName() %></td>
								<td><%=f.get(f) %></td>
							</tr>
<%} %>
						</tbody>
						
					</table>


				</div>
			
     		</div>
     		
        </div>
        
		<%@ include file="/WEB-INF/jsp/_inc/html-footer.jsp"%>
	</div>
	
</body>

</html>