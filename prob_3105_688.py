function knightProbability(n, k, row, column):
    # Initialize 3D DP array with 0s
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
    dp[0][row][column] = 1
    
    # Possible knight moves
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    # Fill DP table
    for move in range(1, k + 1):
        for r in range(n):
            for c in range(n):
                for dr, dc in moves:
                    prev_r, prev_c = r - dr, c - dc
                    if 0 <= prev_r < n and 0 <= prev_c < n:
                        dp[move][r][c] += dp[move - 1][prev_r][prev_c] / 8
    
    # Calculate total probability of staying on the board after k moves
    total_probability = 0
    for r in range(n):
        for c in range(n):
            total_probability += dp[k][r][c]
    
    return total_probability
