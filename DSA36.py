#Given the  HEad of a linked list, reverse the nodes of the list k ata a time, and return the modified list.
# K is a positive integer and is less than or equal to the length of the linked list. If the numbers of nodes is nota a multiple of k then left-out nodes, in the end, should remain as it it.
#You may not akter the cakues in the list's nodes only nodesd themselves

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    count = 0
    
    # First pass: count the number of nodes in the list
    while curr.next:
        curr = curr.next
        count += 1
    
    prev = dummy
    while count >= k:
        curr = prev.next
        nxt = curr.next
        for _ in range(1, k):
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            nxt = curr.next
        prev = curr
        count -= k
    
    return dummy.next

# Example usage:
# Define the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse in groups of 2
new_head = reverseKGroup(head, 2)

# Print the reversed linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
# Output should be: 2 -> 1 -> 4 -> 3 -> 5 -> 

