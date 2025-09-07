class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Kadane's Algorithm to find the maximum subarray sum
        # Iterate through the array, keeping track of the current sum and the maximum sum found so far
        # If the current sum becomes negative, reset it to zero as starting a new subarray

        max_sum = float("-inf")
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if (
                curr_sum < 0
            ):  # If the current sum is negative, reset it to zero because this wont profit the a new subarray as we move forward
                curr_sum = 0
        return max_sum

    # Time Complexity: O(n) where n is the number of elements in the array
    # Space Complexity: O(1) since we are using only a constant amount of extra
