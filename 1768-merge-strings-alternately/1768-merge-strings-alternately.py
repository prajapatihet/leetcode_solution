class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # w1=list(word1)
        # w2=list(word2)
        # wo1=len(w1)
        # wo2=len(w2)
        i=0
        j=0
        arr=[]
        while i<len(word1) and j<len(word2):
            arr.append(word1[i])
            arr.append(word2[j])
            i+=1
            j+=1
        while i<len(word1):
            arr.append(word1[i])
            i+=1
        while j<len(word2):
            arr.append(word2[j])
            j+=1
        
        s=''.join(arr)
        return s

