## Exercices de programmation

Il est demandé d'écrire les `docstrings` pour toutes les fonctions réalisées en écrivant quelques résultats escomptés en sortie et de les faire vérifier en important le module `doctest` avec le code ci-dessous.

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

On donne la présentation usuelle pour la `docstring` d'une fonction à travers un exemple :

```Python
def eleve_au_carre(n):
    """
    renvoie le carré du nombre entier n
    param : n : int
    return : int
    >>> eleve_au_carre(4)
    16
    """
    carre=n**2
    return carre
```

On n'hésitera pas également à ajouter des commentaires en les précédant du caractère # ; l'interpréteur Python ignore tout ce qui suit jusqu'à la fin de la ligne courante.

On réalisera un fichier avec l'extension .py par exercice et on les rangera tous dans le même dossier.

### Exercice 1 : de l'utilisation des boucles `for` ou `while` en programmation

<u>Ce qu'il faut savoir :</u> 

Une <b>bloucle non conditionnelle et bornée</b> se fait avec **`for i in range(n)`** qui produit n tours de boucle, i est une variable qui prend les valeurs de 0 à n-1 ; on peut également décider d'une autre valeur initiale pour la variable, en écrivant par exemple `for i in range(2, n)` qui fait varier la variable i de 2 compris à n-1. Enfin, on peut également modifier le pas `p` de l'incrémentation à l'aide d'un troisième paramètre : `for i in range(2, n, p)`.

Par exemple : on affiche le mot "salut" ainsi que l'état de la variable à l'aide de ces différentes boucles.

```Python
>>> for tour in range(5):
    print(tour,"salut")   
0 salut
1 salut
2 salut
3 salut
4 salut
>>> for tour in range(2,8):
    print(tour,"salut")    
2 salut
3 salut
4 salut
5 salut
6 salut
7 salut
>>> for tour in range(2,8,2):
    print(tour,"salut")    
2 salut
4 salut
6 salut
```



Une <b>bloucle conditionnelle et non bornée</b> se fait avec l'instruction **`while`**.

Par exemple : on fait la même chose que précédemment mais d'une autre manière en imposant une condition qui limite l'évolution de la variable, il faut penser cette fois à incrémenter la variable à chaque tour de boucle : 

```Python
>>> tour=0
>>> while tour<5:
    print(tour,"salut")
    tour +=1 # on augmente la variable d'une unité à chaque tour   
0 salut
1 salut
2 salut
3 salut
4 salut
```

Problème : Une légende de l'Inde ancienne raconte que le jeu d'échecs a été inventé par un vieux sage que son roi voulut remercier en lui affirmant qu'il lui accorderait n'importe quel cadeau en récompense. Le vieux sage demanda qu'on lui fournisse simplement un peu de riz pour ses vieux jours, et plus précisément un nombre de grains de riz suffisant pour qu'on puisse en déposer 1 sur la première case du jeu qu'il venait d'inventer, deux sur la suivante, quatre sur la troisième, en doublant ainsi chaque fois le nombre de grains déposés, et ainsi de suite jusqu'à la 64e case. 

Écrire un script qui permet d'afficher le résultat suivant :

numero de case :  1  ; nombre de grains déposés sur cette case :  1.0  ; nombre total de grains déposés sur l'échiquier:  1.0    

numero de case :  2  ; nombre de grains déposés sur cette case :  2.0  ; nombre total de grains déposés sur l'échiquier:  3.0   

numero de case :  3  ; nombre de grains déposés sur cette case :  4.0  ; nombre total de grains déposés sur l'échiquier:  7.0

etc...    

numero de case :  64  ; nombre de grains déposés sur cette case :  ?  ; nombre total de grains déposés sur l'échiquier:  ?

N.B : pour otenir le résultat en notation scientifique, on écrira non pas 1 qui est du type int mais 1.0 qui est du type float.

### Exercice 2 : de l'utilisation de l'instruction conditionnelle `if` en programmation

La structure conditionnelle utilise les mots : **`if ; elif ; else`** dans cet ordre.
`elif` est utilisé dans le cas où se présentent plusieurs alternatives.

