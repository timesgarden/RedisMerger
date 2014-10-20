#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by tsli on 14-10-20
#
__author__ = 'tsli'

import RedisOperator
from ConfigReader import REDIS_HOST, REDIS_PORT

if __name__ == "__main__":
    redisOperator = RedisOperator.RedisOperator()
    cur = redisOperator.connect(REDIS_HOST, REDIS_PORT, 1)
    for key in cur.keys():
        print key,
        print cur.get(key)
    #print cur.get('3_84')
