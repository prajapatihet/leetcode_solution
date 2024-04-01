class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int ans = numBottles;
        
        int empty = ans;
        while (empty>=numExchange){
            ans++;
            empty-=numExchange;
            empty++;
            numExchange++;
        }
        return ans;
    }
}