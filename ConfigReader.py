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

FROM_REDIS_HOST = cp.get("FROM REDIS", "FROM_REDIS_HOST")
FROM_REDIS_PORT = cp.get("FROM REDIS", "FROM_REDIS_PORT")
FROM_REDIS_DB = cp.get("FROM REDIS", "FROM_REDIS_DB")

TO_REDIS_HOST = cp.get("TO REDIS", "TO_REDIS_HOST")
TO_REDIS_PORT = cp.get("TO REDIS", "TO_REDIS_PORT")
TO_REDIS_DB = cp.get("TO REDIS", "TO_REDIS_DB")