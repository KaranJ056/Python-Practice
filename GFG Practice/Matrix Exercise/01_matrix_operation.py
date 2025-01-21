# Matrix Operations
# https://www.geeksforgeeks.org/problems/matrix-operations/1

# Solution:
class Solution:
    def endPoints(self, matrix, m, n):
        ##code here
        dir = "right"
        row, col = 0, 0
        while (row >= 0 and row < m) and (col >= 0 and col < n):
            if matrix[row][col] == 0:
                if dir == "right":
                    col += 1
                elif dir == "down":
                    row += 1
                elif dir == "left":
                    col -= 1
                elif dir == "up":
                    row -= 1
            else:
                matrix[row][col] = 0
                if dir == "right":
                    row += 1
                    dir = "down"
                elif dir == "down":
                    col -= 1
                    dir = "left"
                elif dir == "left":
                    row -= 1
                    dir = "up"
                elif dir == "up":
                    col += 1
                    dir = "right"
            
        if dir == "right":
            return (row, col-1)
        elif dir == "down":
            return (row-1, col)
        elif dir == "left":
            return (row, col+1)
        elif dir == "up":
            return (row+1, col)