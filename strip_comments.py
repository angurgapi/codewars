#4 kyu

#Complete the solution so that it strips all text
#that follows any of a set of comment markers passed in.
#Any whitespace at the end of the line should also be stripped out. 

def solution(string, markers):
	lines = string.split('\n')
	newlist = []
	def line_cleaned(line,markers):
		nl = ''
		for char in line:
			if char not in markers:
				nl+=char
			else:
				break
		return nl.strip()

	for line in lines:
		newlist.append(line_cleaned(line,markers))
    
	return '\n'.join(newlist)

#print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))


