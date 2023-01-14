"""
This is the Python solution for the Two Sum problem in Leetcode
Problem: Given an array of integers "nums" and an integer "target",
         return indices of the two numbers such that they add up to target.
         You may assume that each input would have exactly one solution,
         and you may not use the same element twice.
"""


class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        for k, v in enumerate(nums):
            nums_dict[v] = k

        print(f"list with ordered values {nums_dict}")
        results = []

        for k, v in nums_dict.items():
            diff = target - k
            if diff in nums_dict.keys() \
                    and (target - k) != k:
                results = [v, nums_dict[diff]]

        print(f"desired target: {target}")
        return results


s = Solution()

test_list = [
    ([1, 3, 5, 7], 10),
    ([1, 3, 5, 7], 8),
    ([0, 3, 8, 13], 14),
    ([5, 10, 15, 20], 30)
]

for r in test_list:
    print(s.twoSum(r[0], r[1]))
