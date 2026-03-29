class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_substring = 0
        set_letter = set()

        for right in range(len(s)):
            char = s[right]

            while char in set_letter:
                set_letter.remove(s[left])
                left += 1
            
            set_letter.add(char)
            max_substring = max(max_substring, right - left + 1)
        return max_substring