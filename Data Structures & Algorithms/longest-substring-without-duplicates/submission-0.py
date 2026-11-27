class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        newSet = set()
        best = 0

        for i in range(len(s)):
            while s[i] in newSet:
                newSet.remove(s[left])
                left += 1
            newSet.add(s[i])
            best = max(best, i - left + 1)
        
        return best