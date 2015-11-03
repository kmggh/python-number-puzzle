#!/usr/bin/env python
# Copyright (c) 2015 by Ken Guyton.  All Rights Reserved.

"""Try a number to see if 4 * num == revnum(num)."""

from __future__ import print_function

import sys

FIVE_DIGIT_MAX = 10000000


def reverse(astr):
  """Reverse a string."""

  return astr[::-1]


def revnum(anum):
  """Reverse a number."""

  return int(reverse(str(anum)))


def main():
  """Find the solution."""

  num = int(sys.argv[1])
  if 4 * num == revnum(num):
    print('Yep, it works.')


if __name__ == '__main__':
  main()
