# -*- coding: utf-8 -*-
__author__ = 'AbyssViper'

import requests
from config import *
from utils import request_api

login = "/action/login"


# Login the router, return login data.
def login_route():
    data = {
        "username": USERNAME,
        "password": PASSWORD
    }

    return requests.post(request_api(login), data)


# Get new cookie by login again.
def get_cookie():
    response_header = login_route().headers
    if not response_header.get("Set-Cookie"):
        return None
    else:
        return response_header.get("Set-Cookie").split(";")[0]


# Get default cookie.
def get_default_cookie():
    return DEFAULT_COOKIE
