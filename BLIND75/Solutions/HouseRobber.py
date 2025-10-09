class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Using dynamic programming to find the maximum amount of money that can be stolen
        # At each house, decide whether to rob it or not based on the maximum amount that can be stolen from previous houses

        # I tracked upto the previous house and the house before that
        # The decision is made by comparing the amount that can be stolen by robbing the current
        stolen = 0

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        one_back = max(
            nums[0], nums[1]
        )  # Represents the best total amount you can steal upto the previous house
        two_back = nums[0]
        for i in range(2, len(nums)):

            stolen = max(
                nums[i] + two_back, one_back
            )  # Deciding whether to rob the current house or not, based on the maximum amount that can be stolen from previous houses
            two_back = one_back
            one_back = stolen

        return stolen

    # Time Complexity: O(n) where n is the number of houses
    # Space Complexity: O(1) since we are using only a constant amount of extra space
