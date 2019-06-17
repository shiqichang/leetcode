#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Author   : shiqi.chang
# @Email    : shiqi.chang@carrobot.com
# @Time     : 2019/6/17 上午10:18
# @Filename : palindrome_number.py
# @Software : PyCharm


class Solution:
    def is_palindrome(self, x: int) -> bool:
        """回文数

        解题思路：
            int 转换成 str, 利用 [::-1] 性质判断
        :param x:
        :return:
        """
        string = str(x)
        reverse_string = string[::-1]
        if string == reverse_string:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().is_palindrome(-121))
