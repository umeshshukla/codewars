# Summary

the repository *codewars* includes all of my completed code-katas from the
[CodeWars challenges](http://wwww.codewars.com) with a difficulty of
kyu5 or higher. [History of the term kyu](https://en.wikipedia.org/wiki/Ky%C5%AB)

# Python coding challenges:

## kyu5

* Base -2
* RPG dice roller
* Extract the domain name from a URL
* not-very-secure
* Excel's COUNTIF, SUMIF and AVERAGEIF functions
* Mod 4 Regex
* Convert string to camel case
* Calculate Fibonacci return count of digit occurrences
* Primes with Even Digits
* First n Prime Numbers
* Prime Factorization
* Valid Parentheses
* Simple Fun #81: Digits Product
* Car Park Escape
* Did I Finish my Sudoku?
* Find the unique string
* Best Travel

## kyu4

* Validate Sudoku with size `NxN`
* Valid Braces
* Next Bigger Number with same digits
* One Line Task: Palindrome String
* Strip Url Params
* Ranking Poker Hands
* Sortable Poker Hands

## kyu3

* Sudoku Solver
* Hard Sudoku Solver
* Texas Holdem

## kyu2
* Hard Unique Sudoku Solver

# C# coding challenges:

## kyu4

* Ranking Poker Hands
* Sortable Poker Hands

# SQL coding challenges:

## kyu5

* SQL Tuning: Function Calls
* Simple Hierarchical structure
* Simple PIVOTING data
* Simple View
* Group By Day
* Relational Division
* Calculating Running Total
* SQLonacci sequence

## beta

* Using Window Functions To Get Top N per Group
* SQL Data: Company Data - totals per day
* Count Weekdays

# JavaScript coding challenges:

## kyu3
* Texas Holdem

## Details for each kata completed

### Base -2
* Description of Kata: In this Kata you must convert integers numbers from and to
a negative-base binary system.
* Difficulty: kyu5
* Module: base_neg_2.py
* Tests: test_base_neg_2.py
* Link:(https://www.codewars.com/kata/base-2/train/python)
* Comments about most interesting solution/best practice:
I spent quite a bit reading up on this topic and came across a shortcut to convert
from decimal to negabinary by using the Librik, Szudzik & Schroeppel algorithm
which is mentioned [here] (https://en.wikipedia.org/wiki/Negative_base). A more
detailed explanation happened in this SO thread:
http://stackoverflow.com/questions/37637781/calculating-the-negabinary-representation-of-a-given-number-without-loops
Solution using Librik, Szudzik & Schroeppel algo:
```python
def int_to_negabinary(i):
    return str(bin((i + mask) ^ mask))[2:]

def negabinary_to_int(s):
    return (mask ^ int(s,2)) - mask
```
Most upvoted solution using bit-shifting:
```python
def int_to_negabinary(i):
    ds = []
    while i != 0:
        ds.append(i & 1)
        i = -(i >> 1)
    return ''.join(str(d) for d in reversed(ds)) if ds else '0'

def negabinary_to_int(s):
    i = 0
    for c in s:
        i = -(i << 1) + int(c)
    return i
```

### RPG dice roller
* Description of Kata: Your task in this kata is to write a "dice roller" that
interprets a subset of [dice notation] (https://en.wikipedia.org/wiki/Dice_notation)
Your function must support two types of output depending on the second argument;
verbose and summed.
* Difficulty: kyu5
* Module: diceroller.py
* Tests: test_diceroller.py
* Link:(https://www.codewars.com/kata/rpg-dice-roller)
* Comments about most interesting solution/best practice:
I like the use of unpacking the match.groups() into the 3 variables.
Not sure ```isinstance``` is a preferred solution though as it violates the
principle of asking for forgiveness rather than permission philosophy.
```python
import re
import random

def roll(desc, verbose=False):
    if isinstance(desc, str):
        desc_cleared = re.sub(r'\s', '', desc)
        match = re.match(r'^(\d*)d(\d+)((?:[+-]\d+)*)$', desc_cleared)
        if match:
            (dices, sides, modifiers) = match.groups()
            dices, sides = [int(x) if x else 1 for x in [dices, sides]]
            modifier = eval(modifiers) if modifiers else 0
            rolls = [random.randint(1, sides) for _ in range(dices)]
            return {'dice': rolls, 'modifier': modifier} if verbose else sum(rolls) + modifier
    return False
```

### Extract the domain name from a URL
* Description of Kata: Write a function that when given a URL as a string, parses
out just the domain name and returns it as a string. For example:
```
domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```
* Difficulty: kyu5
* Module: domain_name.py
* Tests: test_domain_name.py
* Link:(https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python)
* Comments about most interesting solution/best practice:
Below solution is not the most up-voted one for this kata but in my view the one
which solves the problem description the best.
```python
import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
```

### Not very secure
* Description of Kata: In this example you have to validate if a user input
string is alphanumeric. The given string is not nil, so you don't have to check
that.

The string has the following conditions to be alphanumeric:
```
- At least one character ("" is not valid)
- Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
- No whitespaces/underscore
```
* Difficulty: kyu5
* Module: not_secure.py
* Tests: test_not_secure.py
* Link:(https://www.codewars.com/kata/not-very-secure/train/python)
* Comments about most interesting solution/best practice:
```python
import re
def alphanumeric(string):
    return bool(re.match(r'^[A-Za-z0-9]+$', string))
```

### Excel's COUNTIF, SUMIF and AVERAGEIF functions
* Description of Kata: Microsoft Excel provides a number of useful functions for
counting, summing, and averaging values if they meet a certain criteria. Your
task is to write three functions that work similarly to Excel's COUNTIF, SUMIF
and AVERAGEIF functions.

Each function will take the same two arguments:

- A list object containing ```values``` to be counted, summed, or averaged.
- A ```criteria``` in either an integer, float, or string
* Integer or float indicates equality
* Strings can indicate >, >=, <, <= or <> (use the Excel-style "Not equal to"
operator) to a number (ex. ">=3"). In the ```count_if``` function, a string without
an operator indicates equality to this string.

The tests will all include properly formatted inputs. The test cases all avoid
rounding issues associated with floats.

* Difficulty: kyu5
* Module: basic_excel.py
* Tests: test_basic_excel.py
* Link:(https://www.codewars.com/kata/56055244356dc5c45c00001e)
* Comments about most interesting solution/best practice:
Not many solutions which didn't use eval or simply checked for the parameters
given in the test. I feel this should be solved programmatically. I like the
creativity of the below solutions but don't agree with checking for type.
```python
def parse(values, criteria):
    if type(criteria) in [int, float] or (type(criteria) is str and criteria[0] not in "<>"):
        return [item for item in values if item == criteria]

    rel = criteria.translate(None, "0123456789.")
    limit = float(criteria.translate(None, "<>="))

    if   rel == "<>":
        return [item for item in values if item <> limit]
    elif rel == "<=":
        return [item for item in values if item <= limit]
    elif rel == ">=":
        return [item for item in values if item >= limit]
    elif rel == "<":
        return [item for item in values if item < limit]
    elif rel == ">":
        return [item for item in values if item > limit]


def count_if(values, criteria):
    return len(parse(values, criteria))

def sum_if(values, criteria):
    return sum(parse(values, criteria))

def average_if(values, criteria):
    return sum(parse(values, criteria)) * 1.0 / len(parse(values, criteria))
```

### Mod4 Regex
* Description of Kata: You are to write a Regular Expression that matches any
string with at least one number divisible by 4 (with no remainder). In most
languages, you could do this easily by using ```number % 4 == 0```. How would
you do it with Regex?
* Difficulty: kyu5
* Module: mod4regex.py
* Tests: test_mod4regex.py
* Link:(https://www.codewars.com/kata/mod4-regex)
* Comments about most interesting solution/best practice:
Not the highest voted but best solution nonetheless
```python
import re

class Mod:
    mod4 = re.compile(r'.*\[[+-]?\d*((\b|[02468])[048]|[13579][26])\]')
```

### Convert string to camel case
* Description of Kata: Complete the method/function so that it converts dash/underscore
delimited words into camel casing. The first word within the output should be
capitalized only if the original word was capitalized.
* Difficulty: kyu5
* Module: camelcase.py
* Tests: test_camelcase.py
* Link:(https://www.codewars.com/kata/convert-string-to-camel-case/python)
* Comments about most interesting solution/best practice:
```python
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
```

### Calculate Fibonacci return count of digit occurrences
* Description of Kata: Your task is to efficiently calculate the nth element in
the Fibonacci sequence and then count the occurrence of each digit in the number
returning a list of integer pairs sorted in descending order.
* Difficulty: kyu5
* Module: fib_digit_occurence.py
* Tests: test_fib_digit_occurence.py
* Link:(https://www.codewars.com/kata/calculate-fibonacci-return-count-of-digit-occurrences)
* Comments about most interesting solution/best practice:
```python
from collections import Counter

def fib_digits(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b, a+b
    counts = Counter(str(b))
    return sorted(((count, int(digit)) for digit, count in counts.items()), reverse=True)
```

### Validate Sudoku with size `NxN`
* Description of Kata: Given a Sudoku data structure with size NxN, N > 0 and
√N == integer, write a method to validate if it has been filled out correctly.
* Difficulty: kyu4
* Module: sudoku_validator.py
* Tests: test_sudoku_validator.py
* Link:(https://www.codewars.com/kata/validate-sudoku-with-size-nxn)

### Primes with Even Digits
* Description of Kata: Find the closest prime number under a certain integer n
that has the maximum possible amount of even digits.
* Difficulty: kyu5
* Module: even_digit_primes.py
* Tests: test_even_digit_primes.py
* Link:(https://www.codewars.com/kata/primes-with-even-digits)
* Comments about most interesting solution/best practice:
I checked a few of the solutions at the top but most of them seem to time out and
are not optimized.

### First n Prime Numbers
* Description of Kata: Write your own Primes class with class method Primes.first(n)
 that returns an array of the first n prime numbers.
* Difficulty: kyu5
* Module: primes.py
* Tests: test_primes.py
* Link:(https://www.codewars.com/kata/first-n-prime-numbers)
* Comments about most interesting solution/best practice:
Not the most pythonic code but interesting Python2 solution
```python
primes = [2, 3, 5, 7, 11, 13] + \
[n for n in xrange(15, 10**6, 2) if n%3 and n%5 and n%7 and n%11 and n%13 and pow(2, n-1, n) == 1]
i = False
while i < len(primes):
    n = primes[i]
    for x in primes:
        if x**2 > n: i += 1; break
        if not n%x: del primes[i]; break

class Primes:
    @staticmethod
    def first(n):
        return primes[:n]
```

### Prime Factorization
* Description of Kata: The prime factorization of a positive integer is a list of
 the integer's prime factors, together with their multiplicities; the process of
 determining these factors is called integer factorization. The fundamental theorem
 of arithmetic says that every positive integer has a single unique prime factorization.

The prime factorization of 24, for instance, is ```(2^3) * (3^1)```.

Without using the prime library, write a class called PrimeFactorizer that takes
in an integer greater than 1 and has a method called factor which returns a hash
where the keys are prime numbers and the values are the multiplicities.

* Difficulty: kyu5
* Module: prime_factorization.py
* Tests: test_prime_factorization.py
* Link:(https://www.codewars.com/kata/prime-factorization)

### Valid Parentheses
* Description of Kata: Write a function called validParentheses that takes
a string of parentheses, and determines if the order of the parentheses
is valid. validParentheses should return true if the string is valid,
and false if it's invalid.
* Difficulty: kyu5
* Module: valid_parentheses.py
* Tests: test_valid_parentheses.py
* Link:(https://www.codewars.com/kata/valid-parentheses/python)

### Simple Fun #81: Digits Product
* Description of Kata: Given an integer product, find the smallest positive integer
the product of whose digits is equal to product. If there is no such integer,
return -1 instead.
* Difficulty: kyu5
* Module: digits_product.py
* Tests: test_digits_product.py
* Link:(https://www.codewars.com/kata/simple-fun-number-81-digits-product)
* Comments about most interesting solution/best practice:
```python
def digits_product(product):
    if product < 10:
        return 10 + product
    n = ''
    for d in range(9, 1, -1):
        while not product % d:
            n += str(d)
            product //= d
    return int(n[::-1]) if product == 1 else -1
```

### Car Park Escape
* Description of Kata: Your task is to escape from the carpark using only the
staircases provided to reach the exit. You may not jump over the edge of the levels
(you’re not Superman!) and the exit is always on the far right of the ground floor.
* Difficulty: kyu5
* Module: carpark.py
* Tests: test_carpark.py
* Link:(https://www.codewars.com/kata/car-park-escape/)

### Did I Finish my Sudoku?
* Description of Kata: Write a function done_or_not passing a board (list[list_lines])
as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'
* Difficulty: kyu5
* Module: sud_validator.py
* Tests: test_sud_validator.py
* Link:(https://www.codewars.com/kata/did-i-finish-my-sudoku/)

### Find the unique string
* Description of Kata: There is an array of strings. All strings contains similar
letters except one. Try to find it!
* Difficulty: kyu5
* Module: find_unique_str.py
* Tests: test_find_unique_str.py
* Link:(https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3)

## Best Travel
* Description of Kata: The function chooseBestSum (or choose_best_sum or ...
  depending on the language) will take as parameters t (maximum sum of distances,
  integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances,
  all distances are positive or null integers and this list has at least one element).
  The function returns the "best" sum ie the biggest possible sum of k distances
  less than or equal to the given limit t, if that sum exists, or otherwise null or None.
* Difficulty: kyu5
* Module: best_travel.py
* Tests: test_best_travel.py
* Link:(https://www.codewars.com/kata/best-travel/train/python)
* Comments about most interesting solution/best practice: Nice use of default for
Python version 3.4+
```python
def choose_best_sum(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)
```


### Valid Braces
* Description of Kata: Write a function called validBraces that takes a string of
braces, and determines if the order of the braces is valid. validBraces should
return true if the string is valid, and false if it's invalid.
* Difficulty: kyu4
* Module: valid_braces.py
* Tests: test_valid_braces.py
* Link:(https://www.codewars.com/kata/valid-braces)

### Next Bigger Number
* Description of Kata: You have to create a function that takes a positive integer
number and returns the next bigger number formed by the same digits:
* Difficulty: kyu4
* Module: next_bigger.py
* Tests: test_next_bigger.py
* Link:(https://www.codewars.com/kata/next-bigger-number-with-the-same-digits)
* Comments about most interesting solution/best practice:
Some of the solutions are short but are basically brute-forcing it. The below
solution is 2nd highest voted but I like it better than the top voted one due to
readability and speed.
```python
import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1
```

### One Line Task: Palindrome String
* Description of Kata: Your task is to generate a palindrome string, using the
specified length n, the specified characters c(all characters in c must be used
at least once), and the code length should less than 55 characters
* Difficulty: kyu4
* Module: palindrome_one_liner.py
* Tests: test_palindrome_one_liner.py
* Link:(https://www.codewars.com/kata/one-line-task-palindrome-string)
* Comments about most interesting solution/best practice: Didn't know about method
center, nice use here.
```python
palindrome=lambda n,s:(s+s[-1-n%2::-1]).center(n,s[0])
```

### Strip Url Params
* Description of Kata: Write a method that
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)
* Difficulty: kyu4
* Module: url_strip_params.py
* Tests: test_palindrome_one_liner.py
* Link:(https://www.codewars.com/kata/strip-url-params)

### Ranking Poker Hands
* Descripton of Kata: Create a poker hand that has a method to compare itself to another poker hand:
    compare_with(self, other_hand)
A poker hand has a constructor that accepts a string containing 5 cards:
    PokerHand(hand)
* Difficulty: kyu4
* Module: poker_rankings.py
* Tests: test_poker_rankings.py
* Link: https://www.codewars.com/kata/ranking-poker-hands/python

### Sudoku Solver
* Description of Kata: Write a function that will solve a 9x9 Sudoku puzzle. The
function will take one argument consisting of the 2D puzzle array, with the value
0 representing an unknown square.
* Difficulty: kyu3
* Module: sudoku_solver.py
* Tests: test_sudoku_solver.py
* Link:(https://www.codewars.com/kata/sudoku-solver)
* Comments about most interesting solution/best practice:
```python
import numpy as np

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    count = 0
    puzzle = np.array(puzzle)
    while(not all([all(row.tolist()) for row in puzzle])):
        for i in range(9):
            for j in range(9):
                if puzzle[i,j]: continue
                n = {1,2,3,4,5,6,7,8,9} - (set(puzzle[i].tolist()).union(set(puzzle[:,j].tolist())).union(set(puzzle[3*(i//3):3*(i//3) + 3, 3*(j//3): 3*(j//3) + 3].flatten().tolist())) - {0})
                if len(n) == 1:
                    puzzle[i,j] = list(n)[0]
                    print(i,j)

        count += 1
        print(puzzle[0])
        if count == 10:
            return "aaaa"
    print(count)

    return puzzle.tolist()
```

```python


def row_numbers(puzzle, row):
  return set(puzzle[row][i] for i in range(9) if puzzle[row][i] != 0)

def col_numbers(puzzle, col):
  return set(puzzle[i][col] for i in range(9) if puzzle[i][col] != 0)

def subsquare(puzzle, row, col):
  return set([puzzle[i][j] for i in range(row, row+3) for j in range(col, col+3) if puzzle[i][j] != 0])

def count(puzzle):
  return sum((puzzle[i].count(0) for i in range(9)))


def sudoku(puzzle):
  sol = set(i for i in range(1, 10))

  while count(puzzle) > 0:
    for x in range(9):
      for y in range(9):
        if puzzle[x][y] == 0:
          possible = sol - (row_numbers(puzzle, x) | col_numbers(puzzle, y) | subsquare(puzzle, 3*(x//3), 3*(y//3)))
          if len(possible) == 1:
            puzzle[x][y] = list(possible)[0]

  return puzzle
```

```python
  from itertools import product

def possibles(puzzle, x, y):
    a, b = 3*(x/3), 3*(y/3)
    square = set([puzzle[r][c] for r, c in product(range(a,a + 3), range(b,b + 3))])
    row = set(puzzle[x])
    col = set(zip(*puzzle)[y])
    return set(range(1,10)).difference(square.union(row).union(col))

def sudoku(puzzle):
    z = [(r,c) for (r,c) in product(range(9),range(9)) if puzzle[r][c] == 0]    
    if z == []:
        return puzzle
    for (r,c) in z:
        p = possibles(puzzle, r, c)
        if len(p) == 1:
            puzzle[r][c] = p.pop()
    return sudoku(puzzle)
```

### Hard Sudoku Solver
* Descripton of Kata: Write a function that will solve a 9x9 Sudoku puzzle. The
function will take one argument consisting of the 2D puzzle array, with the value
0 representing an unknown square. Puzzle is of hard or higher difficulty.
* Difficulty: kyu3
* Module: sudoku_solver_hard_cw_submission.py
* Tests: test_sudoku_solver_hard_cw_submission.py
* Link: https://www.codewars.com/kata/hard-sudoku-solver
* Comments: implementing more advanced Sudoku solving strategies like naked pairs/sets/quads are
actually increasing the runtime over brute forcing

### Hard Unique Sudoku Solver
* Descripton of Kata: Write a function that will solve a 9x9 Sudoku puzzle. The
function will take one argument consisting of the 2D puzzle array, with the value
0 representing an unknown square. Puzzle is of hard or higher difficulty. Also check that
the given Sudoku only has 1 possible solution.
* Difficulty: kyu2
* Module: sudoku_solver_hard_unique.py
* Tests: test_sudoku_solver_hard_unique.py
* Link: https://www.codewars.com/kata/hard-sudoku-solver-1