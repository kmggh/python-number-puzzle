#!/usr/bin/env python
# Copyright (c) 2015 by Ken Guyton.  All Rights Reserved.

"""Solve the five digit (and six digit), reverse number puzzle by brute force."""

from __future__ import print_function

import sys

MAX = 1000000


def reverse(astr):
  """Reverse a string."""

  return astr[::-1]


def revnum(anum):
  """Reverse a number."""

  return int(reverse(str(anum)))


def main():
  """Find the solution."""

  for num in range(1, MAX):
    if 4 * num == revnum(num):
      print(num)


if __name__ == '__main__':
  main()
