
import os


def remove(string):
    return string.replace(" ", "")

# Example strings
string1 = "abd"
string2 = "dac"

import numpy as np

def levenshteinDistance(s1, s2):
    N, M = len(s1), len(s2)
    # Create an array of size NxM
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    # Base Case: When M = 0
    for i in range(N + 1):
        dp[i][0] = i
    # Base Case: When N = 0
    for j in range(M + 1):
        dp[0][j] = j
        
    # Transitions
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j], # Insertion
                    dp[i][j-1], # Deletion
                    dp[i-1][j-1] # Substitution
                )

    return dp[N][M]


WrongScan = levenshteinDistance(string1, string2)
print("Wrong: ", WrongScan)
#CorrectScan = stringlength2 - WrongScan
#print("CorrectScan: ", CorrectScan)
