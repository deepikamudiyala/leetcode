class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            idx=s.index(i)
            if s.count(i)==1:
                return idx
        return -1