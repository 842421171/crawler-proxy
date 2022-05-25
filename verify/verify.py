#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: verify.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/3/2 22:01
version: 1.0
"""
from __future__ import annotations
from base import *
from datetime import datetime
import json
import time


def verify(method: str, proxy: UseProxy) -> str | None:
    """
    verify proxy
    :param method: request method
    :param proxy: verify proxy
    :return: verify result
    """
    if method == 'http':
        return verify_http(proxy)
    elif method == 'https':
        return verify_https(proxy)


def verify_http(proxy: UseProxy) -> str | None:
    """
    verify http proxy
    :param proxy:
    :return: verify result
    """
    # url = 'http://proxy.seofangfa.com/checkproxy/'
    # url = 'http://httpbin.org/ip'
    # url = 'http://httpbin.org/headers'
    # url = 'http://icanhazip.com/'
    url = 'http://httpbin.org/get?show_env=1'
    proxies = None
    if proxy:
        logi(proxy.proxies())
        proxies = proxy.proxies()
    try:
        return get('http', url, proxies=proxies).text
    except Exception as ex:
        loge(ex)
        pass


def verify_https(proxy: UseProxy) -> str | None:
    """
    verify https proxy
    :param proxy:
    :return: verify result
    """
    # url = 'https://httpbin.org/ip'
    url = 'https://httpbin.org/get?show_env=1'
    proxies = None
    if proxy:
        logi(proxy.proxies())
        proxies = proxy.proxies()
    try:
        return get('https', url, proxies=proxies, verify=False).text
    except Exception as ex:
        loge(ex)
        pass


def verify_ip_validity(proxy: UseProxy) -> bool:
    protocol = proxy.protocol.lower()
    try:
        content = verify(protocol, proxy)
        if content is None:
            return False
        if json.loads(content)['origin'].find(',') == -1:
            proxy.anonymity = '匿名'
        else:
            proxy.anonymity = '透明'
        return True
    except Exception as ex:
        loge(ex)
        return False
