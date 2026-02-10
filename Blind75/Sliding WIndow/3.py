class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in result:
                result.remove(s[l])
                l+=1
            result.add(s[r])
            longest = max(longest, (r-l)+1) #+1 because index start with index 0
            r += 1
        return longest 

                

