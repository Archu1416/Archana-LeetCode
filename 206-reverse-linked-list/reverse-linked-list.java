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
    public ListNode reverseList(ListNode head) {
        ListNode p=null;
        ListNode cur=head;
        while(cur!=null){
            ListNode nn=cur.next;
            cur.next=p;
            p=cur;
            cur=nn;

        }
        return p;
    }
}