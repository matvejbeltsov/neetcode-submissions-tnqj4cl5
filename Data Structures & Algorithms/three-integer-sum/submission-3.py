class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx - 1] == num:
                continue
            
            
            l = idx + 1
            r = len(nums) - 1 

            while l < r:

                three_sum = num + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1

                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return res

        