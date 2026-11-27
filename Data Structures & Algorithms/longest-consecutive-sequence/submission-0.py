class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = 0
        newset = set(nums)

        for num in nums:
            a, current = 0, num
            while current in newset:
                a += 1
                current += 1
            number = max(number, a)
        return number
