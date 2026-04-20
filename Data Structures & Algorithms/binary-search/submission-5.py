class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        height = len(nums) - 1
        while height >= low:
            med = (low + height) // 2 

            if nums[med] < target:
                low = med + 1
            elif nums[med] > target:
                height = med - 1
            else:
                return med
        return -1