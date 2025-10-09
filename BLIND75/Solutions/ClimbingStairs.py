class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Using dynamic programming to find the number of distinct ways to climb to the top
        # The number of ways to reach the nth step is the sum of the ways to reach
        # the (n-1)th step and the (n-2)th step because from those steps you can take
        # either 1 step or 2 steps to reach the nth step.
        # This is similar to the Fibonacci sequence where each number is the sum of
        # the (n-1)th step and the (n-2)th step
        # Recurrence relation: dp[n] = dp[n-1] + dp[n-2]
        # Base cases: dp[1] = 1, dp[2] = 2
        # dp array to store the number of ways to reach each step

        # I used a bottom-up approach to build the solution iteratively
        # Space optimization by only keeping track of the last two computed values

        # Bottom up(tabulaton) approach with space optimization
        # Another way of dp is Top down (Memoization)

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
