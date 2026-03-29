class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_str = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))

            dict_str[sorted_word].append(word)

        return list(dict_str.values())
        