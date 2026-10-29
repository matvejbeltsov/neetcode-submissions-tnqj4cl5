class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for elem in s:
            dict_s[elem] = dict_s.get(elem, 0) + 1

        for elem in t:
            dict_t[elem] = dict_t.get(elem, 0) + 1

        return dict_s == dict_t