# Sort a String
# https://www.geeksforgeeks.org/problems/sort-a-string2943/1

# Input:
# S = "edcab"
# Output: "abcde"
# Explanation: characters are in ascending
# order in "abcde".

# Solution:
class Solution:
    def sort(self, s): 
        #code here
        lst = [letter for letter in s]
        lst.sort()
        ans = ""
        for letter in lst:
            ans += letter
        return ans