# 88. Merge Sorted Array

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[m:] = nums2
#         nums1.sort()

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         idx, idx1, idx2 = m+n-1, m-1, n-1
        
#         while idx1 >=0 and idx2 >= 0:
#             if nums1[idx1] > nums2[idx2]:
#                 nums1[idx] = nums1[idx1]
#                 idx1 -= 1
#                 idx -=1
#             else:
#                 nums1[idx] = nums2[idx2]
#                 idx2 -= 1
#                 idx -=1
        
#         while idx1 >= 0:
#             nums1[idx] = nums1[idx1]
#             idx1 -= 1
#             idx -=1
            
#         while idx2 >= 0:
#             nums1[idx] = nums2[idx2]
#             idx2 -= 1
#             idx -=1
            
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        i = m+n+1
        
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1