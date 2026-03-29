class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_string = defaultdict(list)

        for word in strs:
            tuple_word = tuple(sorted(word))
            dict_string[tuple_word].append(word)
        
        return list(dict_string.values())