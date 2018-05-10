import os
from collections import defaultdict
import re


def getCharCounts(charFile, name):
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

		charDict = defaultdict(int)

		for char in charsLower:

			for text in actText:

				cleaned_text = regex.sub('', text)
				if char == cleaned_text:

					charDict[char]+=1

		print(charDict) 
		print('\n')

	print('\n')


getCharCounts('hamletChars.txt', 'Hamlet')
getCharCounts('titusChars.txt', 'Titus')
getCharCounts('theSpanishTragedyChars.txt', 'Hieronimo')


