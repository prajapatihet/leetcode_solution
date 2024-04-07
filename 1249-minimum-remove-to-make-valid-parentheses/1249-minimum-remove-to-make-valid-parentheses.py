class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st=[]
        for i,c in enumerate(s):
            if c =='(':
                st.append(i)
            elif c == ')':
                if st and s[st[-1]] == '(':
                    st.pop()
                else:
                    st.append(i)

        res = []
        for i,c in enumerate(s):
            if st and i==st[0]:
                st.pop(0)
                continue
            res.append(c)
        return ''.join(res)