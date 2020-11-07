from unittest import TestCase

from november2020 import sum_values_to_k, product_array


class SumValuesToK(TestCase):
    def setUp(self):
        self.k = 17
        self.true_list = [10, 15, 3, 7]
        self.false_list = [10, 15, 3, 8, 11]

    def test_true_list(self):
        self.assertTrue(sum_values_to_k(self.true_list, self.k))

    def test_false_list(self):
        self.assertFalse(sum_values_to_k(self.false_list, self.k))


class ProductArrayTestCase(TestCase):
    def setUp(self):
        self.lst = [1, 2, 3, 4, 5]
        self.lst_output = [120, 60, 40, 30, 24]
        self.lst_2 = [3, 2, 1]
        self.lst_2_output = [2, 3, 6]

    def test_product_array(self):
        self.assertEqual(self.lst_output, product_array(self.lst))
        self.assertEqual(self.lst_2_output, product_array(self.lst_2))
