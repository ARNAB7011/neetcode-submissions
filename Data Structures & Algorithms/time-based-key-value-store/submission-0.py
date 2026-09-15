class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key, value, timestamp):
        if key not in self.data:
            self.data[key] = []

        self.data[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.data:
            return ""

        values = self.data[key]

        left = 0
        right = len(values) - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                answer = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return answer