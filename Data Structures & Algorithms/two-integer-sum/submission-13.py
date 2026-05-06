class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_pair = dict()


        for i, num in enumerate(nums):
            pair = target - num

            if pair in dict_pair:
                return [dict_pair[pair], i]

            dict_pair[num] = i