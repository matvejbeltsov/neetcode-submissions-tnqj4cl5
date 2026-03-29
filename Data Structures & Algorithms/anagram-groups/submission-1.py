class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_str = defaultdict(list)

        for ch in strs:
            key = tuple(sorted(ch))

            dict_str[key].append(ch)
        
        return list(dict_str.values())