from lib2to3.pgen2.token import EQUAL
import unittest
from linked_lists import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked = LinkedList()

    def testAddToTail(self):
        self.linked.addToTail(1)
        # print(self.linked, self.linked.head.val)
        assert self.linked.head.val == 1

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


if __name__ == "__main__":
    unittest.main()