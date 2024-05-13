import os

def remove(string):
    return string.replace(" ", "")

def sequence_matcher(string1, string2):
    global SimilarText
    len1, len2 = len(string1), len(string2)

    # Initialize a matrix to store the lengths of common subsequences
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Populate the matrix using dynamic programming
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the similarity ratio
    SimilarText = dp[len1][len2]
    similarity_ratio = SimilarText / len2

    return similarity_ratio

# Example strings
string1 = "reset"
string2 = "delete"

# Calculate similarity ratio
similarity_ratio = sequence_matcher(string1, string2)

# Print the result
print("Similar Text: ", SimilarText)
stringlength2 = len(string2)
print("Correct Text in Document: ", stringlength2)
print("Similarity Ratio:", similarity_ratio)
print("\n")
stringlength1 = len(string1)
print("Total Text Scan: ", stringlength1)



if stringlength1 > stringlength2:
    stringdiff = stringlength1 - stringlength2
    print("diff character: {}".format(stringdiff))
elif stringlength1 == stringlength2:
    print("diff character: 0")
else:
    stringdiff = stringlength2 - stringlength1
    print("diff character: {}".format(stringdiff))
