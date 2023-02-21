# Define the crossword puzzle
puzzle = [
    ['C', '_', '_', '_', '_', 'E', 'L', 'L', 'O', '_', '_', '_', '_', '_'],
    ['A', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['T', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['S', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['T', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['O', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['N', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
]

# Define the word list
words = ['CELL', 'ATONE', 'STONED', 'STOIC', 'TOAST', 'ONE']

# Define a function to check if a word can fit in a given position in the puzzle
def fits(word, i, j, dir):
    for k, letter in enumerate(word):
        if dir == 0:  # horizontal
            if j + k >= len(puzzle[i]) or (puzzle[i][j + k] != '_' and puzzle[i][j + k] != letter):
                return False
        else:  # vertical
            if i + k >= len(puzzle) or (puzzle[i + k][j] != '_' and puzzle[i + k][j] != letter):
                return False
    return True

# Define a function to insert a word in the puzzle
def insert(word, i, j, dir):
    for k, letter in enumerate(word):
        if dir == 0:  # horizontal
            puzzle[i][j + k] = letter
        else:  # vertical
            puzzle[i + k][j] = letter

# Define a function to solve the crossword puzzle
def solve(words, i=0, j=0):
    if i == len(puzzle):  # base case: puzzle is solved
        return True
    if puzzle[i][j] != '_':  # skip filled positions
        if j == len(puzzle[i]) - 1:  # move to next row
            return solve(words, i + 1, 0)
        else:  # move to next column
            return solve(words, i, j + 1)
    for word in words:  # try each word
        for dir in range(2):  # try both directions
            if fits(word, i, j, dir):
                insert(word, i, j, dir)
                if j == len(puzzle[i]) - 1:  # move to next row
                    if solve(words, i + 1, 0):
                        return True
                else:  # move to next column
                    if solve(words, i, j + 1):
                        return True
                insert(word, i, j, dir)  # backtrack
    return False  # no solution found

# Solve the puzzle and print the solution
if solve(words):
    for row in puzzle:
        print(' '.join(row))
else:
    print('No solution found')
