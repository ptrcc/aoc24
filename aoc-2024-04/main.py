import numpy as np

with open('input.txt', 'r') as file:
    grid = file.read().splitlines()

grid_array = np.array([list(row) for row in grid])

TARGET_WORD = "XMAS"
WORD_LENGTH = len(TARGET_WORD)
rows, cols = grid_array.shape

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]

def count_word_occurrences(grid, word, start_row, start_col, direction):
    delta_row, delta_col = direction
    for i in range(len(word)):
        current_row = start_row + i * delta_row
        current_col = start_col + i * delta_col

        if not (0 <= current_row < rows and 0 <= current_col < cols):
            return 0
        if grid[current_row][current_col] != word[i]:
            return 0
    return 1

total_word_occurrences = 0
for row in range(rows):
    for col in range(cols):
        for direction in DIRECTIONS:
            total_word_occurrences += count_word_occurrences(grid_array, TARGET_WORD, row, col, direction)

print(total_word_occurrences)

PART_TWO_PATTERNS = {"MAS", "SAM"}

def count_xmas_patterns(grid, start_row, start_col):
    diagonals = [(1, 1), (-1, 1)]
    starts = [(start_row, start_col), (start_row + 2, start_col)]

    for (delta_row, delta_col), (base_row, base_col) in zip(diagonals, starts):
        try:
            pattern = "".join(grid[base_row + delta_row * step, base_col + delta_col * step] for step in range(3))
            if pattern not in PART_TWO_PATTERNS:
                return 0
        except IndexError:
            return 0
    return 1

total_xmas_patterns = 0
for row in range(rows - 2):
    for col in range(cols - 2):
        total_xmas_patterns += count_xmas_patterns(grid_array, row, col)

print(total_xmas_patterns)
