import unittest
from task_1 import convert_commulative, check_intersection


class MyTestCase(unittest.TestCase):

    def test_commulative(self):
        _input = [1, 2, 2, -1, 2]
        right_answer = [1, 3, 5, 4, 6]
        _output = convert_commulative(_input)
        self.assertEqual(_output, right_answer)

    def test_check_intersection(self):
        first_input = [0, 3]
        second_input = [3, 0]
        right_answer = [[0.5, 1.5]]
        output = check_intersection(first_input, second_input)
        self.assertEqual(right_answer, output)

    def test_check_not_intersection(self):
        first_input = [1, 2]
        second_input = [5, 5]
        right_answer = []
        output = check_intersection(first_input, second_input)
        self.assertEqual(right_answer, output)

if __name__ == '__main__':
    unittest.main()
