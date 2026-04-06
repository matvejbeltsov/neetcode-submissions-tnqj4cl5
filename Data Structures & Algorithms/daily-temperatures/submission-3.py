class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                idx_stack, val_stack = stack.pop()
                res[idx_stack] = idx - idx_stack
            stack.append((idx, temp))
        return res
        