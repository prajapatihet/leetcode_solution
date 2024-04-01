class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        st = sorted(s, reverse=True)
        for i in range(len(s) - 1, -1, -1):
            if st[i] == '1':
                st[i], st[-1] = st[-1], st[i]
                break
        return ''.join(st)