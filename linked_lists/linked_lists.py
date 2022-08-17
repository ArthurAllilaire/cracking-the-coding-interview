# How to remove all duplicates in a linked list

from ctypes import pointer
from operator import index


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def addToTail(self, val) -> None:
        node = self.head
        if node == None:
            self.head = Node(val)
            return None
        while node.next:
            node = node.next

        node.next = Node(val, None, node)
        return None

    def addToHead(self, val):
        new = Node(val, self.head)
        if self.head:
            self.head.prev = new
        self.head = new

    def addNode(self, val, index):
        if index == 0:
            self.addToHead(val)
            return None
        #Get one before and change next to node
        prev_node = self.head
        for i in range(index-1):
            if prev_node.next:
                prev_node = prev_node.next
            else:
                return -1
                
        new = Node(val, prev_node.next, prev_node)
        if prev_node.next:
            prev_node.next.prev = new
        prev_node.next = new

    def getNodeByVal(self, val) -> int:
        """
        Return -1 if not found else index
        """
        counter = 0
        node = self.head
        while node:
            if node.val == val:
                return counter
            node = node.next
            counter += 1

        return -1

    def getNodeByIndex(self, index):
        """
        Return -1 if not found else node
        """
        node = self.head
        for i in range(index):
            node = node.next

        return node

    def deleteNodeByVal(self, val, all=False):
        """
        Deletes first node with val, or all if all=True
        """
        node = self.head
        while True:
            if val == node.val:
                self.deleteNode(node)
                if not all:
                    break   
            node = node.next

    def deleteNode(self, node):
        if node.prev: #Not at head
            node.prev.next = node.next
        else: # at head
            self.head = node.next 
            self.head.prev = None
            del node

        if node.next: # not at tail otherwise don't need to
            node.next.prev = node.prev

    def removeDups(self):
        """
        Go through the list and remove duplicates
        """
        #Solution 1 - Hash set
        node = self.head
        nodes = set()
        while node:
            old_len = len(nodes)
            nodes.add(node.val)
            if old_len == len(nodes):
                node_to_del = node
                node = node.prev
                self.deleteNode(node_to_del)
            node = node.next
        
        return None

    def removeDupsPointers(self):
        """
        Code when no buffer is possible
        """
        node = self.head
        while node:
            node2 = node.next
            while node2:
                if node2.val == node.val:
                    self.deleteNode(node2)
                node2 = node2.next

            node = node.next

    def getFromEnd(self,index):
        """
        Starts at 0
        """
        len = 0
        node = self.head
        while node:
            len += 1
            node = node.next
        index = len-index
        node = self.head
        for i in range(index-1):
            node = node.next

        return node

    def getFromEndRec(self, index):
        return self.getFromEndReal(self.head, [index, False])

    def getFromEndReal(self, curr, params):
        """
        * @params: [index, reached_bottom]

        """
        if curr.next == None:
            params[1] = True # Reached the bottom
            params[0] += 1
        elif params[1] is False:
            next = self.getFromEndReal(curr.next, params)

        if params[0] == 0:
            return next

        params[0] -= 1
        return curr # Not right index

    def getFromEndPointers(self, index):
        p1 = self.head
        p2 = p1
        for _ in range(index+1):
            p2 = p2.next
        while p2:
            p2 = p2.next
            p1 = p1.next

        return p1

    def vals(self) -> list:
        """
        """
        result = []
        node = self.head
        while node:
            result.append(node.val)
            node = node.next
        return result

    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(node.val)
            node = node.next

        return str(result)



class Node:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)

    