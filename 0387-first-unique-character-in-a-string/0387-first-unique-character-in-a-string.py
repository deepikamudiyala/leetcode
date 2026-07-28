class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            idx=s.index(i)
            if i not in s[idx+1:]:
                return idx
        return -1