#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: main_crawler.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/5/27 22:55
version: 1.0
"""
from base import *
from crawler import *
import os

target = os.environ.get('target')
protocol = os.environ.get('protocol')

proxy = UseProxy(protocol=protocol)
proxies = find_proxy(proxy)

if target == 'yundaili':
    YunDaiLi().crawler(proxies)
elif target == 'yundaili_free':
    YunDaiLiFree().crawler(proxies)
elif target == 'jiangxianli':
    JiangXianLi().crawler(proxies)
elif target == 'fatezero':
    FateZero().crawler(proxies)