def charsToSpaces(s):
    #changes characters in 'chars' into spaces
    output = ''
    chars = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
    for i in range(len(s)):
        if not s[i] in chars:
            output += s[i]
        else:
            output += ' '
    return output

def formatLine(l, maxLen, index, term, lineNumber):
    #formats the output for ease of us in front end
    if len(term) > maxLen:
    	print("ERROR: max output length shorter than term.")
    	return None
    if len(l) <= maxLen:
        #if the length of the line is less than maxLength, you don't need to do anything
        line = l
        loc = index
    elif index + len(term) + (maxLen - len(term)) // 2 > len(l):
        #if the term is too far to the RIGHT of the line to be centered, format
        line = '... ' + l[-(maxLen - 1):]
        loc = maxLen - (len(l) - index + 1) + 4
    elif index - (maxLen - len(term)) // 2 < 0:
        #if the term is too far to the LEFT of the line to be centered, format
        line = l[0:maxLen] + ' ...'
        loc = index
    else:
        #if the term can be centered and the line is too long, format
        line = '... ' + l[index - (maxLen - len(term)) // 2:index + len(term) + (maxLen - len(term)) // 2] + ' ...'
        loc = (maxLen + 8 - len(term)) // 2
    return [line, lineNumber, loc, loc + len(term) - 1]