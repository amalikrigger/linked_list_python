import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_append(self):
        self.list.append(10)
        self.assertEqual(self.list.length(), 1)
        self.list.append(20)
        self.assertEqual(self.list.length(), 2)
        self.assertTrue(self.list.contains(20))

    def test_prepend(self):
        self.list.prepend(10)
        self.assertEqual(self.list.length(), 1)
        self.list.prepend(20)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.index_of(20), 0)

    def test_insert_at(self):
        self.list.append(1)
        self.list.append(3)
        self.list.insert_at(1, 2)
        self.assertEqual(self.list.index_of(2), 1)
        with self.assertRaises(IndexError):
            self.list.insert_at(10, 99)

    def test_delete_by_value(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.delete_by_value(2)
        self.assertFalse(self.list.contains(2))
        self.assertEqual(self.list.length(), 2)
        self.list.delete_by_value(1)
        self.assertFalse(self.list.contains(1))
        self.assertEqual(self.list.length(), 1)

    def test_delete_at(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.list.delete_at(1)
        self.assertFalse(self.list.contains(20))
        self.assertEqual(self.list.length(), 2)
        with self.assertRaises(IndexError):
            self.list.delete_at(5)

    def test_index_of(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c')
        self.assertEqual(self.list.index_of('b'), 1)
        self.assertEqual(self.list.index_of('z'), -1)

    def test_contains(self):
        self.list.append(100)
        self.assertTrue(self.list.contains(100))
        self.assertFalse(self.list.contains(200))

    def test_length(self):
        self.assertEqual(self.list.length(), 0)
        self.list.append(1)
        self.list.append(2)
        self.assertEqual(self.list.length(), 2)

    def test_clear(self):
        self.list.append(1)
        self.list.append(2)
        self.list.clear(None)
        self.assertEqual(self.list.length(), 0)
        self.assertFalse(self.list.contains(1))

    def test_reverse(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.reverse()
        self.assertEqual(self.list.index_of(3), 0)
        self.assertEqual(self.list.index_of(1), 2)

    def test_print_method(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(self.list.print(), '1 -> 2 -> 3 -> None')

    def test_print_empty_list(self):
        self.assertEqual(self.list.print(), ' -> None')

    def test_print_single_element(self):
        self.list.append('a')
        self.assertEqual(self.list.print(), 'a -> None')

    def test_print_after_delete(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.delete_at(1)
        self.assertEqual(self.list.print(), '1 -> 3 -> None')

    def test_print_after_clear(self):
        self.list.append(5)
        self.list.clear(None)
        self.assertEqual(self.list.print(), ' -> None')

    def test_print_after_reverse(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.reverse()
        self.assertEqual(self.list.print(), '3 -> 2 -> 1 -> None')

    def test_reverse_single_element(self):
        self.list.append('X')
        self.list.reverse()
        self.assertEqual(self.list.print(), 'X -> None')

    def test_reverse_empty_list(self):
        self.list.reverse()
        self.assertEqual(self.list.print(), ' -> None')

    def test_contains_on_empty_list(self):
        self.assertFalse(self.list.contains(10))

    def test_index_of_empty_list(self):
        self.assertEqual(self.list.index_of(100), -1)

    def test_multiple_deletes(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.list.delete_by_value(10)
        self.list.delete_by_value(30)
        self.assertEqual(self.list.print(), '20 -> None')

    def test_insert_at_zero_on_empty(self):
        self.list.insert_at(0, 'start')
        self.assertEqual(self.list.print(), 'start -> None')

    def test_insert_at_size_minus_one(self):
        self.list.append(1)
        self.list.append(2)
        self.list.insert_at(1, 1.5)
        self.assertEqual(self.list.print(), '1 -> 1.5 -> 2 -> None')

    def test_append_after_clear(self):
        self.list.append(1)
        self.list.clear(None)
        self.list.append(2)
        self.assertEqual(self.list.print(), '2 -> None')

    def test_prepend_after_clear(self):
        self.list.append(1)
        self.list.clear(None)
        self.list.prepend(0)
        self.assertEqual(self.list.print(), '0 -> None')

    def test_mixed_operations(self):
        self.list.prepend(3)
        self.list.append(4)
        self.list.insert_at(1, 'middle')
        self.list.delete_by_value(3)
        self.list.prepend('start')
        self.assertEqual(self.list.print(), 'start -> middle -> 4 -> None')


if __name__ == '__main__':
    unittest.main()
