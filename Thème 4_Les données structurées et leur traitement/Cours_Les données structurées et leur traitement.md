## Les données structurées et leurs traitements

### Introduction

L'informatique s'est révélée d'une très grande efficacité pour manier des fichiers immenses ce qui a permis aux entreprises comme à l'administration une gestion rapide et efficace des données. Pour y parvenir, les informaticiens ont conçu des algorithmes très astucieux et d'une très grande fiabilité.

### Histoire

- 1725 : Basile Bouchon invente un système de programmation utilisant un ruban perforé qui permet d'automatiser un métier à tisser.
- 1928 : IBM fait breveter ses cartes perforées à 80 colonnes qui sont les premiers supports de stockage des données.
- 1956 : Invention du premier disque dur, l'IBM 350, constitué de 50 disques de 24 pouces (61 cm) de diamètre et permettant de stocker environ 5Mo de données. Actuellement on peut obtenir une capacité de stockage de 16 To (3 milliards de fois plus) sans dépasser les 3,5 pouces (9 cm).
- 1970 : Invention du modèle relationnel, grâce à E.F.Codd, permettant de structure et d'indexer des bases de données
- 1979 : Création du premier tableur : VisiCalc.
- 1997 : Apparition du terme Big Data, faisant référence à des ensembles massifs de données générés par l'utilisation des outils numériques
- 2000 : Utilisation de la clé USB et la carte SD comme supports de stockage
- 2009 : Le président Obama lance l'<i>Open Government Initiative</i> afin d'instaurer davantage de transparence dans la gouvernance. Cette « initiative » vise à créer un niveau sans précédent de transparence et d'ouverture du gouvernement. Elle se situe dans une tendance émergente qui est celle de l' <i>Open source governance</i>, qui prône l'application en politique et dans la gouvernance des démocraties de philosophies telles que l'open source et les « contenus ouverts » (Open data), pour permettre à tout citoyen intéressé de contribuer à créer les contenus de la Politique, et pour permettre aux gouvernements de mieux bénéficier des savoirs et savoir-faire locaux. Les agences gouvernementales ont en 2010 commencé, autour du gouvernement fédéral, à produire des pages Web de gouvernance élargie, proposant des informations autrefois inaccessibles au public, et invitant les citoyens américains à produire des idées et suggestions.


### Les données structurées

Lorsqu'on parle de **données structurées**, une **donnée** est une valeur (nombre ou chaîne de caractères) décrivant une entité (une personne, un objet, un événement).
Une même entité peut être décrite par plusieurs **descripteurs**.
Dans le cas de données portant sur un individu identifiable, on parle de **données personnelles**.

Exemple : Un contact dans son téléphone portable peut être décrit par les descripteurs : "Nom", "Prénom", "Numéro de téléphone", "Adresse e-mail", "Date de naissance". Il s'agit évidemment de données personnelles.

Une **collection de données**, c'est-à-dire un ensemble de données décrivant plusieurs entités avec les mêmes descripteurs, peut être représentée à l'aide d'un tableur : les objets en ligne, les descripteurs en colonne. On parle aussi de **table de données**.

Une **base de données** est une ensemble de tables de données pouvant être reliées entre elles.

Différents formats peuvent être utilisés pour représenter des données structurées, notamment les formats CSV, XML, JSON et VCF.

Exemple de données :

Nom	Prénom	Numéro de téléphone	Adresse e-mail	Date de naissance	Ville
Green	Emma	06 36 62 23 66	emma.green@free.fr	16/05/2002	Lyon
Gascon	Robert	06 64 58 54 36	robert.gascon@wanadoo.fr	08/02/1988	Orléans
Villefort	Valentine	06 82 25 36 84	valentine.villefort@gmail.com	20/06/1994	Tours
Poclain	Alexandre	06 25 39 26 37	alexandre.poclain@orange.fr	11/02/1961	Nancy

Vue des [données](Assets/contacts.xls) mises en tableau réalisé dans un tableur tel que Excel ou LibreofficeCalc : <img src="Assets/image_excel.png" width="200" height="100">

Le même [fichier](Assets/contacts.csv) au format **csv** lu dans un éditeur de texte :

<img src="Assets/format_csv.png" width="500" height="300">

Le même fichier au format **xml** lu dans un éditeur de texte :

<img src="Assets/format_xml.png" width="900" height="900">

Le même fichier au format **json** lu dans un éditeur de texte :

<img src="Assets/format_json.png" width="800" height="800">

Les fichiers au format PDF, JPG, MP3...constituent également des fichiers de données mais ceux-ci sont **non structurées**.

Une partie de fichier au format mp3 lu dans un éditeur de texte :

<img src="Assets/format_mp3.png" width="800" height="800">

Cependant, à chacun de ces fichiers sont toujours associées des **métadonnées** indiquant selon le type de fichier une date, un auteur, une donnée de géolocalisation, un matériel utilisé... 

Exemple de métadonnées d'un fichier audio :

<img src="Assets/metadonnees.png" width="1200" height="1200">


### Collecte des données

L'utilisation actuelle des outils numériques fait qu'une quantité incroyable de données sont stockées et exploitées, ce que l'on appelle le **Big Data**.

