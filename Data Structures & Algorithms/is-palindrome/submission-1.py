class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        print('?'.isalnum())


        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                print("what is ",s[r])
                r-=1

            if s[l]!= s[r]:
                print(s[l])
                print(s[r])
                return False
            
            l+=1
            r-=1
        
        return True
        
