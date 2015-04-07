# coding=utf-8
from api_hub.exceptions import ApiResponseError
from api_hub.open import *


class OAuth2(OAuth2Base):
    AUTH_URL = 'https://www.douban.com/service/auth2/auth'
    TOKEN_URL = 'https://www.douban.com/service/auth2/token'

    def _parse_token(self, response):
        r = response.json_dict()
        if 'code' in r and 'msg' in r:
            raise ApiResponseError(response, r.code, r.msg)
        return Token(**r)