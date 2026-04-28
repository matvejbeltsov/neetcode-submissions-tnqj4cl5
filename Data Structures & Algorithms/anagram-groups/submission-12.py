class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_res = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))

            dict_res[sorted_word].append(word)
        
        return list(dict_res.values())