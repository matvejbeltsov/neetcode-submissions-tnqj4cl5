class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_s = 0
        left_t = 0

        while left_s < len(s) and left_t < len(t):
            if s[left_s] == t[left_t]:
                left_s += 1
            left_t += 1

        return left_s == len(s)
        