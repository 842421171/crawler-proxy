#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: use_proxy.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/5/25 21:15
version: 1.0
"""
from attr import attrs, attr


@attrs
class UseProxy:
    ip = attr(type=str, default=None)
    port = attr(type=str, default=None)
    protocol = attr(type=str, default=None)
    anonymity = attr(type=str, default=None)
    score = attr(type=int, default=None)

    def dict(self):
        return {
            'ip': self.ip,
            'port': self.port,
            'protocol': self.protocol,
            'anonymity': self.anonymity,
            'score': self.score
        }

    def __str__(self):
        return f'{self.ip}:{self.port}'

    def string(self) -> str:
        return self.__str__()

    def proxies(self) -> dict:
        """
        get proxies
        :return: proxies
        """
        return {
            'http': self.string(),
            'https': self.string()
        }