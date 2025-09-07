class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Using a dictionary to count occurrences of each character
        # First count characters in s
        # Then decrement counts based on characters in t
        # Finally, check if all counts are zero
        # If any count is not zero, return False; otherwise, return True

        # Previous solution using sorting:
        # dict_val = {}

        # if len(s) != len(t):
        #     return False

        # for char in s:
        #     if char in dict_val:
        #         dict_val[char] += 1
        #     else:
        #         dict_val[char] = 1

        # for char in t:
        #     if char in dict_val:
        #         dict_val[char] -= 1
        #         if dict_val[char] < 0:
        #             return False
        #     else:
        #         return False

        # for val in dict_val.values():
        #     if val != 0:
        #         return False
        # return True
        #

        check_dict = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i not in check_dict:
                check_dict[i] = 1
            else:
                check_dict[i] += 1

        for j in t:
            if j not in check_dict:
                return False
            else:
                check_dict[j] -= 1

        for k in check_dict:
            if check_dict[k] != 0:
                return False

        return True
