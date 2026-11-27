class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newMap = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in newMap:
                newMap[key] = [word]
            else:
                newMap[key].append(word)
        
        return list(newMap.values())

