# dp = [-1]*100


# def count(a, i):
#     if i <= -1:
#         return 0
#     if dp[i] != -1:
#         return dp[i]
#     op1 = count(a, i-1)
#     op2 = a[i] + count(a, i-2)
#     dp[i] = max(op1, op2)
#     # print(dp[i])
#     return dp[i]
# # Function to find the maximum money the thief can get.


# def FindMaxSum(a, n):

#     # code here
#     a = count(a, n-1)
#     return a


# n = 5
# a = [1, 200, 10, 2, 3]

# print(FindMaxSum(a, n))

# User function Template for python3

import sys
import io
import atexit


class Solution:
    dp = [-1]*100

    def count(self, a, i):
        if i <= -1:
            return 0
        if self.dp[i] != -1:
            return self.dp[i]
        op1 = self.count(a, i-1)
        op2 = a[i] + self.count(a, i-2)
        self.dp[i] = max(op1, op2)
        print(self.dp[i])
        return self.dp[i]
    # Function to find the maximum money the thief can get.

    def FindMaxSum(self, a, n):
        # code here
        a = self.count(a, n-1)
        return a

# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        print(ob.FindMaxSum(a, n))
# } Driver Code Ends
