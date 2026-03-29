class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1

        for ch_t in t:
            dict_t[ch_t] = dict_t.get(ch_t, 0) + 1    
        
        return dict_s == dict_t