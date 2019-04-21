#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# @Author   : shiqi.chang
# @Email    : shiqi.chang@carrobot.com
# @Time     : 2019/4/21 下午10:16
# @Filename : two_sum.py
# @Software : PyCharm


def two_sum(nums, target):
    """
    时间复杂度：O(n^2)
    :param list nums:
    :param int target:
    :return list result:
    """
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
