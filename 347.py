from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = 0

        for num in nums:
            h[num]+=1

        hr = {}
        for i in h.values():
            value = i
            key = list(h.keys())[list(h.values()).index(i)]
            hr[value] = key
        ret = []

        i = k
        m = list(hr.keys()) 
        reversed(m)
        z = m[0]
    
        while z>=k:
            ret.append(hr[z])

            z-=1
        
        return ret

print(Solution().topKFrequent([-1,-1],1))