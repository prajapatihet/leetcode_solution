class Solution {
    public int minOperations(int k) {
        int res = Integer.MAX_VALUE;
        int a=1;
        int ops=0;
        int sum=1;
        while(true){
            int dup = ops;
            dup = dup + k/a;
            if (k%a!=0){
                dup+=1;
            }
            if (dup>res){
                break;
            }
            res = Math.min(res,dup);
            a++;
            ops++;
        }        
        return res-1;
    }
}