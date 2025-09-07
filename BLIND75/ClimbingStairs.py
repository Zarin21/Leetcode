class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Using dynamic programming to find the number of distinct ways to climb to the top
        # The number of ways to reach the nth step is the sum of the ways to reach
        # the (n-1)th step and the (n-2)th step
        # I used a bottom-up approach to build the solution iteratively
        # Space optimization by only keeping track of the last two computed values

        if n == 1:
            return 1
        if n == 2:
            return 2

        one, two = 1, 2

        for i in range(2, n):
            curr_step = one + two
            one = two
            two = curr_step

        return curr_step

    # Time complexity: O(n)
    # Space complexity: O(1)
