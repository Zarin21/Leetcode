class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # I created an empty list to get the clean characters only from the string, removing all alpha-numeric characters
        # Then I just checked if they both are same from both ways.
        clean_s = []
        for i in s:
            if i.isalnum():
                clean_s += i.lower()
        if clean_s == clean_s[::-1]:
            return True
        return False
