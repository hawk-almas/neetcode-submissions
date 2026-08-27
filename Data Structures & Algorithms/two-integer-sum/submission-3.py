class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        hm = {}
        for i in range(0, len(nums)):
            yet = target - nums[i]
            
            if yet in hm:
                return [hm[yet], i]
            
            hm[nums[i]] = i
            """
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            
