from Ex1 import evenOddNumber
import unittest


class TestExample(unittest.TestCase):

    def testOdd(self):
        self.assertEqual(evenOddNumber(5), 'Odd!')

    def testEven(self):
        self.assertEqual(evenOddNumber(0), 'Even!')

    def testWrongInput(self):
        self.assertEqual(evenOddNumber('Input'), 'Your input is not integer!')


# Необходимо установить coverage.py: pip install pytest-cov
# Затем протестировать: coverage run -m unittest Ex1_test.py
# И вывести отчет: coverage report -m


# if __name__ == '__main__':
#     unittest.main()
