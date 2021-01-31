## Exercices Thème 4 : Les données structurées et leurs traitements

### Exercice 1

Parmi les formats suivants, lesquels sont utilisés pour les données structurées.

XML ; PDF ; CSV ; JPEG ; MP3 ; VCF

### Exercice 2

Saisir dans un fichier XML les données relatives à ses proches en utilisant les descripteurs : 'nom', 'prenom', 'lien', 'anniversaire'.


### Exercice 3

Aller sur le site www.data.gouv.fr et effectuer la recherche "indices qualité de l'air Île de France" ;  télécharger puis ouvrir le fichier indices_QA_commune_IDF_04_2018.csv. Répondre aux questions suivantes avec Python. 

1. Quels sont les descripteurs utilisés ? Affichez-les.
2. **Trier** les données en fonction de l'indice de pollution au dioxyde d'azote NO<sub>2</sub>, puis **filtrer** les données correspondant à l'Île de France (code Insee : 0) afin de déterminer quel jour était le plus pollué en dioxyde d'azote en Île de France.

**Indications** : trier les données dans l'ordre décroissant d'indice de pollution au NO<sub>2</sub>, puis filtrer les résultats à la date du 20/04/2018.
On sera amené à écrire les fonctions : `tri_selon_no2(tableau)` et `filtre_selon_ninsee(ninsee,tableau)`.

3. Déterminer les numéro d'insee des deux communes d'Île-de-France les plus polluées en particules fines (pm10) le 20/04/2018.    

**Indications** : trier les données dans l'ordre décroissant d'indice de pollution aux particules fines, puis filtrer les résultats à la date du 20/04/2018.
On sera amené à écrire les fonctions : `tri_selon_pm10(tableau)` et `filtre_selon_date(date,tableau)`.

Résultat attendu à afficher : `Les insee des deux communes d'Île-de-France les plus polluées aux particules fines (pm10) le 20/04/2018 sont :  92026  ,  92035`

4. Pendant combien de jours l'indice de pollution à l'ozone O<sub>3</sub> a-t-il été supérieur à 45 dans le Val-de-Marne (code d'Insee : 94) au mois d'avril 2018 ?   

**Indications** : trier les données dans l'ordre décroissant d'indice de pollution à l'ozone, puis filtrer les résultats selon le code Insee 94.
On sera amené à écrire les fonctions : `tri_selon_o3(tableau)` puis `filtre_selon_code(code,tableau,seuil)`. Pour transformer une chaîne de caractère représentant une valeur entière en nombre entier, utiliser int : 
```Python
>>> int("45")
45
```

Résultat attendu à afficher : `Le nombre de jour où l'indice de pollution à l'ozone a été supérieur à 45 dans le Val-de-Marne est :  7 `


### Exercice 4

On souhaite traiter la table ci-dessous appelée fruits à l'aide des fonctions suivantes : `fonction1`, `fonction2`, `fonction3` présentées ci-après :

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
Répondre d'abord "à la main" aux questions suivantes à la lecture du code puis vérifiez avec Thonny en utilisant la console puis réaliser les docstrings des fonctions.

On rappelle le code pour faire les doctests.

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

On rappelle la présentation usuelle pour la docstring d'une fonction à travers un exemple :

```Python
def eleve_au_carre(n):
    """
    renvoie le carré du nombre entier n
    param : n : int
    return : int
    >>> eleve_au_carre(4)
    16
    """
    return n**2
```

1. Quel est le rôle de `fonction1` et que renvoie `fonction1(fruits)` ? Faire la docstring de cette fonction avec le test `fonction1(fruits)`.
2. Quel est le rôle de `fonction2` et que renvoie `fonction2(fruits,1,'rouge')` ? Faire la docstring de cette fonction avec le test `fonction2(fruits,1,'rouge')`.
3. Quel est le rôle de `fonction3` et que renvoie `fonction3(fruits,'fraise')` ? Faire la docstring de cette fonction avec le test `fonction3(fruits,'fraise')`.
4. Modifier `fonction3` pour créer `fonction4` ; celle-ci doit renvoyer la liste des valeurs que prennent tous les descripteurs associés à l'objet si `nom` a été trouvé dans la table, et un message (chaîne de caractère ou string) indiquant dans le cas contraire que `nom` n'a pas été trouvé <sup>*</sup>.      
La docstring de cette `fonction4` doit permettre de vérifier les deux tests suivants :

```Python
>>> fonction4(fruits,'fraise')
['fraise', 'rouge', 'sol', 'sans']
>>> fonction4(fruits,'pomme')
"L'objet pomme est absent de la table"
```

<sup>*</sup> Indication : on sera amené à utiliser la concaténation de chaînes de caractères, par exemple : 

```Python
>>> partie2="la suite"#partie2 est une variable égale à une chaîne de caractères ou string (str)
>>> "ceci est le début, " +partie2 +" et la fin de la phrase"
'ceci est le début, la suite et la fin de la phrase'
```

Exemple : réponses à la question 1

```Python
def fonction1(table):
    """
    renvoie la longueur de table, et la longueur de son premier élément (d'indice 0 dans table)
    param : table : list
    return : tuple
    >>> fonction1(fruits)
    (6, 4)
    """
    return len(table),len(table[0])
```
