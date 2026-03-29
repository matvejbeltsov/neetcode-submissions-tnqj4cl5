class Solution:
    def isValid(self, s: str) -> bool:
        dict_type_of_brackets = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        stack = []

        for c in s:
            if c in dict_type_of_brackets:
                if not (stack and (stack.pop() == dict_type_of_brackets[c])):
                    return False
            else:
                stack.append(c)

        return len(stack) == 0