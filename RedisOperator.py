#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by tsli on 14-10-20
#
__author__ = 'tsli'
# task 1: 192.168.79.159:6382 db1~db4 data export
# task 2: all data import to 192.168.79.159:6389(staging) and 192.168.79.159:6390(production) db0
import redis

class RedisOperator:
    def __init__(self):
        pass

    def connect(self, host, port, db):
        try:
            cur = redis.StrictRedis(host=host, port=port, db=db)
            if cur.ping():
                print "已经连接"

            info = cur.info()
            for key in info:
                print "%s: %s" % (key, info[key])

            print cur.get_type('3_84')

            return cur
        except Exception, e:
            print "connect to redis error: ", e
