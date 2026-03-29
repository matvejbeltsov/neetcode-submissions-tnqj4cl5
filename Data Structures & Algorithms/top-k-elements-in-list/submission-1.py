class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        for elem, cnt in nums_dict.items():
             freq[cnt].append(elem)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for el in freq[i]:
                res.append(el)
                if len(res) == k:
                    return res
        return res