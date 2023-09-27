class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) <= len(nums2):
            base, query = nums2, nums1
        else:
            base, query = nums1, nums2

        idx = 0
        for number in query:
            while base[idx] < number:
                idx += 1
            else:
                base.insert(idx, number)
                idx += 1

        list_size = len(base)
        median = base[list_size//2] if list_size%2 != 0 else (base[list_size//2] + base[(list_size//2)-1])/2

        return median