#!/usr/bin/env python
#coding=utf-8
# *******************************************************************
#     Filename @  data.py.py
#       Author @  xshi
#  Change date @  11/13/2017 4:55 PM
#        Email @  xshi@kth.se
#  Description @  ISLR In Python
# ********************************************************************
"""
Introduction
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

import os
from itertools import islice
import numpy as np
import scipy as sc
os.path.dirname(os.path.abspath('__file__'))
f = np.loadtxt(r'C:\Users\gakki\Dropbox\read\ISLRInPython\testDataSet\data.txt')

def cov_large(f):
    it1 = enumerate(f)
    it2 = enumerate(f)

    for idx1, col1 in it1:
        mean1 = np.mean(col1)
        var1 = np.var(col1)
        it2 = islice(enumerate(f),idx1,None)
        for idx2, col2 in it2:
            cov = np.mean(col1*col2) - np.mean(col1)*np.mean(col2)
            rho = cov/np.sqrt(np.var(col1)*np.var(col2))
            if np.abs(rho) > 0.5:
                yield (idx1,idx2,cov)

with open('cov.txt','wt') as g:
    for suitable in cov_large(f):
        g.write(str(suitable))

it1 = enumerate(f)
it2 = enumerate(f)
f.shape
col1 = f[2,:]
col2 = f[100,:]
cov = np.mean(col1*col2) - np.mean(col1)*np.mean(col2)
rho = cov/np.sqrt(np.var(col1)*np.var(col2))
rho
np.corrcoef(np.vstack((f[2,:],f[100,:])))
a = 10