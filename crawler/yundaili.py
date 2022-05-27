#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: yundaili.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/5/25 23:25
version: 1.0
"""
from __future__ import annotations
import random
from typing import List
from base import *
from bs4 import BeautifulSoup
import time
from verify import *


def parse_and_verify(html: str) -> None:
    """
    get ip data
    :param html: source code
    :return: ip data
    """
    bs = BeautifulSoup(html, 'lxml')

    ip_elements = bs.select('#list > table > tbody > tr > td:nth-child(1)')
    port_elements = bs.select('#list > table > tbody > tr > td:nth-child(2)')
    protocol_type_elements = bs.select('#list > table > tbody > tr > td:nth-child(4)')

    ips = [ip.get_text() for ip in ip_elements if ip.get_text()]
    ports = [port.get_text() for port in port_elements]
    protocol_types = [protocol_type.get_text() for protocol_type in protocol_type_elements]

    for ip, port, protocol_type in zip(ips, ports, protocol_types):
        proxy = UseProxy(ip, port, protocol_type)
        logi(f'{proxy.dict()} 开始验证')
        if is_valided_proxy(proxy) and verify_ip_validity(proxy):
            logi(f'{proxy.dict()} 验证通过')
            add_proxy(proxy)
        else:
            logi(f'{proxy.dict()} 验证失败')


class YunDaiLi:
    url = 'http://www.ip3366.net/?stype={stype}&page=1'
    interval = 5

    # def get_html(self, proxy: UseProxy | None, stype: int) -> str | None:
    def get_html(self, proxy: UseProxy | None, stype: int) -> str | None:
        """
        get html source code
        :param proxy: proxy ip
        :param stype: url param
        :return: html source code
        """
        proxies = None
        if proxy:
            logi(proxy.proxies())
            proxies = proxy.proxies()
        try:
            return get('http', url=self.url.format(stype=stype), proxies=proxies).content.decode('gb2312')
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
        html = None
        for stype in range(1, 6):
            count = 0
            while html is None:
                if len(proxies) > 0:
                    proxy = random.sample(proxies, 1)[0]
                html = self.get_html(proxy, stype)
                count += 1
                if html is None:
                    logi(f'wait {self.interval} seconds, retry ...')
                    time.sleep(self.interval)
                if count > 3:
                    break
            parse_and_verify(html)
            logi(f'wait {self.interval} seconds, start stype num {stype}')
            time.sleep(self.interval)
