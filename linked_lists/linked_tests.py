import unittest
from linked_lists import LinkedList
import random

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

class TestPartition(unittest.TestCase):
    def setUp(self):
        num_lists = 5
        num_terms = 10
        self.lists = [list() for i in range(num_lists)]
        self.vals = [list() for i in range(num_lists)]
        for j in range(num_lists):
            self.lists[j] = LinkedList()
            for i in range(num_terms):
                #Create a list of vals randomly
                rint = random.randint(0,9)
                self.vals[j].append(rint)
                self.lists[j].addToTail(rint)

    def testPartition(self):
        """
        If nodes are less than x delete and add to Head
        """
        par = 5
        for linked in self.lists:
            linked.partition(par)
            vals = linked.vals()
            par_reached = False
            for i in range(len(vals)):
                val = vals[i]
                if par_reached is False:
                    if val >= par:
                        par_reached = True
                elif val < par:
                    assert False, f'{vals}'
                    
class TestListSum(unittest.TestCase):
    def setUp(self):
        num_lists = 2
        num_terms = 5
        self.lists = [list() for i in range(num_lists)]
        self.vals = [list() for i in range(num_lists)]
        for j in range(num_lists):
            self.lists[j] = LinkedList()
            for i in range(num_terms):
                #Create a list of vals randomly
                rint = random.randint(0,9)
                self.vals[j].append(rint)
                self.lists[j].addToTail(rint)

    def testListSum(self):
        """
        If nodes are less than x delete and add to Head
        """
        result_sum = self.getResultSum()

        result = self.lists[0].sumLists(self.lists[1])

        assert result.sum() == result_sum

    def getResultSum(self, rev=False):
        result_sum = 0
        for val in self.vals:
            num = []
            if rev is False:
                val = reversed(val)
            for i in val:
                num.append(str(i))
            result_sum += int("".join(num))

        return result_sum

    def testSum(self):
        for rev in [False, True]:
            result_sum = self.getResultSum(rev)
            real_sum = 0
            for linked in self.lists:
                real_sum += linked.sum(rev)

            assert result_sum == real_sum

    def testSumListsRec(self):
        for rev in [False, True]:
            real_sum = self.lists[0].sumListsRec(self.lists[1], rev)
            assert self.getResultSum(rev) == real_sum.sum(rev), f'Reversed: {rev}'

    def testSumListsRecDiff(self):
        #Test different length nodes
        for rev in [False, True]:
            pass


if __name__ == "__main__":
    unittest.main()