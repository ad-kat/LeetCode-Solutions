class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
            
        # m = rows, n = columns
        m, n = len(matrix), len(matrix[0])
        
        # Correctly assign boundaries
        l, r = 0, n - 1  # Column boundaries
        t, b = 0, m - 1  # Row boundaries
        
        ans = []
        
        while l <= r and t <= b:
            # 1. Move Right across the top row
            for j in range(l, r + 1):
                ans.append(matrix[t][j])
            t += 1 # Shrink top boundary
            
            # 2. Move Down down the right column
            for i in range(t, b + 1):
                ans.append(matrix[i][r])
            r -= 1 # Shrink right boundary
            
            # 3. Move Left across the bottom row (Check if row still exists)
            if t <= b:
                for j in range(r, l - 1, -1):
                    ans.append(matrix[b][j])
                b -= 1 # Shrink bottom boundary
                
            # 4. Move Up up the left column (Check if column still exists)
            if l <= r:
                for i in range(b, t - 1, -1):
                    ans.append(matrix[i][l])
                l += 1 # Shrink left boundary

        return ans
