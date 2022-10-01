
class ListNode {
    // For the Linked List
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    /**
     * Required to be able to run on console.
     * @param args
     */
    public static void main(String[] args) {
        ListNode solution = new ListNode();
        
        ListNode example1 = 
        solution.removeNthFromEnd(
            new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))))
            , 2);
        ListNode example2 = 
        solution.removeNthFromEnd(new ListNode(1)
            , 1);
        ListNode example3 = 
        solution.removeNthFromEnd(new ListNode(1, new ListNode(2))
            , 1);
        
        System.out.printf("Output: {%d,%d,%d,%d}\n", 
            Integer.valueOf(example1.val), 
            Integer.valueOf(example1.next.val), 
            Integer.valueOf(example1.next.next.val), 
            Integer.valueOf(example1.next.next.next.val));
        
        try {
            System.out.printf("Output: {%d}\n", 
                Integer.valueOf(example2.val));
        } catch (Exception e) {
            // To prove that there is no example2.val
            System.out.println("Output: {}");
        }
            
        System.out.printf("Output: {%d}\n", 
            Integer.valueOf(example3.val));
    }

    /**
     * The method provided by https://leetcode.com/problems/remove-nth-node-from-end-of-list/
     * @param head
     * @param n
     * @return ListNode
     */
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);

        ListNode slow = dummy;
        ListNode fast = head;

        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }

        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;
        return dummy.next;
    }
}