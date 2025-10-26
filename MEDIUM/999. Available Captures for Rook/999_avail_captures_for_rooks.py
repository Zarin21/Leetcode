# I first locate the position of the Rook on the chessboard.
# Then, I check in all four directions (up, down, left, right) from
# the Rook's position to see if there are any pawns ('p') that can
# be captured before encountering a bishop ('B') or the edge of the board.
# Each time a pawn is found that can be captured, I increment a counter.
from typing import List



class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8): # row
            for j in range(8): # cols
                if board[i][j] == "R":
                    rookie_row = i
                    rookie_col = j
                    break
                    
        pawns = 0

        i = rookie_row
        while i > 0:
            # going up from rookie
            i -= 1
            if board[i][rookie_col] == "p":
                pawns += 1
                break
            elif board[i][rookie_col] == "B":
                break

        i = rookie_row
        while i < 7:
            # going down from rookie
            i += 1
            if board[i][rookie_col] == "p":
                pawns += 1
                break
            elif board[i][rookie_col] == "B":
                break
        
        j = rookie_col
        while j > 0:
            # going left from rookie
            j -= 1
            if board[rookie_row][j] == "p":
                pawns += 1
                break
            elif board[rookie_row][j] == "B":
                break
        
        j = rookie_col
        while j < 7:
            # going right from rookie
            j += 1
            if board[rookie_row][j] == "p":
                pawns += 1
                break
            elif board[rookie_row][j] == "B":
                break
                
        return pawns
    
# Time Complexity: O(1), since the board size is fixed (8x8).
# Space Complexity: O(1), as we are using a constant amount of extra space.