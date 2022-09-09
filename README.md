# Matrix Row Sum

A 2D Array is a list of lists. Imagine the pixels on your screen, represented in
Python. The screen is a list of rows, and each row is a list of individual
pixel values.

Operating in two dimensions is really common: lots of data shows
up like this! A list of users, each with a list of favorite shows, or a list of
classes, each with a list of assignments.

In this exercise, you'll practice working with data laid out in a 2D array.

## Instructions

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
works. Then, run the automated tests to confirm that your solution is correct.
