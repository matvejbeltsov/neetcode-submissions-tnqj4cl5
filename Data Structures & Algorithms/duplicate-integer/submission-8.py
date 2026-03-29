class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()

        for elem in nums:
            if elem in set_nums:
                return True
            set_nums.add(elem)
        return False