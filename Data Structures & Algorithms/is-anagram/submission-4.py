class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for sym in s:
            dict_s[sym] = dict_s.get(sym, 0) + 1

        for sym in t:
            dict_t[sym] = dict_t.get(sym, 0) + 1
        
        return dict_s == dict_t