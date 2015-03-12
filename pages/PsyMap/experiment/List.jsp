<%@ page language="java" pageEncoding="utf-8"
	import="java.util.*"
	import="ac.ccpl.psymap.bo.*"
%>
<%@ include file="/WEB-INF/jsp/_inc/header.jsp"%>
<%
	String _pageTitle = "心理地图 - 参加心理学实验";
	Map<Experiment,List<Quiz>> mapExp =
		(Map<Experiment,List<Quiz>>)request.getAttribute("mapExp");
%>

<html>
<%@ include file="/WEB-INF/jsp/_inc/html-head.jsp"%>

<body>
	<%@ include file="/WEB-INF/jsp/_inc/html-navbar.jsp"%>

	<div class="container">
		<div id="maincontent">
		
			<div class="container" style="padding-top:150px;">
				<div class="span3" style="padding:0 0px 0 50px;">
				
					
					<h3>
						心理学实验平台
					</h3>
					<h4>
						“心理地图”应用在提供科学的心理状况评估的同时，也将作为一个邀请心理学被试用户填写问卷调查的平台，为与心理学相关的研究提供数据支持和服务，希望您支持我们的研究。
					</h4>
					<span>如果您也想在“心理地图”上发布您的心理实验，欢迎通过<a href="http://weibo.com/u/2721210291">我们的微博</a>联系我们。</span>
					
				</div>
								
				<div class="span7">
				
<%
					for(Experiment exp : mapExp.keySet()){
					List<Quiz> lstQuiz = mapExp.get(exp);
				%>
					<div class="hero-unit">
						<h3><%=exp.getName() %></h3>
						<h4><%=exp.getDescription() %></h4>
						<ul>
						
	<%for(Quiz q : lstQuiz){%>
							<li>
	     						<a href="./Quiz/Fill.do?grpId=<%=exp.getQGroup().getQGroupId() %>&quizId=<%=q.getQuizId()%>"><%=q.getScreenName()%></a>
	     					</li>
	<%}%>
	     				</ul>
					</div>
<%}%>
				
				
				
				</div>
				
     		</div>
        </div>
		
		<%@ include file="/WEB-INF/jsp/_inc/html-footer.jsp"%>
	</div>
	
</body>

</html>