class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans=[]
        for i in range (len(nums)-k+1):
            cur=Counter(nums[i:i+k])
            pair=[]
            for val,freq in cur.items():
                pair.append((freq,val))
            pair.sort(reverse=True)
            total=0
            for freq,val in pair[:x]:
                total+=freq*val
            ans.append(total)
        return ans