fruits=[
        ['fraise','rouge','sol','sans'],
        ['abricot','orange','arbre','noyau'],
        ['peche','orange','arbre','noyau'],
        ['cerise','rouge','arbre','noyau'],
        ['melon','vert','sol','pepins'],
        ['avocat','vert','arbre','noyau']
        ]

def fonction1(table):
    """
    Renvoie un tuple donnant le nombre d'éléments du tableau et le nombre de données dans élément[0]
    param: table : list
    return : tuple
    >>> fonction1(fruits)
    (6, 4)
    """
    return len(table),len(table[0])

def fonction2(table,indice,valeur):
    """
    Renvoie un nombre qui comptabilise le nombre d'élements pour lesquels la donnée d'indice donné prend la valeur donnée
    param : table : list
    param : indice : int
    param : valeur : str
    return : int
    >>> fonction2(fruits,1,'rouge')
    2
    """
    compteur=0
    for objet in table:
        if objet[indice]==valeur:
            compteur+=1
    return compteur

def fonction3(table,nom):
    """
    Renvoie True si un élément comportant comme première donnée nom est présent dans table
    param : table : list
    param : nom : str
    return : bool
    >>> fonction3(fruits,'fraise')
    True
    """
    for objet in table:
        if objet[0]==nom:
            return True
    return False


def fonction4(table,nom):
    """
    Renvoie True si un élément comportant comme première donnée nom est présent dans table
    param : table : list
    param : nom : str
    return : bool
    >>> fonction4(fruits,'fraise')
    ['fraise', 'rouge', 'sol', 'sans']
    >>> fonction4(fruits,'pomme')
    "L'objet pomme est absent de la table"
    """
    for objet in table:
        if objet[0]==nom:
            return objet
    return "L'objet "+ nom + " est absent de la table"



if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)