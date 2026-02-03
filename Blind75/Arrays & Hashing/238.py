class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums = [1,2,3,4]
        result = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range (len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1): #start,stop,decrement
            result[i] *= postfix
            postfix *= nums[i] 
        return result
        



                

