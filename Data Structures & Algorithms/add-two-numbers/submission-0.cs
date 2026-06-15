/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode result = new ListNode();
        ListNode resultStart = result;        

        while(l1 != null || l2 != null) {
            var l1v = l1?.val ?? 0;
            var l2v = l2?.val ?? 0;
            var sum = l1v + l2v + carry;

            if (sum >= 10) {
                carry = 1;
                sum -= 10;
            }
            else {
                carry = 0;
            }

            result.next = new ListNode(sum);
            result = result.next;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }

        if (carry == 1) {
            result.next = new ListNode(1);
        }



        return resultStart.next;
    }
}