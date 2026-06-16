/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB) {
        int sizeA = 0;
        int sizeB = 0;

        var runnerA = headA;
        var runnerB = headB;

        while (runnerA != null) {
            runnerA = runnerA.next;
            sizeA++;
        }

        while (runnerB != null) {
            runnerB = runnerB.next;
            sizeB++;
        }

        runnerB = headB;
        runnerA = headA;

        if (sizeA > sizeB) {
            for (int i = 0; i < sizeA-sizeB; i++) {
                runnerA = runnerA.next;
            }
        }
        else if (sizeB > sizeA) {
            for (int i = 0; i < sizeB-sizeA; i++) {
                runnerB = runnerB.next;
            }
        }

        while(runnerA != null) {
            if (runnerA == runnerB) {
                return runnerA;
            }

            runnerA = runnerA.next;
            runnerB = runnerB.next;
        }

        return null;
    }
}