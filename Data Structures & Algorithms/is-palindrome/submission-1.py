class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right = 0, len(s) - 1

        
        while left < right :
            if (self.is_alphaneumeric(s[left])) == False:
                
                left += 1
                continue
            if (self.is_alphaneumeric(s[right])) == False:
                
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                
                

                return False

            left += 1
            right -= 1
        return True
        print(self.is_alphaneumeric("l"))


    def is_alphaneumeric(self, c):
        return ( ord("A") <= ord(c) <= ord("Z") ) or ( ord("a") <= ord(c) <= ord("z") ) or ( ord("0") <= ord(c) <= ord("9") )