# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, HttpResponseBadRequest
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage


@csrf_exempt
def api_wechat(request):
    # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    xml = request.body

    # 实例化 WechatBasic 并检验合法性
    wechat_instance = WechatBasic(token='CCPL')
    if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        return HttpResponseBadRequest('Verify Failed')

    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=xml)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')

    print xml

    message = wechat_instance.get_message()  # 获取解析好的微信请求信息
    ret = u'感谢关注“心理地图”！欢迎您登陆我们的网站：http://ccpl.psych.ac.cn/PsyMap/ (网站功能还在开发中，敬请期待。)' #message.type
    response = wechat_instance.response_text(ret)
    return HttpResponse(response)