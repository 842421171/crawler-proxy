#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: fatezero.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/5/27 23:03
version: 1.0
"""
from __future__ import annotations
from base import *
import time
from verify import *
from typing import List
import random


def parse_and_verify(html: str) -> bool | None:
    """
    get ip data
    :param html: source code
    :return: ip data
    """

    data = html.split('\n')

    if not len(data):
        return True

    data.pop(len(data) - 1)

    for d in data:
        d = eval(d)
        proxy = UseProxy(d['host'], d['port'], d['type'])
        logi(f'{proxy.dict()} 开始验证')
        if is_valided_proxy(proxy) and verify_ip_validity(proxy):
            logi(f'{proxy.dict()} 验证通过')
            add_proxy(proxy)
        else:
            logi(f'{proxy.dict()} 验证失败')


class FateZero:
    url = 'http://proxylist.fatezero.org/proxy.list'
    interval = 5

    def get_html(self, proxy: UseProxy | None) -> str | None:
        """
        get html source code
        :param proxy: proxy ip
        :param page: url param
        :return: html source code
        """
        proxies = None
        if proxy:
            logi(proxy.proxies())
            proxies = proxy.proxies()
        try:
            return get('http', url=self.url, proxies=proxies).text
        except Exception as ex:
            loge(ex)
            pass

    def crawler(self, proxies: List[UseProxy]) -> None:
        """
        save to file
        :param proxies: proxy list
        :return: None
        """
        proxy = None
        data_list = None
        count = 0
        while data_list is None:
            if len(proxies) > 0:
                proxy = random.sample(proxies, 1)[0]
            data_list = self.get_html(proxy)
            count += 1
            if data_list is None:
                logi(f'wait {self.interval} seconds, retry ...')
                time.sleep(self.interval)
            if count > 3:
                break
        parse_and_verify(data_list)
