class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sum = {}

        for idx, num in enumerate(nums):
            pair = target - num

            if pair in dict_sum:
                return [dict_sum[pair], idx]
            
            dict_sum[num] = idx
            
        