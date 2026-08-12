class Solution:
    def calculate(self, s: str) -> int:

        s= s.replace(' ','') + ' '
        sumStack = []
        num = 0
        op = '+'

        for i in range(len(s)):
            currentToken = s[i]
            if(currentToken.isdigit()):
                num = num * 10 + int(currentToken)
            else:
                if op == '+':
                    sumStack.append(int(num))
                if op == '-':
                    sumStack.append(int(-num))
                if op == '*':
                    sumStack.append(int(sumStack.pop() * num))
                if op == '/':
                    sumStack.append(int(sumStack.pop() / num))
                op = currentToken
                num = 0
            
        return sum(sumStack)
        
            

            






        