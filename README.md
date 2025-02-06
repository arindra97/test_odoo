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

### 4. Logika Huruf Vokal [open here](https://github.com/arindra97/test_odoo/blob/main/Python/4_logic_huruf_vokal.py)

For this exercise, I developed a function to count vowels in words. The function takes a word as input, iterates through its characters, checks for vowel occurrences, and returns the total vowel count. If no vowels are found, it reports accordingly.

### 5. Logika Terbilang [open here](https://github.com/arindra97/test_odoo/blob/main/Python/5_logic_terbilang.py)

This exercise involved developing two functions: terbilang_pecahan_uang for converting numerical currency amounts into their Indonesian text representation, and terbilang_angka for translating individual numbers into Indonesian words. The terbilang_pecahan_uang function operates by segmenting the input number into three-digit groups and converting each group to its word equivalent

## C. Test Odoo Framework - Odoo 14 [open here](https://github.com/arindra97/test_odoo/tree/main/custom_purchase)

This custom Odoo module enhances the purchase process by adding a "Berita Acara" (BA) or news update feature. It introduces a new purchase.order.news model to track BA information related to purchase orders. The module modifies the purchase.purchase model to create and manage these BAs, triggered when a purchase order is confirmed. It also modifies the account.move model to link invoices to the BAs. The BA workflow involves a 'draft', 'submit', 'approved', and 'done' states, with approval handled by users in the group_general_affair security group. Approving a BA automatically generates a related invoice. This summary provides a high-level overview of the module's functionality and its impact on the purchase workflow.

### Purchase Order View

<image src="public/image/purchase_order_view.png">

### Purchase Order News View

This view accessible to Purchase users upon Berita Acara created.

<image src="public/image/purchase_order_news_view.png">

### Purchase Order News View

This view becomes accessible to General Affairs users upon submission of a Berita Acara.

<image src="public/image/view_approve_group_ga.png">

### Create Invoice View

This view becomes accessible after General Affairs users approve a Berita Acara.

<image src="public/image/view_approve_create_invoice.png">
