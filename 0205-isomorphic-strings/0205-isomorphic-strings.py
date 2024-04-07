class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        maps = {}
        val = set()

        for i in range(len(s)):
            if s[i] in maps:
                if maps[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in val:
                    return False
                maps[s[i]] = t[i]
                val.add(t[i])
        return True