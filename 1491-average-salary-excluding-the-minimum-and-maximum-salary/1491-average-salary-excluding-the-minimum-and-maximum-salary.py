class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)
        sum=0
        c=0
        for i in range(1,n-1):
            sum+=salary[i]
            c+=1

        return sum/c
        