# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#      sumMap = {}

#      for i, n in enumerate(nums):
#         sumMap[n] = i
#      print(sumMap)
#      for i,n in enumerate(nums):
#         diff = target - n
#         if diff in sumMap and sumMap[diff] != i:
#             return([i,sumMap[diff]])


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      sumMap ={}

      for index, value in enumerate(nums):
            sumMap[value] = index
      
      print(sumMap)

      for i in range(0,len(nums)):
         diff = target - nums[i]
         if (diff in sumMap and sumMap[diff]!=i):
            return([i,sumMap[diff]])
            














































        