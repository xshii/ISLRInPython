#!/usr/bin/env python
#coding=utf-8
# *******************************************************************
#     Filename @  simple.py
#       Author @  xshi
#  Change date @  11/16/2017 6:36 PM
#        Email @  xshi@kth.se
#  Description @  ISLR In Python
# ********************************************************************
"""
test unit
"""

import unittest
# A simple function to illustrate
def parse_int(s):
    return int(s)
class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'a')

if __name__=='__main__':
    unittest.main()