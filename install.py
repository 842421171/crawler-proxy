#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
File Name: install.py
Author: Pengcc
Email: pcc_pengcc@163.com
Time: 2022/3/2 9:21
version: 1.0
"""

import os

# install
libs = {'requests', 'beautifulsoup4', 'lxml', 'fake-useragent', 'pandas', 'attr', 'attrs', 'apscheduler'}

for lib in libs:
    os.system('pipenv run pipenv install ' + lib + ' -d')

os.system('pipenv run pip freeze > requirements.txt')
