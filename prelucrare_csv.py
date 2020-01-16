import pandas
import json
import os

movies = pandas.read_csv('ml-latest-small/movies.csv')  # movieId,title,genres;
movies = movies.dropna(axis=0, how='any')
ratings = pandas.read_csv('ml-latest-small/ratings.csv', usecols=['movieId', 'rating'])
ratings = ratings.dropna(axis=0, how='any')
tags = pandas.read_csv('ml-latest-small/tags.csv', usecols=['movieId', 'tag'])
tags = tags.dropna(axis=0, how='any')

# print(ratings)

dictionar = {}

for i in range(len(movies)):
    try:
        item = int(movies['movieId'][i])
        temp_list = movies['genres;'][i].split("|")
        temp_list[-1] = temp_list[-1].replace(';', '')
        temp_dict = dict([('title', movies['title'][i]),
                          ('genres', temp_list), ('tags', []), ('rating', 0.0)])
        dictionar[item] = temp_dict
    except ValueError:
        pass
    except KeyError:
        pass

for i in range(len(tags)):
    try:
        temp_id = int(tags['movieId'][i])
        temp_tag = str(tags['tag'][i])
        dictionar[temp_id]['tags'].append(temp_tag)
    except ValueError:
        pass
    except KeyError:
        pass

for i in range(len(ratings)):
    try:
        temp_id = int(ratings['movieId'][i])
        temp_rating = float(ratings['rating'][i])
        dictionar[temp_id]['rating'] = temp_rating
    except ValueError:
        pass
    except KeyError:
        pass

os.remove('./database.json')

with open('./database.json', 'w') as f:
    json.dump(dictionar, f, indent=4)

