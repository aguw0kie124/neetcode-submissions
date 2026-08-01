class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        totallen = len(nums1) + len(nums2)
        merged.sort()
        if len(merged) % 2 == 0:
            med = (merged[totallen // 2 - 1] + merged[totallen // 2]) / 2
            return med  
        else:
            return merged[totallen // 2]
        