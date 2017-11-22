#!/usr/bin/env python
#coding=utf-8
# *******************************************************************
#     Filename @  DataPool.py
#       Author @  xshi
#  Change date @  11/16/2017 12:09 PM
#        Email @  xshi@kth.se
#  Description @  ISLR In Python
# ********************************************************************
"""
datapool for allowing multiple modelling without
re cache data
"""
import weakref
# receipt 8.25 create cached instances
class DataPool:

    def __init__(self):
        self._cache = weakref.WeakKeyDictionary()

    def train_data(self, ID, train_data):
        if ID not in self._cache:
            self._cache[ID] = train_data
        else:
            train_data = self._cache[ID]
        return train_data

    def clear(self):
        self._cache.clear()