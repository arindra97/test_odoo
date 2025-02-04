# Test Programmer IT Odoo Developer

This constitutes the answer to the test IT Programmer Odoo.

## A. Test Programming SQL [open here](https://github.com/arindra97/test_odoo/tree/main/SQL%20Test)

My approach for this test, using PostgreSQL, involved an initial ERD design phase to ensure efficient data mapping

### ERD

<image src="public/image/ERD_SQL_Test.png">

## B. Test Programming (Python)

For this assessment, I use python version 3.12.1

### 1. Logika Bilangan Prima [open here](https://github.com/arindra97/test_odoo/blob/main/Python/1_logic_bilangan_prima.py)

This Python function checks if a given number is a prime number or not.

The function `logic_bilangan_prima` have a params number and checks if a given number is a prime number. It follows the logic below:
The function `logic_bilangan_prima` returns a boolean value - `True` if the input number is a prime number, and `False` if it is not a prime number.

My primality test begins by handling base cases:

-   numbers less than 1 are immediately classified as non-prime, while 2 is identified as prime.
-   Subsequently, even numbers are eliminated, as they are not prime (with the exception of 2).
-   The core logic involves iterating through odd numbers up to the square root of the input number. If any of these odd numbers divide the input evenly, the number is deemed non-prime; otherwise, it is considered prime.

### 2. Logika Cek Kata PALINDROM [open here](https://github.com/arindra97/test_odoo/blob/main/Python/2_check_palindrom_word.py)

A palindrome is a word that reads the same forwards and backwards.

The function `check_palindrome` in Python checks if a given word is a palindrome or not.

The function `check_palindrome` takes a word as input and checks if it is a palindrome.
The function `check_palindrome` returns `True` if the input `word` is a palindrome (reads
the same forwards and backwards), and `False` otherwise.

I explored two distinct approaches for palindrome detection.

1. The first involved a manual string reversal: converting the input to lowercase, determining its length, creating a reversed copy, and then comparing it to the original.
2. The second approach leveraged Python's built-in string slicing capabilities for a more concise reversal. Specifically, the [::-1] slice was employed to efficiently generate the reversed string for comparison.

### 3. Logika Pecahan Uang [open here](https://github.com/arindra97/test_odoo/blob/main/Python/3_logic_pecahan_uang.py)

The function `pecah_uang` in Python is format number into currency format.

The function `pecah_uang` takes a number as input and validate it is an integer or not and takes a lang for the format currency default value is `id`.
The function `pecah_uang` returns format currency number with grouping 3 digit

For representing currency formatting (pecahan uang), I explored two distinct formatting approaches.

1. The first involved a manual grouping method: validating the input as an integer, converting it to a string, reversing the string, grouping it into three-digit chunks via slicing, joining the chunks, and then reversing the result again to match the desired locale.
2. The second approach leveraged Python's built-in string formatting capabilities. Using the {:,} format specifier, numerical values are automatically grouped according to currency conventions, adapting to the specified locale.
