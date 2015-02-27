#!usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 4 created"""

def too_many_kittens(kittens, litterboxes, catfood=False):
    if litterboxes >= kittens and catfood == True:
        return False
    else:
        return True
