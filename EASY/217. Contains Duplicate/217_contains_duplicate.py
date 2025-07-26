class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Putting all elements in a set to check for duplicates
        # If a duplicate is found, return True; otherwise, return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
