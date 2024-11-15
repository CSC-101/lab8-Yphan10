import unittest
from group import groups_of_3

class TestGroupsOf3(unittest.TestCase):
    def test_full_groups(self):
        # Test case with full groups of three
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_partial_group(self):
        # Test case with a partial final group
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]), [[1, 2, 3], [4, 5, 6], [7, 8]])

    def test_empty_list(self):
        # Test case with an empty list
        self.assertEqual(groups_of_3([]), [])

    def test_one_element(self):
        # Test case with a single element
        self.assertEqual(groups_of_3([1]), [[1]])

    def test_two_elements(self):
        # Test case with two elements
        self.assertEqual(groups_of_3([1, 2]), [[1, 2]])

if __name__ == '__main__':
    unittest.main()
