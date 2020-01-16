from input import *

#input_message = input("Introdu search: ")
def form_function(input_message):
    message_tokens = word_tokenize(input_message)
    #print(message_tokens)

    message_tokens = lower_case_tokens(message_tokens)
    #print(message_tokens)

    message_tokens = clear_punctuation(message_tokens)
    #print(message_tokens)

    #message_tokens = lematizare_tokens(message_tokens)
    #print(message_tokens)

    #message_tokens = elimination_of_stopwords(message_tokens)
    #print(message_tokens)

    import nltk

    #print(nltk.pos_tag(message_tokens))

    tagged_tokens = nltk.pos_tag(message_tokens)

    message_tokens = lematizare_tokens(message_tokens)

    message_tokens = elimination_of_stopwords(message_tokens)

    altered_tagged_list = tagged_tokens.copy()

    verbs_tags = ['VB','VBD','VBG','VBN','VBP','VBZ']
    irrelevant_nouns = ['movie', 'story', 'film', 'year', 'rating']

    #print(altered_tagged_list)

    year = None
    rating = None

    for tag in tagged_tokens:
        if tag[0] not in message_tokens:
            altered_tagged_list.remove(tag)
        elif tag[0] in irrelevant_nouns:
            altered_tagged_list.remove(tag)
        elif tag[1] in verbs_tags:
            altered_tagged_list.remove(tag)
        elif tag[1] == 'CD' and len(tag[0]) > 3:
            altered_tagged_list.remove(tag)
            year = tag[0]
        elif tag[1] == 'CD':
            altered_tagged_list.remove(tag)
            rating = tag[0]
        
    #print(message_tokens)

    #print(altered_tagged_list)

    from nltk.corpus import wordnet 

    lista_genuri = ['action','adventure','animation','children','comedy','crime','documentary','drama','fantasy','horror','musical','mystery','romance','thriller','war','western','film-noir','sci-fi']

    lista_recomandari_genuri = []

    for (cuvant,tag) in altered_tagged_list:
        lista_distante = []
        synsets1 = wordnet.synsets(cuvant)
        #print(syn1)
        for item in lista_genuri:

            try:
                synsets2 = wordnet.synsets(item)
                #print(syn2)
                maxim_path = 0
                for syn1 in synsets1:
                    for syn2 in synsets2:
                        path = wordnet.wup_similarity(syn1,syn2)
                        try:
                            if path > maxim_path:
                                maxim_path = path
                        except TypeError:
                            pass
                lista_distante.append(maxim_path)
            except IndexError:
                pass
        #print(lista_distante)
        try:
            maxim = max(lista_distante)
            index = lista_distante.index(maxim)
            lista_recomandari_genuri.append(lista_genuri[index]) 
        except TypeError:
            pass


    #print(lista_recomandari_genuri)  

    import json
    import itertools

    with open('./keywords.json','r') as f:
        dictionar = json.load(f)

    temp_tuple = ()

    for string in lista_recomandari_genuri:
        temp = (string,)
        temp_tuple = temp_tuple + temp

    #print(temp_tuple)
    #print([x for x in itertools.permutations(temp)])

    combinatii_genuri = [str(x) for x in itertools.permutations(temp_tuple)]
    #print(combinatii_genuri)

    movies = []

    for combinatie in combinatii_genuri:
        try:
            movies = dictionar[combinatie]
        except KeyError:
            pass

    import random

    final_list_ids = []

    if len(movies) > 10 and year == None and rating == None:
        list_of_movies = random.sample(movies, 10)
    else:
        list_of_movies = movies.copy()

    #print(list_of_movies)

    #print(year)

    if year is None and rating is None:
        final_list_ids = list_of_movies.copy()
        #print(final_list_ids)
    elif rating is None:
        with open('./years.json','r') as f:
            years_dictionar = json.load(f)
        years_movies = years_dictionar[str(year)]
        #print(years_movies)
        if len(years_movies) > 10:
            list_of_years_movies = random.sample(years_movies, 10)
        else:
            list_of_years_movies = years_movies.copy()
        if len(list_of_movies) == 0 :
            final_list_ids = list_of_years_movies.copy()
        else:
            for item in list_of_years_movies:
                if item in list_of_movies:
                    final_list_ids.append(item)
    elif year is None:
        with open('./ratings.json','r') as f:
            rating_dictionar = json.load(f)
        rating_movies = rating_dictionar[rating[0]+"."+rating[1]]
        #print(rating_movies)
        if len(rating_movies) > 10:
            list_of_rating_movies = random.sample(rating_movies, 10)
        else:
            list_of_rating_movies = rating_movies.copy()
        if len(list_of_movies) == 0:
            final_list_ids = list_of_rating_movies.copy()
        else:
            for item in list_of_movies:
                if item in list_of_rating_movies:
                    final_list_ids.append(item)
    else:
        with open('./ratings.json','r') as f:
            rating_dictionar = json.load(f)
        with open('./years.json','r') as g:
            years_dictionar = json.load(g)
        years_movies = years_dictionar[str(year)]
        rating_movies = rating_dictionar[rating[0]+"."+rating[1]]
        if len(list_of_movies) == 0:
            for item in years_movies:
                if item in rating_movies and len(final_list_ids) < 10:
                    final_list_ids.append(item)
        else:
            for item in years_movies:
                if item in rating_movies and item in list_of_movies and len(final_list_ids) < 10:
                    final_list_ids.append(item)
        

    final_list = []

    with open('./database.json','r') as f:
        database = json.load(f)

    for item in final_list_ids:
        #print(database[str(item)])
        final_list.append(database[str(item)])

    #print(final_list)
    return final_list

