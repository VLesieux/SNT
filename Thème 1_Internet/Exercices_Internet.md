## Exercices Internet

### Exercice 1

Déterminer sa propre adresse IP.  

Sous Windows
- ouvrir un terminal en cliquant sur `Démarrer`, `exécuter` et en tapant `cmd`
- saisir la commande `ipconfig`

### Exercice 2

Coder en écriture binaire l'adresse IP 192.168.1.13

Procéder "à la main" puis utiliser l'implémentation en Python de l'**algorithme de conversion  décimal-binaire** expliquée [ici](Assets/Algorithmes_Conversions_binaires.md).


### Exercice 3

Donner l'adresse IP codée par 10011000110000110110110001100010
Procéder "à la main" puis utiliser l'implémentation en Python de l'**algorithme de conversion binaire-décimal** expliquée [ici](Assets/Algorithmes_Conversions_binaires.md).

Remarque : On trouvera également [ici](http://isnangellier.alwaysdata.net/php/Conversions_binaire_secondaire.html) une implémentation en JavaScript qui est le langage des navigateurs ; on se limitera à observer le code et on retrouvera, implémentés de façon analogue, les algorithmes de conversion. 

### Exercice 4

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

### Exercice 8

1) Lorsqu'on parle d'interaction client/serveur, un client est-il une machine qui envoie ou qui reçoit des requêtes ?
2) Un ordinateur connecté à un réseau pair-à-pair est-il un client, un serveur ou les deux ?
 
