# Last Match
# https://www.geeksforgeeks.org/problems/last-match1928/1

# Input:
# A = abcdefghijklghifghsd
# B = ghi
# Output:
# 13
# Input:
# A = abdbccaeab
# B = abc
# Output:
# -1

# Solution
# 1
class Solution:
    def findLastOccurence(self, A, B):
        # code here 
        res = A.rfind(B)
        if res != -1:
            return res+1
        return -1
    
#2
import re
class Solution:
    def findLastOccurence(self, A, B):
        # code here 
        matches = [match.start() for match in re.finditer(f"(?={re.escape(B)})", A)]
        return matches[-1]+1 if matches else -1