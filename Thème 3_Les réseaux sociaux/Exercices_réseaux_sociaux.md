## Exercices Thème 3 : Réseaux sociaux

On rappelle le code pour faire les doctests.

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

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

<img src="Assets/graphe.png">

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

5.   Écrire une fonction `sommets(graphe)` qui retourne les différents sommets du graphe.

```Python
>>> sommets(G)
[0, 1, 2, 3, 4, 5, 6]
```

6. Utiliser les fonctions précédentes `sommets` et `chemin` pour écrire les fonctions :

a. `excentricite(graphe,i)`.  
b. `diametre(graphe)`.        
c. `rayon(graphe)`.  
d. `centre(graphe)`.

Retrouver ainsi les résultats établis "à la main". 

Indications :

a. Pour déterminer l'excentricité du sommet i, créer une liste contenant, pour chacun des sommets du graphe, la longueur du chemin allant du sommet i à ce sommet. Puis utiliser la fonction max(liste) qui retourne le maximum de la liste.   
b. Déterminer le maximum des excentricités pour tous les sommets du graphe.     
c. Déterminer le minimum des excentricités pour tous les sommets du graphe.     
d. Utiliser la fonction `liste.index(valeur)` qui retourne l'indice de position de `valeur` dans `liste`.    


### Exercice 4

Il peut être intéressant de trouver la plus grande communauté dans un réseau social. On a vu qu'une communauté peut être vue comme une clique (sommets tous reliés entre eux) dans un graphe. Dans les graphes suivants, quel est le nombre maximum de sommets d'une clique ?

<img src="Assets/cliques.png">
