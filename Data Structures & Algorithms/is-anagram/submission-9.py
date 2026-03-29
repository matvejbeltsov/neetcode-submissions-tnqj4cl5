class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1
        
        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1

        return dict_s == dict_t