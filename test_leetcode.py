from typing import List

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = set(nums)
#         longest = 0
        
#         for num in nums_set:
#             if num-1 not in nums_set:
#                 temp_longest = 1
#                 while(num + temp_longest) in nums_set:
#                     temp_longest += 1
#                 longest = max(longest, temp_longest)
#         return longest

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s =s.lower()
#         print(f"s before -- {s}")
#         for x in s:
#             if x.isalnum() is False:
#                 s = s.replace(x, "")
#         print(f"s after -- {s}")
#         if s == s[::-1]:
#             return True
#         return False


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s)-1

#         while left < right:
#             # print(f"left -- {s[left]} and right -- {s[right]}")
#             while left < right and not self.is_alphanumeric(s[left]):
#                 print(f"left -- {s[left]} is not alphanumeric")
#                 left += 1 
#             while right > left and not self.is_alphanumeric(s[right]):
#                 print(f"right -- {s[right]} is not alphanumeric")
#                 right -= 1 
#             print(f"left -- {s[left]} and right -- {s[right]}")
#             if s[left].lower() != s[right].lower():
#                 return False
#             left += 1
#             right -= 1
#             # print(f"after left -- {s[left]} and right -- {s[right]}")
#         return True

#     def is_alphanumeric(self, c:str) -> bool:
#         return (ord('A') <= ord(c) <= ord('Z'))or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         result = []
#         for i, a in enumerate (nums):
#             if a > 0:
#                 break
#             if a == nums[i-1] and i > 0:
#                 continue
#             l, r = i +1, len(nums)-1
#             while l < r :
#                 threesum = a + nums[l] + nums[r]
#                 if threesum < 0:
#                     l += 1
#                 elif threesum > 0:
#                     r -= 1 
#                 else:
#                     result.append([a, nums[l], nums[r]])
#                     #cause == 0, if we continue just l increment without r decrement, we will get the same result again
#                     l += 1
#                     r -= 1
#                     #check current value l not same previous value, if same, continue
#                     while nums[l] == nums[l-1] and l < r:
#                         l += 1
#                     #check current value r not same previous value, if same, continue
#                     while nums[r] == nums[r+1] and l < r:
#                         r -= 1
#         return result

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l, r = 0 , len(height)-1
#         max_area = 0
#         while l < r:
#             area = (r - l) * min(height[l], height[r])
#             max_area = max(max_area, area)
#             if height[r] > height[l]:
#                 l += 1 
#             elif height[r] <= height[l]:
#                 r -= 1 
#         return max_area
   
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         result = set()
#         l = 0
#         longest = 0
#         for r in range(len(s)):
#             while s[r] in result:
#                 result.remove(s[l])
#                 l+=1
#             result.add(s[r])
#             print(result)
#             print(f"r--{r} l--{l}")
#             longest = max(longest, (r-l)+1) #+1 because index start with index 0
#             r += 1
#         return longest 



# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         countf = {}
#         maxf = 0 
#         res = 0 
#         l = 0 
#         for r in range (len(s)):
#             countf[s[r]] =  1 + countf.get(s[r],0)
#             maxf = max(maxf, countf[s[r]])

#             while ( r - l + 1 ) - maxf > k:
#                 countf[s[l]] -= 1
#                 l += 1
            
#             res = max(res, r - l + 1)
        
#         return res


# test = Solution()
# print(test.characterReplacement(("AAAB"), 0))

