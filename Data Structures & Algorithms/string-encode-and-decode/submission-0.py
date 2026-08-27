class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for i in strs:
            encoded+= str(len(i)) + "#" + i
        return encoded
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        
        while i < len(s):
            
            j = i
            while s[j] != "#":
                j+=1
                
            size = int(s[i:j])
            res.append(s[j+1: j+size+1])
            i = j+size+1
        return res
            
            
