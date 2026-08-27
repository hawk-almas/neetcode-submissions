class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        if len(s) != len(t):
            return False
        
        hash_map_s = {}
        hash_map_t = {}

        for i in s:
            hash_map_s[i] = hash_map_s.get(i, 0) + 1
        for i in t:
            hash_map_t[i] = hash_map_t.get(i, 0) + 1

        

        

        for i in hash_map_s.keys():
            if i not in hash_map_t.keys():
                return False
            elif hash_map_s.get(i) != hash_map_t.get(i) :
                return False
        
        return True   
            
            
            