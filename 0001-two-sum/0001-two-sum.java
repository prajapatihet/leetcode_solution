class Solution {
    public int[] twoSum(int[] num, int target) {
        int[] ret = new int[2];
        for(int i=0;i<num.length;i++){
            for(int j=i+1;j<num.length;j++){
                if(num[i] + num[j] == target) {
                    ret[0] = i;
                    ret[1] = j;
                }
            }
        }
        return ret;
    }
}