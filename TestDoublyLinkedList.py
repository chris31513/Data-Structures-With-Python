import unittest
from DoublyLinkedList import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):

    def test_add(self):
        l = DoublyLinkedList()
        for i in range(100):
            l.add(i)
        self.assertTrue(l.contains(1))
        self.assertFalse(l.contains(1000))

    def test_delete(self):
        l = DoublyLinkedList()
        for i in range(10):
            l.add(i)
        l.delete(10)
        self.assertTrue(l.contains(1))
        self.assertFalse(l.contains(10))

    def test_contains(self):
        l = DoublyLinkedList()
        l.clean()
        l.add("hola")
        self.assertTrue(l.contains("hola"))

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestDoublyLinkedList)

    unittest.TextTestRunner(verbosity=2).run(suite)
        
