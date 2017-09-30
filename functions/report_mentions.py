import os
import sys
import re
from report_keywords import reportFormat

def reportMentions(fileContents,fileList):
	flag = False
	output = reportFormat('Mentions Report:\n')
	for i in range(len(fileContents)):
		tempMentions = []
		for j in range(len(fileContents[i])):
			if re.search('[@#]', fileContents[i][j]):
				line = fileContents[i][j].split(' ')
				for k in range(len(line)):
					if re.search('^[@#]', line[k]):
						tempMentions.append(line[k].strip())
		if len(tempMentions) > 0:
			output += fileList[i] + '\n'
			tempMentions = list(set(tempMentions))
			for j in range(len(tempMentions)):
				output += '\t' + tempMentions[j] + '\n'
			flag = True
	if not flag:
		output += 'None\n'
	return output
