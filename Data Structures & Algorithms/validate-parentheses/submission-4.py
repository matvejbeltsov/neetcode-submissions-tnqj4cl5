class Solution:
        def isValid(self, s: str) -> bool:
            dict_type_bracket = {')': '(', ']': '[', '}': '{'}

            stack = []

            for brac in s:
                if brac in dict_type_bracket:
                    if not (stack and (dict_type_bracket[brac] == stack.pop())):
                        return False
                else:
                    stack.append(brac)
            
            return len(stack) == 0
        