<%@ page language="java" pageEncoding="utf-8"
	import="java.util.*"
	import="ac.ccpl.psymap.bo.*"
%>
<%@ include file="/WEB-INF/jsp/_inc/header.jsp"%>
<%
	String _pageTitle = "心理地图 - 参加心理学实验 - 完成实验内容";
	
	Experiment exp = (Experiment)request.getAttribute("exp");
	Participant iU = (Participant)request.getAttribute("invitedUser");
	
	Map<String, List<UserFillQuiz>> ufqMap = (Map<String, List<UserFillQuiz>>)request.getAttribute("ufqMap");
	List<Quiz> lstQuiz = (List<Quiz>)request.getAttribute("lstQuiz");
	
	QGroup grp = exp.getQGroup();
	Date now = new Date();
	
	session.setAttribute("lastExpId", ""+exp.getExperimentId());
%>

<html>
<%@ include file="/WEB-INF/jsp/_inc/html-head.jsp"%>

<body>
<in-header-code>
	<style>
		.exp-c{
			width:80%;
			margin:auto;
			display:table;
		}
		.quiz-title{
			font-size: 22px;
			color: #333333;
			margin-bottom:5px;
		}
		.quiz-title:HOVER{
			color:#555555;
			text-decoration: none;
		}
		.red{
			font-style:inherit;
			color:red;
		}
	</style>
</in-header-code>
	<%@ include file="/WEB-INF/jsp/_inc/html-navbar.jsp"%>
	
   	<div class="hero-unit" style="padding-top:100px;"> 
		<img class="img-circle pull-right" src="./res/img/exp-3.png" style="width:500px;margin-top:-40px;"/>
		<h3>完成实验内容/填写问卷</h3>
		<h2>　　<%=exp.getName() %>
<%if(exp.getEndTime().before(now)){%>
			<span class="label label-important">该实验已结束。</span>
<%}else if(exp.getBeginTime().after(now)){%>
			<span class="label label-warning">实验尚未开始，敬请等待。</span>
<%}%>
		</h2>
		<span class="badge badge-info offset1">
			<i class="icon-time"></i>
			实验起止时间：
		</span>
		<span>
			【<%=exp.getBeginTime().toLocaleString() %> 至 <%=exp.getEndTime().toLocaleString() %>】
		</span>
		<hr/>
		<p>　　<%=exp.getDescription()%></p>
	</div>

   	<div class="container" style="padding-top:20px;" >
   	
   		<div class="exp-c">
<% int i=0, n = lstQuiz.size();%>
			<h2>请<i class="red">依次</i>填写完成下面的<i class="red">所有<%=n%>个</i>问卷</h2>
<%if(null==iU){%>
			<span class="badge badge-important"><i class="icon-info-sign"></i>温馨提示</span>实验报酬仅向邀请用户发放，您不在本次实验邀请之列，填写后不享受报酬；我们欢迎您继续填写完成下面的问卷，支持我们的科学研究。
<%}else{
	if(null==iU.getAgreeTime()){ %>
			<span class="badge badge-warning"><i class="icon-warning-sign"></i>提示信息</span>您尚未签署同意<a href="./Exp/Consent.do?ExpId=<%=exp.getExperimentId()%>">“知情同意书”</a>，请您签署同意之后再完成下列问卷，否则填写完成后不享受报酬。
	<%}else{ %>
			<span class="badge badge-success"><i class="icon-heart"></i>欢迎填写</span>您已于<%=iU.getAgreeTime().toLocaleString() %>签署同意了<a href="./Exp/Consent.do?ExpId=<%=exp.getExperimentId()%>">“知情同意书”</a>，欢迎您参加本实验，请完成下面所有的问卷。
	<%}
}
%>
   			<div>
				<ul>						
<%List<UserFillQuiz> lstUfqLast = null;
for(Quiz q : lstQuiz){
	String href = "./Quiz/Fill.do?grpId=" + grp.getQGroupId() + "&quizId=" + q.getQuizId();
%>
				<hr/>
					<li>
   						<a class="quiz-title" href="<%=href%>"><%=q.getScreenName()%></a>
		
	<%List<UserFillQuiz> ufqList = null;
	if(ufqMap!=null){
	 	ufqList = ufqMap.get(q.getQuizId());
	 	if(i>0)lstUfqLast = ufqMap.get(lstQuiz.get(i-1).getQuizId());
	}%>
   						<div class="btn-group pull-right">
	<%if(null!=ufqList && ufqList.size()>0){%>
							<button class="btn dropdown-toggle btn-success" data-toggle="dropdown">
								已填写过<%=ufqList.size() %>次<span class="caret"></span>
							</button>
							
							<ul class="dropdown-menu">
								<li><a>该问卷您已填过<%=ufqList.size() %>次，点击下面的<br/>填写时间可查看原填写结果的反馈。</a></li>
								<li class="divider"></li>
		<%for(UserFillQuiz ufq : ufqList){%>
								<li><a href="./Quiz/Result.do?fillId=<%=ufq.getFillId() %>">[<%=ufq.getFillTime().toLocaleString() %>] 的填写结果</a></li>
		<%}%>
								<li class="divider"></li>
								<li><a href="<%=href%>">再次填写</a></li>
							</ul>
	<%}else{
		if(i>0 && null==lstUfqLast){%>
							<a class="btn" onclick="alert('温馨提示：请先填写完成前面的问卷后再填写本问卷！');">请先填写完前面的问卷</a>
		<%}else{ %>
							<a class="btn btn-warning"  href="<%=href%>">马上填写</a>
		<%} %>
	<%} %>
						</div>
		
     					<div>　　<%=q.getIntro() %></div>
   					</li>
<%	i++;
}%>
					<hr/>
   				</ul>
			</div>
			
			<div class="btn-group" style="margin:auto; display:table;">
				<a class="btn btn-primary" href="./Exp/Experiment.do?ExpId=<%= exp.getExperimentId() %>">返回实验流程界面</a>
			</div>
			
   		</div>

		<%@ include file="/WEB-INF/jsp/_inc/html-footer.jsp"%>
	</div>
	
  	</body>
</html>