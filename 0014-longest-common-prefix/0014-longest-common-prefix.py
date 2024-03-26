class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # st=''
        # m=len(strs)
        # if m==0:
        #     return st
        # if m<2:
        #     return strs
        # n=0
        # for i in range(m-1):
        #     n=min(len(strs[i]),len(strs[i+1]))
        # for i in range(n):
        #     if strs[0][i]==strs[1][i] and strs[1][i]==strs[2][i]:
        #         st+=strs[0][i]
        #         i+=1
        #     else:
        #         break
        # return st

        short = min(strs, key=len) 
        for item in strs:
            while len(short) > 0:
                if item.startswith(short):
                    break
                else:
                    short = short[:-1]
        return short
                
        