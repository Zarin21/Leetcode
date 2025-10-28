from typing import List

# I used a dynamic programming approach to solve the Longest Increasing Subsequence (LIS) problem.
# I created an array `LIS` where each element at index `i` represents the length of the longest increasing subsequence that ends with the element at index `i`. 
# I initialized all elements of `LIS` to 1, since the minimum length of an increasing subsequence that includes any single element is 1. 
# I then iterated through the input array `nums` in reverse order.
# For each element, I checked all subsequent elements to see if they are greater than the current element.
# If they are, I updated the `LIS` value for the current element to be the maximum of its current value
# and 1 plus the `LIS` value of the subsequent element. Finally, I returned the maximum value from the `LIS` array,
# which represents the length of the longest increasing subsequence in the entire array.


# ATTACHED: NEETCODE
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1 , -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)
    
# Time Complexity: O(n^2), where n is the length of the input array `nums`.
# Space Complexity: O(n), where n is the length of the input array `nums`, due to the additional `LIS` array used for dynamic programming.