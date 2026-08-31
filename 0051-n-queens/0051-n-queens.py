class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        
        # Track occupied lines to avoid attacks
        cols = set()
        pos_diag = set()  # (row + col)
        neg_diag = set()  # (row - col)
        
        def backtrack(r: int):
            # Base case: placed queens in all rows
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                # Check for conflicts
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Place the queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                # Recurse to the next row
                backtrack(r + 1)
                
                # Backtrack and remove the queen
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res
