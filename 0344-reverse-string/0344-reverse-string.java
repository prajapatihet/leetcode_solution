class Solution {
    public void reverseString(char[] ch) {
        int s=0;
        int e=ch.length-1;
        while(s<=e){
            char a = ch[s];
            ch[s]=ch[e];
            ch[e]=a;
            s++;
            e--;
        }
    }
}