class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

     sumMap = {}

     for i, n in enumerate(nums):
        sumMap[n] = i
     print(sumMap)
     for i,n in enumerate(nums):
        diff = target - n
        if diff in sumMap and sumMap[diff] != i:
            return([i,sumMap[diff]])


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#       sumMap = {}

#       for i in nums:
#          sumMap[i] = (target-i)

#       for index,key in enumerate(sumMap):
#          if sumMap[key] in (sumMap):
#             second_index = list(sumMap).index(sumMap[key])
#             if second_index!=index:
#                return([index,second_index])
      











































        