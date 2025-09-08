class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Using a sliding window approach with two pointers and a set to track characters in the current window
        # If a repeating character is found, move the left pointer to the right until the repeating character is removed
        # Update the maximum length of the substring found so far

        left = 0
        check = set()

        s_len = 0
        for right in range(len(s)):
            if s[right] in check:
                while (
                    s[right] in check
                ):  # This loop will run until the repeating character is removed from the set; in the worst case, it will run n times
                    check.remove(s[left])
                    left += 1
            check.add(s[right])
            if s_len < (
                right - left + 1
            ):  # I was putting this in the if condition before, but it should be outside to update the length every time.
                s_len = right - left + 1

        return s_len
