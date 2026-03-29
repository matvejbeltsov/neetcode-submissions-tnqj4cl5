class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq = {}

        freq = [[] for i in range(len(nums) + 1)]

        for elem in nums:
            dict_freq[elem] = dict_freq.get(elem, 0) + 1

        
        for el, idx in dict_freq.items():
            freq[idx].append(el)

        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for elem in freq[i]:
                res.append(elem)
                if len(res) == k:
                    return res
        
        return res
        