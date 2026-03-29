class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for el in s:
            dict_s[el] = dict_s.get(el, 0) + 1

        for el in t:
            dict_t[el] = dict_t.get(el, 0) + 1

        return dict_s == dict_t