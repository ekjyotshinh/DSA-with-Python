'''
island count
Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function
should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.
test_00:
grid = [
['W', 'L', 'W', 'W', 'W'],
['W', 'L', 'W', 'W', 'W'],
['W', 'W', 'W', 'L', 'W'],
['W', 'W', 'L', 'L', 'W'],
['L', 'W', 'W', 'L', 'L'],
['L', 'L', 'W', 'W', 'W'],
]
island_count(grid) # -> 3

approach when you get the land explore it (dfs) and mark those land pices as visited
time : O(rc)
Space : O (rc)
'''


def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid,r,c,visited):
                count += 1
    return count

def explore(grid, row, column, visited):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= column < len(grid[0])

    if not row_inbounds or not col_inbounds: 
        return False
    if grid[row][column] == 'W':
        return False
    
    pos = (row,column)

    if pos in visited:
        return False
    
    visited.add(pos)

    explore(grid, row - 1, column, visited)
    explore(grid, row + 1, column, visited)
    explore(grid, row , column - 1, visited)
    explore(grid, row , column + 1, visited)
    return True
    



# Test Case 0
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]
assert island_count(grid) == 3  # Three distinct islands

# Test Case 1
grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
]
assert island_count(grid) == 4  # Four distinct islands

# Test Case 2
grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
]
assert island_count(grid) == 1  # One large island

# Test Case 3
grid = [
    ['W', 'W'],
    ['W', 'W'],
    ['W', 'W'],
]
assert island_count(grid) == 0  # No islands

# Test Case 4
grid = [
    ['L', 'W'],
    ['W', 'L']
]
assert island_count(grid) == 2  # Two small islands

# Test Case 5
grid = [
    ['L']
]
assert island_count(grid) == 1  # Single cell island

# Test Case 6
grid = [
    ['W']
]
assert island_count(grid) == 0  # Single cell water

# Test Case 7
grid = [
    ['L', 'L', 'W', 'W', 'L'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'W', 'L', 'L', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
]
assert island_count(grid) == 5  # Five distinct islands

print("All test cases passed!")
