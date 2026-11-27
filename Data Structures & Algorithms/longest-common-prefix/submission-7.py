class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or strs[0][i] != word[i]:
                    return str
            str += word[i]
        return str