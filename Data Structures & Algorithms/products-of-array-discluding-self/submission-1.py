class Solution:
    def calculater(self, index: int, prev: int, nums: list[int], length: int) -> int:
        for i in range(length - index):
            prev *= nums[index + i]
        return prev


    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prev = 1
        list_num = []
        length = len(nums)
        for i in range(length):
            if i:
                prev *= nums[i - 1]
            list_num.append(self.calculater(i + 1, prev, nums, length))
        return list_num