<u>Exemple</u>: 

On se propose d'écrire un petit programme qui va répondre à l'objectif suivant que l'on traduit d'abord en langage naturel : un utilisateur entre son âge, le programme concluera que l'individu est soit un enfant (<10), soit un adolescent (≥10 ; <19), soit un adulte (≥19).

```Python
age=int(input("Entrez votre âge s.v.p : "))#le résultat d'un input est une chaîne de caractères, d'où la nécessité de la convertir en entier avec int()
if age <10:
    print("Vous êtes un enfant")
elif age>=10 and age<19:
    print("Vous êtes un adolescent")
else:
    print("Vous êtes un adulte")
```

Connaissance : le symbole % est appelé <b>modulo</b>, il donne le reste de la division de deux nombres : 

```Python
>>> 9/2
4.5
#le résultat de la division
>>> 9%2
1
#le reste de la division
>>> 9//2
4
#le quotient de la division
```

1) Dans un premier temps, écrire un script qui permet d'afficher sur une seule ligne, séparés par le caractère " ; ", les 20 premiers multiples de 7 en utilisant l'instruction while. Pour afficher une variable sans changer de ligne et en insérant le caractère " ; ", on utilise l'instruction print(variable, end=" ; " ).   

Vous devez obtenir :
0;7;14;21;28;35;42;49;56;63;70;77;84;91;98;105;112;119;126;133;

2) Réaliser ensuite la fonction affichage(m,n) dont la docstring vous est donnée.

```Python
def affichage(m,n):
    """
    affiche les n premiers multiples de m séparés par ;
    param : m : int
    param : n : int
    return : None 
    # la fonction ne renvoie effectivement rien mais affiche quelque chose
    >>> affichage(7,20)
    0;7;14;21;28;35;42;49;56;63;70;77;84;91;98;105;112;119;126;133;
    """
```

3) Amélioration : faire en sorte d'indiquer à l'aide d'une * les multiples de m qui sont aussi des multiples de 3. On utilisera l'instruction conditionnelle `if`, l'opérateur modulo `%` qui donne le reste de la division entière de 2 nombres, et l'opérateur de comparaison `==` .

```Python
def affichage_ameliore1(m,n):
    """
    affiche les n premiers multiples de m séparés par ; et ajoute * pour un multiple de 3
    param : m : int
    param : n : int
    return : None
    >>> affichage_ameliore1(7,20)
    0*;7;14;21*;28;35;42*;49;56;63*;70;77;84*;91;98;105*;112;119;126*;133;
    """
```

4) De la même façon indiquer également à l'aide d'un ! les multiples de m qui sont aussi des multiples de 2.

```Python
def affichage_ameliore2(m,n):
    """
    affiche les n premiers multiples de m séparés par ; et ajoute * pour un multiple de 3 et ou ! pour un multiple de 2
    param : m : int
    param : n : int
    return : None
    >>> affichage_ameliore2(7,20)
    0*!;7;14!;21*;28!;35;42*!;49;56!;63*;70!;77;84*!;91;98!;105*;112!;119;126*!;133;
    """
```


### Exercice 3 : interagir avec l'utilisateur avec `input()`

Une entreprise fournit des ramettes de papier à prix dégressif en fonction du nombre de lots achetés : les 50 premiers lots sont vendus 3,68€, au-delà chaque lot est vendu 3,22€. Écrire une fonction `prix(n)` qui lorsqu'on saisit le nombre `n` de lots achetés retourne (avec un return) le prix à payer puis procéder à l'affichage (avec un print) du résultat.

```Python
>>> %Run exercices_programmation_snt.py
nombre de lots de ramettes de papier achetés ? 100
Il vous en reviendra 345.0€
```

Utiliser :

1) `input` pour interroger l'utilisateur ; le résultat est une chaîne de caractères à convertir en nombre entier à l'aide de `int()`.

exemple :
```Python
nombre=int(input("nombre de lots de ramettes de papier achetés ? "))
```

