class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      
      distance = []
      res = []
      r = len(points)
      for i in range(r):
         x = points[i][0]
         y = points[i][1]

         euc = math.sqrt(x**2 + y**2)
         print(euc,x,y)
         distance.append([euc,x,y])
      
      heapq.heapify(distance)
      for j in range(k):
         nearest = heapq.heappop(distance)
         print(nearest)
         res.append([nearest[1],nearest[2]])
         
      return(res)
