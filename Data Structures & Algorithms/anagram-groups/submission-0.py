class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        if len(strs) == 0 or len(strs) == 1:
            return [strs]

        hm = defaultdict(list)
        for i in strs:
            key = [0] *26

            for j in i:
                key[ord(j)-ord('a')]+=1

            hm[tuple(key)].append(i)
            
        hm = dict(hm) 
        
        
        return list(hm.values())