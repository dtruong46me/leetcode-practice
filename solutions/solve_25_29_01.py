from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        fishCount: int = 0
        num_rows, num_cols = len(grid), len(grid[0])

        result = 0
        visited = [[False] * num_cols for _ in range(num_rows)]

        # Iterating through the entire grid
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] and not visited[i][j]:
                    result = max(result, self._countFishes(grid, visited, i, j))
        
        return result

    def _countFishes(self, grid: List[List[int]], visited: List[List[bool]], row: int, col: int) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        fish_count = 0
        q = [(row, col)]
        visited[row][col] = True

        # Directions for exploring up, down, left, right
        row_directions = [0, 0, 1, -1]
        col_directions = [1, -1, 0, 0]

        # BFS traversal
        while q:
            row, col = q.pop(0)
            fish_count += grid[row][col]

            # Exploring all four directions
            for i in range(4):
                new_row = row + row_directions[i]
                new_col = col + col_directions[i]
                if (
                    0 <= new_row < num_rows
                    and 0 <= new_col < num_cols
                    and grid[new_row][new_col]
                    and not visited[new_row][new_col]
                ):
                    q.append((new_row, new_col))
                    visited[new_row][new_col] = True

        return fish_count
