from lib2to3.pgen2.token import EQUAL
import unittest
from linked_lists import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked = LinkedList()
        self.vals = [0,1,0,0,11,11]

    def testAddToTail(self):
        for i in self.vals:
            self.linked.addToTail(i)
        assert self.linked.vals() == self.vals

    def testAddToHead(self):
        for i in self.vals:
            self.linked.addToHead(i)
        assert self.linked.vals() == list(reversed(self.vals))


    def testGetNodeByIndex(self):
        pass
        # self.linked.getNodeByIndex

    def testAdd(self):
        self.linked.addNode(1,0)
        assert self.linked.getNodeByIndex(0).val == 1



class TestRemoveDups(unittest.TestCase):
    def setUp(self):
        self.linked = LinkedList()
        self.vals = [0,1,0,0,11,11]
        for i in self.vals:
            self.linked.addToTail(i)

    def testRemoveDups(self):
        self.linked.removeDups()
        assert self.linked.vals() == [0,1,11]

    def testRemoveDupsPointers(self):
        self.linked.removeDupsPointers()
        assert self.linked.vals() == [0,1,11]

class TestGetKthLast(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.linked = LinkedList()
        self.vals = [0,1,0,0,11,11]
        for i in self.vals:
            self.linked.addToTail(i)

    def testGetFromEnd(self):
        counter = 0
        for i in reversed(self.vals):
            assert self.linked.getFromEnd(counter).val == i
            counter += 1

    def testGetFromEndRec(self):
        counter = 0
        for i in reversed(self.vals):
            assert self.linked.getFromEndRec(counter).val == i
            counter += 1

    def testGetFromEndPointers(self):
        counter = 0
        for i in reversed(self.vals):
            assert self.linked.getFromEndPointers(counter).val == i
            counter += 1

class TestDelMiddleNode(unittest.TestCase):
    def setUp(self):
        self.linked = LinkedList()
        self.vals = [0,1,2,3,4,5,6]
        for i in self.vals:
            self.linked.addToTail(i)

    def testDelMiddleNode(self):
        for i in range(1, len(self.vals)-1):
            result = self.vals[:i]+self.vals[i+1:]
            node = self.linked.getNodeByIndex(i)
            val = node.val
            self.linked.delMiddleNode(node)
            assert self.linked.vals() == result
            self.linked.addNode(val, i)

if __name__ == "__main__":
    unittest.main()