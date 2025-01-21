# Last Cell in Matrix
# https://www.geeksforgeeks.org/problems/last-cell-in-a-matrix/1

# Solution:
class Solution:
    def endPoints(self, matrix, R, C):
        #code here
        dirs = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        dirx = 0
        row, col = 0, 0
        while (row >= 0 and col >= 0) and (row < R and col < C):
            ans = (row, col)
            if matrix[row][col] == 1:
                matrix[row][col] = 0
                dirx = (dirx+1) % 4
            row += dirs[dirx][0]
            col += dirs[dirx][1]
        
        return ans