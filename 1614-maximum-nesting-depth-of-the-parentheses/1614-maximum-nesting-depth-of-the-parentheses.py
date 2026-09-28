class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        st=[]
        for i in s:
            if i=='(':
                st.append(i)
            elif i==')':
                st.pop()
            ans=max(ans,len(st))
        return ans