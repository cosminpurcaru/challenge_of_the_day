# Trailing zeros in N factorial

I know that a number gets a zero at the end of it if the number has 10 as a factor. For instance, 10 is a factor of 50, 120, and 1234567890. So I need to find out how many times 10 is a factor in the expansion of 23!.

But since 5×2 = 10, I need to account for all the products of 5 and 2. Looking at the factors in the above expansion, there are many more numbers that are multiples of 2 (2, 4, 6, 8, 10, 12, 14,...) than are multiples of 5 (5, 10, 15,...). That is, if I take all the numbers with 5 as a factor, I'll have way more than enough even numbers to pair with them to get factors of 10 (and another trailing zero on my factorial). So to find the number of times 10 is a factor, all I really need to worry about is how many times 5 is a factor in all of the numbers between 1 and N.

# Examples

### 1) Find the number of trailing zeroes in 101!

100 is the closest multiple of 5 below 101, and 100 ÷ 5 = 20, so there are 20 multiples of 5 between 1 and 101.

But wait: 25 is 5×5, so each multiple of 25 has an extra factor of 5 that I need to account for. How many multiples of 25 are between 1 and 101? Since 100 ÷ 25 = 4, there are four multiples of 25 between 1 and 101.

    Adding these, I get 20 + 4 = 24 trailing zeroes in 101!
   
### 2) Find the number of trailing zeroes in the expansion of 1000!

There are 1000 ÷ 5 = 200 multiples of 5 between 1 and 1000. The next power of 5, namely 25, has 1000 ÷ 25 = 40 multiples between 1 and 1000. The next power of 5, namely 125, will also fit in the expansion, and has 1000 ÷ 125 = 8 multiples between 1 and 1000. The next power of 5, namely 625, also fits in the expansion, and has 1000 ÷ 625 = 1.6... um, okay, 625 has 1 multiple between 1 and 1000. (I don't care about the 0.6 "multiples", only the one full multiple, so I truncate my division down to a whole number.)

    In total, I have 200 + 40 + 8 + 1 = 249 trailing zeroes in the expansion of 1000!

  
# Solution

The previous examples highlights the general method for answering this question, no matter what factorial they give you.

    * Take the number that you've been given the factorial of.
    * Divide by 5; if you get a decimal, truncate to a whole number.
    * Divide by 5^2 = 25; if you get a decimal, truncate to a whole number.
    * Divide by 5^3 = 125; if you get a decimal, truncate to a whole number.
    * Continue with ever-higher powers of 5, until your division results in a number less than 1. Once the division is less than 1, stop.
    * Sum all the whole numbers you got in your divisions. This is the number of trailing zeroes.
