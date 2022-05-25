#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: log.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/3/10 19:22
version: 1.0
"""
import logging

log = logging.getLogger('proxypool')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - [%(thread)u] - [%(levelname)s]: %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)
log.setLevel(logging.DEBUG)


def logd(msg: object):
    log.debug(msg)


def logi(msg: object):
    log.info(msg)


def logw(msg: object):
    log.warning(msg)


def loge(msg: object):
    log.error(msg)
