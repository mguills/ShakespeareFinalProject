import numpy as np
import os
import ast
import matplotlib.pyplot as plt

# score = (10.51, 9.71, 8.71, 8.19)

# ind = np.arange(len(score))  # the x locations for the groups
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(ind - width/2, score, width, color='SkyBlue')

# ax.set_ylabel('Scores')
# ax.set_title('Collocation by Scores')
# ax.set_xticks(ind)
# ax.set_xticklabels(('Sweet, Bianca', 'BIANCA, Leave', 'BIANCA, Save', 'sweet, Bianca'))
# ax.legend()

# plt.show()

"""
Sentiment Analysis: look at how a given character describes other characters.
We can do this by looking at dialogue of the given character.
See when they mention other characters and collations of adjectives surrounding
character collations.
"""

def plot(num, filelist):
    for filename in filelist:
        with open(filename) as f:

            name = filename[filename.find('/')+1:filename.find('act')]
            act_num = filename[filename.find('act')+3:filename.find('act')+4]
            name = name[0].upper() + name[1:]
            title = name + ' Act ' + act_num

            words = f.readlines()
            mylist = [ast.literal_eval(words[i]) for i in range(1,len(words))]
            score = tuple(map(lambda x: x[1], mylist[:num]))
            ind = np.arange(len(score))
            width = 0.35
            fig, ax = plt.subplots()
            rects1 = ax.bar(ind - width/2, score, width, color='SkyBlue')
            ax.set_ylabel('Scores')
            ax.set_title('Bigram Scores for ' + title)
            ax.set_xticks(ind)
            labels = tuple(map(lambda x: str(x[0][0] + ", " + x[0][1]), mylist[:num]))
            ax.set_xticklabels(labels)
            ax.legend()
            plt.show()

plot(4, ['HamletActBigrams/iact1.txt', 'HamletActBigrams/iact2.txt', 'HamletActBigrams/iact3.txt', 'HamletActBigrams/iact4.txt', 'HamletActBigrams/iact5.txt',
        'HamletActBigrams/meact1.txt', 'HamletActBigrams/meact2.txt', 'HamletActBigrams/meact3.txt', 'HamletActBigrams/meact4.txt', 'HamletActBigrams/meact5.txt',
        'HamletActBigrams/motheract1.txt', 'HamletActBigrams/motheract2.txt', 'HamletActBigrams/motheract3.txt', 'HamletActBigrams/motheract4.txt', 'HamletActBigrams/motheract5.txt',
        'HamletActBigrams/fatheract1.txt', 'HamletActBigrams/fatheract2.txt', 'HamletActBigrams/fatheract3.txt', 'HamletActBigrams/fatheract4.txt', 'HamletActBigrams/fatheract5.txt',
        'HamletActBigrams/kingact1.txt', 'HamletActBigrams/kingact2.txt', 'HamletActBigrams/kingact3.txt', 'HamletActBigrams/kingact4.txt', 'HamletActBigrams/kingact5.txt',
        'HamletActBigrams/kingact1.txt', 'HamletActBigrams/kingact2.txt', 'HamletActBigrams/kingact3.txt', 'HamletActBigrams/kingact4.txt', 'HamletActBigrams/kingact5.txt'])
