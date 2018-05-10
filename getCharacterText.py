def getTitusText():
	file = open('titusAndronicus.txt')
	lines = file.read().split('\n')
	titus_lines = ''

	for i in range(len(lines)):
		if lines[i] == 'TITUS' or lines[i].startswith('ACT'):
			while lines[i] != '':
				if not lines[i].startswith('[') or not lines[i].endswith(']'):
					titus_lines += removeBrackets(lines[i].strip()) + '\n'
				i+=1
			titus_lines += '\n'
		i+=1

	file.close()
	file = open("titusLines.txt", "w")
	file.write(titus_lines)
	file.close()

def getSpanishText():
	file = open('theSpanishTragedy.txt')
	lines = file.read().split('\n')
	main_lines = ''

	for i in range(len(lines)):
		if lines[i].startswith('HIERONIMO:') or lines[i].startswith('ACT'):
			while lines[i] != '':
				if not lines[i].startswith('[') or not lines[i].endswith(']'):
					main_lines += removeBrackets(lines[i].replace('~', '').strip()) + '\n'
				i+= 1
			main_lines += '\n'
		i+=1

	file.close()
	file = open('hieronimoLines.txt', 'w')
	file.write(main_lines)
	file.close()

def getHamletText():
	file = open('hamlet.txt')
	lines = file.read().split('\n')
	main_lines = ''

	for i in range(len(lines)):
		if lines[i].startswith('HAMLET') or lines[i].startswith('ACT'):
			while lines[i] != '':
				if not lines[i].startswith('[') or not lines[i].endswith(']'):
					main_lines += removeBrackets(lines[i].strip()) + '\n'
				i+= 1
			main_lines += '\n'
		i+=1

	file.close()
	file = open('hamletLines.txt', 'w')
	file.write(main_lines)
	file.close()

def removeBrackets(s):
	s1 = ""
	i=0
	while i < len(s):
		if s[i] != '[' and s[i] != ']':
			s1 += s[i]
			i+=1
		else:
			i+=1
			while i < len(s) and s[i] != ']':
				i+=1
			i+=1
	return s1

getTitusText()
getSpanishText()
getHamletText()