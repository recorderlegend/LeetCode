
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        hs = {}
        ht = {}
        for i in range(len(s)):
            hs[s[i]] = 0
            ht[t[i]] = 0

        for i in range(len(s)):
            hs[s[i]]+=1
            ht[t[i]]+=1

        if hs == ht:
            return True
        
        return False


print(Solution().isAnagram("rat","car"))