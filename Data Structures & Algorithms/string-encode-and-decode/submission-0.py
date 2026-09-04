class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != '#':
                j += 1

            # Get the length of the string
            length = int(s[i:j])

            # Get the actual string
            j += 1
            result.append(s[j:j + length])

            # Move to the next encoded string
            i = j + length

        return result