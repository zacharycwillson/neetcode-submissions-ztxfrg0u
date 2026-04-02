class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)

        for i, num in enumerate(nums):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                product = product * nums[j]
            res[i] = product
        return res


        