#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# @Author   : shiqi.chang
# @Email    : shiqi.chang@carrobot.com
# @Time     : 2019/4/25 上午9:47
# @Filename : __init__.py
# @Software : PyCharm


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        """Z 字形变换

        解题思路：
            将字符串转换成二维数组
        :param str s:
        :param int num_rows:
        :return str res:
        """
        len_s = len(s)
        if len_s <= 1 or num_rows == 1:
            return s

        count = 2 * num_rows - 2

        # list * n—>n shallow copies of list concatenated, n个list的浅拷贝的连接
        # [[]]是一个含有一个空列表元素的列表,所以[[]]*3表示3个指向这个空列表元素的引用,修改任何一个元素都会改变整个列表
        lists = [['' for _ in range(len_s)] for _ in range(num_rows)]

        for i in range(len_s):
            num = i // count

            if (i >= count * num) and (i < count * num + num_rows):
                lists[i - count * num][num * (count - num_rows + 1)] = s[i]
            elif (i >= count * num + num_rows) and (i < count * (num + 1)):
                lists[count * (num + 1) - i][i - (num_rows - 1) * (num + 1)] = s[i]

        res = ''
        for l in lists:
            text = ''.join(l)
            res += text

        return res


if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 3))
