class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        mp = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
        

        
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        """

        hm = {}

        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in hm:
                l = max(hm[s[r]] + 1, l)
                hm[s[r]] = r
            res = max(res, r - l + 1)
            hm[s[r]] = r
        return res





