# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# I created two new nodes, one to keep track of the head and one to build the new list.
# I needed the head node to return the head.next.next which is the actual head and new is pointer towards the real head and head is pointing to new
# I used a while loop to iterate through both lists until one of them is empty.
# Inside the loop, I compared the values of the current nodes of both lists and appended the smaller value to the new list.
# I then moved the pointer of the list from which I took the value to the next node.
# After the loop, I checked if there are any remaining nodes in either list and appended them to the new list.
# Finally, I returned the head of the merged list, which is head.next.next.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new = ListNode()
        head = ListNode()

        head.next = new
      
        while list1 and list2:
            if list1.val < list2.val:
                new.next = list1
                list1 = list1.next
            else:
                new.next = list2
                list2 = list2.next
            
            new = new.next
        if list1:
            new.next = list1
        if list2:
            new.next = list2
            
        return head.next.next
    
    # Time Complexity: O(n + m) where n and m are the lengths of list1 and list2 respectively.
    # Space Complexity: O(1) because we are not using any extra space that grows with the input size.