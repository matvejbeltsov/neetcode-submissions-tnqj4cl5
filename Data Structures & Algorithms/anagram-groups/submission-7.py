class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagram = defaultdict(list)

        for word in strs:
            word_turple = tuple(sorted(word))

            dict_anagram[word_turple].append(word)

        return list(dict_anagram.values())
        