class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx - 1] == num:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])

                    left += 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return res

        