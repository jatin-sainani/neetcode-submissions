# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r-l+1)
#         return res
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      if s == "":
         return 0
      l,r = 0,1
      substring = {s[l]: l}
      maxSize = 1

      for i in range (len(s)-1):
         while s[r] in substring :
            del substring[s[l]]
            l+=1
         substring[s[r]] = r
         r+=1
         maxSize = max(maxSize, r-l)
         
         
      return maxSize
      




        
        




































