class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

     sumMap = {}

     for i, n in enumerate(nums):
        sumMap[n] = i

     for i,n in enumerate(nums):
         diff = target - n
         if diff in sumMap and sumMap[diff] != i:
             return([i,sumMap[diff]])

        