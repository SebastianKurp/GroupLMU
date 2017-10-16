import os
import sys
import re
from report_keywords import removeChars, reportFormat

def searchTerm(fileContents, fileList, term):
    flag = True
    output = reportFormat('Search for term: ' + term + '\n')
    for i in range(len(fileContents)):
        found = []
        for j in range(len(fileContents[i])):
            words = map(str.strip, fileContents[i][j].split(' '))
            words = map(removeChars, words)
            for k in range(len(words)):
                if term.lower() == words[k].lower():
                    found.append(j)
        if len(found) > 0:
            flag = False
            output += fileList[i] + '\n'
            output += "\tfound " + str(len(found)) + ' times.\n' 
    if flag:
        output += 'None\n'
    return output
    