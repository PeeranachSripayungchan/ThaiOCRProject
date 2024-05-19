'''
import difflib
'''
import os
from pywebio.input import input, FLOAT
from pywebio.output import put_text
from pywebio.output import put_row
from pywebio.output import put_column
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server

import subprocess
import requests
import getpass

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

def main():
    global filename, computername, img, imgs, imgs2, filename, filename2

    data = input_group("เลือกไฟล์ text 2 ไฟล์เพื่อนำมาวัดประสิทธิภาพ",[
        file_upload("text ที่สแกนออกมาได้:", name='imgs', accept="text/*", multiple=True),
        file_upload("text ตามต้นฉบับ:", name='imgs2', accept="text/*", multiple=True)
    ])

    imgs = data['imgs']
    for img in imgs:
        put_image(img['filename'])
    filename = str(img['filename'])

    imgs2 = data['imgs2']
    for img in imgs2:
        put_image(img['filename'])
    filename2 = str(img['filename'])

    computername = getpass.getuser()
    print(filename)
    print(filename2)

def find_file_by_name(file_path):
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.join(root, filename)
def find_file_by_name_two(file_path):
    for root, dirs, files in os.walk(path):
        if filename2 in files:
            return os.path.join(root, filename2)

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

if __name__=="__main__": 
    put_text("โปรแกรมวัดประสิทธิภาพของ Thai-OCR").style('font-size: 48px')
    dummyvariable1 = 1
    while dummyvariable1 == 1:
        main()

        path = os.getcwd()
        filepath1 = find_file_by_name(filename)
        filepath2 = find_file_by_name_two(filename2)
        
        #filepath1 = filename1
        #filepath2 = filename2

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
        #string1 = "123456"
        #string2 = "123456  fg"
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
        put_text('Correct Scan = %r' % SimilarText)
        put_text('Original Text = %r' % stringlength2)
        put_text('Scanned Text = %r' % stringlength1)
        put_text('Different Amount of Text = %r' % stringdiff)
        put_text('Wrong = %r' % WrongScan)
        put_text('Accuracy = %r' % Accuracy)  
