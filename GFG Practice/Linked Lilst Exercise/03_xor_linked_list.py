# XOR Linked Lis
# https://www.geeksforgeeks.org/problems/xor-linked-list/1

# Solution:
def insert(head, data):
    new_node = Node(data)
    new_node.npx = head
    head = new_node
    return head
    
def getList(head):
    lst = []
    while head:
        lst.append(head.data)
        head = head.npx
    return lst