#!usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 4 created"""


def too_many_kittens(kittens, litterboxes, catfood=False):
    """Looking to see if there is too many cats.

    Args:
        kittens(int): how many kittens
        littleboxes(int): how many kittens
        catfood(bool): if there is any cat food

    Return:
        if there is too many cats

    Examples:
        >>> too_many_kittens(12, 13, False)
        True

        >>> too_many_kittens(
    """

    if kittens > litterboxes and catfood == False:
        return True
    else:
        return False
