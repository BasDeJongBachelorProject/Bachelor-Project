from statistics import *
import sys
import re
import rdflib

# to use this file, change the raw text variable to any .trig dataset in the .txt format
# an empty 'tempdump.txt' file needs to be present

#create empty lists to be used later
nanopublication = []
prefixes_per_nanopublication = []
size_per_nanopublication = []
triples_per_nanopublication = []
pieces_of_information_per_nanopublication = []

#'split' the text on the separate sections
raw_text = open("wp-monthy_all.trig.txt").read()
prefixes = re.findall('@prefix.*?sub:head', raw_text, re.DOTALL | re.IGNORECASE)
heads = re.findall('sub:head {.*?}\n', raw_text, re.DOTALL | re.IGNORECASE)
assertions = re.findall('sub:assertion {.*?}\n', raw_text, re.DOTALL | re.IGNORECASE)
provenances = re.findall('sub:provenance {.*?}\n', raw_text, re.DOTALL | re.IGNORECASE)
publicationInfos = re.findall('sub:publicationInfo {.*?}', raw_text, re.DOTALL | re.IGNORECASE)
pubInfos = re.findall('sub:pubinfo {.*?}', raw_text, re.DOTALL | re.IGNORECASE)


publicationindex=0
pubindex=0




for i in range(len(prefixes)):
    #rebuild prefixes from splitting to how it originally was
    splitter = re.split('\nsub:head', prefixes[i], flags=re.IGNORECASE)
    prefixes[i] = splitter[0]

    #recreate nanopublication
    enter = '\n'

    #deal with different graph names
    if heads[i].split('\n')[3].split()[1].lower() == 'sub:publicationinfo':
        publication = publicationInfos[publicationindex]
        publicationindex += 1
    else:
        publication = pubInfos[pubindex]
        pubindex += 1

    seq = (prefixes[i], heads[i], assertions[i], provenances[i], publication)
    nanopublication.append(enter.join(seq))
    nanolines = nanopublication[i]

    #create graph and initialize for loops for going through triples
    #done through extra text file because rdflib does not accept a string as input
    file = open('tempdump.txt', 'w')
    file.write(nanolines)
    file.close()
    g = rdflib.ConjunctiveGraph()
    g.parse('tempdump.txt', format="trig")
    j = 0
    number_of_triples = 0
    pieces_of_information = 0

    #go through all graphs
    for ctx in g.contexts():
        j += 1
        for s, p, o in g.triples((None, None, None), context=ctx):
            number_of_triples += 1
            if j % 4 == 2:
                pieces_of_information += 1

    #write to file for easy access
    file = open('nanostats.txt', 'a')
    textwrite = str(len(prefixes[i].split('\n')) - 1)
    textwrite += ','
    textwrite += str(sys.getsizeof(nanolines))
    textwrite += ','
    textwrite += str(number_of_triples)
    textwrite += ','
    textwrite += str(pieces_of_information)
    textwrite += '\n'
    file.write(textwrite)
    file.close()


#simple way to get all statistics at once
statistics = [prefixes_per_nanopublication, size_per_nanopublication,
              triples_per_nanopublication, pieces_of_information_per_nanopublication]

for i in statistics:
    print(mean(i), harmonic_mean(i), median(i), median_low(i),
      median_high(i), median_grouped(i), pvariance(i),
      variance(i), pstdev(i), stdev(i))


