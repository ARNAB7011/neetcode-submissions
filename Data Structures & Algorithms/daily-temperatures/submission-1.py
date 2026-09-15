class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        st = []

        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                index = st.pop()
                result[index] = i - index

            st.append(i)

        return result