class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total=0
        
        for i in range(len(tickets)):
            if i<=k:
                if tickets[i]<tickets[k]:
                    total+=tickets[i]
                else:
                    total+=tickets[k]
            else:
                if tickets[i]<tickets[k]:
                    total+=tickets[i]
                else:
                    total+=tickets[k]-1
        
        return total