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
    res = bmob.find(classname, where=proxy.dict_ip_and_port())
    data = res.jsonData.get('results')
    logi(data)
    if not data or len(data) == 0:
        proxy.score = 100
        bmob.insert(classname, proxy.dict())
    else:
        proxy.score = data[0]['score']
        bmob.update(classname, data[0]['objectId'], proxy.dict())


def delete_proxy(proxy:UseProxy) -> None:
    res = bmob.find(classname, where=proxy.dict_ip_and_port())
    data = res.jsonData.get('results')
    logi(data)
    if not data and len(data) > 0:
        proxy.score = data[0]['score'] - 1
        if proxy.score > 0:
            bmob.update(classname, data[0]['objectId'], proxy.dict())
        else:
            bmob.remove(classname, data[0]['objectId'])


def find_proxy(proxy:UseProxy = None) -> List[UseProxy]:
    if proxy:
        res = bmob.find(classname, where=proxy.dict_protocol())
    else:
        res = bmob.find(classname)
    data = res.jsonData.get('results')
    proxy_list = []
    if not data:
        return proxy_list
    for d in data:
        proxy = UseProxy(d['ip'], d['port'], d['protocol'], d['anonymity'], d['score'])
        proxy_list.append(proxy)
    return proxy_list


def is_valided_proxy(proxy:UseProxy = None) -> bool:
    res = bmob.find(classname, where=proxy.dict_ip_and_port())
    data = res.jsonData.get('results')
    return False if not data and len(data) > 0 else True
