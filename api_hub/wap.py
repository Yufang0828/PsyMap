# coding=utf-8
from api_hub.request import Request


class ClientBase(Request):
    def __init__(self):
        super(ClientBase, self).__init__()
