class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_and_sorted_list = nums1 + nums2
        merged_and_sorted_list.sort()
        if len(merged_and_sorted_list) % 2 == 0:
            length = len(merged_and_sorted_list)
            return float((merged_and_sorted_list[int(length/2) - 1] + merged_and_sorted_list[int(length/2)])/2)
        else:
            return float(merged_and_sorted_list[int(len(merged_and_sorted_list)/2)])
