class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checking through each row and column using hash map
        cols = defaultdict(set)
        rows = defaultdict(set)
        # Checking through each 3x3 squares using hash map
        # To find each the corresponding index of the row and column to the square
        # We divide the index by 3 (r//3, c//3)
        squares = defaultdict(set)

        # Matrices go by rows x columns
        for r in range(9):
            for c in range(9):
                # Skip if it is blank
                if board[r][c] == ".":
                    continue
                # If duplicate is found we return false
                # We check for the columns, rows and each squares
                elif (board[r][c] in cols[c] or
                     board[r][c] in rows[r] or
                     board[r][c] in squares[(r//3, c//3)]):
                     return False
                # If no duplicate then we add to the hash map
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])

        return True

