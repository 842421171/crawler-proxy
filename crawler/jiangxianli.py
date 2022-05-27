#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: jiangxianli.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/3/5 18:55
version: 1.0
"""
from __future__ import annotations
from base import *
from bs4 import BeautifulSoup
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
    bs = BeautifulSoup(html, 'lxml')

    ip_elements = bs.select(
        'body > div.layui-layout.layui-layout-admin > div.layui-row > div.layui-col-md9.ip-tables > div.layui-form '
        '> table > tbody > tr > td:nth-child(1)')
    port_elements = bs.select(
        'body > div.layui-layout.layui-layout-admin > div.layui-row > div.layui-col-md9.ip-tables > div.layui-form '
        '> table > tbody > tr > td:nth-child(2)')
    protocol_type_elements = bs.select(
        'body > div.layui-layout.layui-layout-admin > div.layui-row > div.layui-col-md9.ip-tables > div.layui-form '
        '> table > tbody > tr > td:nth-child(4)')

    ips = [ip.get_text() for ip in ip_elements if ip.get_text()]
    ports = [port.get_text() for port in port_elements]
    protocol_types = [protocol_type.get_text() for protocol_type in protocol_type_elements]

    if not len(ips):
        return True

    for ip, port, protocol_type in zip(ips, ports, protocol_types):
        proxy = UseProxy(ip, port, protocol_type)
        logi(f'{proxy.dict()} 开始验证')
        if is_valided_proxy(proxy) and verify_ip_validity(proxy):
            logi(f'{proxy.dict()} 验证通过')
            add_proxy(proxy)
        else:
            logi(f'{proxy.dict()} 验证失败')


class JiangXianLi:
    url = 'https://ip.jiangxianli.com/?page={page}'
    interval = 5

    def get_html(self, proxy: UseProxy | None, page: int) -> str | None:
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
            return get('https', url=self.url.format(page=page), proxies=proxies, verify=False).text
        except Exception as ex:
            loge(ex)
            pass

    def crawler(self, proxies: List[UseProxy]) -> None:
        """
        save to file
        :param proxies: proxy list
        :return: None
        """
        page = 1
        logi(f'start page num {page}')
        proxy = None
        while True:
            html = None
            count = 0
            while html is None:
                if len(proxies) > 0:
                    proxy = random.sample(proxies, 1)[0]
                html = self.get_html(proxy, page)
                count += 1
                if html is None:
                    logi(f'wait {self.interval} seconds, retry page num {page}')
                    time.sleep(self.interval)
                if count > 3:
                    break
            if count > 3 or parse_and_verify(html):
                break

            page += 1

            logi(f'wait {self.interval} seconds, start page num {page}')
            time.sleep(self.interval)
        logi(f'The total pages is {page - 1}')
