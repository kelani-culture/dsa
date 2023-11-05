"""
remove every element equal to the value
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return None
        elif head.next is None:
            return head

        curr = head
        prev = None
        while curr:
            if curr.val == val:
                if curr is head:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
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
head = sol.removeElements(head, 2)
print(print_list(head))
