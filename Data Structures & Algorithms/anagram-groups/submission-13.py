class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagrams = defaultdict(list)

        for word in strs:
            tuple_word = tuple(sorted(word))

            dict_anagrams[tuple_word].append(word)

        return list(dict_anagrams.values())
        