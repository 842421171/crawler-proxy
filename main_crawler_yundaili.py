#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: main_crawler_yundaili.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/3/5 18:55
version: 1.0
"""
from base import *
from crawler import *

proxy = UseProxy(protocol='HTTP')
proxies = find_proxy(proxy)

YunDaiLi().crawler(proxies)