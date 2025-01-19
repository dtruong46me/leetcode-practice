# solutions/2025_01_19.py
# Problem link: https://leetcode.com/problems/trapping-rain-water-ii/

from heapq import heappush, heappop
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Add all the boundary cells to the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        water_trapped = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        while heap:
            height, x, y = heappop(heap)
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # If the neighboring cell is lower, it traps water
                    water_trapped += max(0, height - heightMap[nx][ny])
                    # Update the height for the next boundary
                    heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return water_trapped
