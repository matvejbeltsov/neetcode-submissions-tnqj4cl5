class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        set_letter = set()

        res = 0

        for right in range(len(s)):
            char = s[right]

            while char in set_letter:
                set_letter.remove(s[left])
                left += 1

            set_letter.add(char)
            res = max(res, right - left + 1)
        return res        