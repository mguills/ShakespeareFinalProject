import io, nltk, re, os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.collocations import *

def filter_stop_words(name ,text, stop_words, filtered_output_file):
	"""
	filter stop words from english language. 
	Also filters some new stop words from elizabethan english stopword list, 
	and writes output i.e filterd text into a new file named filtered_output_file.

	"""
	words = text.split() # The method split() returns a list of all the words in the string
	appendFile = open(filtered_output_file,'w')
	if not os.path.exists("/Users/matthewguillory/nltk_data/corpora/genesis/" + name + "ActsFiltered"):
		os.makedirs("/Users/matthewguillory/nltk_data/corpora/genesis/" + name + "ActsFiltered")
	corpusFile = open("/Users/matthewguillory/nltk_data/corpora/genesis/" + filtered_output_file, "w")
	for r in words:
		if not r in stop_words and r != name.upper(): # can also use functions like if r.isalpha() to filter punctuation
				appendFile.write(" "+r)
				corpusFile.write(" "+r)
	appendFile.close()
	corpusFile.close()

def getBigrams(charactersFile, name):
	index = 1
	for filename in os.listdir(name + 'Acts'):

		raw_text = open(os.path.join(name + 'Acts', filename))
		filtered_output_file = name + "ActsFiltered/" + "act" + str(index) + ".txt"

		bigram_measures = nltk.collocations.BigramAssocMeasures()
		# trigram_measures = nltk.collocations.TrigramAssocMeasures()

		new_stop_words = 'art,doth,dost,hast,hath,hence,hither,nigh,oft,thither,tither,thee,thou,thine,thy,wast,whence,wherefore,whereto,withal,ye,yon,yonder'
		new_stop_words_list = new_stop_words.split(',')
		stop_words = set(stopwords.words('english')) # We get a set of English stop words using the line
		stop_words.add(tuple(new_stop_words_list))
		filter_stop_words(name,raw_text.read(), stop_words, filtered_output_file) # function call

		finder = nltk.collocations.BigramCollocationFinder.from_words(nltk.corpus.genesis.words(filtered_output_file))
		# print(finder)
		bi_gram = finder.score_ngrams(bigram_measures.pmi)
		#Error check Characters file
		try: 
			rawCharacters=open(charactersFile).read()
		except IOError: 
			parser.error("Can't find characters file. Do you have a characters.txt in this directory, or did you specify its location in an option?") 


		character_list = rawCharacters.lower().split(',')
		#print(character_list)

		for character in character_list:
			filename = character + 'act' + str(index) + '.txt'
			f = open(name +'ActBigrams/' + filename, 'w+')
			f.write("-----------------" + character +"----------------\n")
			for i in bi_gram:
				if character.lower() == (i[0][0]).lower() or character.lower() == (i[0][1]).lower():
					f.write(str(i) +"\n")
			f.close()
		index +=1

getBigrams('hamletChars.txt', 'Hamlet')
getBigrams('titusChars.txt', 'Titus')
getBigrams('theSpanishTragedyChars.txt', 'Hieronimo')
