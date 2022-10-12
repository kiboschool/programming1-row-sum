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
