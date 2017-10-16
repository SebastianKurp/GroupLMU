import os
import sys
import re
from report_mentions import reportMentions
from organize_by_mention import organizeByMention
from report_keywords import reportKeywords, isNum, reportFormat
from notes_by_keyword import notesByKeyword
from topological_sort import topologicalSort
from search_term import searchTerm

def menu(isWrite):
	if isWrite:
		toggle = 'ON '
	else:
		toggle = 'OFF'
	output = ''
	output += "+------------------------------------------------------------+\n"
	output += "| Please select a tool:                                      |\n"
	output += "|                                                            |\n"
	output += "| +--------------------+              +--------------------+ |\n"
	output += "| | A. Report mentions |              | Write to file: " + toggle + " | |\n"
	output += "| +--------------------+              | T. Toggle          | |\n"
	output += "|                                     +--------------------+ |\n"
	output += "| +------------------------------+                           |\n"
	output += "| | B. Organize notes by mention |                           |\n"
	output += "| +------------------------------+                           |\n"
	output += "|                                                            |\n"
	output += "| +--------------------+                                     |\n"
	output += "| | C. Report keywords |                                     |\n"
	output += "| +--------------------+                                     |\n"
	output += "|                                                            |\n"
	output += "| +-----------------------------------+                      |\n"
	output += "| | D. Search term (syntax: D [term]) |                      |\n"
	output += "| +-----------------------------------+                      |\n"
	output += "|                                                            |\n"
	output += "| +---------------------+                                    |\n"
	output += "| | E. Notes by keyword |                                    |\n"
	output += "| +---------------------+                                    |\n"
	output += "|                                                            |\n"
	output += "| +---------------------------------+                        |\n"
	output += "| | F. Topologically sort all notes |                        |\n"
	output += "| +---------------------------------+                        |\n"
	output += "|                                                            |\n"
	output += "| +---------------+                                          |\n"
	output += "| | Q. QUIT NOTES |                                          |\n"
	output += "| +---------------+                                          |\n"
	output += "+------------------------------------------------------------+\n"
	return output
	
def save(output,wroteSomething):
	os.chdir('..')
	while True:
		print reportFormat("Thank you for using Notes.\n")
		if wroteSomething:
			userInput = '-'
			while userInput != 'y' and userInput != 'n':
				print reportFormat("Would you like to save your work? (y/n)\n")
				userInput = raw_input().strip().lower()
			if userInput == 'y':
				print reportFormat('Please name your save file.\n')
				fileName = raw_input()
				if os.path.isfile(fileName):
					userInput = '-'
					while userInput.lower() != 'y' and userInput.lower() != 'n':
						print reportFormat(fileName + ' already exists. Overwrite? (y/n)\n')
						userInput = raw_input().strip().lower()
					if userInput == 'y':
						o = open(fileName, 'w')
						o.write(output)
						o.close()
						break
				else:
					try:
						o = open(fileName, 'w')
						o.write(output)
						o.close()
						break
					except:
						print reportFormat('invalid file name/directory.\n')
			else:
				break
		else:
			break

def checkSyntaxValidity(fn,line,terms,desc,isNumList,isRequired,defaults):
	output = defaults
	error = 'Invalid entry; correct input:\n' + fn
	for i in range(len(terms)):
		if isNumList[i]:
			n = 'integer'
		else:
			n = 'string'
		if isRequired[i]:
			m = 'required'
		else:
			m = 'default = ' + str(defaults[i])
		error += ' ' + terms[i] + ' ' + '[' + n + ': ' + desc[i] + ' | ' + m + ']'
	for i in range(len(isRequired)):
		if isRequired[i]:
			if terms[i] not in line:
				print '1'
				return [False, error + '\n']
	if len(line) % 2 == 0:
		print '2'
		return [False, error + '\n']
	for i in range((len(line)-1)/2):
		if line[i*2+1] in terms:
			index = terms.index(line[i*2+1])
			if (isNum(line[i*2+2]) and isNumList[index]) or not isNumList[index]:
				if (isNum(line[i*2+2]) and isNumList[index]):
					line[i*2+2] = int(line[i*2+2])
				output[index] = line[i*2+2]
			else:
				print '3'
				return [False, error + '\n']
		else:
			print '4'
			return [False, error + '\n']
	return output

def main():
	if len(sys.argv) < 2:
		print reportFormat('Please add the directory in which your notes are found:\npython notes.py path/to/notes/\n')
		return
	os.chdir(sys.argv[1])
	fileList = os.listdir(os.curdir)
	fileContents = list(fileList)

	for i in range(len(fileList)):
		fileContents[i] = open(fileList[i], 'r').readlines()
		
	userInput = '-'
	newData = ''
	write = True
	output = ''
	wroteSomething = False
	
	while True:
		flag = True
		print menu(write)
		userInput = map(str.strip,raw_input().split(' '))
		
		if userInput[0].lower() == 'a':
			newData = reportMentions(fileContents,fileList)
			
		elif userInput[0].lower() == 'b':
			newData = organizeByMention(fileContents, fileList)
			
		elif userInput[0].lower() == 'c':
			userInput = checkSyntaxValidity('C', userInput, ['-c','-s'], ['number of columns','minimum number of occurrences'], [True,True], [False,False], [2,3])
			if not userInput[0]:
				print reportFormat(userInput[1])
				flag = False
			else:
				newData = reportKeywords(fileContents,fileList,'s',userInput[0],userInput[1])
				
		elif userInput[0].lower() == 'd':
			userInput = checkSyntaxValidity('D', userInput, ['-t'], ['term to be searched for'], [False], [True], [0])
			if not userInput[0]:
				print reportFormat(userInput[1])
				flag = False
			else:
				newData = searchTerm(fileContents,fileList,userInput[0])
		elif userInput[0].lower() == 'e':
			userInput = checkSyntaxValidity('E', userInput, ['-f','-n'], ['minimum number of files containing a given keyword','minimum number of keyword occurrences'], [True,True], [False,False], [2,3])
			if not userInput[0]:
				print reportFormat(userInput[1])
				flag = False
			else:
				newData = notesByKeyword(fileContents,fileList,userInput[0],userInput[1])
			
		elif userInput[0].lower() == 'f':
			newData = topologicalSort(fileContents, fileList)
			
		elif userInput[0].lower() == 't':
			if write:
				toggle = 'OFF'
				write = False
			else:
				toggle = 'ON '
				write = True
			print reportFormat('Writing to file has been toggled ' + toggle + '\n')
			flag = False
			
		elif userInput[0].lower() == 'q':
			break
		
		else:
			print reportFormat("Please choose one of the options below.\n")
			flag = False
		if flag:
			if write:
				wroteSomething = True
				print reportFormat("The following has been added to your Analysis Output:\n")
				output += newData + '\n'
			print reportFormat(newData)
		print reportFormat('PRESS ENTER TO CONTINUE\n')
		z = raw_input()
			
	save(output,wroteSomething)
	
main()