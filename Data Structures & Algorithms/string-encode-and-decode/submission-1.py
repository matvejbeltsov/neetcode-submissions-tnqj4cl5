class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '#'
        res = ''
        for word in strs:
            res += f'{len(word)}{delimiter}{word}'
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        delimiter = '#'
        i = 0
        while i < len(s):
            j = i
            while s[j] != delimiter:
                j += 1
            length = int(s[i:j])
            j += 1
            res.append(s[j:j+length])
            i = j + length
        return res