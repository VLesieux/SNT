G=[[1,3,4],[0,4],[3],[0,2],[0,1]]

def lien(i,j,Graphe):
    """
    Renvoie True si i et j sont liés
    param : i : int
    param : j : int
    param : Graphe : list
    >>> lien(0,3,G)
    True
    >>> lien(0,2,G)
    False
    """
    for valeur in Graphe[i]:
        if j==valeur:
            return True
    return False

def degre(Graphe,i):
    """
    Renvoie le nombre de sommets auquel est lié le sommet i dans Graphe
    param : i : int
    param : Graphe : list
    >>> degre(G,1)
    2
    """
    return len(Graphe[i])

def nb_aretes(Graphe):
    """
    Renvoie le nombre d'arêtes du graphe
    param : Graphe : list
    >>> nb_aretes(G)
    5.0
    """
    nombre=0
    for element in Graphe:
        nombre+=len(element)
    return nombre/2

def est_clique(Graphe,Liste_sommets):
    """
    Renvoie True si Liste_sommets est une clique, c'est-à-dire que les sommets sont reliés mutuellement entre eux
    param : Graphe : list
    param : Liste_sommets : list
    >>> est_clique(G,[0,1,4])
    True
    >>> est_clique(G,[0,1,3])
    False
    """
    for sommet1 in Liste_sommets:
        for sommet2 in Liste_sommets:
            if sommet2 !=sommet1 and not lien(sommet1,sommet2,Graphe):
                return False
    return True

from collections import deque

def excentricite(graphe, sommet):
    """
    Renvoie la plus grande distance du sommet passé en paramètre aux autres sommets de graphe
    param : graphe : list
    param : sommet : int
    >>> excentricite([[1,3,4],[0,4],[3],[0,2],[0,1]], 0)
    2
    >>> excentricite([[1,3,4],[0,4],[3],[0,2],[0,1]], 1)
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

def diametre(graphe):
    """
    >>> diametre([[1,3,4],[0,4],[3],[0,2],[0,1]])
    3
    """
    liste=[]
    for i in range(len(graphe)):
        liste.append(excentricite(graphe, i))
    return max(liste)

def rayon(graphe):
    """
    >>> rayon([[1,3,4],[0,4],[3],[0,2],[0,1]])
    2
    """
    liste=[]
    for i in range(len(graphe)):
        liste.append(excentricite(graphe, i))
    return min(liste)

def centre(graphe):
    """
    >>> centre([[1,3,4],[0,4],[3],[0,2],[0,1]])
    ['A', 'D']
    """
    liste=[]
    noms=["A","B","C","D","E"]
    for i in range(len(graphe)):
        if excentricite(graphe, i)==rayon(graphe):
            liste.append(noms[i])
    return liste
        

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
  
