import re

# 1. Regex - Python
# https://www.geeksforgeeks.org/problems/regex-python/1

# Solution:
def numberMatcher(str):
    pat=r"\d+"
    match=re.findall(pat,str) ##find all finds all the matched texts and returns a list
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")

# 2. Regular Expressions 2 - Python
# https://www.geeksforgeeks.org/problems/regular-expressions-2-python/1

# Solution:
def validate(str):
    pat= r"\w+\W+\d+"
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False