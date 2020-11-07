
"""November 2020 Daily Coding Problems"""
from functools import reduce


def sum_values_to_k(lst, k):
    """5th November: Given a list of numbers and a number k, return whether any two numbers from the list add up to k"""
    """Thoughts on solution: 
        - Initially loop through list twice in full and see whether the sum ever equals k
        - Change to only loop through the later indices than the list
        - BONUS: If you can only loop the list once how could you implement this"""
    for i, x in enumerate(lst):
        j = i + 1
        while j < len(lst):
            if x + lst[j] == k:
                return True
            j += 1
    else:
        return False


def product_array(lst):
    """6th November: Given an array of integers, return  a new array such that each element ar index i of the new array
    is the product of all the numbers in the original array except the one at i.
    Bonus: What if you can't use divide?"""
    product = reduce(lambda x, y: x*y, lst)
    product_lst = list(product/i for i in lst)
    return product_lst
