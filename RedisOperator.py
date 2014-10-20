#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Created by tsli on 14-10-20
#
__author__ = 'tsli'
import redis

class StringOperator:
    def __init__(self):
        pass

    def getStringValue(self, key):
        return self.cur.get(key)

    def setStringValue(self, key, value):
        self.cur.setnx(key, value)

class HashOperator:
    def __init__(self):
        pass

    def getHashAllFields(self, key):
        return self.cur.hkeys(key)

    def getHashValue(self, key, field):
        return self.cur.hget(key, field)

    def setHashValue(self, key, field, value):
        self.cur.hsetnx(key, field, value)

class ListOperator:
    def __init__(self):
        pass

    def getListLength(self, key):
        return self.cur.llen(key)

    def getListValue(self, key, index):
        return self.cur.lindex(key, index)

    def setListValue(self, key, value):
        self.cur.rpush(key, value)

class SetOperator:
    pass

class ZsetOperator:
    def __init__(self):
        pass

    def getZsetValue(self, key):
        return self.cur.zrange(key, 0, -1, withscores=True)

    def setZsetValue(self, key, score, name):
        self.cur.zadd(key, score, name)

class RedisOperator(StringOperator, HashOperator, ListOperator, SetOperator, ZsetOperator):
    def __init__(self):
        pass

    def connect(self, host, port, db):
        try:
            self.cur = redis.StrictRedis(host=host, port=port, db=db)
            if self.cur.ping():
                print "已经连接到%s:%s, DB %s" %(host, port, db)
        except Exception, e:
            raise Exception(e)

    def close(self):
        pass

    def porting2(self, toRedis):
        for key in self.__getAllKeys():
            type = self.__getType(key)
            if "string" == type:
                print "porting string type, key: ", key
                value = self.getStringValue(key)
                toRedis.setStringValue(key, value)
            elif "hash" == type:
                print "porting hash type, key: ", key
                for field in self.getHashAllFields(key):
                    value = self.getHashValue(key, field)
                    toRedis.setHashValue(key, field, value)
            elif "list" == type:
                print "porting list type, key: ", key
                len = self.getListLength(key)
                for index in xrange(len):
                    value = self.getListValue(key, index)
                    toRedis.setListValue(key, value)
            elif "set" == type:
                pass
            elif "zset" == type:
                print "porting zset type, key: ", key
                valueList =  self.getZsetValue(key)
                for value in valueList:
                    toRedis.setZsetValue(key, value[1], value[0])
            else:
                pass

    def __getAllKeys(self):
        return self.cur.keys()

    def __getType(self, key):
        return self.cur.type(key)


