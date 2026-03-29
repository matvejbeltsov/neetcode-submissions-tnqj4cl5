class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}

        for idx, elem in enumerate(nums):
            pair = target - elem

            if pair in dict_num:
                return [dict_num[pair], idx]

            dict_num[elem] = idx
        