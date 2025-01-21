# Remove loop in Linked List
# https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1

# Custom Input format:
# A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.
# The generated output will be true if your submitted code is correct, otherwise, false.

# Input: head = 1 -> 3 -> 4, pos = 2
# Output: true
# Explanation: The linked list looks like
# A loop is present. If you remove it successfully, the answer will be true. 

# Solution:
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        temp_head = head
        prev = head
        while temp_head.next:
            if temp_head.next.data == "":
                prev.next = None
                break
            temp_head.data = ""
            prev = prev.next
            temp_head = temp_head.next
