import os
import re


def getCharPhrases(charFile, name):

	index = 1
	charsList = open(charFile).read().split(',')
	charsLower = [c.lower() for c in charsList if c != name]
	regex = re.compile('[^a-zA-Z]')

	for filename in os.listdir(name + 'Acts'):
		
		actText = open(os.path.join(name + 'Acts', filename)).read()
		actText = actText.replace('\n', '')
		actText = actText.lower()
		actText = actText.replace(name.lower(), '')
		actText = actText.split()
		
		for char in charsLower:

			charFile = open(os.path.join(name+ 'CharPhrases', char + 'Act' + str(index) + '.txt'), 'a')

			i = 0
			while i < len(actText):

				cleaned_text = regex.sub('', actText[i])
				if char == cleaned_text:

					low_bound = max(0, i-10)
					high_bound = min(i+10, len(actText))
					phrase = ''

					for j in range(low_bound, high_bound):

						if j != high_bound-1: 
							phrase += actText[j] + ' '
						else:
							phrase += actText[j] + '\n'
							
					i = high_bound-1
					charFile.write(phrase)
				i+= 1

			charFile.close()

		index+=1


getCharPhrases('hamletChars.txt', 'Hamlet')
getCharPhrases('titusChars.txt', 'Titus')
getCharPhrases('theSpanishTragedyChars.txt', 'Hieronimo')