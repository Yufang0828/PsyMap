<%@ page language="java" pageEncoding="utf-8"
	import="java.util.*"
	import="ac.ccpl.psymap.bo.*"
%>
<%@ include file="/WEB-INF/jsp/_inc/header.jsp"%>
<%
	String _pageTitle = "心理地图 - 参加心理学实验 - 查看和填写知情同意书";
	
	Experiment exp = (Experiment)request.getAttribute("exp");
	Participant iU = (Participant)request.getAttribute("invitedUser");
	Date now = new Date();

	String consentFile = "/WEB-INF/classes/quiz/consent/" + exp.getAgreementFile() + ".htm";
%>

<html>
<%@ include file="/WEB-INF/jsp/_inc/html-head.jsp"%>

<body>
<in-header-code>
	<script language="javascript" type="text/javascript">
	function chk(){
		var agr = $("#agr");
		var msg = '温馨提示：您必须要认真阅读并且同意“知情同意书"后方可参加实验。';
    	if (agr.attr("checked")){
			$.post("<%=basePath%>Exp/Accept.do",{"expId":<%=exp.getExperimentId()%>},function(d){
				var s = d.status;
				switch(s){
					case 'no-login':
						msg= "请您登录后再参加实验！" ;
						alert(msg);
						break;
					case 'no-invite':
						msg = "您好，您未被邀请参加本次实验，参与实验后不享受报酬；如果您愿意欢迎您继续填写问卷。\n\n\n点击“确认”在不享受报酬的情况下填写，否则点击“取消”。";
						if(confirm(msg)){
							window.location = "<%=basePath%>Exp/Show.do?ExpId=<%=exp.getExperimentId()%>";
						}else{
							return false;
						}
						break;
					case 'wrong-expid':
						msg= "请您正确操作，不要捣乱~" ;
						alert(msg);
						break;
					case 'success':
						msg = null;
						window.location = "<%=basePath%>Exp/Show.do?ExpId=<%=exp.getExperimentId()%>";
						break;
				}
			});
		}else{
    		alert(msg);
			agr.focus();
		}
	}
	</script>

	<style>
		.exp-c{
			width:70%;
			margin:auto;
			display:table;
		}
	</style>
</in-header-code>
	<%@ include file="/WEB-INF/jsp/_inc/html-navbar.jsp"%>
	
   	<div class="hero-unit" style="padding-top:100px;"> 
		<img class="img-circle pull-right" src="./res/img/exp-2.png" style="width:500px;margin-top:-40px;"/>
		<h3>查看和填写“知情同意书”</h3>
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

   	<div class="container" style="padding-top:30px;" >
   		<div>
   			<h2>知情同意书</h2>
			<hr/>
			
   			<jsp:include page="<%=consentFile %>"></jsp:include>
   		
   			<hr/>

<%if(null!=iU && null!=iU.getAgreeTime()){%>
			<span class="badge badge-success"><i class="icon-check"></i>提示</span>您已于<%=iU.getAgreeTime().toLocaleString() %>签署同意了本“知情同意书”，在本页勾选和点击“同意”按钮的效力等同于填写纸质“知情同意书”。<br/><br/>
			<a class="btn btn-success offset1" href="./Exp/Show.do?ExpId=<%=exp.getExperimentId()%>">　转到问卷填写页面　</a>　　
			<a class="btn btn-warning" href="./Exp/Experiment.do?ExpId=<%=exp.getExperimentId()%>">　返回实验流程页面　</a>
<%}else{%>
			<fieldset>
				<label class="checkbox">
					<input id="agr" type="checkbox"/>我已阅读并同意<strong>心理测试知情协议</strong>，并且知晓在本页勾选和点击“同意”按钮的效力等同于填写纸质“知情同意书”。
				</label>
				<button class="btn btn-success offset1" onclick="chk()">　同意　</button>
				<a class="btn btn-warning" href="./Exp/Experiment.do?ExpId=<%=exp.getExperimentId()%>">　返回　</a>
			</fieldset>
<%}%>   			
   		</div>

		<%@ include file="/WEB-INF/jsp/_inc/html-footer.jsp"%>
	</div>
	
  	</body>
</html>
