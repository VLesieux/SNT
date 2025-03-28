Graphe=[[1,3,4],[0,4],[3],[0,2],[0,1]]
#Cette liste d'adjacence, appelée Graphe, correspond à notre exemple et sert pour valider les tests de nos fonctions.
#Pour chaque sommet numéroté (à partir de 0), on a une sous-liste indiquant les liens qu'il fait avec les autres sommets.
noms_sommets_Graphe=['A','B','C','D','E']
#Ce sont les noms de sommets de notre exemple.
######################################################################



def lien(i,j,graphe):
    """
    Renvoie True si les sommets i et j sont liés
    param : i : int
    param : j : int
    param : graphe : list
    return : bool
    >>> lien(0,3,Graphe)
    True
    >>> lien(0,2,Graphe)
    False
    """
    return j in graphe[i]#il suffit de voir si j est dans la sous-liste de i.


def degre(graphe,i):
    """
    Renvoie le nombre de sommets auquel est lié le sommet i dans Graphe
    param : i : int
    param : graphe : list
    return : int
    >>> degre(Graphe,1)
    2
    """
    return len(graphe[i])#il suffit de renvoyer le nombre d'éléments de la sous-liste de i.


def nb_aretes(graphe):
    """
    Renvoie le nombre d'arêtes du graphe
    param : graphe : list
    return : int
    >>> nb_aretes(Graphe)
    5
    """
    compteur=0
    for i in range(len(graphe)):
        compteur+=degre(graphe,i)
    return compteur//2#il y a moitié moins d'arêtes que de liens, car une arête est commune à deux liens partagés.


def liste_des_amis_commun(i,j,graphe):
    """
    Renvoie la liste des liens communs à i et à j dans le graphe
    param : i : int
    param : j : int
    param : graphe : list
    return : list
    >>> liste_des_amis_commun(0,2,Graphe)
    [3]
    >>> liste_des_amis_commun(1,2,Graphe)
    "Les deux utilisateurs du réseau social n'ont pas d'ami en commun"
    """
    communs=[]
    for k in range(len(graphe)):
        if k in graphe[i] and k in graphe[j] and k !=i and k !=j:#on cherche les liens communs à i et à j différents de i et de j.
            communs.append(k)
    if len(communs)==0:
        return "Les deux utilisateurs du réseau social n'ont pas d'ami en commun"
    else:
        return communs
    
def est_clique(graphe,liste_sommets):
    """
    Renvoie True si Liste_sommets est une clique, c'est-à-dire que les sommets sont reliés mutuellement entre eux
    param : graphe : list
    param : liste_sommets : list
    return : bool
    >>> est_clique(Graphe,[0,1,4])
    True
    >>> est_clique(Graphe,[0,1,3])
    False
    """
    for sommet1 in liste_sommets:
        for sommet2 in liste_sommets:
            if sommet1 != sommet2 and not lien(sommet1,sommet2,graphe):#on regarde si tous les sommets de la clique sont interconnectés.
                return False
    return True


from collections import deque

def excentricite(graphe, sommet):
    """
    Renvoie la plus grande distance du sommet passé en paramètre aux autres sommets de graphe
    param : graphe : list
    param : sommet : int
    return : int
    >>> excentricite(Graphe, 0)
    2
    >>> excentricite(Graphe, 1)
    3
    """
    # Initialiser la distance de chaque sommet à l'infini
    distances = {s: float('inf') for s in range(len(graphe))}
    # Initialiser la distance du sommet de départ à 0
    distances[sommet] = 0

    # Initialiser la file d'attente avec le sommet de départ
    queue = deque([sommet])

    # Itérer jusqu'à ce que la file d'attente soit vide
    while queue:
    # Prendre le premier sommet de la file d'attente
        sommet = queue.popleft()
    # Parcourir tous les sommets adjacents au sommet actuel
        for voisin in graphe[sommet]:
      # Si la distance du voisin est infinie, cela signifie qu'il n'a pas encore été visité
            if distances[voisin] == float('inf'):
        # Mettre à jour la distance du voisin en lui attribuant la distance du sommet actuel + 1
                distances[voisin] = distances[sommet] + 1
        # Ajouter le voisin à la file d'attente pour être traité ultérieurement
                queue.append(voisin)

    # Retourner la distance maximale des sommets par rapport au sommet de départ
    return max(distances.values())


def diametre(graphe):#Il s'agit de la plus grande valeur des excentrencités des sommets du graphe
    """
    Renvoie la plus grande valeur de l'excentricité
    param : graphe : list
    return : int
    >>> diametre(Graphe)
    3
    """
    valeurs=[]
    for k in range(len(graphe)):
        valeurs.append(excentricite(graphe, k))
    return max(valeurs)


def rayon(graphe):#Il s'agit de la plus petite valeur des excentrencités des sommets du graphe
    """
    Renvoie la plus petite valeur de l'excentricité
    param : graphe : list
    return : int
    >>> rayon(Graphe)
    2
    """
    valeurs=[]
    for k in range(len(graphe)):
        valeurs.append(excentricite(graphe, k))
    return min(valeurs)    

def centre(graphe):# Ce sont le ou les sommets où l'excentricité est égale à celle du rayon
    """
    Renvoie le ou les sommets de plus petite excentricité
    param : graphe : list
    return : list
    >>> centre(Graphe)
    [0, 3]
    """
    centres=[]
    for k in range(len(graphe)):
        if excentricite(graphe,k)==rayon(graphe):
            centres.append(k)
    return centres        

def centre_noms(graphe,noms):
    """
    Renvoie le ou les sommets de plus petite excentricité
    param : graphe : list
    return : list
    >>> centre_noms(Graphe,noms_sommets_Graphe)
    ['A', 'D']
    """
    centres=[]
    for k in range(len(graphe)):
        if excentricite(graphe,k)==rayon(graphe):
            centres.append(noms[k])
    return centres



if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)