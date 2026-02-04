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


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort + check double variable x, x + y + z , then x and y using two pointers
        


        

test = Solution()
print(test.threeSum([-1,0,1,2,-1,-4]))