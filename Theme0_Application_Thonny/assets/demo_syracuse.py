def syracuse(valeur):
    resultat=0
    if valeur%2==0:
        resultat=valeur//2
    else:
        resultat=3*valeur+1
    return resultat

def liste_termes_syracuse(premier_terme,nb_termes):
    liste_termes=[premier_terme]
    terme=premier_terme
    for i in range(nb_termes):
        terme=syracuse(terme)
        liste_termes.append(terme)
    return liste_termes

def atterrissage_syracuse(premier_terme):
    nb_termes=0
    terme=premier_terme
    while terme !=1:
        terme=syracuse(terme)
        nb_termes +=1
    return nb_termes
