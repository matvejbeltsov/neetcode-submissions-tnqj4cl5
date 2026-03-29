class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_one = {}
        dict_two = {}

        for i in s:
            dict_one[i] = dict_one.get(i, 0) + 1
        for i in t:
            dict_two[i] = dict_two.get(i, 0) + 1
        
        return dict_one == dict_two
        