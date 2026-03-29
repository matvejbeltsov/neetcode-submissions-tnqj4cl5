class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cnt_nums = Counter(nums)

        maxx = -1

        for k, v in cnt_nums.items():
            if v == 1:
                maxx = max(maxx, k)
        
        return maxx

        