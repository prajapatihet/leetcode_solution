/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode temp = new ListNode(0);
        temp.next = list1;
        ListNode curr = temp;
        for (int i = 0; i < a; i++) {
            curr = curr.next;
        }
        ListNode leftA = curr;

        for (int i = a; i <= b; i++) {
            curr = curr.next;
        }
        ListNode rightB = curr.next;

        leftA.next = list2;

        while (list2.next != null) {
            list2 = list2.next;
        }
        
        list2.next = rightB;
        
        return temp.next;
    }
}