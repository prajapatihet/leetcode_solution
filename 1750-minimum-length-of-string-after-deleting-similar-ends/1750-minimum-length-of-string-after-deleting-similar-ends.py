class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r and s[l] == s[r]:
            current = s[l]
            while l <= r and s[l] == current:
                l += 1
            while r >= l and s[r] == current:
                r -= 1
        
        return r - l + 1
        # count=0
        # for i in range(len(s)//2):
        #     if s[i]==s[-1-i]:
        #         count+=2
        #     else:
        #         break
        # return len(s)//2-count
        