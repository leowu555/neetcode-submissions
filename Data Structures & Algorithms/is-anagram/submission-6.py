class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}

        for c in s:
            if c not in dic_s:
                dic_s[c] = 1
            else:
                dic_s[c] += 1
        
        for c in t:
            if c not in dic_t:
                dic_t[c] = 1
            else:
                dic_t[c] += 1
        
        return dic_s == dic_t