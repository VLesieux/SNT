### Devoir Maison 

Code pour vérifier les tests des docstring

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```
Pour faire ce DM, il est conseillé de revoir les [exercices de programmation](Exercices_programmation.md).
#### Ex 1 : Programmer la fonction multiplication en utilisant uniquement les opérations addition et soustraction.

```Python
def multiplication(n1,n2):
    """
    Renvoie le produit des deux entiers relatifs en utilisant uniquement les opérations + et -
    param : n1,n2 : int
    return : int
    >>> multiplication(3,5)
    15
    >>> multiplication(-4,-8)
    32
    >>> multiplication(-2,6)
    -12
    >>> multiplication(-2,0)    
    0
    """
    # à compléter
```

Indication : réaliser une boucle non conditionnelle et bornée.

####  Ex 2 : Programmer une fonction moyenne qui renvoie la moyenne pondérée d'une liste de notes coefficientées.

```Python
def moyenne(liste_notes_coef):
    """
    Renvoie la moyenne pondérée d'une liste de notes coefficientées
    param : liste_notes_coef : list
    return : float
    >>> moyenne([(15,2),(9,1),(12,3)])
    12.5
    """
    # à compléter
```

Indication : parcourir les éléments (tuple) de la liste, élément après élément, accéder à une valeur du tuple par son indice de position.

Exemple :

```Python
def moyenne(liste_individus):
    """
    Renvoie l'âge moyen d'une liste d'individus
    param : liste_individus : list
    return : float
    >>> moyenne([('Hervé',51),('Sacha',24),('Tom',65),('Rose',16)])
    39.0
    """
    somme=0
    for element in liste_individus:
        somme+=element[1]
    moyenne=somme/len(liste_individus)
    return moyenne
```

#### Ex 3 : Le codage de César 

Le codage de César transforme un message en changeant chaque lettre en la décalant dans l’alphabet. Par exemple, avec un décalage de 3, le A se transforme en D, le B en E, ..., le X en A, le Y en B et le Z en C. Les autres caractères (‘!’,’ ?’…) ne sont pas codés.



Compléter le code ci-dessous :

```Python
ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'#une chaîne de 26 caractères
def position_alphabet(lettre):
    """
    Renvoie l'indice de position de lettre dans ALPHABET
    param : str
    return : int
    >>> position_alphabet('E')
    4
    >>> position_alphabet('!')
    -1
    """
    for i in range(len(ALPHABET)):#parcourt la chaîne en faisant varier l'indice de position i dans la chaîne
		# à compléter
		# à compléter

    """
    Renvoie le message avec le décalage souhaité
    param : message : str
    param : decalage : int
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE SNT !',4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI WRX !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ XSY !',-5)
    'BONJOUR A TOUS. VIVE LA MATIERE SNT !'
    """    
    for lettre in message :#parcourt les différents lettres de la chaînes 
        if lettre in ALPHABET :
             indice = ( # à compléter #)%26
             resultat = # à compléter
        else:
             resultat = # à compléter
    return resultat    
```

Commentaire : `%26` permet de se retrouver toujours dans l'alphabet quelque soit le décalage effectué.


#### Ex 4 : Les palindromes

Un mot palindrome peut se lire de la même façon de gauche à droite ou de droite à gauche : bob, radar, et non sont des mots palindromes.
De même certains nombres sont eux aussi des palindromes : 33, 121, 345543.






```Python
def inverse_chaine(chaine):
    """
    Renvoie la chaine dans l'odre inverse
    param : str
    return : str
    >>> inverse_chaine('bac')
    'cab'
    """
    # à compléter

def est_palindrome(chaine):
    """
    Renvoie True si la chaine est un palindrome, False sinon
    param : str
    return : bool
    >>> est_palindrome('SNT')
    False
    >>> est_palindrome('SNT-TNS')
    True
    """

def est_nbre_palindrome(nombre):
    """
    Renvoie True si le nombre est un palindrome, False sinon
    param : nombre : int
    return : bool
    >>> est_nbre_palindrome(214312)
    False
    >>> est_nbre_palindrome(213312)
    True
    """
    # à compléter

```

Indication : pour réaliser la fonction `inverse_chaine`, parcourir les caractères de la chaîne en reconsituant son inverse.