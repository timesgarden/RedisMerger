#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by tsli on 14-10-20
#


# task 1: 192.168.79.159:6382 db1~db4 data export
# task 2: all data import to 192.168.79.159:6389(staging) and 192.168.79.159:6390(production) db0

__author__ = 'tsli'

import RedisOperator
from ConfigReader import FROM_REDIS_HOST, FROM_REDIS_PORT, FROM_REDIS_DB, TO_REDIS_HOST, TO_REDIS_PORT, TO_REDIS_DB

if __name__ == "__main__":
    fromRedisOperator = RedisOperator.RedisOperator()

    toRedisOperator = RedisOperator.RedisOperator()
    toRedisOperator.connect(TO_REDIS_HOST, TO_REDIS_PORT, TO_REDIS_DB)

    for fromDB in FROM_REDIS_DB.split(','):
        fromRedisOperator.connect(FROM_REDIS_HOST, FROM_REDIS_PORT, fromDB)
        fromRedisOperator.porting2(toRedisOperator)
        fromRedisOperator.close()

    toRedisOperator.close()


