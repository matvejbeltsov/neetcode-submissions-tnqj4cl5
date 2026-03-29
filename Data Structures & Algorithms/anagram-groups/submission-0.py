class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        db = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))

            db[key].append(s)

        return list(db.values())
        