class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int total=0;
        int n = nums.length;
        if (k==0){
            return total;
        }
        for (int i=0;i<n;i++){
            int mul=1;
            for (int j=i;j<n;j++){
                mul*=nums[j];
                if(mul<k){
                    total+=1;
                }else{
                    break;
                }
            }
        }
        return total;
    }
}