class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range (len(nums)+1)]
        temp = defaultdict(int)
        for num in nums:
            temp[num] += 1
        for key, value in temp.items():
            freq[value].append(key)
        result = []
        for i in range (len(freq)-1, 0 , -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
#bucket method 