## Exercices Thème 3 : Réseaux sociaux

### Exercice 1

Une personne malveillante décide d'envoyer une fausse nouvelle à 3 personnes. Le jour suivant, chacune de ces 3 personnes envoie à nouveau à 3 nouvelles personnes cette nouvelle, et ainsi de suite. Combien faudra-t-il de jours avant que le monde entier l'ait reçu ?
Population mondiale : 7,8 milliards.

Indications :

1. Donner, en fonction de n, une expression du nombre de nouvelles personnes touchées par la fake news le nième jour.
2. Écrire un programme en Python permettant de répondre à la question.

### Exercice 2

Consulter le [kit complet de sensibilisation aux risques numériques](Assets/kit_complet_de_sensibilisation.pdf) réalisé par cybermalveillance.gouv.fr puis effectué le test de connaissances.

### Exercice 3

Soit le graphe ci-dessous :

<img src="Assets/graphe.png" width="300" height="300">

1. Donner une représentation par liste d'adjacence de ce graphe.
2. Déterminer "à la main" son diamètre et son rayon.
3. Indiquer le ou les centres de ce graphe.
4. L'algorithme ci-dessous permet d'afficher la liste des sommets d'un point à un autre

```Python
def chemin(graphe,i,j,liste):
    rencontre=i
    liste.append(rencontre)
    for element in graphe[rencontre]:
        if element not in liste:
            if element==j:
                liste.append(j)
                return(liste)
            elif len(graphe[element])!=1:
                chemin(graphe,element,j,liste)
                return(liste)
>>> chemin(G,6,4,[])
[6, 3, 1, 2, 4]
```
Quelle est la particularité de cet algorithme ? Proposez une explication.
Vérifier en utilisant le débugger.
5. Utiliser la fonction précédente pour écrire les fonctions `excentricite(graphe,i)` ; `diametre(graphe)`, `rayon(graphe)`, `centre(graphe)` .
Retrouver les résultats établis "à la main". 


### Exercice 4

Il peut être intéressant de trouver la plus grande communauté dans un réseau social. On a vu qu'une communauté peut être vue comme une clique (sommets tous reliés entre eux) dans un graphe. Dans les graphes suivants, quel est le nombre maximum de sommets d'une clique ?

<img src="Assets/cliques.png" width="300" height="300">

### Exercice 5

Écrire une fonction degree telle que `degre(G,i)` renvoie le degré du sommet i dans le graphe G représenté par liste d'adjacence.


### Exercice 6

Écrire une fonction `nb_aretes` renvoyant le nombre d'arêtes dans un graphe représenté par une liste d'adjacence.


