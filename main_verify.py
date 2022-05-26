#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: main_verify.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/5/25 22:41
version: 1.0
"""
from verify import *
from base import *

proxies = find_proxy()
use_proxy_list = []

for proxy in proxies:
    if verify_ip_validity(proxy):
        add_proxy(proxy)
        use_proxy_list.append(proxy)
    else:
        delete_proxy(proxy)

print(use_proxy_list)