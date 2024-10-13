# Matrix Row Sum

A 2D Array is a list of lists. Imagine the pixels on your screen, represented in
Python. The screen is a list of rows, and each row is a list of individual
pixel values.

Operating in two dimensions is really common: lots of data shows
up like this! A list of users, each with a list of favorite shows, or a list of
classes, each with a list of assignments.

In this exercise, you'll practice working with data laid out in a 2D array.

## Your Task

Write a function `row_sum` that calculates the sum of each row in a 2D array. It
should accept a single argument, a list of lists of numbers. It should return a
list of numbers, representing the sum of each row.

## Sample run

Here's a sample run with a small 3x3 array:

```python
row_sum([
  [10, 10, 10],
  [21, 32, 43],
  [15, 25, 35],
]) #=> [30, 96, 75]
```

(The `row_sum` function should work with lists of any size, not just 3x3.)

## Testing

Try running the code by hand on some sample inputs to check for yourself that it 
works.

Open up a python terminal, then run `from main import *` to load your code.
Then, you can run the example above to check that it has the same result as
expected.

Then, run the automated tests to confirm that your solution is correct.

## Bonus: `sum` function and list comprehensions

As usual, there are multiple ways to solve the same problem. Try rewriting your
solution using:

* the built-in `sum` function
* Python's [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

Remember to run the tests again to check your new solution.

## Bonus: Checksums

A [checksum](https://en.wikipedia.org/wiki/Checksum) is a way to add a little
bit of information to a message that lets the recipient check if the message was
transmitted correctly, or if there is some corruption. This is really useful for
sending data over networks, as radio signals and signal cables and components
can have errors.

There are lots of different checksum algorithms that work similarly to the 
`row_sum` function you implemented in this practice exercise. A basic [_check
digit_](https://en.wikipedia.org/wiki/Check_digit) algorithm would be to take 
the sum of the bytes in a message, apply `mod 10`, then add that byte to the end 
of the message. Then on the recipient's end, they could check that the sum of 
the digits correctly add up to the check digit. That would catch many errors in 
transmission, like if a 4 was swapped for a 5. Try implementing a `check_digit` 
function that appends the sum modulo 10 to each array in the list. 

There are lots of other interesting checksum algorithms you could compute. Two
particularly interesting ones are the Luhn algorithm and Hamming Codes.

The [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) is used for 
checking credit card numbers in transmission (as well as many national 
identification numbers). It is slightly more complicated than the check digit, 
but it can detect _transposition_ errors, like if someone typed in a credit card 
number with a `45` instead of a `54`.

[Hamming Codes](https://en.wikipedia.org/wiki/Hamming_code) are an example of
_error correcting codes_. Not only can they detect whether there was an error,
they can also tell what the error was! 3Blue1Brown has an excellent pair of
youtube videos ([part 1](https://www.youtube.com/watch?v=X8jsijhllIA), 
[part 2](https://www.youtube.com/watch?v=b3NxrZOu_CE)) that focuses on the math 
behind Hamming codes.

As a stretch challenge, you could try to implement the Luhn algorithm or Hamming
codes. These are pretty tricky, but quite satisfying once you get them working!
