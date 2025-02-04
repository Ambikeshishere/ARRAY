class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(start: ListNode, end: ListNode) -> ListNode:
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            kth = prev_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_start = prev_group_end.next
            next_group_start = kth.next

            
            reversed_group_start = reverse(group_start, next_group_start)

            prev_group_end.next = reversed_group_start
            group_start.next = next_group_start

            prev_group_end = group_start

def print_list(node: ListNode):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    k = 3  
    print("Original Linked List:")
    print_list(head)

    solution = Solution()
    new_head = solution.reverseKGroup(head, k)

    print(f"\nLinked List after reversing in groups of {k}:")
    print_list(new_head)
