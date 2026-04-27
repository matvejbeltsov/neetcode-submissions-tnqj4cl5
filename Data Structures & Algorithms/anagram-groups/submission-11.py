class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:
            key_word = tuple(sorted(word))

            anagram[key_word].append(word)

        return list(anagram.values())