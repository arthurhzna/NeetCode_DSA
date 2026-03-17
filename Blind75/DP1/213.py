from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def f(arr):
            rob1 = rob2 = 0
            for n in arr:
                rob1, rob2 = rob2, max(rob2, rob1 + n)
            return rob2

        return max(f(nums[1:]), f(nums[:-1]))