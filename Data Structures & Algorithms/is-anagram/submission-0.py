# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False

#         new_s=sorted(s)
#         new_t=sorted(t)   
        
#         for i in range(0, len(s)):
#             if new_s[i]!=new_t[i]:
#                 return False
#         return True



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      sMap = {}
      tMap = {}


      for i in s:
         if i in sMap:
            sMap[i] +=1
         else:
            sMap[i] =1
      
      
      for j in t:
         if j in tMap:
            tMap[j] +=1
         else:
            tMap[j] = 1

      print(sMap,tMap)
      
      if sMap == tMap:
         return True
      else:
         return False






































