"""
You have an N by N board. Write a function that, given N, 
returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, 
i.e. no two queens share the same row, column, or diagonal.

"""
def totalNQueens(n):
    def backtrack(row, cols, diagonals, anti_diagonals):
        if row == n:
            return 1

        count = 0
        for col in range(n):
            diagonal = row - col
            anti_diagonal = row + col
            if col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals:
                continue

            cols.add(col)
            diagonals.add(diagonal)
            anti_diagonals.add(anti_diagonal)

            count += backtrack(row + 1, cols, diagonals, anti_diagonals)

            cols.remove(col)
            diagonals.remove(diagonal)
            anti_diagonals.remove(anti_diagonal)

        return count

    return backtrack(0, set(), set(), set())

n = 4
result = totalNQueens(n)
print(result) # output: 2
