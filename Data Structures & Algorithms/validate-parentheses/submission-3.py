class Solution:
    def isValid(self, s: str) -> bool:
        dict_bracket_type = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for brac in s:
            if brac in dict_bracket_type:
                if not (stack and (dict_bracket_type[brac] == stack.pop())):
                    return False
            else:
                stack.append(brac)

        return len(stack) == 0

        