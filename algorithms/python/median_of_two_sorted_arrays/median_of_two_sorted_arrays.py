#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# @Author   : shiqi.chang
# @Email    : shiqi.chang@carrobot.com
# @Time     : 2019/5/11 下午7:03
# @Filename : median_of_two_sorted_arrays.py
# @Software : PyCharm


def find_median_sorted_arrays(nums1, nums2):
    """寻找两个有序数组的中位数

    解题思路：
        要求时间复杂度为 O(log(m+n))，为二叉树的题型，
        但我暂时想不出二叉树的解法，取巧用了python内嵌的sorted()方法
    :param list nums1:
    :param list nums2:
    :return float result:
    """
    tmp_nums = nums1 + nums2
    sorted_nums = sorted(tmp_nums)
    length = len(sorted_nums)
    if length % 2 == 0:
        result = (sorted_nums[length // 2 - 1] + sorted_nums[length // 2]) / 2
    else:
        result = sorted_nums[length // 2]
    return result


if __name__ == '__main__':
    print(find_median_sorted_arrays([1, 3], [2]))
