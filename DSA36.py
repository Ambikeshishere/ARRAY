from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr and curr.next:
            first = curr
            second = curr.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            curr = first.next

        return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head): 
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(" -> ".join(map(str, result)))

if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    head = create_linked_list(input_list)
    solution = Solution()
    swapped_head = solution.swapPairs(head)
    print("Swapped Linked List:")
    print_linked_list(swapped_head)
