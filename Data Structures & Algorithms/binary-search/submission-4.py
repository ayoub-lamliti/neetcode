class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        height = len(nums) - 1
        while height >= low:
            med = (low + height) // 2 

            if nums[med] == target:
                return med
            elif nums[med] > target:
                height = med - 1
            else:
                low = med + 1
        return -1