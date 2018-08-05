#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : Kyle
# @License : MIT
# @Contact : kairu_madigan@yahoo.co.jp
# @Date    : 2018/08/05 12:58

import unittest

from sakurailib import text as text_lib


class EastLiteralWidthTestCase(unittest.TestCase):
    
    def test_get_east_asian_width_count_1(self):
        text = "你好，世界!"
        expect = 11
        result = text_lib.get_east_asian_width_count(text)
        self.assertEqual(expect, result)
        
    def test_get_east_asian_width_count_2(self):
        text = "hello, world!"
        expect = 13
        result = text_lib.get_east_asian_width_count(text)
        self.assertEqual(expect, result)
        
    def test_get_east_asian_width_count_3(self):
        text = "你好，世界！"
        expect = 12
        result = text_lib.get_east_asian_width_count(text)
        self.assertEqual(expect, result)
