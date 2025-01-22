# Binary Search
# https://www.geeksforgeeks.org/problems/binary-search-1587115620/1

# Input: arr[] = [1, 2, 3, 4, 5], k = 4
# Output: 3
# Explanation: 4 appears at index 3.
# Input: arr[] = [1, 1, 1, 1, 2], k = 1
# Output: 0
# Explanation: 1 appears at index 0.

# Solution
class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        if k < arr[0] or k > arr[len(arr)-1]:
            return -1
        ans = ""
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == k:
                if mid != 0 and arr[mid-1] != k:
                    return mid
                else:
                    ans = left
                    right = mid-1
            elif arr[mid] < k:
                left = mid+1
            else:
                right = mid-1
        return left if ans != "" else -1