#!/usr/bin/env python
#coding=utf-8
# *******************************************************************
#     Filename @  imageIO.py
#       Author @  xshi
#  Change date @  11/6/2017 10:05 AM
#        Email @  xshi@kth.se
#  Description @  ISLR In Python
# ********************************************************************
"""
This is preprocessing of image data
# .*** (support ['png'] only @install Pillow to support more)
#
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imresize
from os import listdir
from os.path import isfile, join

def readImage(path,rgb = [0,1,2], *rescale):
    """
    read in image in gray Scale through RGB Pannel default is R
    :param path:
    :param rgb: 0 = R, 1 = G, 2 = B
    :param *rescale = tuple(height,width)
    :return: np.array
    """
    image = plt.imread(path)[:,:,rgb]
    height = image.shape[0]
    width = image.shape[1]
    try:
        # rescale the image by using bilinear interpolation
        for x in rescale:
            height = x[0]
            width = x[1]
            image = imresize(image, x, interp='bilinear', mode=None)
    except IndexError:
        pass
        #print("no given rescale command ")
    return np.array(image)

def readImages(respository,*rescale):
    """
    not recursively! read image from respository
    :param respository:
    :return: list[np.array]
    """
    record = []
    onlyfiles = [f for f in listdir(respository) if isfile(join(respository, f))]
    for image in onlyfiles:
        record = record+[readImage(join(respository, image),[0,1,2],rescale)]
    return record
    pass

def readLabel():
    pass

def test_readImageIO():
    plt.figure()
    image = readImage(r"C:\Users\gakki\Dropbox\ISLRInPython\testDataSet\image\2.jpg",[0,1,2],[400,200])
    plt.imshow(image)

def test_readImages():
    s = readImages(r"C:\Users\gakki\Dropbox\ISLRInPython\testDataSet\image")
    return s