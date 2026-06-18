class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h1 = {
            "}" :"{", 
            "]" : "[",
            ")" :"("
        }

        for i in s:
            if i not in h1:
                stack.append(i)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if h1[i] != x:
                    return False 
        if stack:
            return False
        return True 

    
        