from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


tone_analyzer = ToneAnalyzerV3(
	username='ff66eb7b-7442-4681-9449-86aa38dad37d',
	password='flKl6t2dX73q',
	version='2017-09-26'
)

def get_tones(filelist):

	for file in filelist:
		word = file[file.find('/')+1:file.find('act')]
		word = word[0].upper() + word[1:]
		act_num = file[file.find('act')+3:file.find('act')+4]
		title = word + ' Act ' + act_num

		text = open(file).read()
		tones_dict = defaultdict(float)
		tones = json.dumps(tone_analyzer.tone(tone_input=text, content_type="text/plain"))
		tones = json.loads(tones)

		for sentence in tones['sentences_tone']:
			print(sentence['text'])
			for tone in sentence['tones']:
				print(tone['tone_id'])
				print(tone['score'])
				tones_dict[tone['tone_id']] += tone['score']
			print('\n')

		tones_list = ['anger', 'fear', 
		'joy', 'sadness', 'analytical', 'confident', 'tentative']

		scores = [tones_dict[tones_list[i]] for i in range(len(tones_list))]

		ind = np.arange(len(scores))
		width = 0.35
		fig, ax = plt.subplots()
		rects1 = ax.bar(ind - width/2, scores, width, color='SkyBlue')
		ax.set_ylabel('Scores')
		ax.set_title('Tone Scores for ' + title)
		ax.set_xticks(ind)
		ax.set_xticklabels(tones_list)
		ax.legend()
		plt.show() 

get_tones(['HieronimoCharPhrases/youact4.txt', 'HieronimoCharPhrases/lorenzoact4.txt', 'HieronimoCharPhrases/iact4.txt', 'HieronimoCharPhrases/meact4.txt'])





	