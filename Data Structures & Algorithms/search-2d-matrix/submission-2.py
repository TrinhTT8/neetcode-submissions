class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We need to find which row is in the range of the target
        # Use binary search to reduce the row (O(log m)) 
        # Then we use binary search to find the target in that specific row O(log n)

        # m = rows
        # n = columns
        m_l, m_r = 0, len(matrix) - 1
        n_l, n_r = 0, len(matrix[0]) - 1
        mid_row = 0

        while m_l <= m_r:
            mid_row = (m_l + m_r) // 2
            # If target is within the range of the mid_row
            if matrix[mid_row][0] <= target <= matrix[mid_row][n_r]:
                # break to find if the target exists in the mid_row
                break
            # If the first integer is larger than target
            elif matrix[mid_row][0] > target:
                # Move our search up
                m_r = mid_row - 1
            # Else if the first integer is smaller than target
            else:
                m_l = mid_row + 1
        
        while n_l <= n_r:
            mid_col = (n_l + n_r) // 2
            if matrix[mid_row][mid_col] == target:
                return True
            # If the mid point is larger than target, we search the left side
            elif matrix[mid_row][mid_col] > target:
                n_r = mid_col - 1
            # Else if the mid point is smaller than target, we search right
            else:
                n_l = mid_col + 1

        return False