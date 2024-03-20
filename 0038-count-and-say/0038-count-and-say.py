class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        string='1'
        temp=''
        count=0
        for i in range(n-1):
            s=string[0]
            for char in string:
                if char==s:
                    count+=1
                else:
                    temp+=str(count)+s
                    s=char
                    count=1
            temp+=str(count)+char
            string=temp
            temp=''
            count=0
        return string

        