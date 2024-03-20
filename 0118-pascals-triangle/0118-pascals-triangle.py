class Solution:
    def fact(self,n):
        if n==1:
            return 1
        return n*fact(n-1)
    
    def comb(self,n,r):
        return self.fact(n)/(self.fact(n-r)*self.fact(r))
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                temp.append(comb(i,j))
            arr.append(temp)
        return arr
        