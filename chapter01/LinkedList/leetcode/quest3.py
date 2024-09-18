class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head):
        if head is None:
            return None
        if head.next is None:
            return head

        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(6)


def print_list(head):
    curr = head
    res = ""
    while curr:
        res += str(curr.val)
        if curr.next is not None:
            res += '--->'
        curr = curr.next
    return res

print(print_list(head))
sol = Solution()
head = sol.reverse(head)
print(print_list(head))
