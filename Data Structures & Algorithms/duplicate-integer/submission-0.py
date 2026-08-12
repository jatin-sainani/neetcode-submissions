class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numMap = {}

        for index, value in enumerate(nums):
            if value in numMap:
                return True
            else:
                numMap[value] = index
        
        return False