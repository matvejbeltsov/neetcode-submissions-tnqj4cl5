class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}

        for i, num in enumerate(nums):
            pair = target - num

            if pair in dict_num:
                return [dict_num[pair], i]

            dict_num[num] = i
        