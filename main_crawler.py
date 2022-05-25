#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: main_crawler.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/3/5 18:55
version: 1.0
"""
from base import *
from crawler import *

proxies = find_proxy()

YunDaiLiFree().crawler(proxies)
YunDaiLi().crawler(proxies)
# JiangXianLi().crawler(proxies)