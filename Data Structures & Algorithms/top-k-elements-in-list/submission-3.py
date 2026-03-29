class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1
        
        for elem, cnt in dict_nums.items():
            freq[cnt].append(elem)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for elem in freq[i]:
                res.append(elem)
                if len(res) == k:
                    return res
        return res
        