class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Using a hashmap to store the indices of the numbers

        # Then for each number, I check if the complement (target - number) exists in the hashmap, applying the 2-sum logic
        # If it does, I add the triplet to the answer list
        # To avoid duplicates, I use a set to track seen triplets
        # Finally, I return the answer list
        num_map = {}  # maps number to the indices
        for i in range(len(nums)):
            num_map[nums[i]] = i

        answer = []

        seen = set()
        for j in range(len(nums)):
            # 2sum starts
            target = -nums[j]  # target = num
            for k in range(j + 1, len(nums)):  # k = index
                remaining = target - nums[k]  # remaining = num
                if remaining in num_map and (
                    num_map[remaining] != j and num_map[remaining] != k
                ):
                    triplet = tuple(sorted([nums[j], nums[k], remaining]))
                    if triplet not in seen:
                        seen.add(triplet)
                        answer.append(list(triplet))
        return answer


# People do 2 pointer approach with sorting i know. Both are O(n^2) time, O(n) space anyways.
