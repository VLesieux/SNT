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

4) Coder en écriture binaire l'adresse IP 192.168.1.13

5)  Compléter le programme suivant de conversion binaire-décimal en python dont une ligne est manquante.

```python
a=0
code=input("Veuillez entrer un code binaire : ")
inversion_code=code[::-1]#permet d'inverser la chaîne de caractères
for i in range(len(code)):
	# ligne à compléter
print(a)
```

6) Donner l'adresse IP codée par 10011000110000110110110001100010. 

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


