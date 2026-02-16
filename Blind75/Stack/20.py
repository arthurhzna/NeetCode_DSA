class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        memo ={
            "}" : "{",
            ")" : "(",
            "]" : "[",
        }

        for c in s:
            if c in memo:
                if stack and stack[-1] == memo[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True
            




  


