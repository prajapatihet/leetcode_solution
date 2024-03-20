class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a = Counter(tasks)
        maaxi = max(a.values())
        return max(len(tasks),(maaxi-1)*(n+1)+list(a.values()).count(maaxi))
        