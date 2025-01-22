# Counting Sort
# https://www.geeksforgeeks.org/problems/counting-sort/1

# Input:
# N = 5
# S = "edsab"
# Output:
# abdes
# Explanation: 
# In lexicographical order, string will be 
# abdes

# Solution:
class Solution:
    #Function to arrange all letters of a string in lexicographical 
    #order using Counting Sort.
    def countSort(self,arr):
        # code here
        freq = [0]*26
        for letter in arr:
            freq[ord(letter)-ord('a')] += 1
        ans = ""
        for i in range(26):
            if freq[i] > 0:
                for j in range(freq[i]):
                    ans += chr(i+ord('a'))
        return ans