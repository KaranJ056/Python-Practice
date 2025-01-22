# Pattern searching
# https://www.geeksforgeeks.org/problems/pattern-searching5231/1

# Input: txt = "abcdefh", pat = "bcd"
# Output: true
# Input: txt = "axzy", pat = "xy"
# Output: false

# Solution
def searchPattern(txt, pat):
    # code here
    return True if txt.find(pat) != -1 else False