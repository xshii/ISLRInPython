#!/usr/bin/env python
#coding=utf-8
# *******************************************************************
#     Filename @  KNN.py.py
#       Author @  xshi
#  Change date @  11/11/2017 8:53 PM
#        Email @  xshi@kth.se
#  Description @  ISLR In Python
# ********************************************************************
"""
K-nearest neighbor classifier
support multiple classes
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import heapq
from operator import attrgetter
from collections import Counter
from norm.Typed import *
from norm.Regression import *
# receipt 8.9 Creating a New Kind of Class or Instance Attribute
@typeassert(train_x=np.ndarray, train_y=np.ndarray,K=int)
class KNN():
    def __init__(self):
        pass

    # Alternative constructor
    def train(self, train_x, train_y, K):
        self.train_x = train_x
        self.train_y = train_y
        self.K = K

    def predict(self,test_x):
        result = np.zeros(len(test_x))
        for ind_i,i in enumerate(test_x):
            klargest_pair = heapq.nsmallest(self.K, [(np.inner(i - s, i - s),y[ind_s][0]) for ind_s,s in enumerate(self.train_x)])
            klargest_y = [x[1] for x in klargest_pair]
            result[ind_i] = Counter(klargest_y).most_common(1)[0][0]
        return result

    def detail_pred_y(self):
        pass

if __name__ == '__main__':
    # only a binary demo
    mu1 = [1, 1]
    sigma1 = [[1, 0], [0, 2]]
    mu2 = [3, 3]
    sigma2 = [[1, 0], [0, 2]]
    np.random.seed(100)
    x1 = np.random.multivariate_normal(mu1, sigma1, 2)
    x2 = np.random.multivariate_normal(mu2, sigma2, 100)
    plt.plot(x1[:, 0], x1[:, 1], 'ro')
    plt.plot(x2[:, 0], x2[:, 1], 'rx')
    plt.show()
    y1 = np.zeros((len(x1), 1))
    y2 = np.ones((len(x2), 1))

    x = np.vstack((x1, x2))
    y = np.vstack((y1, y2))
    knn = KNN()
    knn.train(x,y,2)
    pred_x0 = np.random.multivariate_normal(np.array(mu1), sigma1, 20)

    pred_x1 = np.random.multivariate_normal(np.array(mu2), sigma2, 25)
    pred_x = np.vstack((pred_x0,pred_x1))
    res = heapq.nsmallest(3, [(np.inner(pred_x[40,:] - s, pred_x[40,:] - s),y[ind_s][0]) for ind_s,s in enumerate(x)])
    pred_y = knn.predict(pred_x)
    pred_yp = knn.p_predict(pred_x)
    pred_x0 = np.array([pred_x[ind_x] for ind_x,val_x in enumerate(pred_y) if val_x == 0])
    pred_x1 = np.array([pred_x[ind_x] for ind_x,val_x in enumerate(pred_y) if val_x == 1])
    plt.plot(pred_x0[:,0],pred_x0[:,1],'bo')
    plt.plot(pred_x1[:, 0], pred_x1[:, 1], 'bx')
    plt.show()
    pass

