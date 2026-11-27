class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set(nums1)
        seen2 = set(nums2)
        result = []

        for num in seen1:
            if num in seen2:
                result.append(num)

        return result

        