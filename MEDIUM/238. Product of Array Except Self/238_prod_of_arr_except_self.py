class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # So I broke this down into three parts:
        # 1. Calculate the prefix product
        # 2. Calculate the suffix product
        # 3. Multiply the prefix and suffix products to get the answer

        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)
        answer = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_product[i] = nums[i - 1] * prefix_product[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            suffix_product[j] = suffix_product[j + 1] * nums[j + 1]
        for i in range(len(nums)):
            answer[i] = prefix_product[i] * suffix_product[i]

        return answer
