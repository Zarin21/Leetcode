
from ast import List

# I use a two-pointer approach starting from the end of both arrays.
# I compare the elements pointed by the two pointers and place the larger one at the end of nums1.
# I move the corresponding pointer and the position pointer backwards.
# If there are remaining elements in nums2, I copy them to the front of nums1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1