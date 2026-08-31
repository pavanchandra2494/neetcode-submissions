class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        paranth_close={")":"(","]":"[","}":"{"}
        for c in s:
            if c in paranth_close:
                if stack and stack[-1]==paranth_close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        
            

        