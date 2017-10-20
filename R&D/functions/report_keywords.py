import os
import sys
import re

def removeChars(s):
    c = '\'!@#$%^&*().,><;:"[]{}\\|?/`~=+-_'
    a = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    output = ''
    for i in range(len(s)):
        if s[i] not in c and s[i] in a:
            output += s[i]
    return output
    
def isNum(s):
    for i in range(len(s)):
        if s[i] not in '0123456789':
            return False
    return True
    
def reportFormat(t):
	t = t.split('\n')
	t = map(tabsToSpaces, t)
	lengths = map(len, t)
	output = '+' + '-' * (max(lengths) + 2) + '+\n'
	for i in range(len(t)):
		if i != len(t) - 1:
			output += '| ' + t[i] + ' ' * (max(lengths) - lengths[i]) + ' |\n'
	output += '+' + '-' * (max(lengths) + 2) + '+\n\n'
	return output
	
def tabsToSpaces(s):
	output = ''
	for i in range(len(s)):
		if s[i] == '\t':
			output = ' '*4
		else:
			output += s[i]
	return output

def reportKeywords(fileContents,fileList,style,columns,occurrences):
    #Style should be set to l for list return
    #Style should be set to s for formatted string return
    f = open('/home/ubuntu/workspace/boring_words_filtered.txt', 'r') #Shouldn't require path
    boringWords = map(str.lower, map(str.strip, f.readlines()))
    f.close()
    output = reportFormat('All Keywords (' + str(columns) + ' column(s))\n(at least ' + str(occurrences) + ' occurrence(s)):\n')
    wordCounts = {}
    for i in range(len(fileContents)):
		for j in range(len(fileContents[i])):
		    words = map(str.strip, fileContents[i][j].split(' '))
		    words = map(removeChars, words)
		    for k in range(len(words)):
		        if words[k].lower() in map(str.lower, wordCounts.keys()) and words[k].lower() not in boringWords and not isNum(words[k].lower()):
		            wordCounts[words[k].lower()] += 1
		        else:
		            wordCounts[words[k].lower()] = 1
    finalOutput = []
    for key, value in wordCounts.iteritems():
        if value >= occurrences:
            finalOutput.append(key)
    finalOutput = sorted(finalOutput)
    if style == 'l':
        return finalOutput
    else: #do some column formatting
        if len(finalOutput) == 0:
            return output + 'None\n'
        formattedOutput = []
        columnWidths = []
        for i in range(columns):
            formattedOutput.append([])
        for i in range(len(finalOutput)):
            formattedOutput[i%columns].append(finalOutput[i])
        for i in range(len(formattedOutput)):
            columnWidths.append(max(map(len, formattedOutput[i])))
        for i in range(len(formattedOutput[0])):
            for j in range(len(formattedOutput)):
                if i < len(formattedOutput[j]):
                    output += formattedOutput[j][i] + ' ' * (columnWidths[j] - len(formattedOutput[j][i]) + 2)
            output += '\n'
        return output