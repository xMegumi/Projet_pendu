def indices(lettre, mot):
    '''Documentation :
Utilise 2 arguments "lettre" puis "mot" et
renvoie sous forme d'une liste l'indiçage de la répétition de
la lettre dans le mot.

exemple :
>>> indices('a', 'essai')
[3]
>>> indices('s','essai')
[1,2]
'''
    indice = []
    for i in range(len(mot)):
        if mot[i] == lettre:
            indice.append(i)
    return indice

def remove_accents(word):
    '''Documentation : 
Retire les accents du mot 'word' et renvoie 
le mot en minuscule.

exemple :
>>> remove_accents("théâtre")
theatre
>>> remove_accents("ÉPÉISTE")
epeiste
'''
    word = word.lower()
    word = list(word)
    accents = {'a' : ['à', 'â', 'ä'],'e' : ['é','è','ê','ë'],'i' : ['ï','î'], 'o' : ['ô','ö'], 'u' : ['ù','û','ü'], 'c' : 'ç'}
    for key, value in accents.items():
        for i in word:
            if i in value:
                index = word.index(i)
                word[index] = key
    return ''.join(word)
