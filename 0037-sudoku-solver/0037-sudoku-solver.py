class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Track rows, columns, and 3x3 boxes using lists of sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # Populate initially filled digits and find empty positions
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    # Unique box index formula: (r // 3) * 3 + (c // 3)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))
                    
        def backtrack(cell_idx: int) -> bool:
            # Base case: All empty cells have been successfully filled
            if cell_idx == len(empty_cells):
                return True
                
            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try placing digits from '1' to '9'
            for digit in map(str, range(1, 10)):
                if (digit not in rows[r]) and (digit not in cols[c]) and (digit not in boxes[box_idx]):
                    # Place candidate digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)
                    
                    # Recurse to fill the next empty cell
                    if backtrack(cell_idx + 1):
                        return True
                        
                    # Backtrack if the layout becomes invalid down the line
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)
                    
            return False

        # Initiate the search from the first empty cell
        backtrack(0)
