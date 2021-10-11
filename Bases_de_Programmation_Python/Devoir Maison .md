### Devoir Maison 

Code pour vérifier les tests des docstring

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```


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

#### Ex 3 : Le codage de César 
Le codage de César transforme un message en changeant chaque lettre en la décalant dans l’alphabet. Par exemple, avec un décalage de 3, le A se transforme en D, le B en E, ..., le X en A, le Y en B et le Z en C. Les autres caractères (‘!’,’ ?’…) ne sont pas codés.La fonction position_alphabet ci-dessous prend en paramètre un caractère lettre et renvoie la position de lettre dans la chaîne de caractères ALPHABET s’il s’y trouve et -1 sinon.La fonction cesar prend en paramètre une chaîne de caractères message et un nombre entier decalage et renvoie le nouveau message codé avec le codage de César utilisant le décalage decalage. 

Compléter le code ci-dessous :

```Python
def position_alphabet(lettre):
    """
    Renvoie l'indice de position de lettre dans ALPHABET
    param : str
    return : int
    >>> position_alphabet('E')
    4
    """
    for i in range(len(ALPHABET)):
		# à compléter
		# à compléter
def cesar(message, decalage):
    """
    Renvoie le message avec le décalage souhaité
    param : message : str
    param : decalage : int	  >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE SNT !',4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI WRX !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ XSY !',-5)
    'BONJOUR A TOUS. VIVE LA MATIERE SNT !'
    """    	  resultat = ''
	  for lettre in message :
	      if lettre in ALPHABET :
	            indice = ( # à compléter #)%26
	            resultat = # à compléter
	      else:
	            resultat = # à compléter
	  return resultat    
```

#### Ex 4 : Les palindromes

Un mot palindrome peut se lire de la même façon de gauche à droite ou de droite à gauche : bob, radar, et non sont des mots palindromes.De même certains nombres sont eux aussi des palindromes : 33, 121, 345543.L’objectif de cet exercice est d’obtenir un programme Python permettant de tester si un nombre est un nombre palindrome.Pour remplir cette tâche, on vous demande de compléter le code des trois fonctions ci-dessous sachant que la fonction est `_nbre_palindrome` s’appuiera sur la fonction `est_palindrome` qui elle-même s’appuiera sur la fonction `inverse_chaine`.La fonction `inverse_chaine` inverse l'ordre des caractères d'une chaîne de caractères chaine et renvoie la chaîne inversée.La fonction `est_palindrome` teste si une chaine de caractères chaine est un palindrome. Elle renvoie True si c’est le cas et False sinon. Cette fonction s’appuie sur la fonction précédente.La fonction `est_nbre_palindrome` teste si un nombre nbre est un palindrome. Elle renvoie True si c’est le cas et False sinon. Cette fonction s’appuie sur la fonction précédente.

```Python

def inverse_chaine(chaine):
    """
    Renvoie la chaine dans l'odre inverse
    param : str
    return : str
    >>> inverse_chaine('bac')
    'cab'
    """
    # à compléter #

def est_palindrome(chaine):
    """
    Renvoie True si la chaine est un palindrome, False sinon
    param : str
    return : bool
    >>> est_palindrome('SNT')
    False
    >>> est_palindrome('SNT-TNS')
    True
    """    # à compléter #

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
    # à compléter #

```