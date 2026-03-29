class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_pair = {}

        for idx, num in enumerate(nums):
            pair = target - num

            if pair in dict_pair:
                return [dict_pair[pair], idx]

            dict_pair[num] = idx
        