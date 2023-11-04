class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        seen = set()
        curr = head
        prev = None

        while curr:
            if curr.val in seen:
                prev.next = curr.next
            else:
                seen.add(curr.val)
                prev = curr
            curr = curr.next



node = ListNode(1)
node.next = ListNode(3)
node.next.next = ListNode(1)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(2)
node.next.next.next.next.next.next = ListNode(2)
node.next.next.next.next.next.next.next = ListNode(3)

def print_list(head):
    # print nodes in the list
    curr = head
    lst = ""
    while curr:
        lst += str(curr.val)
        if curr.next is not None:
            lst += "-->"
        curr = curr.next
    return lst
print(print_list(node))
sol = Solution()
sol.deleteDuplicates(node)
print(print_list(node))
