#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : Kyle
# @License : MIT
# @Contact : kairu_madigan@yahoo.co.jp
# @Date    : 2018/08/05 12:56

import unicodedata


def get_east_asian_width_count(text: str) -> int:
    """获取文本的长度

    判断每个文字的属于全角或是半角，半角的文字长度为1，全角文字长度为2，
    然后将长度累加。

    Args:
        text: 需要获取长度的文本

    Return:
        文本长度，int类型
    """
    count = 0
    for char in text:
        # 半角为: H, Na, N, 全角为: F, W, A
        if unicodedata.east_asian_width(char) in "FWA":
            count += 2
        else:
            count += 1
    return count
