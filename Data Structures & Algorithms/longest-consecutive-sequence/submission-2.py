class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = 0
        newset = set(nums)

        for num in nums:
            streak, current = 0, num
            while current in newset:
                streak += 1
                current += 1
            number = max(number, streak)
        return number
