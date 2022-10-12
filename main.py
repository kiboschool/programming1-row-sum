# Implement the row_sum function here

def row_sum(matrix):
    result = []
    for row in matrix:
        total = 0
        for num in row:
            total += num
        result.append(total)
    return result

# alternative implementation using sum function and list comprehension
def alt_row_sum(matrix):
    return [sum(row) for row in matrix]
