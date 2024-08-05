from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for num in nums:
            s[num] = 0

        for num in nums:
            s[num]+=1

        for key in s:
            if s[key]>1:
                return True  


        return False

