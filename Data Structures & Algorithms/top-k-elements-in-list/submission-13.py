class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_k = {}

        for num in nums:
            dict_k[num] = dict_k.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in dict_k.items():
            freq[count].append(num)

        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res
        return res
        