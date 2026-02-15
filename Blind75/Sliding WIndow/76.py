
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window, countT = {}, {}
        resIndex, resLen = [-1, -1], float("infinity")
        for n in t :
            countT[n] = 1 + countT.get(n, 0)
        have, need = 0, len(countT)
        l = 0
        for r in range (len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]: 
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    resIndex = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = resIndex
        return s[l:r+1]