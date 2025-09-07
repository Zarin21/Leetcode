class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Using a dictionary to track occurrences of each number
        # If a number appears more than once, return True
        # Otherwise, return False

        # Previous solution using a set:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        num_dict = {}

        for num in nums:
            if num not in num_dict:
                num_dict[num] = True  # Or 1 also works
            else:
                return True

        return False


# Both are O(n) time, O(n) space.
# Set is slightly lighter in space (stores just the key instead of key+value) and cleaner in code.
