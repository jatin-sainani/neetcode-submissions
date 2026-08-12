class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

      l = 0
      # r = 0, k-1
      # res = arr[l:r+1]

      # print(res)
      # q= collections.deque()
      # for i in range(l,r+1):
      #    q.append(abs(arr[i]-x))
      #    # print(abs(arr[i]-x))
      
      # # print(q)

      for j in range(k,len(arr)):
         diff = abs(arr[j] - x)
         print(f"diff",diff)
         if diff<abs(arr[l]-x):
            # r+=1
            l+=1
            # print(res)
         # else:
         #    break
      return(arr[l:l+k])
         
      
      
        