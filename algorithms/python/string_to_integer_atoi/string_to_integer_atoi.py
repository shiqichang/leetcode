#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Author   : shiqi.chang
# @Email    : shiqi.chang@carrobot.com
# @Time     : 2019/6/10 上午10:51
# @Filename : string_to_integer_atoi.py
# @Software : PyCharm


class Solution:
    def my_atoi(self, string: str) -> int:
        """字符串转换整数(atoi)

        解题思路：
            重点考虑边界情况，如空字符串 '', '+', '-', 不在 [-2**31, 2**31-1] 区间范围
            利用列表的 join() 方法将列表转换成字符串
        :param string:
        :return:
        """
        string = string.strip()

        if string == '':
            return 0

        num_str_list = [str(i) for i in range(10)]
        start_char = string[0]
        if (start_char not in num_str_list and
                start_char != '-' and start_char != '+'):
            return 0

        tmp_list = [start_char]
        for char in string[1:]:
            if char in num_str_list:
                tmp_list.append(char)
            else:
                break

        res_str = ''.join(tmp_list)
        if res_str == '-' or res_str == '+':
            return 0
        res = int(res_str)

        if res < -2**31:
            res = -2**31
        elif res > 2**31 - 1:
            res = 2**31 - 1

        return res


if __name__ == '__main__':
    print(Solution().my_atoi('-'))
