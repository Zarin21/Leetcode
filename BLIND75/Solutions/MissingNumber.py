class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Using a set to store the numbers in the input list for O(1) lookups
        # Then checking for the missing number in the range from 0 to n
        # First checking for the edge cases where 0 or n is missing
        # Then iterating through the set to find the missing number by checking up or down by 1; if not found, return that number
        nums_set = set(nums)

        if 0 not in nums_set:
            return 0
        if len(nums) not in nums_set:
            return len(nums)

        for i in range(len(nums_set)):

            if nums[i] == len(nums):
                if nums[i] - 1 not in nums_set:
                    return nums[i] - 1
            else:
                if nums[i] + 1 not in nums_set:
                    return nums[i] + 1

        # Time complexity: O(n) where n is the number of elements in the input list
        # Space complexity: O(n) where n is the number of elements in the input list
