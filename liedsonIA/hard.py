class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        m, n = len(nums1), len(nums2)

        if m == 0:
            return (nums2[n // 2] + nums2[(n - 1) // 2]) / 2.0 if n > 0 else 0
        elif n == 0:
            return (nums1[m // 2] + nums1[(m - 1) // 2]) / 2.0 if m > 0 else 0

        i = 0
        j = 0
        result = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        if i < m:
            result += nums1[i:]
        elif j < n:
            result += nums2[j:]

        mid = len(result) // 2
        if len(result) % 2 == 0:
            return (result[mid] + result[mid - 1]) / 2.0
        else:
            return result[mid]


