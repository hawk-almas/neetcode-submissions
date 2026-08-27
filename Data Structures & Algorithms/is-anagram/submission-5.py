from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ddS = defaultdict(int)
        ddT = defaultdict(int)
        for char in s:
            ddS[char] += 1
        for char in t:
            ddT[char] += 1
        ddS = dict(ddS)
        ddT = dict(ddT)

        for key, value in ddS.items():
            if key not in ddT:
                return False
            if value != ddT[key]:
                return False
            continue
        return True

        
