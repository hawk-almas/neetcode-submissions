from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        hm = defaultdict(list)
        res = []

        for st in strs:
            count = [0]*26
            for char in st:
                count[ord(char) - ord("a")] += 1
            hm[tuple(count)].append(st)

        return (list(hm.values()))

