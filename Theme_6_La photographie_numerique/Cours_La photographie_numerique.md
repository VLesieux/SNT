## Thème 6 : La photographie numérique

On trouvera [ici](http://vfsilesieux.free.fr/Photography.pdf) un document complet et illustré portant sur le sujet de l'histoire de la photographie (argentique puis numérique) provenant de la revue scientifique New Scientist.  

### Introduction

L'apparition de la photographie numérique a bouleversé notre rapport à l'image et à ses utilisations. L'imagerie astronomique, pour sa part, a gagné en précision grâce aux capteurs photographiques.

### Historique

- 1826 : Première photographie argentique du français Nicéphore Niépce
- 1900 : Début de la photographie en couleur. Généralisation du format 24×36 et de la visée reflex après la seconde guerre mondiale.
- 1969 : Premiers capteurs CCD (Charge Coupled Device)
- 1975 : Premiers appareils numériques
- 2007 : Arrivée du smartphone
- 2024 : iPhone 15 : Le moteur neuronal à 16 coeurs a une capacité de 35 billions d'opérations par seconde !

### Capture et numérisation de l'image

Le principe de la capture de l'image par un appareil photographique numérique est similaire au principe de la vision réalisée par l'œil humain : l'objectif de l'appareil photographique (avec ses multiples lentilles) joue un rôle analogue au cristallin de l'œil et permet de projeter l'image sur le capteur CCD comme le cristallin le fait sur la rétine. Le diaphragme de l'appareil photographique, tout comme l'iris de l'œil, permet de réguler la quantité de lumière entrant dans l'objectif.   
Cependant la mise au point de l'appareil photographique diffère de l'accommodation de l'œil ; dans le premier cas la lentille ou les lentilles se déplacent, dans le second cas, ce sont les muscles ciliaires qui appuient sur le critallin en modifiant sa vergence ; plus celui-ci est bombé, plus le cristallin est convergent, plus sa vergence est grande (par définition elle est l'inverse de la distance focale f'=OF' où F' désigne le foyer image où converge un faisceau incident de lumière parallèle).


<img width="650" height="500" src="Assets/analogie_oeil_camera.png">

La rétine est constituée de cellules photosensibles : les cônes (bleus, rouges, verts), qui permettent d'analyser les différentes couleurs de l'image en vision diurne (elles sont sensibles à des domaines spécifiques du spectre visible) et les bâtonnets pour la vision nocturne.

<img width="650" height="500" src="Assets/cones.png">

De même le **capteur** d'un appareil numérique est constitué de **photosites** : il s'agit de cellules mesurant l'intensité lumineuse. Chacune de ces cellules est munie d'un filtre coloré (rouge, vert, bleu) ne laissant passer que les rayons de la couleur en question et d'une microlentille convergente permettant de concentrer les rayons au centre du photosite. Les photosites sont disposés comme sur la figure ci-dessous : deux sites "vert" pour un site "rouge" et un site "bleu". La **définition** du capteur correspond au nombre de ses photosites.


<img width="650" height="500" src="Assets/photosite.png">

Une fois l'image capturée, les informations reçues par chaque photosite permettent d'obtenir un premier fichier au format RAW, c'est-à-dire un fichier brut de données non interprétées.
Les données subissent ensuite plusieurs traitements, notamment le **dématriçage**, afin d'obtenir une image numérique (format JPEG ou TIFF) constituée de petits carrés de couleur : les pixels.

Voir [exercice sur le capteur de l'appareil photo intégré dans un smartphone](Assets/Exercice_physique.pdf)

### Le codage RVB des couleurs sur nos écrans

Une image numérique peut être considérée comme un tableau de pixels, chaque pixel est formé de 3 sous-pixels : rouge, vert, bleu. Il utilise le principe de la **synthèse additive des couleurs** avec trois couleurs primaire : le rouge, le vert et le bleu.

<img width="600" height="500" src="Assets/additive_synthesis.png">

Ce principe est à distinguer de la **synthèse soustractive des couleurs** utilisée par les peintres ou les imprimantes couleurs avec trois couleurs primaires : le jaune, le cyan, le magenta.

<img src="Assets/subtractive_synthesis.png">

<img width="400" height="300" src="Assets/pixels.png"><img width="300" height="300" src="Assets/pixel_microscope.jpg">

La **définition d'une image** est le nombre de pixels constituant l'image. Par exemple, une image contenant 2592 pixels en largeur et 1936 pixels en hauteur (2592×1936) a une définition de 5 018 112 pixels, soit environ 5 Mpx (mégapixels).
Remarque : il n'y a pas nécessairement le même nombre de pixels sur l'image que de photosites sur le capteur. Cela dépend des algorithmes utilisés lors du dématriçage. La définition du capteur peut donc être différente de la définition de l'image.

La **résolution d'une image** quant à elle correspond au nombre de pixels par unité de longueur. Elle est généralement exprimée en ppp (pixel par pouce) ou ppi (pixel per inch) ou dpi (dot per inch) pour les imprimantes. Plus la résolution est importante, plus l'image sera de bonne qualité lors d'un zoom. On obtient une très bonne qualité d'impression avec une résolution de 300 ppi par exemple ; tandis que les écrans d'ordinateur ont désormais généralement une résolution entre 85 et 150 ppi. Cependant certains smartphones ont désormais des écrans avec une très bonne résolution avec par exemple 326 ppi.

La couleur de chaque sous-pixel est codée sur un octet(8 bits), ainsi chaque pixel est codé sur 3 octets renseignant sur les niveaux de ces trois composantes : rouge, vert et bleu, qui sont les couleurs primaires en synthèse additive des couleurs.  
On parle de **codage RVB ou RGB** pour Red-Green-Blue. Il s'agit pour chacune des trois composantes d'indiquer l'intensité lumineuse de la couleur par un nombre compris entre 0 et 255.  
En effet, chaque couleur est codée sur 1 octet formé de 8 bits ce qui offre 2<sup>8</sup>=256 possibilités de niveau de couleur pour le rouge, autant pour le vert et le bleu, soit une totalité de 2<sup>8</sup>×2<sup>8</sup>×2<sup>8</sup>=2<sup>24</sup>=16 777 216 couleurs. 
Ainsi le rouge est codé par (255,0,0) ; le vert par (0,255,0) ; le bleu par (0,0,255).  
Une égalité des trois niveaux correspond à un niveaux de gris, il y en a donc 256 niveaux de gris.

On trouvera ici une application web permettant d'observer [le codage des couleurs](http://isnangellier.alwaysdata.net/php/colours.html) .

Remarque :  le codage RVB des couleurs en binaire n'est pas le seul type de codage possible. Lorsqu'on code une page web par exemple, dans la feuille de style CSS on peut aussi préciser la couleur en utilisant le codage hexadécimal de cette couleur. On trouvera [ici](http://vfsilesieux.free.fr/exemple_page_web/page_web.html) une page html dont on pourra regarder le code source qui montre que trois types de codages des couleurs dans le CSS sont possibles pour un résultat analogue, par exemple : green, rgb(0,128,0) ou #008000. 

Avec un éditeur de texte tel que Sublime Text, on peut voir le contenu d'un fichier jpg, on y trouve le codage hexadécimal des pixels :

<img width="300" height="300" src="Assets/perrot.jpg"><img width="300" height="300" src="Assets/code_image_perrot.png">


### Métadonnées

Un fichier RAW, JPEG ou TIFF ne contient pas uniquement des données permettant l'affichage de l'image, il contient également des données sur la date et l'heure de la prise de vue, l'appareil utilisé, éventuellement le lieu etc. Toutes ces données sont appelées des **métadonnées** et sont stockées au format EXIF (Exchangeable Image File Format). On peut accéder à ces données, en effectuant un clic-droit sur le fichier, et en regardant dans les **propriétés de l'image**.

<img src="Assets/proprietes_images1.png">
<img src="Assets/proprietes_images2.png">



### Algorithmes de traitement de l'image

Entre le moment où l'on presse sur le bouton de l'appareil numérique pour déclencher une prise de vue et la publication de l'image sur un réseau social, de nombreux algorithmes ont été réalisés.

- Avant même le déclenchement de la prise de vue : 

	. Stabilisation de l'image afin de compenser le mouvement du photographe.  
	. Mise au point.  
	. Correction du flou.  

- Capture de l'image : obtention du fichier RAW
- Après la capture de l'image :

	. Dématriçage.  
	. Balance des blancs. 
	. Contraste.    
	. Saturation.  

- Compression de l'image : obtention du fichier JPEG
- Amélioration de l'image
	
	Une fois l'image enregistrée on peut encore utiliser différents algorithmes grâce à des logiciels de retouche afin de corriger des imperfections, améliorer le rendu des couleurs ou passer en noir et blanc, découper des zones de l'image (détection des contours) etc.


On peut également évoquer les [algorithmes de reconnaissance faciale](Assets/Image_recognition.pdf).
	
### Droit à l'image - droit d'auteur

À l'heure des réseaux sociaux, il est important de rester vigilant et de connaître ses droits afin de maîtriser la diffusion de ses données personnelles.

L'article 226-1 du code pénal indique : 

   « - Est puni d'un an d'emprisonnement et de 45000 euros d'amende le fait, au moyen d'un procédé quelconque, volontairement de porter atteinte à l'intimité de la vie privée d'autrui :  
   « 1° En captant, enregistrant ou transmettant, sans le consentement de leur auteur, des paroles prononcées à titre privé ou confidentiel ;    
   « 2° En fixant, enregistrant ou transmettant, sans le consentement de celle-ci, l'image d'une personne se trouvant dans un lieu privé.   
   « Lorsque les actes mentionnés au présent article ont été accomplis au vu et au su des intéressés sans qu'ils s'y soient opposés, alors qu'ils étaient en mesure de le faire, le consentement de ceux-ci est présumé ».

Chaque personne dispose d'un droit exclusif sur son image et l'utilisation qui en est faite. Ainsi, lorsqu'une image a été prise dans un lieu privé, sa publication nécessite le consentement écrit des personnes identifiables. Toutefois, sous reserve de ne pas porter atteinte à la dignité des personnes, certaines images ne sont pas soumises à cette règle, comme par exemple :

- les images illustrant des événements d'actualité (droit à l'information)
- les images de personnalités publiques dans l'exercice de leurs fonctions
- les images illustrant un sujet historique

Dans le cas où le droit n'est pas respecté, il convient alors de demander le retrait de l'image, puis, si cela n'aboutit pas, une plainte peut être déposée auprès du CNIL (Commission Nationale de l'Informatique et des Libertés) : https://www.cnil.fr/fr/plaintes

Par ailleurs, il existe un **droit à l'oubli**. Ainsi on peut demander le retrait de certaines données dès lors qu'on estime qu'elles nous portent préjudice.

Enfin, rappelons que les images numériques sont également soumises au **droit d'auteur**. Avant de publier une image il faut donc s'assurer que cela est possible, par exemple parce qu'il s'agit d'une image diffusée sous la licence Creative Commons. Notons qu'en cas de litige, les métadonnées EXIF peuvent fournir des informations essentielles.
