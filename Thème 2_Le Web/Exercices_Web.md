## Exercices Thème 2 : Web

### Exercice 1

On souhaite implémenter une version minimaliste de l'algorithme PageRank du moteur de recherche Google. Par souci de simplicité, chaque page web sera numérotée.
Considérons seulement 5 pages web:

<img src="Assets/PageRank.png" width="300" height="300">

Chaque flèche représente un lien hypertexte. Ainsi, la page 0 possède un lien vers la page 1 et vers la page 2. Inversement, trois pages possèdent des liens vers la page 0 : les pages 2, 3 et 4.
En Python, on utilise une liste web contenant, pour chaque page web, la liste des liens contenus sur cette page vers d'autres pages web ; c'est ce que l'on appelle la représentation par liste d'adjacence du graphe du Web. Dans notre exemple, web[0] va donc s'écrire [1,2] car la page 0 contient un lien vers la page 1 et un lien vers la page 2.

On donne alors l'algorithme suivant :

```Python
from random import choice
web=[[1,2],[4],[0,3],[0,4],[0]]
passages=[0,0,0,0,0]
page=2

for i in range(1000):
    page=choice(web[page])
    passages[page]=passages[page]+1
    
print(passages)
```

On a utilisé la fonction choice importée du module random qui permet d'obtenir aléatoirement un élément dans une liste.

```Python
>>> liste=['A','B','C','D']
>>> from random import choice
>>> >>> choice(liste)
'A'
>>> choice(liste)
'C'
```
1. Compléter le tableau suivant :

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

Proposer "à la main" un classement par ordre de popularité des différentes pages web. 

2. Exécuter le code pour observer le classement par ordre de popularité des différentes pages web obtenu grâce à l'algorithme. 

3. Proposer une interprétation de ce code. Utiliser le Debugger de Thonny.

### Exercice 2

Aller à l'adresse https://www.gouvernement.fr/composition-du-gouvernement et télécharger le code HTML en faisant un clic droit puis "Enregistrer sous..". Modifier le contenu de la page pour afficher votre nom au lieu d'un ministre (bien sûr, cette modification sera uniquement présente sur le fichier HTML que vous venez de télécharger...).

### Exercice 3

Écrire une histoire dont vous êtes le héros où chaque page possède un hyperlien pour chaque choix possible dans l'histoire.
Voici un exemple, où le couple de balises `<ul> </ul>` sert à définir une liste à puces (non ordonnée) et où les balises `<li> </li>` délimite un élement de la liste, en l'occurence un choix possible.

script de la page debut.html

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

script de la page palais.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Palais royal</title>
</head>
<body>
Alors que vous rentrez dans le palais royal, un bruit assourdissant s'échappe des cuisines.
<ul>
	<li><a href="roi.html"> Vous passez votre chemin et allez voir le roi.</a></li>
	<li><a href="cuisine.html">Vous allez voir ce qui se passe aux cuisines.</a></li>
</ul>
</body>
</html>
```


### Exercice 4

Réaliser une [page web](http://vfsilesieux.free.fr/page_web.html) présentant le lieu de votre choix respectant un cahier des charges.
 
