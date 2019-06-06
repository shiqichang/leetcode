#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# @Author   : shiqi.chang
# @Email    : shiqi.chang@carrobot.com
# @Time     : 2019/4/27 下午2:12
# @Filename : add_two_numbers.py
# @Software : PyCharm


class ListNode(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def gen_list_node(l):
    """生成 `ListNode`

    :param list, l:
    :return list, ln:
    """
    ln = []
    for val in reversed(l):
        if not ln:
            node = ListNode(val)
        else:
            node = ListNode(val, ln[-1])
        ln.append(node)
    return ln


def add_two_numbers(ln1, ln2):
    """两数相加

    解题思路：
        取列表结点中较短长度，进行循环，因为列表结点是按照逆序排的，所以从左至右分别是个，十，百等等；
        将两个列表结点对应的值相加，若和大于等于 10，则　高位进一，低位为和减去 10;
        循环结束之后，如果两个列表长度不一样，那么结果列表的最后一个值为长度长的列表的最后一个

    todo 待改进
    本地测试用例通过，
    但 leetcode 没通过，报错原因：TypeError: object of type 'ListNode' has no len()
    :param list, ln1:
    :param list, ln2:
    :return list, result:
    """
    min_len = min(len(ln1), len(ln2))
    l_val = []
    for i in range(min_len):
        val = ln1[i].value + ln2[i].value
        if val >= 10:
            val -= 10
            val_next = 1
        else:
            val_next = 0

        if i == len(l_val):
            l_val.append(val)
        else:
            l_val[-1] += val

        if val_next == 1:
            l_val.append(val_next)

    if len(ln1) != len(ln2):
        if min_len == len(ln1):
            l_val.append(ln2[-1].value)
        else:
            l_val.append(ln1[-1].value)

    print(l_val)

    result = gen_list_node(l_val)
    return result


if __name__ == '__main__':
    l1 = [4, 3]
    ln1 = gen_list_node(l1)
    l2 = [5, 6, 4]
    ln2 = gen_list_node(l2)
    print(add_two_numbers(list(reversed(ln1)), list(reversed(ln2))))
