#!usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 4 created"""

def too_many_kittens(kittens, litterboxes, catfood=False):
    if kittens >= litterboxes and catfood == False:
        print True
    else:
        print False
