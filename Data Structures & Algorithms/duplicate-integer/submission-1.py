class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        for key in hm.keys():
            if hm[key] > 1:
                return True
                
        return False