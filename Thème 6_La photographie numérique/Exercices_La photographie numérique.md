## Exercices Thème 7 : La photographie numérique

### Exercice 1

On dispose d'une image carrée dont la définition est de 4 Mpx. 
On rappelle que la **définition** d'une image est le produit du nombre de pixels sur la hauteur par le nombre de pixels sur la largeur de l'image.
Déterminer les dimensions en cm de cette image :
- si elle est affichée sur un écran de résolution 144 ppi (pixels per inch)
- si elle est imprimée par une imprimante de résolution 300 dpi (dots per inch).

1 inch = 1 pouce = 2.54 cm

### Exercice 2

Un magasin propose deux ordinateurs à des prix intéressants.
Le premier possède un écran de définition 1233 × 925 px et de dimensions 345,44 × 259,08 mm (écran 17").
Le second a un écran de définition 1219 × 914 px et de dimensions 304,80 × 228,60 mm (écran 15").
Lequel a la meilleure résolution ?
On rappelle que la **résolution** d'un écran est la densité de pixels affichés sur chaque pouce de l'écran, elle s'exprime en ppi (pixels per inch).

### Exercice 3

La **luminance** relative est une grandeur correspondant à la sensation visuelle de luminosité ; elle varie entre 0 pour le noir et 1 pour le blanc pris comme référence, la pondération est basée sur la sensibilité de l'oeil humain  ; le vert contribue le plus à l'intensité perçue par l'œil humain et le bleu le moins.
Lorsque l'on dispose du code RVB d'une couleur, que l'on note (R,V,B), le calcul de la luminance se calcule à l'aide de la formule L = (0,2126 × R + 0,7152 × V + 0,0722 × B)/255.

Écrire une fonction en Python telle que `lum(couleur)` qui renvoie la valeur de la luminance, lorsque la couleur est donnée sous forme d'un triplet (r,v,b).
Donner sa valeur dans le cas du blanc (255,255,255), du rose clair (255,192,203) et du bordeaux (165,42,42).

### Exercice 4

Dans cet exercice nous allons utiliser le module Image de la librairie PIL de Python.

On suivra [ici](http://vfsilesieux.free.fr/traitements_d_une_me%CC%82me_image.pdf) différents traitements possibles d'une image.

Application : réaliser les programmes permettant d'obtenir les drapeaux suivants (200×200) portant chacun un fin liseré noir :

- France : <img width="50" height="50" src="Assets/Drapeau_france.jpg">
- Belgique : <img width="50" height="50" src="Assets/Drapeau_belge.jpg">
- Hollande : <img width="50" height="50" src="Assets/Drapeau_hollande.jpg">
- Suisse : <img width="50" height="50" src="Assets/Drapeau_suisse.jpg">
- Japon : <img width="50" height="50" src="Assets/Drapeau_japon.jpg">

### Exercice 5

Dans cet exercice nous allons utiliser la possibilité de modifier les données portant sur les pixels d'une image avec JavaScript.    
On trouvera [ici](http://isnangellier.alwaysdata.net/php/Transformations_image.html) différentes transformations réalisées en modifiant les pixels d'une image.

1. Réaliser le traitement permettant d'obtenir le résultat suivant :

<img src="Assets/Transformation_4_tetes.png">

2. Comprendre l'algorithme permettant de réaliser un [effet de loupe.](http://isnangellier.alwaysdata.net/php/Algorithme_loupe.html)
3. Comprendre l'algorithme permettant de repérer le [positionnement d'un point à l'intérieur d'un contour polygonal quelconque](http://isnangellier.alwaysdata.net/php/Algorithme_localisation_quelconque.html).
4. Analyser le code source de la [page html](http://isnangellier.alwaysdata.net/php/melange.html) suivante et procéder à une réalisation similaire. 