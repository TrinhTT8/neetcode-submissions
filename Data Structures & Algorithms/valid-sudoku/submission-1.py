class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # We could combine everything into one for loop

        # Use a set to store the values so we can check for duplicate
        check_dup = set()
        square = defaultdict(set)
        # Check for each row [row][col]

        # Check for each 3x3 square here as well
        # Use a hash map to map each box with the values it holds
        # Each box will have a coordinate like [0][0], [0][1], etc.
        # Divide i and j by 3 to find out what box does that coordinate belongs to
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in check_dup or board[i][j] in square[(i//3, j//3)]:
                        return False
                    else:
                        check_dup.add(board[i][j])
                        square[(i//3 , j//3)].add(board[i][j])

            check_dup.clear()

        # Check for each col [row][col]
        for i in range(9):
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in check_dup:
                        return False
                    else:
                        check_dup.add(board[j][i])
            check_dup.clear()
        
        return True



        