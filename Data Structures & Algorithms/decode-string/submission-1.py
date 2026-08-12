class Solution:
    def decodeString(self, s: str) -> str:
        resultStack = []

        for i in range(len(s)):
            if s[i] != ']':
                resultStack.append(s[i])
            else:
                substring = ''
                constant = 0
                place = 1
                while resultStack and resultStack[-1] != '[':
                    substring = resultStack.pop() + substring
                    print(resultStack)
                    print(substring)
                
                resultStack.pop() #popping extra [
        
                while resultStack and resultStack[-1].isdigit():
                    constant += int(resultStack.pop()) * place
                    place *= 10
                
                resultStack.append(constant*substring)
    
        return "".join(resultStack)





        