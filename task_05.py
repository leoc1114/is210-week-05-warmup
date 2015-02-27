#!usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 5 created"""


def defaults(my_required, my_optional=True):
    """Checking to see if my_required is my_optional.

    Args:
        my_required(bool): to see if arg is equal to my_optional.
        my_optional(bool): my optional has a default vaule, default=True.

    Returns:
        defaults(bool): is my_required equal to my_optional.

    Examples:
        >>> defaults(True)
        True

        >>>defaults(True, False)
        False

        >>>defaults(False, False)
        True
    """

    return my_optional == my_required
