import json
import os
import itertools
import re


with open('./database.json', 'r') as f:
    data = json.load(f)


#l = data['1']['genres']

""" dictionar = {}

for k in range(1, len(data)):
    try:
        l = data[str(k)]['genres']
        for i in range(1, len(l)+1):
            for j in itertools.combinations(l, i):
                temp = str(j).lower()
                dictionar[temp] = []
    except KeyError:
        pass

for k in range(1, len(data)):
    try:
        l = data[str(k)]['genres']
        for i in range(1, len(l)+1):
            for j in itertools.combinations(l, i):
                temp = str(j).lower()
                dictionar[temp].append(k)
    except KeyError:
        pass



os.remove('./keywords.json')

with open('./keywords.json', 'w') as fd:
    json.dump(dictionar, fd, indent=4) """


""" years_dictionar = {}

for k in range(1, len(data)):
    try:
        title = data[str(k)]['title']
        year = re.search(r'\([0-9]+\)',title).group()[1:5]
        years_dictionar[str(year)] = []
    except KeyError:
        pass

for k in range(1, len(data)):
    try:
        title = data[str(k)]['title']
        year = re.search(r'\([0-9]+\)',title).group()[1:5]
        years_dictionar[str(year)].append(k)
    except KeyError:
        pass

os.remove('./years.json')

with open('./years.json', 'w') as fd:
    json.dump(years_dictionar, fd, indent=4) """

ratings_dictionar = {}


for k in range(1, len(data)):
    try:
        rating = data[str(k)]['rating']
        ratings_dictionar[str(rating)] = []
    except KeyError:
        pass

for k in range(1, len(data)):
    try:
        rating = data[str(k)]['rating']
        ratings_dictionar[str(rating)].append(k)
    except KeyError:
        pass

os.remove('./ratings.json')

with open('./ratings.json', 'w') as fd:
    json.dump(ratings_dictionar, fd, indent=4)