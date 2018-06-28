import matplotlib.pyplot as plt
import numpy as np


#open files
nano = open("nanostats.txt").read()
nano = nano.split('\n')
for i in range(len(nano)):
    nano[i] = nano[i].split(',')

wiki = open("wikistats.txt").read()
wiki = wiki.split('\n')
for i in range(len(wiki)):
    wiki[i] = wiki[i].split(',')

#create empty lists
nanoprefixes = []
nanosize = []
nanotriples = []
nanoinformation = []

wikiprefixes = []
wikisize = []
wikitriples = []
wikiinformation = []

#create lists with statistics
for i in nano:
    nanoprefixes.append(int(i[0]))
    nanosize.append(int(i[1]))
    nanotriples.append(int(i[2]))
    nanoinformation.append(int(i[3]))

for i in wiki:
    wikiprefixes.append(int(i[0]))
    wikisize.append(int(i[1]))
    wikitriples.append(int(i[2]))
    wikiinformation.append(int(i[3]))

#use these lists for examples below

#print(max(nanosize))

#plt.hist(nanosize, 2000)
#plt.show()

# data = wikiinformation
# plt.hist(data, 200)
# plt.xlabel('Pieces of information (Wikidata)')
# plt.ylabel('Occurrence')
# plt.show()

# plt.hist(nanosize)
# plt.xlabel('File Size (Nanopublication)')
# plt.ylabel('No of times')
# plt.show()

# plt.boxplot(nanosize)
# plt.show()


# plt.scatter(wikitriples, wikiinformation)
# plt.ylabel('Pieces of information (Wikidata)')
# plt.xlabel('Number of triples (Wikidata)')
# plt.show()


# #wiki
# x_range = range(0, 40000)
# x = np.array(x_range)
#
# formula = 'x*150'
# y = eval(formula)
# plt.plot(x, y)
# formula = 'x*66.6666667'
# y = eval(formula)
# plt.plot(x, y)
#
# #nano
# formula = 'x*70'
# y = eval(formula)
# plt.plot(x, y)
#
# plt.ylabel('File Size in bytes')
# plt.xlabel('Number of triples')
#
# plt.show()
