## Exercices Thème 3 : Réseaux sociaux

On rappelle le code pour valider les tests des docstrings.

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

### Exercice 1

Une personne malveillante décide d'envoyer une fausse nouvelle à 3 personnes. Le jour suivant, chacune de ces 3 personnes envoie à nouveau à 3 nouvelles personnes cette nouvelle, et ainsi de suite. Combien faudra-t-il de jours avant que le monde entier l'ait reçu ?
Population mondiale : 7,8 milliards.

Compléter le code ci-dessous.

```Python
S=3
n=1
while S<7.8*10**9:
    ......
    ......
print(n)
```

### Exercice 2

On donne le code qui permet de trouver l'excentricité d'un sommet.

```Python
from collections import deque

def excentricite(graphe, sommet):
    """
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
```

1. Proposer une interprétation de ce code.
2. En utilisant cette fonction, compléter les codes des fonctions suivantes:

```Python
def diametre(graphe):
    """
    >>> diametre([[1,3,4],[0,4],[3],[0,2],[0,1]])
    3
    """
    

def rayon(graphe):
    """
    >>> rayon([[1,3,4],[0,4],[3],[0,2],[0,1]])
    2
    """


def centre(graphe):
    """
    >>> centre([[1,3,4],[0,4],[3],[0,2],[0,1]])
    ['A', 'D']
    """
```

**Indications** : Pour prendre le maximum ou le minimum d'une liste de valeurs.

```Python
>>> liste=[2,8,5]
>>> max(liste)
8
>>> min(liste)
2
```

Soit le graphe ci-dessous :

<img height="400px" src="Assets/graphe.png">

1. Donner une représentation par liste d'adjacence de ce graphe.
2. En utilisant les définitions du cours, déterminer manuellement son diamètre et son rayon.
3. Indiquer le ou les centres de ce graphe.
4. Retrouver ces résultats à l'aide du programme en Python.

### Exercice 3

Il peut être intéressant de trouver la plus grande communauté dans un réseau social. On a vu qu'une communauté peut être vue comme une clique (sommets tous reliés entre eux) dans un graphe. Dans les graphes suivants, quel est le nombre maximum de sommets d'une clique ?

<img src="Assets/cliques.png">

### Exercice 4

Consulter le [kit complet de sensibilisation aux risques numériques](Assets/kit_complet_de_sensibilisation.pdf) et effectuer le test de connaissances.
