#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Author   : shiqi.chang
# @Email    : shiqi.chang@carrobot.com
# @Time     : 2019/6/4 上午11:24
# @Filename : reverse_integer.py
# @Software : PyCharm


class Solution:
    def reverse(self, x: int) -> int:
        """整数反转

        解题思路：
            利用 Python 分片 [::1]
        :param int x:
        :return int res:
        """
        text = str(x)[::-1]

        if '-' in text:
            text = text.replace('-', '')
            res = -int(text)
        else:
            res = int(text)

        if res not in range(-2**31, 2**31-1):
            res = 0

        return res


if __name__ == '__main__':
    print(Solution().reverse(1534236469))
