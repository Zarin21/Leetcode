from typing import List

# I defined a dictionary to store the numbers and their indices.
# Then I loop through the list and check if the complement (target - current number) exists in the dictionary.
# If it does, I return the indices of the two numbers.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num_dict = {}
        for i in range(len(numbers)):
            num_dict[numbers[i]] = i + 1

        for i in range(len(numbers)):
            if target - numbers[i] in num_dict:
                return i+1, num_dict[target-numbers[i]]

# Time Complexity: O(n)
# Space Complexity: O(n)
# However, since the input array is sorted, we can use the two-pointer technique to achieve O(1) space complexity.