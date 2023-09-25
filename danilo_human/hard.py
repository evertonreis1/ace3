class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        arr_len = len(arr)
        index = (arr_len - 1) // 2
 
        if arr_len % 2:
            return arr[index]
        else:
            return (arr[index] + arr[index + 1]) / 2
