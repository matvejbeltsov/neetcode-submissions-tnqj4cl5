class Solution:
    def isValid(self, s: str) -> bool:
        type_of_bracket = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []

        for brack in s:
            if brack in type_of_bracket:
                if not (stack and type_of_bracket[brack] == stack.pop()):
                    return False
            else:
                stack.append(brack)
        
        return len(stack) == 0