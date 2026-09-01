class Solution:
    def totalNQueens(self, n: int) -> int:
        # Sets to keep track of under-attack positions
        cols = set()
        pos_diag = set()  # (row + col) remains constant
        neg_diag = set()  # (row - col) remains constant
        
        self.count = 0
        
        def backtrack(row: int):
            # Base case: All queens are successfully placed
            if row == n:
                self.count += 1
                return
            
            # Try placing a queen in each column of the current row
            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                # Place the queen and mark paths as attacked
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                
                # Move to the next row
                backtrack(row + 1)
                
                # Backtrack: Remove the queen and clear paths
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                
        backtrack(0)
        return self.count
