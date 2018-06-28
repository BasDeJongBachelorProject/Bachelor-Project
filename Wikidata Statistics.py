from statistics import *
import sys
import rdflib
import os

#to use this file, place it in a folder with only wikidata .ttl entries and an empty 'wikistats.txt'

#read file
filelist = os.listdir("C:/Users/User/PycharmProjects/BPI/Wiki Entries")
filelist = filelist[:-2]

#create empty lists
prefixes_per_wikidata = []
size_per_wikidata = []
pieces_of_information_per_wikidata = []
triples_per_wikidata = []
number = 0

#read every file and parse
for file in filelist:
    number += 1
    print(number)
    i = 0
    text = open(file, encoding="utf8").read()
    original_text = text
    text = text.split('\n')
    prefixes = []
    triples = 0
    pieces_of_information = 0

    g = rdflib.ConjunctiveGraph()
    g.parse(file, format="n3")

    #access ctx
    for ctx in g.contexts():
        x = 5

    for s, p, o in g.triples((None, None, None), context=ctx):
        triples += 1

    #finding amount of prefixes
    while text[i].startswith("@prefix"):
        prefixes.append(text[i])
        i += 1

    #finding pieces of information and triples
    for k in range(len(text)-i):
        j = k + i
        if text[j].startswith('\t'):
            if text[j].startswith('\trdfs'):
                pieces_of_information += 1
            elif text[j].startswith('\tskos:'):
                if text[j+1].startswith('\tschema:'):
                    if text[j-1].startswith('\trdfs'):
                        pieces_of_information += 0
                    else:
                        pieces_of_information += 1
                else:
                    pieces_of_information += 1
            elif text[j].startswith('\tschema:'):
                if text[j-1].startswith('\tskos:'):
                    if text[j-2].startswith('\trdfs'):
                        pieces_of_information += 0
                    else:
                        pieces_of_information += 1
                else:
                    pieces_of_information += 1
            else:
                pieces_of_information += 1

    #determine file size
    file_size = sys.getsizeof(original_text)

    #add statistics
    prefixes_per_wikidata.append(len(prefixes))
    size_per_wikidata.append(file_size)
    pieces_of_information_per_wikidata.append(pieces_of_information)
    triples_per_wikidata.append(triples)

    #write to file for easy access
    file = open('wikistats.txt', 'a')
    textwrite = str(len(prefixes))
    textwrite += ','
    textwrite += str(file_size)
    textwrite += ','
    textwrite += str(triples)
    textwrite += ','
    textwrite += str(pieces_of_information)
    textwrite += '\n'
    file.write(textwrite)
    file.close()


#simple way to get all statistics at once
statistics = [prefixes_per_wikidata, size_per_wikidata,
              triples_per_wikidata, pieces_of_information_per_wikidata]

for i in statistics:
    print(mean(i), harmonic_mean(i), median(i), median_low(i),
      median_high(i), median_grouped(i), pvariance(i),
      variance(i), pstdev(i), stdev(i))
