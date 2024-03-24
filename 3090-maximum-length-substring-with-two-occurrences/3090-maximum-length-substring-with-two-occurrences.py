class Solution:
    def maximumLengthSubstring(self, s,k=2):
        count = {}
        res = 0
        l = 0
        r = 0
        while r < len(s):
            c = s[r]
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
            while count[c] > 2:
                d = s[l]
                if count[d] > 1:
                    count[d] -= 1
                else:
                    count.pop(d)
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res