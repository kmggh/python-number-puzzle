Number Puzzle
=============

Ken Guyton<br />
Tue 2015-11-03 23:58:48 -0500


This is a number puzzle shown to me by my daughter.

Find the five digit number, made of five different digits, that, when
multiplied by four, is those same five digits in reverse order.

    abcde
      x 4
    -----
    edcba



Solve1
------

This program takes the brute force approach and tries every number
with a given number of digits and reports solutions it finds.

    time ./solve1.py
    2178
    21978
    219978
    
    real	0m3.213s
    user	0m3.184s
    sys	0m0.024s


Try_num
-------

This program allows trying any number to see if it works.

    ./try_num.py 2178
    Yep, it works.
    ./try_num.py 2199978
    Yep, it works.
    ./try_num.py 21999978
    Yep, it works.
    ./try_num.py 21999999978
    Yep, it works.
    ./try_num.py 219999999999978
    Yep, it works.


The solution
------------

It turns out, apparently, that any number of the form 21x78 is a
solution where x is zero or more 9's.

