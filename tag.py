import nltk
               
charactersFile='hieronimoLines.txt' 
try: 
    rawCharacters=open(charactersFile).read()
except IOError: 
    parser.error("Can't find Oth_char file. Do you have a characters.txt in this directory, or did you specify its location in an option?") 

tokens = nltk.wordpunct_tokenize(rawCharacters)
def processContent():
    try:
        filename = 'tagged' + '_' + charactersFile + '.txt'
        f = open(filename, 'w+')
        for item in tokens:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            f.write(str(tagged) + "\n")
        f.close()
    except Exception as e:
        print(str(e))
    
processContent()


"""
Pos tag list:
CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-adverb	where, when

"""