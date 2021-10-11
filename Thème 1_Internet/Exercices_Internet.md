## Exercices Thème 1 : Internet

### Exercice 1

Déterminer sa propre adresse IP.  

Sous Windows, aller dans `Système Windows`
- ouvrir un terminal en cliquant sur `Démarrer`, `exécuter` et en tapant `cmd`
- saisir la commande `ipconfig`

### Exercice 2

1) Coder à la main en binaire la valeur décimale 51. Vérifier dans la console de Thonny avec `bin(51)`.

2) Inversement calculer à la main la valeur décimale de l'octet `10110001`. Vérifier dans la console de Thonny avec `0b10110001`.

3) Après avoir observé dans l'algorithme utilisé le rôle que doit prendre à chaque fois le nouveau dividende par rapport au quotient précédent, compléter le programme suivant de conversion décimal-binaire en python dont une seule ligne est manquante.

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
4) On peut transformer le programme précédent en réalisant une fonction que l'on appelera `conversion_decimal_binaire`. Déterminer la ligne manquante.

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
    # ligne à compléter
        a=str(nombre%2)+a
        nombre=nombre//2
    a='0'*(8-len(a))+a##pour rajouter autant de 0 que nécessaire à l'écriture d'un octet
    return a
```

Code à ajouter pour importer le module doctest

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

5) En utilisant le programme précédent, coder en écriture binaire l'adresse IP 192.168.1.13

6) Peut-on concevoir un programme qui donnerait directement le code binaire d'une adresse IP ?

Pour cela, on peut transformer une chaîne de caractères en liste en utilisant un séparateur avec la méthode `split` puis parcourir la liste avec `for element in `.

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

```Python
adresseIP=input("Entrez une adresse IP écrite sous forme décimale")
liste=adresseIP.split(".")
resultat=""
for element in liste:
    nombre=int(element)
    # une ligne à compléter
print(resultat)
```

7)  Compléter le programme suivant de conversion binaire-décimal en python dont une ligne est incomplète.

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

8) Donner l'adresse IP codée par 10011000110000110110110001100010

9) Peut-on concevoir un programme qui donnerait directement l'adresse IP sous forme décimale à partir de son expression sous forme binaire ?

Pour cela, on peut prélever une partie d'une chaîne de caractères en réalisant un `slice` :

```python
>>> "10011000110000110110110001100010"[0:8]
'10011000'
```
```python
adresseIP=input("Entrez une adresse IP écrite sous forme de 4 octets")
resultat=""
for i in range(4):
    resultat+="."+str(conversion_binaire_decimal(# à compléter #))
resultat=resultat[1:len(resultat)]#pour supprimer le premier point
print(resultat)
```


### Exercice 3

Sur le réseau simplifié décrit ci-dessous, citer au moins trois chemins permettant de relier la machine M8 à la machine M4.

<img src="Assets/routages.png" width="800" height="600">

1) Quelle est la valeur minimale du TTL d'un paquet émis par M8 pour qu'il parvienne à M4 ?
On rappelle que le TTL est une donnée placée au niveau de l'en-tête du paquet IP qui indique le nombre maximal de routeurs de transit pour éviter qu'un paquet ne boucle à l'infini s'il existe un problème de boucle de routage.

2) Que se passe-t-il si le routeur B tombe en panne ? si le routeur D tombe en panne ?

### Exercice 5

Accéder à sa propre table de routage.
Sous Windows, dans un terminal saisir la commande `route print`.

### Exercice 6

Identifier la route empruntée pour accéder au site web www.facebook.com

Sous Windows, dans un terminal saisir la commande :  `tracert www.facebook.com`.

### Exercice 7

Vérifier que le site www.wikipedia.org vous est accessible en saisissant dans un terminal la commande `ping www.wikipedia.org` puis accéder au site en utilisant l'adresse IP. 
Rappeler le nom que l'on donne sur Internet aux serveurs qui disposent d’une application logicielle (sorte d’annuaire) permettant de faire la correspondance entre le nom de domaine demandé et l’IP publique associée au serveur. 


