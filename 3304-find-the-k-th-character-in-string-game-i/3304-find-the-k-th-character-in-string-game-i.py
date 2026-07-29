class Solution:
    def kthCharacter(self, k: int) -> str:
        asc=[0]
        while len(asc)<k:
            for i in range(len(asc)):
                asc.append((asc[i]+1)%26)
        return chr(asc[k-1]+ord('a'))