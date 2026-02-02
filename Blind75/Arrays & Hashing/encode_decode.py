class Solution:
    #["Hello","World"]
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s 
        print(f"result{result}")
        return result
        #"5#Hello5#World"

    #"5#Hello5#World"
    def decode(self, s: str) -> List[str]:
        strs = []
        #"5#Hello5#World"
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 # j = 1
            length = int(s[i:j]) # length = 5
            word = s[j+1:j+1+length]
            strs.append(word)
            i = j+1+length
        return strs
    
       
