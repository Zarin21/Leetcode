class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        # Swap elements across the main diagonal
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        # Use slicing to reverse each row
        for i in range(len(matrix)):
            matrix[i].reverse()

        # Time complexity: O(n^2) where n is the number of rows or columns in the matrix
        # Space complexity: O(1) since we are modifying the matrix in place
