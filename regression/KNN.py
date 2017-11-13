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
class KNN:
    def __init__(self):
        pass
    def train(self, train_x, train_y, K):
        self.train_x = train_x
        self.train_y = train_y
        self.k = K
        pass

    def predict(self, pred_x):
        self.result = np.zeros(len(pred_x))
        for ind_i,i in enumerate(pred_x):
            klargest_pair = heapq.nsmallest(self.k, [(np.inner(i - s, i - s),y[ind_s][0]) for ind_s,s in enumerate(self.train_x)])
            klargest_y = [x[1] for x in klargest_pair]
            self.result[ind_i] = Counter(klargest_y).most_common(1)[0][0]
        pass

    def detail_pred_y(self):
        pass

if __name__ == '__main__':
    # only a binary demo
    mu1 = [1, 1]
    sigma1 = [[1, 0], [0, 2]]
    mu2 = [3, 3]
    sigma2 = [[1, 0], [0, 2]]
    np.random.seed(100)
    x1 = np.random.multivariate_normal(mu1, sigma1, 50)
    x2 = np.random.multivariate_normal(mu2, sigma2, 100)
    plt.plot(x1[:, 0], x1[:, 1], 'o')
    plt.plot(x2[:, 0], x2[:, 1], 'rx')
    plt.show()
    y1 = np.ones((len(x1), 1))
    y2 = np.zeros((len(x2), 1))
    x = np.vstack((x1, x2))
    y = np.vstack((y1, y2))
    knn = KNN()
    knn.train(x,y,3)
    pred_x0 = np.random.multivariate_normal(np.array(mu1), sigma1, 20)

    pred_x1 = np.random.multivariate_normal(np.array(mu2), sigma2, 25)
    pred_x = np.vstack((pred_x0,pred_x1))
    res = heapq.nsmallest(3, [(np.inner(pred_x[40,:] - s, pred_x[40,:] - s),y[ind_s][0]) for ind_s,s in enumerate(x)])
    pred_y = knn.predict(pred_x)
    pred_x0 = np.array([pred_x[ind_x] for ind_x,val_x in enumerate(knn.result) if val_x == 0])
    pred_x1 = np.array([pred_x[ind_x] for ind_x,val_x in enumerate(knn.result) if val_x == 1])
    plt.plot(pred_x0[:,0],pred_x0[:,1],'ob')
    plt.plot(pred_x1[:, 0], pred_x1[:, 1], 'x')
    plt.show()
    pass