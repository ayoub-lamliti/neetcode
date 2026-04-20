class Solution:
    def calculater(self, index: int, prev: int, nums: list[int], length: int) -> int:
        for i in range(length - index):
            prev *= nums[index + i]
        return prev


    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result