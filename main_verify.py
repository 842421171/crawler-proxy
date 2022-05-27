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
    logi(f'{proxy.dict()} 开始验证')
    if verify_ip_validity(proxy):
        logi(f'{proxy.dict()} 验证通过')
        add_proxy(proxy)
        use_proxy_list.append(proxy)
    else:
        logi(f'{proxy.dict()} 验证失败')
        delete_proxy(proxy)
        
print(use_proxy_list)