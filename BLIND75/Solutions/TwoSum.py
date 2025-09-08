class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Using a dictionary to store the indices of the numbers
        # Then for each number, I check if the complement (target - number) exists in the dictionary
        # If it does, I return the indices of the two numbers
        num_map = {}

        for i in range(len(nums)):
            num_map[nums[i]] = i

        for k in range(len(nums)):
            j = target - nums[k]
            if j in num_map and num_map[j] != k:
                if k < num_map[j]:
                    return [k, num_map[j]]
                else:
                    return [num_map[j], k]
