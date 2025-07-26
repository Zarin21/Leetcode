class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Creating a dictionary with Keys being the characters of the strings and values being the number of times it appeared
        # For the first string, I keep adding the strings and keep a count of their occurrence
        # Then I use the same dictionary, but this time I substract each time I find the same char
        # If the value of any char gets negative or it's not in the dict in first place, then it's not an Anagram
        # In the end, if any value remains non zero, it's not an Anagram
        # I checked at first if the lengths were equal because if they are of different lengths they can never be Anagrams
        dict_val = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in dict_val:
                dict_val[char] += 1
            else:
                dict_val[char] = 1

        for char in t:
            if char in dict_val:
                dict_val[char] -= 1
                if dict_val[char] < 0:
                    return False
            else:
                return False

        for val in dict_val.values():
            if val != 0:
                return False
            return True
