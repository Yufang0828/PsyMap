<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ include file="/WEB-INF/jsp/_inc/header.jsp"%>
<%
	String _pageTitle = "心理地图 - 基于社交网络的人格分析";
	String r = (String)request.getAttribute("BigFive");
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
						<img src="./res/img/logo_weibo.png">
						我的<a href="http://zh.wikipedia.org/wiki/%E4%BA%94%E5%A4%A7%E6%80%A7%E6%A0%BC%E7%89%B9%E8%B4%A8">大五人格</a>
					</h3>
					<h4>
						我们根据您的新浪微博，对您的人格进行了分析，得分如下：
					</h4>
					<span>得分范围为0~5分</span>
					
					<ul>
						<li>怡人性（Agreeableness）
							<span class="result" id="result-A">正在计算中…</span>
						</li>
						<li>尽责行（Conscientiousness）
							<span class="result" id="result-C">正在计算中…</span>
						</li>
						<li>外向性（Extraversion）
							<span class="result" id="result-E">正在计算中…</span>
						</li>
						<li>神经质（Neuroticism）
							<span class="result" id="result-N">正在计算中…</span>
						</li>
						<li>开放性（ Openness）
							<span class="result" id="result-O">正在计算中…</span>
						</li>
					</ul>

					
					<div>
						<h4>
							通过微博分析您的其他心理特点
						</h4>
						<ul>
							<li>
	     						<a href="./SNSPsych/SinaWeibo/SCL90R.do">查看我的心理健康分析</a>
	     					</li>
	     				</ul>
	     			</div>
					
				</div>
								
				<div class="span6">
					<div id="chart-container" style="width: 700px; height: 400px; margin: 0 auto"></div>
				</div>
			
				
				<script src="./res/js/chart/highcharts.js"></script>
				<script src="./res/js/chart/highcharts-more.js"></script>
				<script src="./res/js/chart/modules/exporting.js"></script>
				<script type="text/javascript">
					var result=<%=r%>;
					if(result){
						for(v in result){$('#result-'+v).html(String(result[v]).substr(0,6));}
						$(function () {
							$('#chart-container').highcharts({
							            
							    chart: {
							        polar: true,
							        type: 'line'
							    },
							    
							    title: {
							        text: '我的大五人格',
							    },
							    
							    pane: {
							    	size: '85%'
							    },
							    
							    xAxis: {
							        categories: ['怡人性', '尽责性', '外向性', '神经质', '开放性'],
							        tickmarkPlacement: 'on',
							        lineWidth: 0
							    },
							        
							    yAxis: {
							        gridLineInterpolation: 'polygon',
							        lineWidth: 0,
							        min: 0
							    },
							    
							    tooltip: {
							    	shared: true,
							        pointFormat: '<span style="color:{series.color}">{series.name}: <b>越向外分数越大</b><br/>'
							    },
							    
							    legend: {
							        align: 'middle',
							        verticalAlign: 'middle',
							        x: 240,
							        y: 170,
							        layout: 'horizontal'
							    },
							    
							    series: [{
							        name: '我的得分',
							        data: [result.A, result.C, result.E, result.N, result.O],
							        pointPlacement: 'on'
							    }, {
							        name: '大家的平均分',
							        data: [3, 3, 3, 3, 3],
							        pointPlacement: 'on'
							    }]
							
							});
						});
					}else{
						for(v in result){$('#result-'+v).html('没算出来…');}
					}
					
				</script>
     		</div>
     
        </div>
		
		<%@ include file="/WEB-INF/jsp/_inc/html-footer.jsp"%>
	</div>
	
</body>

</html>