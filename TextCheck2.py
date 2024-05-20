'''
import difflib
'''
import os

#userfile = file_upload('Upload file')

#open(userfile['filename'], 'wb').write(userfile['content'])

#img = file_upload("Select a image:", accept="image/*")
'''
path = r"D:\Homework\Project\ThaiOCR\sample\all_1"
dir_list = os.listdir(path)
print(dir_list)
'''

def remove(string):
    return string.replace(" ", "")

def find_file_by_name(file_path):
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.join(root, filename)

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
    similarity_ratio = dp[len1][len2] / len2
    SimilarText = dp[len1][len2]

    return similarity_ratio

filepath1 = "D://ngrok/Thai-OCR-WebApp/Example300dpi/Ex10_02_300dpi.txt"
filepath2 = "D://ngrok/Thai-OCR-WebApp/Example300dpi/Ex10_02_correct.txt"
#filepath1 = find_file_by_name(filename)
#filepath2 = find_file_by_name(filename)
00
f = open(filepath1, "r", encoding='utf8')
xx = 1
while xx == 1:
    try:
        line = f.readline()
    except UnicodeDecodeError:
        #f.close()
        encodeing = 'TIS-620'
        break
    if not line:
        #f.close()
        encoding = 'utf8'
        break

with open(filepath1, "r", encoding=encoding) as f:
    prestring1 = f.read().replace("\n", "")
    string1 = remove(prestring1)

f2 = open(filepath1, "r", encoding='utf8')
while xx == 1:
    try:
        line = f2.readline()
    except UnicodeDecodeError:
        #f2.close()
        encodeing = 'TIS-620'
        break
    if not line:
        #f2.close()
        encoding = 'utf8'
        break

with open(filepath2, "r", encoding=encoding) as f2:
    prestring2 = f2.read().replace("\n", "")
    string2 = remove(prestring2)

# Example strings
string1 = "reset"
string2 = "delete"
#string1 = string1.replace(" ", "")
#string2 = string2.replace(" ", "")

# Calculate similarity ratio
similarity_ratio = sequence_matcher(string1, string2)

# Print the result
print("Similar Text: ", SimilarText)
stringlength2 = len(string2)
print("Correct Text in Document: ", stringlength2)
#print("Similarity Ratio:", similarity_ratio)
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

import numpy as np

def levenshteinDistance(s1, s2):
    N, M = len(s1), len(s2)
    # Create an array of size NxM
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    # Base Case: When N = 0
    for j in range(M + 1):
        dp[0][j] = j
    # Base Case: When M = 0
    for i in range(N + 1):
        dp[i][0] = i
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
Accuracy = 1 - (WrongScan / stringlength2)
print("Accuracy: ", Accuracy)
