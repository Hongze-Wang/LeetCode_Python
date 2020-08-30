# 350. Intersection of Two Arrays II

# brute force
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#         for n in nums1:
#             if n in nums2:
#                 res.append(n)
#                 nums2.remove(n)
#         return res

# hashmap 91.66% faster
# Counter is a subclass of Dict
# it stores the key as key and the number of the key as value
# from collections import Counter

# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         dic1, dic2 = Counter(nums1), Counter(nums2)
#         res = []
#         for n in dic1.keys():
#             if not dic2.get(n):
#                 continue
#             res.extend([n] * min(dic1[n], dic2[n]))
#         return res
        
# if using sort
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                # res += [nums1[i1]]
                res.append(nums1[i1])
                i1 += 1
                i2 += 1
        return res
