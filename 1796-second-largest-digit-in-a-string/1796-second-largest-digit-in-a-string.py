class Solution:
    def secondHighest(self, s: str) -> int:
        digit=set()
        for i in s:
            if i.isdigit():
                digit.add(int(i))
        
        if len(digit)<2:
            return -1
        sortt=sorted(digit,reverse=True)
        return int(sortt[1])