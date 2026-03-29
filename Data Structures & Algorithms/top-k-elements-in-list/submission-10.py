class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = {}
        for num in nums:
            dict_num[num] = dict_num.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in dict_num.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for elem in freq[i]:
                res.append(elem)
                if len(res) == k:
                    return res
        return res