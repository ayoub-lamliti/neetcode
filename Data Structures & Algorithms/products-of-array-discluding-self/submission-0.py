class Solution:
    def calculater(self, index: int, prev: int, nums: list[int]) -> int:
        mod = prev
        for i in range(len(nums) - index):
            try:
                mod *= nums[index + i]
            except:
                ...
        return mod
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        list_num = []
        for i, num in enumerate(nums):
            if i:
                prev *= nums[i - 1]
            list_num.append(self.calculater(i + 1, prev, nums))
        return list_num