class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [[nums[0], nums[1], nums[2]]]
            else:
                return []

        res = []

        for i in range(len(nums) - 1):
            if i>0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = - nums[i]

            while left < right :
                if (nums[left] + nums[right]) > target :
                    right -= 1
                    continue
                if (nums[left] + nums[right]) < target :
                    left += 1
                    continue
                if ((nums[left] + nums[right]) == target):
                    
                    res.append([nums[i] , nums[left], nums[right]]) 
                    #Bujhini shuru

                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                    #Bujhini shesh
                    #BUJHISI
                    
        return res
