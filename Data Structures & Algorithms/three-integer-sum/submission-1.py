class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []

        for idx, elem in enumerate(nums):
            if idx > 0 and nums[idx - 1] == elem:
                continue

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                three_sum = nums[idx] + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([nums[idx], nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result 