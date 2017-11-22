#!/usr/bin/env python
#coding=utf-8
# *******************************************************************
#     Filename @  Typed.py
#       Author @  xshi
#  Change date @  11/16/2017 9:10 AM
#        Email @  xshi@kth.se
#  Description @  ISLR In Python
# ********************************************************************
"""
Type-check descriptor
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(owner):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(owner, name, Typed(name, expected_type))
        return owner
    return decorate