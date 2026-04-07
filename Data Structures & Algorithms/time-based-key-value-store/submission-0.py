class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.dict[key]) - 1
        res = ''

        while left <= right:
            mid = (left + right) // 2

            if self.dict[key][mid][0] == timestamp:
                return self.dict[key][mid][1]
            
            elif self.dict[key][mid][0] > timestamp:
                right = mid - 1
            else:
                res = self.dict[key][mid][1]
                left = mid + 1
        return res