Parmi ces données, on retrouve celles renseignées par les utilisateurs de sites internet, par exemple lorsque l'on crée un compte sur un site de vente en ligne ou lorsque l'on s'inscrit sur un réseau social : on renseigne les champs 'Nom', 'Prénom', 'Date de naissance'.. d'un **formulaire**. Ces données sont souvent transmises à des partenaires commerciaux ou des organismes qui pourront les exploiter. On trouve généralement une case à cocher à la fin des formulaires donnant notre accord pour la transmission de nos données à ces partenaires, qu'il suffit donc de ne pas cocher.

D'autres données proviennent, comme on l'a vu dans le thème "web", des **cookies** créés lors de nos navigations sur internet, ou encore des autorisations données lors du téléchargement d'applications sur smartphone ou tablette. On peut donc ainsi transmettre, sans même le savoir, des données de géolocalisation relatives à notre activité sur Internet, voire issues de notre carnet d'adresse. Il est donc important de bien lire les conditions relatives à l'utilisation des données avant de télécharger une application.

Enfin, certaines données dites ouvertes  : **Open data** sont publiques et libres de droits. On trouve par exemple un grand nombre de données de toutes sortes sur le site https://www.data.gouv.fr/fr/ qui est la plateforme ouverte des données publiques françaises.

Le **RGPD**, Règlement Général sur la Protection des Données, entré en vigueur le 25 mai 2018, vise à renforcer la protection des données personnelles dans l'Union Européenne en établissant des règles sur la collecte et la gestion des données récoltées par les entreprises et organismes. On trouve par exemple dans les dispositions un **droit à l'effacement des données personnelles** (c'est-à-dire le droit pour chacun de demander l'effacement de ses données pour certains motifs), un **droit à la portabilité des données personnelles** (on peut ainsi demander à un organisme de nous fournir les données personnelles nous concernant en vue par exemple de les transmettre à un autre organisme), ainsi que des principes de **protection des données** (nécessité de garantir au mieux la sécurité des données).


### Traitement des données structurées

Lorsqu'on dispose d'une table de données, il peut être intéressant d'effectuer des opérations de recherche, de tri, de filtre ou bien des calculs sur les valeurs des descripteurs.

Exemple : dans un fichier client, on peut effectuer les opérations suivantes:
- rechercher le numéro de téléphone d'un client pour le contacter
- trier les données dans l'ordre alphabétique des noms de familles, puis des prénoms
- filtrer les clients dans une catégorie ; par exemple dans la catégorie 18-25 ans pour une publicité ciblée
- déterminer la répartion homme/femme des clients

On peut également croiser les informations de plusieurs tables issues d'une même base de données.

Exemple : Dans le but de distribuer des bons d'achat aux clients les plus fidèles d'un magasin, on peut commencer par filtrer dans le fichier des ventes les clients ayant effectué le plus d'achats, puis chercher dans un deuxième leurs adresses postales dans le fichier client.
Lorsque les données sont représentées sur un tableur, on peut aisément effectuer ce genre d'opérations qui consistent à les **filtrer** ou les **trier**.

<img src="Assets/filtration_donnees.png" width="400" height="400">

On réalise le fichier contacts.py avec Thonny placé dans le même dossier que le fichier contacts.csv.

```Python
import csv
fichier=open('contacts.csv','r')#ouverture du fichier csv
lecteur=csv.reader(fichier)
table=[]
for ligne in lecteur:
    table.append(ligne)
fichier.close
print(table)
print("descripteurs : ",table[0])#affichage des descripteurs
del table[0]#suppression de la ligne des descripteurs
print(table)

>>> %Run contacts.py
[['\ufeffNom', 'Prénom', 'Numéro de téléphone', 'Adresse e-mail', 'Date de naissance', 'Ville'], ['Green', 'Emma', '06 36 62 23 66', 'emma.green@free.fr', '16/05/2002', 'Lyon'], ['Gascon', 'Robert', '06 64 58 54 36', 'robert.gascon@wanadoo.fr', '08/02/1988', 'Orléans'], ['Villefort', 'Valentine', '06 82 25 36 84', 'valentine.villefort@gmail.com', '20/06/1994', 'Tours'], ['Poclain', 'Alexandre', '06 25 39 26 37', 'alexandre.poclai@orange.fr', '11/02/1961', 'Nancy']]
descripteurs :  ['\ufeffNom', 'Prénom', 'Numéro de téléphone', 'Adresse e-mail', 'Date de naissance', 'Ville']
[['Green', 'Emma', '06 36 62 23 66', 'emma.green@free.fr', '16/05/2002', 'Lyon'], ['Gascon', 'Robert', '06 64 58 54 36', 'robert.gascon@wanadoo.fr', '08/02/1988', 'Orléans'], ['Villefort', 'Valentine', '06 82 25 36 84', 'valentine.villefort@gmail.com', '20/06/1994', 'Tours'], ['Poclain', 'Alexandre', '06 25 39 26 37', 'alexandre.poclai@orange.fr', '11/02/1961', 'Nancy']]
```

