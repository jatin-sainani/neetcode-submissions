class Solution:
    def isHappy(self, n: int) -> bool:
       sum = 0
       seen = set()
       print(n)
       print(n/10)
       while(True):

        while(n>0):
            sum += int(math.pow(n%10,2))
            n = int(n/10)
            print("sum: ", sum)
            print("n: ", n)
            print("seen: ", seen)

        if sum == 1:
            return True
        
        if sum in seen:
            return False
        
        seen.add(sum)
        n = sum
        sum = 0


        