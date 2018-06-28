from operator import itemgetter

wiki = open("wikistats.txt").read()

wiki=wiki.split('\n')
for i in range(len(wiki)):
    temp = wiki[i].split(',')
    wiki[i] = list(map(int, temp))


#wiki = sorted(wiki, key=itemgetter(1))

wiki.sort(key=lambda x: x[1])


upper = []
lower = []

counter = 0
for i in wiki:
    counter += 1
    if int(i[1])/int(i[2]) > 100:
        upper.append(counter)
    else:
        lower.append(counter)


print(upper)
print(lower)


print (wiki[0][1])
print (wiki[1][1])
print (wiki[2][1])
print (wiki[3][1])
print (wiki[4][1])
print (wiki[5][1])
print (wiki[6][1])
print (wiki[7][1])