2) la concaténation (addition) de chaînes de caractères ; transformer un nombre en chaîne de caractères se fait avec `str()`.

exemple :

```Python
>>> variable=4
>>> chaine="vous avez acheté "+str(variable)+ " livres"
>>> print(chaine)
vous avez acheté 4 livres
```

3) l'affichage sur une seule ligne peut également se faire avec un `print()` en séparant les éléments avec une virgule.

```Python
>>> variable=4
>>> print("vous avez acheté ",variable," livres")
vous avez acheté  4  livres
```

### Exercice 4 : manipuler les éléments d'un tuple grâce à leur indice de position dans le tuple

Un **tuple** ou n-uplet est constitué de n valeurs, quel que soit leur type, séparées par une virgule.

```Python
>>> type((23,"billes",12.5))
<class 'tuple'>
```

Un cinéma propose une carte d'abonnement mensuel à 15€ permettant d'obtenir une réduction sur le prix des séances : sans réduction la séance est à 8,70€, alors qu'avec l'abonnement la séance est à 5,50€. 
Sans résoudre mathématiquement le problème, écrire une fonction `abo(n)` qui renvoie sous la forme de tuple deux informations numériques : la première étant le prix sans abonnement, la seconde le prix avec abonnement. Pour renvoyer deux variables a et b sous forme de tuple, écrire `return (a,b)`.

```Python
>>> abo(2)
(17.4, 26.0)
>>> abo(8)
(69.6, 59.0)
```

Pour récuperer la première et la deuxième valeur d'un tuple, procéder ainsi : 

```Python
>>> abo(2)[0]
17.4
>>> abo(2)[1]
26.0
```
Une fois que l'on dispose de cette fonction, on cherche à afficher le nombre de séances à partir duquel prendre l'abonnement devient avantageux. 

Afficher le résultat de la façon suivante.

```Python
>>> %Run ex4.py
L'achat d'un abonnement devient intéressant à partir de 5 séances
Sans abonnement :  43.5 €, avec abonnement :  42.5  €.
```

Indications : on augmente la variable `nb_seances` (initialisée à 1) avec une boucle `while` (cf. ex 1) en comparant les prix avec et sans abonnement. Pour l'affichage du résultat : cf.ex 3.

### Exercice 5 : parcourir les éléments d'une liste de deux façons différentes

Une **liste** est constitué d'éléments séparés par une virgule à l'intérieur de crochets.
Les éléments d'une liste sont mutables contrairement aux éléments d'un tuple.

```Python
>>> liste=[3,"chien",4.5]
>>> liste[1]="chat"
>>> liste
[3, 'chat', 4.5]
>>> triplet=(3,"chien",4.5)
>>> triplet[1]="chat"
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

1) Écrire un programme qui analyse un par un tous les éléments d'une liste de mots par exemple liste_complete=['Jean','Maximilien','Brigitte','Sonia','Jean-Pierre'] pour générer deux nouvelles listes : l'une contiendra les mots comportant moins de 6 caractères, l'autre comportant les mots de plus de 6 caractères.

**Indications** : 

a) On utilise la fonction intégrée `len()` qui renvoie la longueur d'une chaîne de caractères et la méthode `append` associée à une occurence d'objet de type liste qui permet d'ajouter un élément à cette liste. 

Exemple : 

```Python
>>> liste=[3,"chien"]
>>> len(liste)
2
>>> liste.append(2.0)
>>> liste
[3, 'chien', 2.0]
```

b) On peut parcourir les éléments d'une liste de deux manières, soit élément après élément, soit index d'élément après index d'élément.

```Python
for element in liste:
    print(element)
    
for i in range(len(liste)):
    print(liste[i])
```

2) Amélioriation : l'utilisateur est invité à entrer sans cesse de nouveaux noms, jusqu'à ce qu'il décide de terminer en frappant `<Enter>` en guise d'entrée. Le programme se termine avec l'affichage des deux listes. Créer une fonction `traitement` qui admettra en argument la liste ainsi constituée et qui en sortie affichera les deux listes comme précédemment.


