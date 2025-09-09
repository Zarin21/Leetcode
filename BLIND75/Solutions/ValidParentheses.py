class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # I use a stack to keep track of opening brackets
        # When I encounter a closing bracket, I check if it matches the last opening bracket
        # If it doesn't match or if the stack is empty when I encounter a closing bracket, I return False
        # At the end, if the stack is empty, it means all brackets were matched correctly, so I return True
        # I use a dictionary to map opening brackets to their corresponding closing brackets for easy checking

        stack = []
        opening = {"(": ")", "{": "}", "[": "]"}
        for _ in s:
            if _ in opening:
                stack.append(_)
            else:
                if stack:
                    check = stack.pop()
                    if _ != opening[check]:
                        return False
                else:
                    return False

        if stack:
            return False
        return True

        # Time Complexity: O(n) because we traverse the string once
        # Space Complexity: O(n) in the worst case if all characters are opening brackets
