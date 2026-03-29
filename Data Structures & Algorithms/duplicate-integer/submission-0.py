class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = dict()
        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        return len(dictionary) != len(nums)
         