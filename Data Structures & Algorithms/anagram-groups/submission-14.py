class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_word = defaultdict(list)

        for word in strs:
            tuple_word = tuple(sorted(word))

            dict_word[tuple_word].append(word)

        return list(dict_word.values())     