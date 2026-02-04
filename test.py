from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        
        for num in nums_set:
            if num-1 not in nums_set:
                temp_longest = 1
                while(num + temp_longest) in nums_set:
                    temp_longest += 1
                longest = max(longest, temp_longest)
        return longest


test = Solution()
print(test.longestConsecutive([100,4,200,1,3,2]))