## Exercices Thème 1 : Internet

### Exercice 1 : Simuler un réseau avec le logiciel Filius

[La transmission des données dans un réseau](Assets/Transmission_donnees.md)

### Exercice 2 : à faire chez soi

a. Déterminer sa propre adresse IP.  

Sous Windows, aller dans `Système Windows`
- ouvrir un terminal en cliquant sur `Démarrer`, `exécuter` et en tapant `cmd`
- saisir la commande `ipconfig`

b. Accéder à sa propre table de routage.
Sous Windows, dans un terminal saisir la commande `route print`.


c. Identifier la route empruntée pour accéder au site web www.facebook.com

Sous Windows, dans un terminal saisir la commande :  `tracert www.facebook.com`.

d. Vérifier que le site www.wikipedia.org vous est accessible en saisissant dans un terminal la commande `ping www.wikipedia.org` puis accéder directement au site en utilisant l'adresse IP.
 
Rappeler le nom que l'on donne sur Internet aux serveurs qui disposent d’une application logicielle (sorte d’annuaire) permettant de faire la correspondance entre le nom de domaine demandé et l’IP publique associée au serveur. 


### Exercice 3 : la notion de TTL (Time to live ou durée de vie)

Sur le réseau simplifié décrit ci-dessous, citer au moins trois chemins permettant de relier la machine M8 à la machine M4.

<img src="Assets/routages.png" width="800" height="600">

1) Quelle est la valeur minimale du TTL d'un paquet émis par M8 pour qu'il parvienne à M4 ?
On rappelle que le TTL est une donnée placée au niveau de l'en-tête du paquet IP qui indique le nombre maximal de routeurs de transit pour éviter qu'un paquet ne boucle à l'infini s'il existe un problème de boucle de routage.

2) Que se passe-t-il si le routeur B tombe en panne ? si le routeur D tombe en panne ?

### Exercice 4 : le codage binaire de l'information transmise dans le réseau

Toute l'information (textes, images, sons) qui transite sur le réseau internet est numérisée en binaire pour être interprétée par nos logiciels aussi est-il intéressant de comprendre la numérisation en binaire.

Un exemple de codage binaire 'à la main' de l'entier 755 : 

<img src="Assets/divisions.png">

Comme le montre cet exemple, la méthode utilisée pour obtenir le code binaire d'un nombre décimal consiste à réaliser une succession de divisions euclidiennes par 2 où chaque fois le quotient devient le nouveau dividende, et cela aussi longtemps que le quotient est strictement plus grand que 0. Les restes sont lus de bas en haut pour composer le code.

1) Coder 'à la main' en binaire la valeur décimale 51. Vérifier dans la console de Thonny avec `bin(51)`.

2) Inversement, calculer 'à la main' la valeur décimale de l'octet `10110001`. Vérifier dans la console de Thonny avec `0b10110001`.

Cette fois les différents bits du code binaire représentent les différentes puissances de 2 (de droite à gauche en commençant par 0) correspondant à la décomposition en base 2 du nombre.
En effet, de même que l'écriture 1|2|8 est la représentation décimale d'une quantité égale à 128  correspondant à la décomposition en base 10 : 8×10^0+2×10^1+1×10^2, de même le code binaire 1|0|1|1 est la représentation binaire de la quantité égale à 11 correspondant à la décomposition en base 2 : 1×2^0+1×2^1+0×2^2+1×2^3=1+2+8.

3) Après avoir observé dans l'algorithme utilisé le rôle que prend, à chaque tour de boucle, le nouveau dividende par rapport au quotient précédent, compléter le programme suivant de conversion décimal-binaire en python dont une seule ligne est manquante.

```python
nombre=input("Entrez un nombre entier : ")
a=""
dividende=int(nombre)
quotient=dividende//2
while quotient>0:
    reste=dividende%2
    quotient=dividende//2
    # ligne à compléter
    a=str(reste)+a#permet la concaténation de la chaîne de caractères de droite à gauche
print(a)
```
4) On peut transformer ce programme en réalisant une **fonction** que l'on appelera `conversion_decimal_binaire`. Déterminer la ligne manquante afin de rendre fonctionnel le test introduit dans la documentation de la fonction.

