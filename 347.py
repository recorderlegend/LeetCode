from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = 0

        for num in nums:
            h[num]+=1

        print(h)


print(Solution().topKFrequent([1,1,1,2,2,3],2))