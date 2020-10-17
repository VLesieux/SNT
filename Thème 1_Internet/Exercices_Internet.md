## Exercices Thème 1 : Internet

### Exercice 1

Déterminer sa propre adresse IP.  

Sous Windows, aller dans `Système Windows`
- ouvrir un terminal en cliquant sur `Démarrer`, `exécuter` et en tapant `cmd`
- saisir la commande `ipconfig`

### Exercice 2

1) Coder en binaire la valeur décimale 51. Vérifier dans la console de Thonny avec `bin(51)`.

2) Déterminer la valeur décimale de l'octet `10110001`. Vérifier dans la console de Thonny avec `0b10110001`.

3) Compléter le programme suivant de conversion décimal-binaire en python dont une ligne est manquante.

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
    a=""
    # ligne à compléter
        a=str(nombre%2)+a
        nombre=nombre//2
    return a
```

5) À l'aide du programme précédent, coder en écriture binaire l'adresse IP 192.168.1.13

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

7)  Compléter le programme suivant de conversion binaire-décimal en python dont une ligne est manquante.

```python
a=0
code=input("Veuillez entrer un code binaire : ")
inversion_code=code[::-1]#permet d'inverser la chaîne de caractères
for i in range(len(code)):
	# ligne à compléter
print(a)
```

8) Donner l'adresse IP codée par 10011000110000110110110001100010

9) Peut-on concevoir un programme qui donnerait directement l'adresse IP sous forme décimale à partir de son expression sous forme binaire ?

Pour cela, on peut prélever une partie d'une chaîne de caractères en réalisant un `slice` :

```python
>>> "10011000110000110110110001100010"[0:8]
'10011000'
```

### Exercice 3

Sur le réseau simplifié décrit ci-dessous, citer au moins trois chemins permettant de relier la machine M8 à la machine M4.

<img src="Assets/routages.png" width="800" height="600">

1) Quelle est la valeur minimale du TTL d'un paquet émis par M8 pour qu'il parvienne à M4 ?
On rappelle que le TTL est une donnée placée au niveau de l'en-tête du paquet IP qui indique le nombre maximal de routeurs de transit pour éviter qu'un paquet ne boucle à l'infini s'il existe un problème de boucle de routage.

2) Que se passe-t-il si le routeur B tombe en panne ? si le routeur D tombe en panne ?

### Exercice 5

Accéder à sa propre table de routage.
Sous Windows, dans un terminal saisir la commande `route print`


### Exercice 6

Identifier la route empruntée pour accéder au site web www.facebook.com
Sous Windows, dans un terminal saisir la commande :  `tracert www.facebook.com`

### Exercice 7

Vérifier que le site www.wikipedia.org vous est accessible en saisissant dans un terminal la commande `ping www.wikipedia.org`


