<%@ page language="java" pageEncoding="utf-8"
	import="java.util.*"
	import="ac.ccpl.psymap.bo.*"
%>
<%@ include file="/WEB-INF/jsp/_inc/header.jsp"%>
<%
	String _pageTitle = "心理地图 - 心理学实验平台";
	Map<Experiment,List<Quiz>> mapExp =
		(Map<Experiment,List<Quiz>>)request.getAttribute("mapExp");
%>

<html>
<%@ include file="/WEB-INF/jsp/_inc/html-head.jsp"%>

<body>
	<in-header-code>
		<style>
			.exp-container{
			 	margin:0 5px 15px 5px;
			 	padding-bottom:15px;
			}
			.exp-thumbnail{
		 		padding:20px 50px 60px 50px;
			}
			.row{
				margin:auto;
				display:table;
			}
		</style>
	</in-header-code>
	
	<%@ include file="/WEB-INF/jsp/_inc/html-navbar.jsp"%>
	
	<div class="hero-unit" style="padding-top:100px;"> 
		<img class="img-circle pull-right" src="./res/img/c-c.png" style="margin-top:-100px;"/>
		<h2>心理学实验平台</h2>
		<p><br/>　　“心理地图”应用在提供科学的心理状况评估的同时，也将作为一个邀请心理学被试用户填写问卷调查的平台，为与心理学相关的研究提供数据支持和服务，希望您支持我们的科学研究。</p>
		<small>　　如果您也想在“心理地图”上发布您的心理实验，欢迎通过<a target="_blank" href="http://weibo.com/u/2721210291">我们的微博</a>联系我们。</small> 
	</div> 

	<div class="container" style="margin-top:135px;">
		<div class="row">
				
<%
					for(Experiment exp : mapExp.keySet()){
					List<Quiz> lstQuiz = mapExp.get(exp);
					int i=0;
					String desc = exp.getDescription();
					if(desc.length()>40)
						desc = desc.substring(0, 40) + "……";
				%>
					<div class="span6 exp-container container">
						<div class="thumbnail exp-thumbnail">
							<h3><%=exp.getName() %></h3>
							<hr/>
							<h4>　　<%=desc %><small>[共<%=lstQuiz.size() %>个问卷]</small></h4>
							<ul>
	<%for(Quiz q : lstQuiz){
		if(++i>4){
	%>
								<li>
									<span>……</span>
		     					</li>
	<%
			break;
		}%>
								<li>
									<span><%=q.getScreenName()%></span>
		     					</li>
	<%}%>
		     				</ul>
		     				<a class="btn btn-success pull-right" type="button" href="./Exp/Experiment.do?ExpId=<%=exp.getExperimentId() %>">了解更多»</a>
						</div>
					</div>
<%}%>
				
		</div>
		<%@ include file="/WEB-INF/jsp/_inc/html-footer.jsp"%>
				
	</div>
		
	
</body>

</html>