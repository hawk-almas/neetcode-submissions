class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ls = list(s)
        t_ls = list(t)
        s_ls.sort()
        t_ls.sort()
        if s_ls == t_ls :
            return True
        else:
            return False