class Solution:
    def isValid(self, s: str) -> bool:

        paris = {')':'(',
        ']':'[',
        '}':'{'
        }
        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] != paris[i]:
                    return False
            
                stack.pop()

        return stack == []
            
