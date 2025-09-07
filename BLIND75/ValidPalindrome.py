class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Clean the string by removing non-alphanumeric characters and converting to lowercase
        # Use two pointers to check for palindrome
        # If characters at both pointers match, move inward; otherwise, return False
        # If all characters match, return True

        clean_s = []
        for i in range(len(s)):
            if s[i].isalnum():
                clean_s.append(s[i].lower())
        left = 0
        right = len(clean_s) - 1

        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        return True
