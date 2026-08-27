from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1

        hm = dict(hm)
        for key, value in hm.items():
            if value > 1:
                return True
        return False