from Ex2 import numberInInterval
import unittest


class TestExample(unittest.TestCase):

    def testInInterval(self):
        self.assertEqual(numberInInterval(50), 'In interval!')

    def testLess(self):
        self.assertEqual(numberInInterval(-50), 'Less!')

    def testGreater(self):
        self.assertEqual(numberInInterval(1000), 'Greater!')

    def testWrongInput(self):
        self.assertEqual(numberInInterval('Input'),
                         'Your input is not integer!')


# Необходимо установить coverage.py: pip install pytest-cov
# Затем протестировать: coverage run -m unittest Ex1_test.py
# И вывести отчет: coverage report -m


# if __name__ == '__main__':
#     unittest.main()
