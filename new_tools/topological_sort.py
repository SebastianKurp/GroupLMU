from formatting import *
import re

def topologicalSort(fileContents, fileNames):
    output = []
    ids = []
    for i in range(len(fileContents)):
        ids.append(['-'])
        #give this file a '-'' as an ID in case it doesn't have an identifier
    for i in range(len(fileContents)):
        lines = fileContents[i].split('\n')
        #for every file
        for j in range(len(lines)):
            words = lines[j].strip().split(' ')
            #for every line in the file
            for k in range(len(words)):
                #for every word on the line
                if len(words[k]) > 0:
                    if re.search('^\\^',words[k]):
                        ids[i].append(words[k][1:])
                        #if this word is a reference to another file, add to references.
                    elif re.search('^!',words[k]):
                        ids[i][0] = words[k][1:]
                        #if this word is the identifier, replace the '-' with this word.
                    elif re.search('[a-zA-Z]{2,256}\\.[a-zA-Z0-9]{2,256}', words[k]):
                        ids[i].append(words[k])
                        #if it's a URL, add to references.
    indegree = []
    for i in range(len(ids)):
        #for each file data [fileID, ref1, ref2, ...]
        temp = 0
        for j in range(len(ids)):
            #for each file data (to compare against all the others)
            for k in range(1,len(ids[j][1:])+1):
                if ids[j][k] == ids[i][0]:
                    temp += 1
        indegree.append(temp)
    checked = []
    #do selection sort based on indegree
    for i in range(len(indegree)):
        checked.append(False)
    for i in range(len(indegree)):
        maxPos = 0
        maxData = indegree[0]
        for j in range(len(indegree)):
            if (indegree[j] > maxData and not checked[j]) or (checked[maxPos] and not checked[j]):
                maxData = indegree[j]
                maxPos = j
        checked[maxPos] = True
        output.append([fileNames[maxPos], indegree[maxPos], len(ids[maxPos])-1])
        #add the file name, indegree, and outdegree to the output
    return output

### View sample input in 'dummy_test.py'

### Format of topological sort hits:
#   [File name, indegree, outdegree]

### SAMPLE OUTPUT:

"""
[
    ["The Cactus", 2, 0],
    ["The Story of An Hour", 1, 1],
    ["How the Camel Got His Hump", 1, 1],
    ["Cousin Tribulation's Story", 0, 2]
]

"""