from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        strs_s = []

        for word in strs:
            
            strs_s.append(''.join(sorted(word)))
            h[''.join(sorted(word))]= []


        

        for word in strs:
            if ''.join(sorted(word)) in h:
                h[''.join(sorted(word))].append(word)
        

        ret = []

        for key in h:
            t = h[key]
            ret.append(t)

        return ret

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))