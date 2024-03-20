class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        maxl=0
        group=set()
        left=0
        for right in range(l):
            if s[right] not in group:
                group.add(s[right])
                maxl=max(maxl,right-left+1)
            else:
                while s[right] in group:
                    group.remove(s[left])
                    left+=1
                group.add(s[right])
        return maxl
        