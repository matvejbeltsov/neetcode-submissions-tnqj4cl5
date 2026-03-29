class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagram = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))

            dict_anagram[sorted_word].append(word)
        
        return list(dict_anagram.values())