class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        numSet = set(nums)
        longest = 0

        for i in nums:
            if (i - 1) not in numSet:
                length = 0
                while (i + length) in numSet:
                    length+=1
                longest = max(length, longest)
            else:
                continue
        return longest
        """
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
