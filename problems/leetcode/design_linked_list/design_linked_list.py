#!/usr/bin/env python


##################################
### --- Singly linked list --- ###
##################################


class SinglyLinkedListNode:

    def __init__(self, val):
        self.val = val
        self.next = None



class SinglyLinkedList:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.head = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

        current_node = self.head


        for i in range(index):
            
            current_node = current_node.next

        return current_node.val
            

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        
        new_node = SinglyLinkedListNode(val)
        new_node.next = self.head
        self.head = new_node


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """

        current_node = self.head

        while current_node.next:

            current_node = current_node.next

        new_node = SinglyLinkedListNode(val)

        current_node.next = new_node
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """


        current_node = self.head

        for i in range(index-1):
           
           current_node = current_node.next

        i_prev_node = current_node
        i_next_node = current_node.next

        new_node = SinglyLinkedListNode(val)
        new_node.next = i_next_node

        i_prev_node.next = new_node

        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """

        current_node = self.head

        for i in range(index-1):
           
           current_node = current_node.next

        i_prev_node = current_node
        i_th_node = current_node.next
        i_next_node = i_th_node.next

        del i_th_node

        i_prev_node.next = i_next_node


    def print_contents(self):

        current_node = self.head

        while current_node:

            print(current_node.val)
            current_node = current_node.next



print("--------------------------")
print("--- Singly linked list ---")
print("--------------------------")


sl = SinglyLinkedList()

print('Testing addAtHead()')

sl.addAtHead(5)
sl.addAtHead(4)
sl.addAtHead(3)

v0 = sl.get(0)
v1 = sl.get(1)
v2 = sl.get(2)

print("v0: {}".format(v0))
print("v1: {}".format(v1))
print("v2: {}".format(v2))

print('Testing addAtTail()')

sl.addAtTail(6)
sl.addAtTail(7)
sl.addAtTail(8)

v3 = sl.get(3)
v4 = sl.get(4)
v5 = sl.get(5)

print("v3: {}".format(v3))
print("v4: {}".format(v4))
print("v5: {}".format(v5))

print('Testing addAtIndex()')

sl.addAtIndex(3, 0)
sl.print_contents()

print('Testing deleteIndex()')

sl.deleteAtIndex(5)
sl.print_contents()

##################################
### --- Doubly linked list --- ###
##################################


