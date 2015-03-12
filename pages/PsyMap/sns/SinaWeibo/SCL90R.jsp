<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ include file="/WEB-INF/jsp/_inc/header.jsp"%>
<%
	String _pageTitle = "心理地图 - 基于社交网络的心理健康分析";
	String r = (String)request.getAttribute("SCL90R");
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
						我的<a href="http://en.wikipedia.org/wiki/Symptom_Checklist_90">心理健康</a>
					</h3>
					<h4>
						我们根据您的新浪微博，对您的心理健康进行了分析，得分如下：
					</h4>
					<span>得分范围为0~5分，分数越低心理健康程度越高</span>
					
					<ul>
						<li>抑郁（Depression）
							<span class="result" id="result-de">正在计算中…</span>
						</li>
						<li>焦虑（ Anxiety）
							<span class="result" id="result-an">正在计算中…</span>
						</li>
						<li>躯体化（Somatization）
							<span class="result" id="result-so">正在计算中…</span>
						</li>
						<li>强迫症状（Obsessive-Compulsive）
							<span class="result" id="result-oc">正在计算中…</span>
						</li>
						<li>人际关系敏感（Interpersonal sensitivity）
							<span class="result" id="result-is">正在计算中…</span>
						</li>
						<li>恐怖（ Photic anxiety）
							<span class="result" id="result-pa">正在计算中…</span>
						</li>
						<li>敌对（ Hostility）
							<span class="result" id="result-ho">正在计算中…</span>
						</li>
						<li>偏执（ Paranoid ideation）
							<span class="result" id="result-pi">正在计算中…</span>
						</li>
						<li>精神病性（ Psychoticism）
							<span class="result" id="result-ps">正在计算中…</span>
						</li>
						
					</ul>

					
					<div>
						<h4>
							通过微博分析您的其他心理特点
						</h4>
						<ul>
							<li>
	     						<a href="./SNSPsych/SinaWeibo/BigFive.do">查看我的人格分析</a>
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
					var r = result=<%=r%>;
					if(result){
						for(v in result){$('#result-'+v).html(String(result[v]).substr(0,6));}
						$(function () {
							$('#chart-container').highcharts({
					            chart: {
					                type: 'column'
					            },
					            title: {
					                text: '我的心理健康分析'
					            },
					            subtitle: {
					                text: '基于SCL90-R心理学测量量表'
					            },
					            xAxis: {
					                categories: ['抑郁', '焦虑', '躯体化', '强迫症状',
					                    '人际关系敏感', '恐怖', '敌对', '偏执', '精神病性']
					            },
					            yAxis: {
					                min: 0,
					                title: {
					                    text: '得分 (分数越低心理健康程度越高)'
					                }
					            },
					            tooltip: {
					                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
					                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
					                    '<td style="padding:0"><b>{point.y:.1f} 分</b></td></tr>',
					                footerFormat: '</table>',
					                shared: true,
					                useHTML: true
					            },
					            plotOptions: {
					                column: {
					                    pointPadding: 0.2,
					                    borderWidth: 0
					                }
					            },
					            series: [{
					                name: '大家的平均得分',
					                data: [1, 1, 1, 1, 1, 1, 1, 1, 1]
					    
					            }, {
					                name: '我的得分',
					                data: [r.de, r.an, r.so, r.oc, r.is, r.pa, r.ho, r.pi, r.ps]					    
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