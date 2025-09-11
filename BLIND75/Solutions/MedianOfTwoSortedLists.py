class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        # Running Binary Search on A
        l = 0
        r = len(A) - 1

        while True:
            i = (l + r) // 2  # (Floor Division); Potential Median index for A
            j = (
                half - i - 2
            )  # Potential Median index for B; -2 because i includes 0 and B also includes 0 index

            # A
            if i >= 0:
                ALeft = A[i]
            else:
                ALeft = float("-infinity")
            if i < len(A) - 1:
                ARight = A[i + 1]
            else:
                ARight = float("infinity")

            # B
            if j >= 0:
                BLeft = B[j]
            else:
                BLeft = float("-infinity")
            if j < len(B) - 1:
                BRight = B[j + 1]
            else:
                BRight = float("infinity")

            # Left Partition is correct
            if ALeft <= BRight and ARight >= BLeft:
                # odd
                if total % 2:
                    return min(ARight, BRight)
                # even
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2.0
            # Partition not correct
            elif ALeft > BLeft:  # A has more item than it should have on the left
                # So we shift the pointer
                r = (
                    i - 1
                )  # Potential Median shifted to left eliminating items from left
            elif ARight < BRight:  # A has less items on the left than it should have
                l = (
                    i + 1
                )  # Potential Median shifted to right to have more items on the left, increasing left partition

        # Time Complexity: O(log(min(n, m))) where n and m are the lengths of the two arrays.
        # Space Complexity: O(1)
