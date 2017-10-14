import os
import sys
import re
from report_keywords import reportFormat

def organizeByMention(fileContents,fileList):
	output = reportFormat('Notes organized by Mention:\n')
	fileMentions = []
	mentions = []
	for i in range(len(fileContents)):
		tempMentions = [fileList[i]]
		for j in range(len(fileContents[i])):
			if re.search('[@#]', fileContents[i][j]):
				line = fileContents[i][j].split(' ')
				for k in range(len(line)):
					if re.search('^[@#]', line[k]):
						tempMentions.append(line[k].strip())
						mentions.append(line[k].strip())
		fileMentions.append(tempMentions)
	mentions = list(set(mentions))
	if len(mentions) == 0:
		output += 'None\n'
	for i in range(len(mentions)):
		output += mentions[i] + '\n'
		for j in range(len(fileMentions)):
			if mentions[i] in fileMentions[j]:
				output += '\t' + fileMentions[j][0] + '\n'
	return output
