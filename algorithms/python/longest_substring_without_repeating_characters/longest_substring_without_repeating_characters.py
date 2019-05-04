#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# @Author   : shiqi.chang
# @Email    : shiqi.chang@carrobot.com
# @Time     : 2019/5/4 下午7:45
# @Filename : longest_substring_without_repeating_characters.py
# @Software : PyCharm


def get_len_of_longest_substr(s):
    """
    解题思路：
        遍历字符串，用一个列表存放子字符串的每个字符，遇到与列表中相同的字符，则记下该字符在列表中的下标；
        然后列表切片，从记下的下标值加 1 开始切分，同时保存之前的列表的长度；
        以此循环，对比一下前后列表（子字符串）的长度，取大的，则是结果
    :param str s:
    :return int length:
    """
    substr = []
    length = 0
    for char in s:
        if char not in substr:
            substr += char

            # 如果 char 是最后一个字符串，则需要比较当前 substring 的长度与 保存的 length 的大小
            if s[-1] == char:
                substr_len = len(substr)
                if substr_len > length:
                    length = substr_len
        else:
            # 获取本次子字符串的长度，并与之前的 length 对比
            substr_len = len(substr)
            if substr_len > length:
                length = substr_len

            # 记下在子字符串中重复字符的下标，并对列表分片
            index = substr.index(char)
            substr = substr[index + 1:] + [char]

    return length


if __name__ == '__main__':
    print(get_len_of_longest_substr('abcbef'))
