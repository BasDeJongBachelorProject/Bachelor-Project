import random

random_list = []
random_list = random.sample(range(1, 9999999), 10000)
for i in random_list:
    print("https://www.wikidata.org/wiki/Special:EntityData/Q", i, ".ttl", sep = '')