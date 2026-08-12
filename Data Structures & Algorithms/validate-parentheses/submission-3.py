class Solution:
    def isValid(self, s: str) -> bool:
        paraStack = []
        
        for i in s:
            print(paraStack)
            if i == ')':
                if not paraStack:
                    return False
                if paraStack.pop() != '(':
                    return False
            
            elif i == ']':
                if not paraStack:
                    return False
                if paraStack.pop() != '[':
                    return False
            
            elif i == '}':
                if not paraStack:
                    return False
                if paraStack.pop() != '{':
                    return False
            else:
                paraStack.append(i)
        
        if paraStack:
            return False
        else:
            return True
        