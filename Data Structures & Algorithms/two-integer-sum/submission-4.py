class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}

        for idx, num in enumerate(nums):
            pair = target - num

            if pair in dict_num:
                return [dict_num[pair], idx]

            dict_num[num] = idx