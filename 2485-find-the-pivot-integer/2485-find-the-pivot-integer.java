class Solution {
    public int pivotInteger(int n) {
        if (n==1){
            return n;
        }
        int pivot = n/2;
        int[] li = new int[n];
        for (int i=0;i<n;i++){
            li[i]=i+1;
        }
        for (int i=pivot;i<n;i++){
            int leftSum=0;
            int rightSum=0;

            for (int j=0;j<i;j++){
                leftSum+=li[j];
            }
            rightSum+=li[i-1];
            for (int j=i;j<n;j++){
                rightSum+=li[j];
            }

            if(leftSum==rightSum){
                return i;
            }
        }
        return -1;
    }
}