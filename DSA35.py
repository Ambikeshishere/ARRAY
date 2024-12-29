from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(l1, l2))
            lists = temp

        return lists[0]

    def merge_lists(self, l1, l2):
        node = ListNode()
        ans = node

        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next

        if l1:
            node.next = l1
        else:
            node.next = l2

        return ans.next


# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to print a linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(" -> ".join(map(str, result)))


# Example usage
if __name__ == "__main__":
    # Example input: list of lists
    input_lists = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6]
    ]

    # Convert input lists to linked lists
    linked_lists = [create_linked_list(lst) for lst in input_lists]

    # Merge the linked lists
    solution = Solution()
    merged_list = solution.mergeKLists(linked_lists)

    # Print the merged linked list
    print("Merged Linked List:")
    print_linked_list(merged_list)

