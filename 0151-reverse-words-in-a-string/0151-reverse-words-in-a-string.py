class Solution:
    def reverseWords(self, s: str) -> str:
        i = s.split()
        i.reverse()

        return ' '.join(i)