Commençons par trier les contacts dans l'ordre alphabétique des noms de famille à l'aide de la fonction `sorted`.

```Python
>>> sorted(table)
[['Gascon', 'Robert', '06 64 58 54 36', 'robert.gascon@wanadoo.fr', '08/02/1988', 'Orléans'], ['Green', 'Emma', '06 36 62 23 66', 'emma.green@free.fr', '16/05/2002', 'Lyon'], ['Poclain', 'Alexandre', '06 25 39 26 37', 'alexandre.poclai@orange.fr', '11/02/1961', 'Nancy'], ['Villefort', 'Valentine', '06 82 25 36 84', 'valentine.villefort@gmail.com', '20/06/1994', 'Tours']]
```

La fonction appelée sans paramètre trie la table par ordre alphabétique sur le premier champ qui est Nom.

Pour trier sur un autre champ par exemple Ville, voici la procédure à suivre :

```Python
def ville(contact):
    return contact[5]#5 est l'indice du champ Ville
>>> sorted(table,key=ville)#ici ville est une fonction 
[['Green', 'Emma', '06 36 62 23 66', 'emma.green@free.fr', '16/05/2002', 'Lyon'], ['Poclain', 'Alexandre', '06 25 39 26 37', 'alexandre.poclai@orange.fr', '11/02/1961', 'Nancy'], ['Gascon', 'Robert', '06 64 58 54 36', 'robert.gascon@wanadoo.fr', '08/02/1988', 'Orléans'], ['Villefort', 'Valentine', '06 82 25 36 84', 'valentine.villefort@gmail.com', '20/06/1994', 'Tours']]
```

Effectuons maintenant la recherche du contact dont le numéro de téléphone est '06 64 58 54 36'. Proposons pour cela une fonction `recherche` qui admet comme paramètre `telephone` qui parcourt l'ensemble des contacts de notre table à la recherche de celui qui possède ce numéro de téléphone : 

```Python
def recherche(telephone):
    for contact in table:
        if contact[2]==telephone:
            return contact
>>> print(recherche('06 64 58 54 36'))
['Gascon', 'Robert', '06 64 58 54 36', 'robert.gascon@wanadoo.fr', '08/02/1988', 'Orléans']
```

Remarque : En réalité la plupart des bases de données sont hébergées et gérées par des **serveurs de bases de données** ; on utilise pour cela un logiciel de bases de données comme MySQL (qui utilise un langage SQL). Ce n'est pas l'objet de ce cours, mais une requête SQL filtrant les cliants ayant entre 18 et 25 ans et indiquant leurs nom et adresse, triés par ordre alphabétique, a cette écriture :

```SQL
SELECT nom, adresse FROM clients WHERE age>=18 AND age<=25 ORDER BY nom 
```

### Le Cloud

Le cloud computing désigne l'utilisation de serveurs informatiques distants via un réseau comme Internet. Un **cloud** correspond à un ensemble de matériels et de logiciels, accessibles en permanence, pouvant servir à stocker des données mais aussi à les traiter en bénéficiant d'une importante puissance de calcul.

En plein essor, le cloud computing est en fait utilisé depuis plusieurs décennies. En effet, lorsqu'on se connecte à sa messagerie électronique, il s'agit de cloud computing : les données de notre messagerie sont stockées sur des serveurs distants, sont accessibles à volonté et n'importe où, et peuvent être traitées (tri, filtre des messages, modification des paramètres etc...) grâce à des logiciels présents sur ces serveurs.

Les entreprises utilisent de plus en plus les serveurs cloud, qu'elles louent avec différents services en fonction de leurs besoins (espaces de stockage, système d'exploitation, logiciels). Cette pratique devient de plus en plus courante chez les particuliers. Il est désormais possible gratuitement (ou parfois en payant pour davantage de services) de stocker l'ensemble des photos et vidéos de son smartphone à distance, et même de les synchroniqer avec une tablette ou un ordinateur. De nombreux logiciels collaboratifs se sont également développés permettant par exemple de travailler à plusieurs sur un même document. Enfin, on trouve d'autres applications comme le "cloud gaming" c'est-à-dire le fait de jouer à des jeux en utilisant des serveurs distants : le joueur n'installe pas de jeu sur son ordinateur et les logiciels de jeu tournent sur des serveurs distants. Le cloud computing permet de ne pas investir dans du matériel de stockage et de bénéficier de logiciels et d'une puissance de calcul bien supérieure à ce que pourrait fournir un ordinateur personnel ou un smartphone.

### Enjeux environnementaux

Le volume massif des données générées et traitées (Big Data) nécessite un nombre de plus en plus important de centres de données appelés **datacenters**, c'est-à-dire des bâtiments abritant des serveurs informatiques dédiés au stockage et à l'exploitation des données. C'est un réel enjeu environnemental du fait de leur consommation en métaux rares, en eau (refroidissement des serveurs) et en électricité. On estime que d'ici 2030 la consommation énergétique de l'informatique constituera plus de 20% de la consommation mondiale, dont un tiers attribué aux datacenters.


<img src="Assets/donnees_graphe.jpg" width="1200" height="1200">
