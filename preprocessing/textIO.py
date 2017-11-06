#!/usr/bin/env python
#coding=utf-8
# *******************************************************************
#     Filename @  textIO.py
#       Author @  xshi
#  Change date @  11/6/2017 6:28 PM
#        Email @  xshi@kth.se
#  Description @  ISLR In Python
# ********************************************************************
"""
Introduction
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from os import listdir
from os.path import isfile, join

def readText(path):
    """
    read one text file
    :param path:
    :return: np.array(str)
    """
    file = open(path,'r')
    return np.array(file.read())

def readTexts(respository):
    """
    not recursively! read multiple text files from given respository
    :param respository:
    :return: [np.array(str)]
    """
    texts = []
    onlyfiles = [f for f in listdir(respository) if isfile(join(respository, f))]
    for text in onlyfiles:
        texts = texts+[readText(join(respository, text))]
    return texts

def readLabel(path):
    """
    remains
    :param path:
    :return: np.array([str])
    """
    pass
def test_readText():
    text = readText(r"C:\Users\gakki\Dropbox\ISLRInPython\testDataSet\text\bbc\business\001.txt")
    return text

def test_readTexts():
    texts = readTexts(r"C:\Users\gakki\Dropbox\ISLRInPython\testDataSet\text\bbc\business")
    return texts

def test_readTexts():
    pass