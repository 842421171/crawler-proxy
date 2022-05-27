#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: main_crawler_fatezero.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/5/28 0:04
version: 1.0
"""
from base import *
from crawler import *

proxy = UseProxy(protocol='HTTP')
proxies = find_proxy(proxy)

FateZero().crawler(proxies)