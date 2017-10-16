import os
import sys
import re
from report_keywords import reportKeywords, removeChars, reportFormat

def notesByKeyword(fileContents,fileList,minFound, occurrences):
    output = reportFormat('Notes by Keyword (found in at least ' + str(minFound) + ' file(s))\n(minimum ' + str(occurrences) + ' keyword occurrence(s)):\n')
    keywords = reportKeywords(fileContents,fileList,'l',2, occurrences)
    anythingFound = False
    for n in range(len(keywords)):
        found = []
        flag = False
        for i in range(len(fileContents)):
            for j in range(len(fileContents[i])):
                words = map(removeChars, fileContents[i][j].split(' '))
                for k in range(len(words)):
                    if keywords[n].lower().strip() == words[k].lower().strip():
                        found.append(fileList[i])
                        flag = True
                        break
                if flag:
                    break
        found = list(set(found))
        if len(found) >= minFound:
            anythingFound = True
            output += keywords[n] + '\n'
            for i in range(len(found)):
                output += '\t' + found[i] + '\n'
    if not anythingFound:
        output += 'None\n'
    return output
                    