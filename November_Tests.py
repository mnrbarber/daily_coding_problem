from unittest import TestCase

from November_2020 import sum_values_to_k


class SumValuesToK(TestCase):
    def setUp(self):
        self.k = 17
        self.true_list = [10, 15, 3, 7]
        self.false_list = [10, 15, 3, 8, 11]

    def test_true_list(self):
        self.assertTrue(sum_values_to_k(self.true_list, self.k))

    def test_false_list(self):
        self.assertFalse(sum_values_to_k(self.false_list, self.k))

