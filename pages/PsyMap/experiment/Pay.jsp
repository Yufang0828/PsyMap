<%@ page language="java" pageEncoding="utf-8"
	import="java.util.*"
	import="ac.ccpl.psymap.bo.*"
%>
<%@ include file="/WEB-INF/jsp/_inc/header.jsp"%>
<%
	String _pageTitle = "心理地图 - 参加心理学实验 - 报酬信息";
	
	Experiment exp = (Experiment)request.getAttribute("exp");
	Participant iU = (Participant)request.getAttribute("invitedUser");
	
	long inviteId = -1;
	if(null!=iU)
		inviteId = iU.getParticipantId();
	
	Date now = new Date();
%>

<html>
<%@ include file="/WEB-INF/jsp/_inc/html-head.jsp"%>

<body>
<in-header-code>
	<script language="javascript" type="text/javascript">
	function chk(){
		var t = $("#info1").val();
		var t1 = $("#info2").val();
		
		if(t!=t1){
			alert("请正确填写支付信息：两次的填写必须一致！");
			return false;
		}
		
		if(!t && t.trim()==""){
			alert("请正确填写支付信息：填写信息不能为空！");
			return false;
		}
		
		if(0><%=inviteId%>){
			alert("您好，您不在受邀请范围之列，填写问卷不享受报酬！（知情同意书中已有详尽说明。）");
			return false;
		}
		
		if(!confirm("请确认您要提交的支付信息："+ t +"。\n\n\n温馨提示：支付信息只能提交一次，提交后不能修改，您确认提交吗？"))
			return false;
		
		$.post("./Exp/Pay.do",{"expId":<%=exp.getExperimentId()%>,"info":t},function(d){
			var s = d.status;
			switch(s){
				case 'no-login':
					msg= "请您登录后再填写！" ;
					alert(msg);
					break;
				case 'no-invite':
					msg = "您好，您不在受邀请范围之列，填写问卷不享受报酬！（知情同意书中已有详尽说明。）";
					alert(msg);
					break;
				case 'wrong-expid':
					msg= "请您正确操作，不要捣乱~" ;
					alert(msg);
					break;
				case 'success':
					msg = "您已成功填写支付信息：" + d.info;
					alert(msg);
					window.location.reload();
					break;
				case 'already-filled':
					msg = "您之前已填写过支付信息：" + d.info + "。\n为保证用户填写信息安全，填写过的支付信息不得再修改，如有问题请通过微博与我们联系。";
					alert(msg);
					break;
			}
		});
	}
	</script>

	<style>
		.exp-c{
			width:70%;
			margin:auto;
			display:table;
		}
		
		.txt, .txt li{
			font-size: 18px;
			line-height: 30px;
		}
	</style>
</in-header-code>
	<%@ include file="/WEB-INF/jsp/_inc/html-navbar.jsp"%>
	
   	<div class="hero-unit" style="padding-top:100px;"> 
		<img class="img-circle pull-right" src="./res/img/exp-4.png" style="width:500px;margin-top:-40px;"/>
		<h3>查看和填写报酬和支付信息</h3>
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

   	<div class="container" style="padding-top:10px;" >
   		<div>
   			<h3>报酬查看和领取须知：</h3>
   			<ol class="txt">
   				<li>在填写支付信息前，必须已经仔细阅读并同意知情同意书，且已经完成所有实验内容，否则即使填写支付信息，也不享受报酬；报酬一般只向邀请用户发放，或者是向抽奖抽中的用户发放，具体以知情同意书中的说明为准。</li>
   				<li>“知情同意书”当中对报酬支付的详细信息，包括支付途径、数额等进行了描述，报酬发放一般只针对邀请用户，如有特殊说明，如“抽奖”等情况，则以“知情同意书”为准。</li>
   				<li>报酬的支付工作，需要在实验全部结束以后再进行，并且我们的工作人员会对用户实验完成的质量进行审核，不认真完成实验、填写问卷的用户，不享受报酬。</li>
   				<li>为保证用户填写信息安全，不被篡改，<span class="badge badge-important">支付信息只允许填写一次，填写后不得再修改</span>，所以在填写之前请务必仔细确认填写正确；确有需要修改的情况，请通过我们的新浪微博私信给我们。</li>
   				<li>因用户填写错误导致的支付失败，责任由用户承担，我们不重复发放报酬。</li>
   				<li style="color:red;">
   					“报酬支付信息”需要填写的内容在<a target="_blank" href="./Exp/Consent.do?ExpId=<%=exp.getExperimentId()%>">“知情同意书”</a>当中有详细说明，一般是：
   					<ul>
   						<li>手机号码（充值号码类型[移动|联通|电信]请严格按照“知情同意书”当中的说明填写，填写不支持的运营商号码将得不到报酬）</li>
   						<li>站点用户UID（例如新浪微博、人人网、豆瓣网的用户ID）</li>
   						<li>其他，以“知情同意书”说明为准</li>
   					</ul>
   				</li>
   			</ol>
			<hr/>
			
			<div style="margin:auto; display:table;">
<%if(null!=iU.getPayInfo()){ %>
				<fieldset>
					<label class="text">
						您已经成功填写了如下的支付信息，如果报酬还未发放，敬请耐心等待，或通过我们的微博关注我们的报酬发放动态。<br/>
						您于<%=iU.getPayInfoUpdated().toLocaleString() %>填写的支付信息　<span class="input-xlarge uneditable-input"><%=iU.getPayInfo() %></span>
					</label>
					<a class="btn btn-warning" href="./Exp/Experiment.do?ExpId=<%=exp.getExperimentId()%>">　返回　</a>
				</fieldset>
<%}else{ %>
				<fieldset>
					<label class="text">
						填写报酬支付支付信息：
						<input id="info1" type="text"/>
					</label>
					<label class="text">
						确认报酬支付支付信息：
						<input id="info2" type="text"/>
					</label>
					<button type="submit" class="btn btn-success offset1" onclick="chk()">　确认提交　</button>
					<a class="btn btn-warning" href="./Exp/Experiment.do?ExpId=<%=exp.getExperimentId()%>">　返回　</a>
				</fieldset>
<%} %>
			</div>
			<div style="clear:both;"></div>
			
			
   		</div>
		<%@ include file="/WEB-INF/jsp/_inc/html-footer.jsp"%>
	</div>
	
  	</body>
</html>
