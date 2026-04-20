class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp: set = list()
        for n in nums:
            if n not in temp:
                temp.append(n)
            else:
                return True
        return False