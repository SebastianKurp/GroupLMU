from formatting import *
import re

def reportBySymbol(fileContents, fileNames, symbol, maxOutputLen = 60, style = 'by note'):
    # file contents is a list of strings, each of which is the entire body of a note/file.
    # file names is a list of strings as well,
    # only containing the name of the file which corresponds by index to the file contents list.
    # symbol is the STARTING CHARACTER that a word must have to be found.
    # max output length limits how long a string of output can be (for a clean output).
    #style: either 'by note' or 'by symbol'. Output for each style shown below.
    output = []
    # final output
    for i in range(len(fileNames)):
        # iterate through each file.
        currFile = [fileNames[i]]
        # start building a result for the current file, starting with this file's name.
        lines = fileContents[i].split('\n')
        for j in range(len(lines)):
            found = []
            mentions = []
            words = (lines[j]).split(' ')
            w = 0
            for k in range(len(words)):
                if re.search('^' + symbol, words[k]):
                    found.append(w)
                    mentions.append(words[k])
                # if the word is a mention, append the index of the word.
                w += len(words[k]) + 1
            for k in range(len(found)):
                # for each location where the word was a mention, format the output.
                line = formatLine(lines[j], maxOutputLen, found[k], mentions[k], j)
                currFile.append(line)
                # append the formatted output to the current file's result.
        if len(currFile) > 1:
            # if a mention in this file.
            output.append(currFile)
            # add this file's results to the final output.
    if style == 'by symbol':
        #if reporting should occur per symbolized phrase.
        dSymbol = {}
        #keep a dictionary of symbols as keys.
        #the value for each dictionary entry is a LIST of file names which contain the symbolized word.
        for i in range(len(output)):
            #go through each symbolized word.
            for j in range(1,len(output[i])):
                word = output[i][j][0]
                if word in dSymbol.keys():
                    #if the word is already in the dictionary.
                    dSymbol[word].append(output[i][0])
                    #just append the name of the file to the key.
                else:
                    dSymbol[word] = [output[i][0]]
                    #otherwise, create a new entry in the dictionary with the word as the key and a list with the single file name in it.
        tempOutput = []
        for key, value in dSymbol.items():
            tempOutput.append([key, list(set(value))])
            #format the output as shown below.
        output = tempOutput
    return output

### View sample input in 'dummy_test.py'

### Format of symbol hits:
#   [term, STRING of text surrounding the symbolized word, the line number, index of first letter of symbolized word in STRING, 
#   index of last letter of symbolized word in STRING]
#       first and last letter indexes to help with highlighting the word

### SAMPLE OUTPUT: search for '@' symbols, with a max output length of 60, with 'by note' style
#       This means the results will be organized per note, and not per symbolized word
"""

[
    ["The Story of An Hour",
        ["@mallard", "... ently as possible the news of her husband's death. @mallard", 2, 55, 62]
    ],
    ["How the Camel Got His Hump",
        ["@camel", '... the Camel; and the Horse went away and told the Man. @camel', 5, 57, 62],
        ["@man", '... aid the Camel; and the Dog went away and told the Man. @man', 7, 59, 62]
    ],
    ["The Cactus",
        ["@carruthers", '... agnified this exhibition of doubtful erudition. @carruthers', 12, 52, 62],
        ["@trysdale", "...  Trysdale's mind a swift @trysdale, scarifying retrospect of ...", 5, 29, 38]
    ]
]

"""

### SAMPLE OUTPUT: search for '#' symbols, with 'by symbol' style
#       This means the results will be organized per symbolized word, and not per note
"""

[
    ["#excited",
        ['How the Camel Got His Hump', "Cousin Tribulation's Story"]
    ],
    ["#porridge",
        ["Cousin Tribulation's Story"]
    ],
    ["#quiet",
        ['The Story of An Hour']
    ],
    ["#medicine",
        ['The Story of An Hour']
    ]
]

"""