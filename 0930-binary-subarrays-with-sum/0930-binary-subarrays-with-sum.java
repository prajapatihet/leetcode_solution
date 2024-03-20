class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        return ex(nums, goal) - ex(nums, goal - 1);
    }
    private int ex(int[] num, int goal) {
        int head, tail = 0, add = 0, result = 0;
        for (head = 0; head < num.length; head++) {
            add += num[head];
            while (add > goal && tail <= head) {
                add -= num[tail];
                tail++;
            }
            result += head - tail + 1;
        }
        return result;
    }
}