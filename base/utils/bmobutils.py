#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
File Name: bmobutils.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/4/30 下午10:15
version: 1.0
"""
import os
from typing import List
from base.domain import *
from base.third import *
from base.utils.log import *

application_id = os.environ.get('application_id')
rest_key = os.environ.get('rest_key')

bmob = Bmob(application_id, rest_key)
classname = 'use_proxy'


def add_proxy(proxy:UseProxy) -> None:
    res = bmob.find(classname, where=proxy.dict())
    data = res.jsonData.get('results')
    logi(res.jsonData)
    logi(data)
    logi(len(data))
    if not data or len(data) == 0:
        bmob.insert(classname, proxy.dict())
    else:
        bmob.update(classname, data['objectId'], proxy.dict())


def delete_proxy(proxy:UseProxy) -> None:
    res = bmob.find(classname, where=proxy.dict())
    data = res.jsonData.get('results')
    logi(data)
    logi(len(data))
    if not data or len(data) > 0:
        bmob.remove(classname, data['objectId'])


def find_proxy() -> List[UseProxy]:
    res = bmob.find(classname)
    data = res.jsonData.get('results')
    proxy_list = []
    if not data:
        return proxy_list
    for d in data:
        proxy = UseProxy(d['ip'], d['port'], d['protocol'], d['anonymity'])
        proxy_list.append(proxy)
    return proxy_list

# 103.152.232.172:8080
