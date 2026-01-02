from typing import List

# I use Kadane's algorithm to find the maximum subarray sum.
# I maintain a current sum and a maximum sum.
# I iterate through the array, adding each element to the current sum.
# If the current sum exceeds the maximum sum, I update the maximum sum.
# If the current sum becomes negative, I reset it to zero since a negative sum won't help in finding a larger sum in the future.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0 # negative sum wont help in the future so we reset
        
        return max_sum
    
# Time Complexity: O(n)
# Space Complexity: O(1)