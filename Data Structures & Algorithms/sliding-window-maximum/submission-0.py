from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        result = []

        for right in range(len(nums)):

            # Remove elements outside the current window
            if dq and dq[0] <= right - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # Add current index
            dq.append(right)

            # Start adding answers once window size reaches k
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result