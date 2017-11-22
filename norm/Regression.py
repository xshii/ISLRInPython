#!/usr/bin/env python
#coding=utf-8
# *******************************************************************
#     Filename @  Regression.py
#       Author @  xshi
#  Change date @  11/16/2017 10:20 AM
#        Email @  xshi@kth.se
#  Description @  ISLR In Python
# ********************************************************************
"""
Introduction
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from abc import ABCMeta, abstractmethod
from cache.DataPool import *
class Regression(metaclass=ABCMeta):
    @abstractmethod
    def train(self,train_x,train_y,*add_setting):
        pass

    @abstractmethod
    def predict(self,test_x):
        pass

    @abstractmethod
    def evaluation(self, pred_y, real_pred_y, fct):
        super().test_accuracy = fct(pred_y-real_pred_y)
        pass
