#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: requestsutil.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/3/9 14:38
version: 1.0
"""
from __future__ import annotations
import requests
from fake_useragent import UserAgent
import urllib3
from base.utils.log import *


def get(method: str, url: str, proxies: dict | None = None, timeout: int = 300, verify: bool = True,
        cert: str | None = None) -> requests.Response:
    """
    get request
    :param method: http/https
    :param url: request url
    :param proxies: request proxies info
    :param timeout: request timeout
    :param verify: https varify cert
    :param cert: cert path
    :return: response
    """
    headers = {}
    try:
        headers['user-agent'] = UserAgent(use_cache_server=False, path='base/utils/useragent0.1.11.json').random
    except Exception as ex:
        loge(ex)
    logi(headers)
    if method == 'http':
        return get_http(url, headers, proxies, timeout)
    elif method == 'https':
        return get_https(url, headers, proxies, timeout, verify, cert)


def get_http(url: str, headers: dict | None = None, proxies: dict | None = None, timeout: int = 300) -> requests.Response:
    """
    get http request
    :param url: request url
    :param headers: request headers info
    :param proxies: request proxies info
    :param timeout: request timeout
    :return: response
    """
    return requests.get(url=url, headers=headers, proxies=proxies, timeout=timeout)


def get_https(url: str, headers: dict | None = None, proxies: dict | None = None, timeout: int = 300, verify: bool = True,
              cert: str | None = None) -> requests.Response:
    """
    get https request
    :param url: request url
    :param headers: request headers info
    :param proxies: request proxies info
    :param timeout: request timeout
    :param verify: https verify cert
    :param cert: cert path
    :return: response
    """
    # 去除警告
    urllib3.disable_warnings()
    return requests.get(url=url, headers=headers, proxies=proxies, timeout=timeout, cert=cert,
                        verify=verify)
