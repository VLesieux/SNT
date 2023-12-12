Graphe=[[1,3,4],[0,4],[3],[0,2],[0,1]]

def lien(i,j,graphe):
    """
    Renvoie True si les sommets i et j sont liés
    param : i : int
    param : j : int
    param : Graphe : list
    >>> lien(0,3,Graphe)
    True
    >>> lien(0,2,Graphe)
    False
    """
    return j in graphe[i]


def degre(graphe,i):
    """
    Renvoie le nombre de sommets auquel est lié le sommet i dans Graphe
    param : i : int
    param : graphe : list
    >>> degre(Graphe,1)
    2
    """
    return len(graphe[i])


def nb_aretes(graphe):
    """
    Renvoie le nombre d'arêtes du graphe
    param : graphe : list
    >>> nb_aretes(Graphe)
    5.0
    """
    compteur=0
    for i in range(len(graphe)):
        compteur+=degre(graphe,i)
    return compteur/2


def liste_des_amis_commun(i,j,graphe):
    """
    Renvoie la liste des liens communs à i et à j dans le graphe
    param : i : int
    param : j : int
    param : graphe : list
    >>> liste_des_amis_commun(0,2,Graphe)
    [3]
    >>> liste_des_amis_commun(1,2,Graphe)
    "Les deux utilisateurs du réseau social n'ont pas d'ami en commun"
    """
    communs=[]
    for k in range(len(graphe)):
        if k in graphe[i] and k in graphe[j] and k !=i and k !=j:
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
    >>> est_clique(Graphe,[0,1,4])
    True
    >>> est_clique(Graphe,[0,1,3])
    False
    """
    for sommet1 in liste_sommets:
        for sommet2 in liste_sommets:
            if sommet1 != sommet2 and not lien(sommet1,sommet2,graphe):
                return False
    return True








if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)