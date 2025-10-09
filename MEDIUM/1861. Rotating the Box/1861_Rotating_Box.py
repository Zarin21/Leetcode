class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        # First, simulating the gravity effect on the box by iterating through each row from right to left
        # Keeping track of the position of the last empty space to drop the stone into
        # Then, rotating the box 90 degrees clockwise by placing elements in their new positions in a new grid
        # The new position for an element at (i, j) in the original grid will be (j, m-1-i) in the new grid where m is the number of rows in the original grid
        # Creating a new grid to store the rotated box

        new_grid_box = [[""] * len(boxGrid) for _ in range(len(boxGrid[0]))]

        for i in range(len(boxGrid)):  # Row
            empty_pos = len(boxGrid[0]) - 1  # resets every row
            empty = False
            for j in range(len(boxGrid[0]) - 1, -1, -1):  # Col
                if boxGrid[i][j] == ".":
                    if not empty:
                        empty_pos = j
                    empty = True
                    new_grid_box[j][len(boxGrid) - 1 - i] = "."
                elif boxGrid[i][j] == "#":
                    if not empty:
                        new_grid_box[j][len(boxGrid) - 1 - i] = "#"
                    else:
                        new_grid_box[empty_pos][len(boxGrid) - 1 - i] = "#"
                        new_grid_box[j][len(boxGrid) - 1 - i] = "."
                        empty_pos -= 1
                elif boxGrid[i][j] == "*":
                    empty_pos = len(boxGrid[0]) - 1
                    empty = False
                    new_grid_box[j][len(boxGrid) - 1 - i] = "*"

        return new_grid_box

        # Time complexity: O(m*n) where m is the number of rows and n is the number of columns in the input grid
        # Space complexity: O(m*n) where m is the number of rows and n is the number of columns in the input grid
