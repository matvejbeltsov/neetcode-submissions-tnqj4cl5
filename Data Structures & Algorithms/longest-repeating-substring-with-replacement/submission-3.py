class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dict_count = {}

        max_count = 0
        res = 0


        for right in range(len(s)):
            dict_count[s[right]] = dict_count.get(s[right], 0) + 1
            max_count = max(dict_count[s[right]], max_count)

            if (right - left + 1) - max_count > k:
                dict_count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
        