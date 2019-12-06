# -*- coding: utf-8 -*-
__author__ = 'AbyssViper'

import requests
from utils import *
from api.authentication import get_default_cookie, get_cookie


# Get request header with base info.
def get_base_headers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": get_default_cookie()
    }

    status_code = requests.post(request_api(""), headers=headers).status_code
    if status_code == 302:
        headers["Cookie"] = get_cookie()

    return headers
