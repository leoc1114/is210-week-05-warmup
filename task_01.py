#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Multiplying variables by 2 and returning a string.

    Args:
        winks(str): arg to be multiplied by 2.
        numwink(int): an assigned number. Default: 2.

    Returns:
        Str: All arguments are concatenated by commas.

    Examples:
        >>>know_what_i_mean('wink', 2)
        'Know_what_i_mean? winkwink, nudge nudge'

        >>>know_what_i_mean('wink', 5)
        'Know_what_i_mean? winkwinkwinkwinkwink, nudge nudge nudge nudge nudge'
    """

    winks = ('wink' * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
