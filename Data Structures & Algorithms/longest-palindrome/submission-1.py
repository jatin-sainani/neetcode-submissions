class Solution:
    def longestPalindrome(self, s: str) -> int:

      letterMap = {}
      palindrome = 0
      middleLetter = 0

      for i in s:
         if i in letterMap:
            letterMap[i] += 1
         else:
            letterMap[i] = 1
      
      for key, value in letterMap.items():
         print(f"key and value",key,value)
         if value%2 ==0:
            palindrome +=value
         else:
            palindrome +=int(value-1/2)
            if value%2 == 1:
               middleLetter = 1
         
      return int(palindrome+middleLetter)

        