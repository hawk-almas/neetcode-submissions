class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount = [0] *26
        tCount = [0] *26

        for char in s:
            ind =  ord(char) - ord('a') 
            sCount[ind] += 1

        for char in t:
            ind =  ord(char) - ord('a') 
            tCount[ind] += 1

        for i in range(26):
            if sCount[i] != tCount[i]:
                return False
            
        return True
        
