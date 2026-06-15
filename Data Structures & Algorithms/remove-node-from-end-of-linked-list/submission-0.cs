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
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        var left = head;
        var right = head;

        for (int i = 0; i < n; i++) {
            if (right == null) {
                return head;
            }
            right = right.next;
        }

        if (right == null) {
            return left.next;
        }
        
        while (right != null && right.next != null) {
            left = left.next;
            right = right.next;
        }
        
        if (left.next != null) {
            left.next = left.next.next;
        }
        return head;
    }
}