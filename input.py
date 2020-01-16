from nltk.tokenize import word_tokenize
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re


word_lem = WordNetLemmatizer()
stop_words = stopwords.words('english')
punctuation = re.compile(r'[-.?!:;\'\"\`\\\/\|()]')

def clear_punctuation(lista_tokens):
    output_list = []

    for item in lista_tokens:
        word = punctuation.sub("", item)
        if len(word) > 0:
            output_list.append(word)

    return output_list

def lower_case_tokens(lista_tokens):
    output_list = []

    for item in lista_tokens:
        item = str.lower(item)
        output_list.append(item)
    
    return output_list

def elimination_of_stopwords(lista_tokens):
    output_list = []

    for item in lista_tokens:
        if item not in stop_words:
            output_list.append(item)
    
    return output_list

def lematizare_tokens(lista_tokens):
    output_list = []

    for item in lista_tokens:
        temp = word_lem.lemmatize(item)
        output_list.append(temp)

    return output_list

#input_message = input("Message introduction: ")
#print(input_message)

def input_function(input_message):
    
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
    irrelevant_nouns = ['movie', 'story', 'film']

    #print(altered_tagged_list)

    for tag in tagged_tokens:
        if tag[0] not in message_tokens:
            altered_tagged_list.remove(tag)
        elif tag[0] in irrelevant_nouns:
            altered_tagged_list.remove(tag)
        elif tag[1] in verbs_tags:
            altered_tagged_list.remove(tag)
        
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

    if len(movies) > 10:
        list_of_movies = random.sample(movies, 10)
    else:
        list_of_movies = movies.copy()

    #print(list_of_movies)

    with open('./database.json','r') as f:
        database = json.load(f)

    final_list = []

    for item in list_of_movies:
        #print(database[str(item)])
        final_list.append(database[str(item)])

    return final_list
