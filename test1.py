import unittest
from program1 import Solution

def explore_island(grid, row, col, visited):
    # Define the four directions: up, down, left, right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Mark the current cell as visited
    visited[row][col] = True
    
    # Explore in all four directions
    for d in directions:
        new_row, new_col = row + d[0], col + d[1]
        # Check if the new cell is within the grid and is land and not visited
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "L" and not visited[new_row][new_col]:
            explore_island(grid, new_row, new_col, visited)

def count_islands(grid):
    if not grid:
        return 0
    
    num_rows, num_cols = len(grid), len(grid[0])
    visited = [[False] * num_cols for _ in range(num_rows)]
    island_count = 0
    
    # Iterate through each cell of the grid
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == "L" and not visited[i][j]:
                # If the cell is land and not visited, explore the island
                explore_island(grid, i, j, visited)
                # Increment the island count after exploring the entire island
                island_count += 1
                
    return island_count

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        result = self.solution.getTotalIsles([["L","L","L","L","W"],["L","L","W","L","W"],["L","L","W","W","W"],["W","W","W","W","W"]])
        self.assertEqual(result, 1)

    def test_case2(self):
        result = self.solution.getTotalIsles([["L","L","W","W","W"],["L","L","W","W","W"],["W","W","L","W","W"],["W","W","W","L","L"]])
        self.assertEqual(result, 3)

    def test_case3(self):
        result = self.solution.getTotalIsles([["W", "W", "W", "W"], ["W", "L", "L", "W"], ["W", "L", "L", "W"], ["W", "W", "W", "W"]])
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)