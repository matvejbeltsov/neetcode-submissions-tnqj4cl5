class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        stack = []

        for idx, elem in enumerate(temperatures):
            while stack and elem > stack[-1][0]:
                prev_elem, prev_idx = stack.pop()

                res[prev_idx] = idx - prev_idx
            
            stack.append((elem, idx))
        return res