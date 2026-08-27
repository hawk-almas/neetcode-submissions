class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(list)
        seen = []
        for i in nums:

            if i in seen:
                continue
            seen.append(i)

            count = nums.count(i)

            hm[count].append(i)

        
        hm = dict(hm)
        hm = dict(sorted(hm.items()))
        print(hm)
        x = [i for j in list(hm.values()) for i in j]
        
        op = []

        for i in range(1, k+1):
            
            op.append(x[-i])
        return op
        