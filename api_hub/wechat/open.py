# coding=utf-8
from api_hub.open import OAuth2Base, Token, App
from api_hub.exceptions import ApiResponseError

App = App

def parse(response):
    r = response.json_dict()
    if 'error_code' in r:
        raise ApiResponseError(response, r.error_code, r.get('error', ''))
    return r

class OAuth2(OAuth2Base):
    BASE_URL = 'https://api.weixin.qq.com/sns/oauth2/'
    TOKEN_URL = BASE_URL + 'access_token'

    def _parse_token(self, response):
        data = parse(response)
        return Token(**data)
