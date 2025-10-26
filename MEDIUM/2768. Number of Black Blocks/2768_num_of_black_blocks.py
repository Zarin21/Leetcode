from typing import List

class Solution:

    # I create a dictionary to count how many black blocks each 2x2 block contains
    # by iterating through the list of black cell coordinates.
    # For each black cell, I check the four possible 2x2 blocks it can belong to
    # (top-left, top-right, bottom-left, bottom-right) and update the count in the dictionary.  

    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        block_counts = {}
        for i, j in coordinates:
            for dx, dy in [(0, 0), (-1, 0), (0, -1), (-1, -1)]:
                x0, y0 = i + dx, j + dy
                if 0 <= x0 < m - 1 and 0 <= y0 < n - 1:
                    block_counts[(x0, y0)] = block_counts.get((x0, y0), 0) + 1

        # Finally, I prepare the result list by counting how many 2x2 blocks have 0, 1, 2, 3, and 4 black cells.
        # I calculate the number of blocks with 0 black cells by subtracting the number of blocks
        # that have at least one black cell from the total number of 2x2 blocks
        # in the m x n grid.
        # I return the result list.
        result = [0] * 5
        for count in block_counts.values():
            result[count] += 1 
        result[0] = (m - 1) * (n - 1) - len(block_counts)
        return result
    
# Time Complexity: O(k), where k is the number of black cells in the input list 'coordinates'.
# Space Complexity: O(k), for storing the counts of 2x2 blocks in the dictionary 'block_counts'.