```python
def conversion_decimal_binaire(nombre):
    """
    Renvoie le code binaire de nombre sur un octet c'est-à-dire 8 bits
    param : nombre : int
    return : str
    >>> conversion_decimal_binaire(51)
    '00110011'
    """
    a=""
    # ligne à compléter en observant que nombre passé en paramètre deviendra le quotient après le premier tour
        a=str(nombre%2)+a
        nombre=nombre//2
    a='0'*(8-len(a))+a##pour rajouter autant de 0 que nécessaire à l'écriture d'un octet
    return a
```

Code à ajouter pour importer le module doctest et vérifier le test de la docstring :

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

5) En utilisant le programme précédent, on cherche à coder en écriture binaire l'adresse IP 192.168.1.13

Peut-on concevoir un programme qui donnerait directement le code binaire d'une adresse IP ?

Pour cela, on peut transformer une chaîne de caractères en liste en utilisant un séparateur avec la méthode `split` puis parcourir cette liste avec `for element in `.

```python
>>> "192.168.1.13".split(".")
['192', '168', '1', '13']
>>> for element in ['192', '168', '1', '13']:
    	print(element)    
192
168
1
13
```

Compléter la fonction ci-dessous : 

```Python
def encodage_adresse_IP_binaire(adresseIP):
    """
    Encode une adresse IP en binaire
    param : adresse IP : str
    return : str
    >>> encodage_adresse_IP_binaire("192.168.1.13")
    '11000000101010000000000100001101'
    """
```

6) Une autre application est l'encodage en binaire d'un texte utilisant le codage ASCII  (American Standard Code for Information Interchange) des caractères.

<img src="Assets/ascii.png"> 

Pour obtenir le code ASCII d'un caractère :

```Python
>>> ord("k")
107
```

Compléter la fonction ci-dessous : 

```Python
def encodage_texte_ASCII_binaire(texte):
    """
    Encode un texte ASCII en binaire
    param : texte : str
    return : str
    >>> encodage_texte_ASCII_binaire("vive la snt")
    '0111011001101001011101100110010100100000011011000110000100100000011100110110111001110100'
    """
```

7)  Compléter maintenant le programme suivant de conversion binaire-décimal en python dont une ligne est incomplète.

```python
def conversion_binaire_decimal(code_binaire):
    """
    Renvoie la valeur décimal de code_binaire
    param : code_binaire : str
    return : int
    >>> conversion_binaire_decimal('00110011')
    51
    """
    resultat=0
    for i in range(len(code_binaire)):
        nombre=int(code_binaire[i])
        resultat+=nombre*(2**(# à compléter #))
    return resultat
```

8) Donner l'adresse IP en notation décimale codée par 10011000110000110110110001100010

9) Peut-on concevoir un programme qui donnerait directement l'adresse IP sous forme décimale à partir de son expression sous forme binaire ?

Pour cela, il faut prélever des parties de la chaîne de caractères en réalisant un `slice` :

```python
>>> "10011000110000110110110001100010"[0:8]
'10011000'
```
```python
def conversion_adresseIP_binaire_decimal(code_binaire):
    """
    Renvoie le code décimal d'une adresse IP sous la forme de 4 octets
    param : code_binaire : str
    return : str
    >>> conversion_adresseIP_binaire_decimal('11000000101010000000000100001101')
    '192.168.1.13'
    """
```

10) Compléter la fonction ci-dessous qui permet de décoder le code binaire correspondant à un texte.

Pour obtenir le caractère correspondant à un code décimal, utiliser 

```Python
>>> chr(52)
'4'
```

```Python
def decodage_binaire_texte_ASCII(code_binaire):
    """
    Décode le code binaire d'un texte ASCII
    param : code_binaire : str
    return : str
    >>> decodage_binaire_texte_ASCII('0111011001101001011101100110010100100000011011000110000100100000011100110110111001110100')
    'vive la snt'
    """
```

