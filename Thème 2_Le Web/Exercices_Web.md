## Exercices Thème 2 : Web

### Exercice 1

On souhaite étudier une version minimaliste de l'algorithme **PageRank** du moteur de recherche Google afin de comprendre son fonctionnement.  
Par souci de simplicité, on travaille avec seulement 5 pages web, chaque page web étant numérotée.

<img src="Assets/PageRank.png" width="300" height="300">

Chaque flèche représente un lien **hypertexte** permettant le passage d'une page à l'autre grâce à votre navigateur (web browser). 

Ainsi, on voit sur le schéma ci-dessus que la page 0 possède un lien vers la page 1 et un lien vers la page 2.   
En retour, trois pages possèdent des liens vers la page 0 : les pages 2, 3 et 4.  

En Python, on utilise une liste appelée `web` contenant, pour chaque page web, la liste des liens contenus sur cette page vers d'autres pages web ; cette liste s'appelle une <b>représentation par liste d'adjacence du graphe</b>.  
Dans notre exemple, web[0] va donc s'écrire [1,2] car la page 0 contient un lien vers la page 1 et un lien vers la page 2.

1. Compléter le tableau suivant à la main :

<table>
<tr>
<td>Numéro de page
</td>
<td>pointant vers
</td>
<td>sortant de
</td>
</tr>
<tr>
<td>Page 0
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Page 1
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Page 2
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Page 3
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Page 4
</td>
<td>
</td>
<td>
</td>
</tr>
</table>

Proposer un classement par ordre de popularité des différentes pages web tel que le ferait un moteur de recherche.


2. On donne le code suivant qui correspond à l'algorithme PageRank implémenté en Python :

```Python
import random#importation de la bibliothèque random
web=[[1,2],[4],[0,3],[0,4],[0]]
passages=[0,0,0,0,0]
page=2

for i in range(1000):
    page=random.choice(web[page])
    passages[page]=passages[page]+1
    
print(passages)
```

On a utilisé la fonction `choice` du module `random` qui permet d'obtenir aléatoirement un élément dans une liste.

```Python
>>> liste=['A','B','C','D']
>>> from random import choice
>>> choice(liste)
'A'
>>> choice(liste)
'C'
```

Exécuter le code pour observer le classement par ordre de popularité des différentes pages web obtenu grâce à l'algorithme. 


3. Proposer une interprétation au fonctionnement de ce code. Utiliser le Debugger de Thonny.

### Exercice 2

Aller à l'adresse https://www.gouvernement.fr/composition-du-gouvernement et télécharger le code HTML en faisant un clic droit puis "Enregistrer sous..".      
Il apparaît un **fichier** avec l'**extension** **htm** ou **html** ainsi qu'un **dossier** contenant les images présentes sur la page.      
À l'aide de l'**éditeur de texte** NotePad++, en utilisant la fonction de recherche (**ctrl F** (pour find)) modifier le contenu de la page **html** pour afficher votre nom au lieu d'un ministre (bien sûr, cette modification sera présente uniquement sur le fichier HTML que vous venez de télécharger et stocker sur votre ordinateur...) et n'affectera pas la page affichée sur le web qui elle est stockée sur le serveur du ministère.
Observer également la structure de la page.

### Exercice 3

Écrire une histoire dont vous êtes le héros où chaque page possède un **hyperlien** pour chaque choix possible dans l'histoire.  

Voici un exemple, où le couple de balises `<ul> </ul>` sert à définir une liste à puces (non ordonnée) et où les balises `<li> </li>` délimite un élement de la liste, en l'occurence un choix possible.

Enregistrer toutes les pages dans le même dossier.

_Script de la page appelée **debut.html**_

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Le début d'une grande aventure</title>
</head>
<body>
Vous incarnez Lancelot, un valeureux chevalier.<br>
Un jour, un messager vous apprend que le roi demande après vous de toute urgence.<br>
<ul>
	<li><a href="palais.html"> Vous vous rendez au palais royal immédiatement.</a></li>
	<li><a href="messager.html"> Vous demandez au messager la nature de sa demande.</a></li>
	<li><a href="epee.html"> Vous faites un détour pour aller chercher votre épée.</a></li>
</ul>
</body>
</html>
```

_Script de la page appelée **palais.html**_

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Palais royal</title>
</head>
<body>
Alors que vous rentrez dans le palais royal, un bruit assourdissant s'échappe des cuisines.
</body>
</html>
```

À vous de réaliser toutes les pages de façon à ce que les trois liens de la page `debut.html` soient actifs.

### Exercice 4

1) Créer une page web appelée exemple.html vous permettant de tester et de mettre en oeuvre les éléments de code html présentés sur la [page suivante] (https://github.com/VLesieux/SNT/blob/master/Th%C3%A8me%202_Le%20Web/Assets/Creation_page_web.md).

2) Réaliser une [page web](http://vfsilesieux.free.fr/page_web.html) présentant le lieu de votre choix en respectant un cahier des charges.
 
### Exercice 5

Comprendre le code qui a permis de réaliser un [quiz en ligne](http://isnangellier.alwaysdata.net/php/Creation_quizz.html) et s'en inspirer pour réaliser son propre quiz. 