#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by tsli on 14-10-20
#
__author__ = 'tsli'

import ConfigParser
import os

cp = ConfigParser.ConfigParser()
cp.read(os.path.join(os.path.dirname(__file__), 'GlobalConfig.ini'))

REDIS_HOST = cp.get("REDIS", "REDIS_HOST")
REDIS_PORT = cp.get("REDIS", "REDIS_PORT")