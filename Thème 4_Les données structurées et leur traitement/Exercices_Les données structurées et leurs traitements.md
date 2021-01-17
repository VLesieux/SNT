## Exercices Thème 4 : Les données structurées et leurs traitements

### Exercice 1

Parmi les formats suivants, lesquels sont utilisés pour les données structurées.

XML ; PDF ; CSV ; JPEG ; MP3 ; VCF

### Exercice 2

Saisir dans un fichier XML les données relatives à ses proches en utilisant les descripteurs : 'nom', 'prenom', 'lien', 'anniversaire'.


### Exercice 3

Aller sur le site www.data.gouv.fr et effectuer la recherche "indices qualité de l'air Île de France" ;  télécharger puis ouvrir le fichier indices_QA_commune_IDF_04_2018.csv. Répondre aux questions suivantes avec Python. 

1. Quels sont les descripteurs utilisés ?
2. **Trier** les données en fonction de l'indice de pollution au dioxyde d'azote NO<sub>2</sub>, puis **filtrer** les données correspondant à l'Île de France (code Insee : 0) afin de déterminer quel jour était le plus pollué en dioxyde d'azote en Île de France.
3. Recherchez quelles communes d'Île-de-France étaient les plus polluées en particules fines (pm10) le 20/04/2018.
4. Pendant combien de jours l'indice de pollution à l'ozone O<sub>3</sub> a-t-il été supérieur à 45 dans le Val-de-Marne (code d'Insee : 94) au mois d'avril 2018 ?

### Exercice 4

On souhaite traiter la table appelée fruits à l'aide des fonctions : fonction1, fonction2, fonction3 :

```Python
fruits=[
        ['fraise','rouge','sol','sans'],
        ['abricot','orange','arbre','noyau'],
        ['peche','orange','arbre','noyau'],
        ['cerise','rouge','arbre','noyau'],
        ['melon','vert','sol','pepins'],
        ['avocat','vert','arbre','noyau']
        ]

def fonction1(table):
    return len(table),len(table[0])

def fonction2(table,indice,valeur):
    compteur=0
    for objet in table:
        if objet[indice]==valeur:
            compteur+=1
    return compteur

def fonction3(table,nom):
    for objet in table:
        if objet[0]==nom:
            return True
    return False

```
Répondre d'abord "à la main" aux questions puis vérifier avec Thonny. 

1. Quel est le rôle de `fonction1` et que renvoie `fonction1(fruits`) ?
2. Quel est le rôle de `fonction2` et que renvoient `fonction2(fruits,1,'rouge')` puis fonction2(fruits,-2,'sol') ?
3. Quel est le rôle de `fonction3` et que renvoie `fonction3(fruits,'fraise')` ?
4. Modifier `fonction3` pour qu'elle renvoie la liste des valeurs de tous les descripteurs associés à l'objet si `nom` a été trouvé dans la table et un message indiquant que `nom` n'a pas été trouvé dans le cas contraire.
```Python
>>> fonction3(fruits,'fraise')
['fraise', 'rouge', 'sol', 'sans']
>>> fonction3(fruits,'pomme')
L'objet  pomme  est absent de la table.
```