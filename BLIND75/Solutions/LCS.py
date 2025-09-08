class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # First I created a set to get rid of duplicates and allow O(1) lookups
        # Then I loop through each number in the set and check if it's the start of a sequence
        # If it is, I keep checking for the next numbers in the sequence and count the length
        # Finally, I return the longest length found
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while (
                    num + length
                ) in num_set:  # I check with num + length because num is the start of the sequence and length starts at 1 which will check for the next while maintaining the start point
                    length += 1  # I keep checking for the next number in the sequence.
                longest = max(
                    length, longest
                )  # I take the max of the current longest and the new length found

        return longest


# Time Complexity: O(n) because each number is processed at most twice (once in the initial loop and once in the while loop)
# Space Complexity: O(n) because of the set used to store the numbers
