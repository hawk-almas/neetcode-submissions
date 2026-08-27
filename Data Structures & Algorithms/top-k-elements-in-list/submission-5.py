class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        hm = {}

        for i in nums:
            hm[i] = 1 + hm.get(i, 0)
        
        bucket = []

        

        for i in range(len(nums)):
            bucket.append([])

        

        for key, val in hm.items():
            bucket[val-1].append(key)

        #print(bucket)

        op = []
        #print(len(bucket))
        for i in range(len(bucket)-1,-1,-1):

            #print(op)

            for j in bucket[i]:

                op.append(j)

                #print(op)
                
                if len(op) == k:
                    return op


        
        
        