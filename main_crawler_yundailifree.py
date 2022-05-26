#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: main_crawler_yundailifree.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/5/26 11:23
version: 1.0
"""
from base import *
from crawler import *

proxies = find_proxy()

YunDaiLiFree().crawler(proxies)