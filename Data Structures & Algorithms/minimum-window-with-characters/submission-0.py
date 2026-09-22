class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Frequency of characters required from t
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        left = 0
        have = 0
        need_count = len(need)

        min_length = float("inf")
        min_start = 0

        for right in range(len(s)):
            ch = s[right]

            # Add character to window
            window[ch] = window.get(ch, 0) + 1

            # Character requirement is satisfied
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Shrink window while it is valid
            while have == need_count:
                # Update minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_start = left

                # Remove leftmost character
                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_start:min_start + min_length]