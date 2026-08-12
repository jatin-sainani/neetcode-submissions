# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         count = {}
#         frequencyBucket = [[] for i in range(0,len(nums)+1)]
#         output = []

#         for i in nums:
#             if i in count:
#                 count[i] +=1
#             else:
#                 count[i] = 1
#         for key, value in count.items():
#             frequencyBucket[value].append(key)
        

#         for j in range(len(frequencyBucket)-1, 0, -1):
#             if len(output)==k:
#                 return output
#             if frequencyBucket[j]!=[]:
#                 for num in frequencyBucket[j]:
#                     output.append(num)

#         return output





























class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        res= []
        for i in nums:
            if i in count:
                count[i] -=1
            else:
                count[i] = -1
        
        # print(count)

        heap = []
        for key, value in count.items():
            heap.append((value,key))

        heapq.heapify(heap)
        # print(heap)

        for j in range(k):
            value, key = heapq.heappop(heap)
            res.append(key)
            # print(key)

        return res
        



        



        
        