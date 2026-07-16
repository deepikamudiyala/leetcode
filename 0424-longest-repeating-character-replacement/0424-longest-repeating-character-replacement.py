class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        repeat = 0
        best = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            repeat = max(repeat, count[s[r]])

            if (r-l+ 1)-repeat > k:
                count[s[l]] -= 1
                l += 1

            best = max(best, r-l+ 1)

        return best