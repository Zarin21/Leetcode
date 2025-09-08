class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Using two pointers to find the maximum area of water that can be contained
        # Move the pointer pointing to the shorter line inward, as this might increase the area
        # Continue until the two pointers meet

        left = 0
        right = len(height) - 1

        area = 0
        while left < right:
            temp = (right - left) * min(
                height[left], height[right]
            )  # right - left = width and taking the minimum height between the two pointers because the water level is limited by the shorter line

            if temp > area:
                area = temp

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return area
