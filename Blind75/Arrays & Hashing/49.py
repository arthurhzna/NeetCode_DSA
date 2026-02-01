class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for i in strs:
            key_temp = ''.join(sorted(i))
            temp[key_temp].append(i)
        return list(temp.values())
