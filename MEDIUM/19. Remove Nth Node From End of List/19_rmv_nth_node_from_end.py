# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# First, we need to find the length of the linked list.
# Then, we can find the node to remove by calculating the position from the start.
# Finally, we can remove the node by adjusting the pointers accordingly.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        val = ListNode(0)
        val.next = head
        length = 0
        while val.next != None:
            length += 1
            val = val.next

        node = length - n

        if node == 0:
            head = head.next
        else:
            val = ListNode(0)
            val.next = head

            for i in range(node):
                val = val.next

            val.next = val.next.next

        return head
