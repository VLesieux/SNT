On trouve énormément de données sur internet. Une partie de ces données sont publiques, par exemple le site data.gouv.fr récence un grand nombre de données publiques. Ces données sont librement réutilisables.

**À faire vous-même 1**

Afin de découvrir ce qu'est "**l'open data**", nous allons utiliser le site [data.gouv.fr](https://www.data.gouv.fr/fr/).

Résumez en quelques lignes ce que vous aurez appris en lisant la [page suivante](https://doc.data.gouv.fr/).

**À faire vous-même 2**

Explorez pendant quelques minutes le site [data.gouv.fr](https://www.data.gouv.fr/fr/). 
Recherchez les données "Opérations coordonnées par les CROSS" à l'aide du moteur de recherche proposé par le site.

Vous pouvez constater que ces données sont au **format csv**.

Le format csv est très courant sur internet, nous allons l'étudier en premier.

Voici ce que nous dit Wikipédia sur le format CSV :

**C**omma-**s**eparated **v**alues, connu sous le sigle CSV, est un format informatique ouvert représentant des données tabulaires sous forme de valeurs séparées par des virgules.

Un fichier CSV est un fichier texte, par opposition aux formats dits « binaires ». Chaque ligne du texte correspond à une ligne du tableau et les virgules correspondent aux séparations entre les colonnes. Les portions de texte séparées par une virgule correspondent ainsi aux contenus des cellules du tableau.

Voici un exemple du contenu d'un fichier CSV :

```csv
nom,prenom,date_naissance
Durand,Jean-Pierre,23/05/1985
Dupont,Christophe,15/12/1967
Terta,Henry,12/06/1978
```

Je pense qu'il est évident pour vous que nous avons ici 3 personnes :

    Jean-Pierre Durand qui est né le 23/05/1985
    Christophe Dupont qui est né le 15/12/1967
    Henry Terta qui est né le 12/06/1978

"nom", "prenom" et "date_naissance" sont appelés des descripteurs alors que, par exemple, "Durand", "Dupont" et "Terta" sont les valeurs du descripteur "nom".

**À faire vous-même 3**

Donnez les différentes valeurs du descripteur "date_naissance".

ATTENTION :

La virgule est un standard pour les données anglo-saxonnes, mais pas pour les données aux normes françaises. En effet, en français, la virgule est le séparateur des chiffres décimaux. Il serait impossible de différencier les virgules des décimaux et les virgules de séparation des informations. C’est pourquoi on utilise un autre séparateur : le point-virgule (;). Dans certains cas cela peut engendrer quelques problèmes, vous devrez donc rester vigilants sur le type de séparateur utilisé.

Les tableurs, tels que "Calc" (Libre Office), sont normalement capables de lire les fichiers au format CSV. J'ai précisé "normalement" car certains tableurs gèrent mal le séparateur CSV "point-virgule" et le séparateur des chiffres décimaux "virgule".
; 
**À faire vous-même 4**

Après avoir téléchargé le fichier `ident_pointVirgule.csv` dans le dossier assets, ouvrez ce dernier à l'aide d'un tableur.

Si par hasard votre tableur ne gère pas correctement le fichier avec le séparateur "point-virgule", voici une version "séparateur virgule" du fichier : ident_virgule.csv

Dans la suite, gardez toujours cet éventuel problème à l'esprit (surtout avec des données "made in France")

Vous devriez obtenir ceci :

![Programme officiel ](assets/snt_donnee_1.png)

Vous pouvez constater que les données sont bien "rangées" dans un tableau avec des lignes et des colonnes ; voilà pourquoi on parle de **données tabulaires**.

Il est possible de trouver sur le web des données beaucoup plus intéressantes à traiter que celles contenues dans le fichier "ident_pointVirgule.csv" (ou "ident_virgule.csv"). Par exemple, le site [sql.sh](https://sql.sh/736-base-donnees-villes-francaises), propose un fichier csv contenant des informations sur l'ensemble des communes françaises.

**À faire vous-même 5**

Ouvrez le fichier `ville_point_virgule.csv` dans le dossier assets à l'aide d'un tableur (c’est une version légèrement modifiée de celle disponible sur le site sql.sh, j’y ai notamment ajouté des entêtes). En cas de problème avec votre tableur, voici une version "séparateur virgule" : ville_virgule.csv (attention le séparateur "décimal" est ici le point)

Comme vous pouvez le constater, nous avons 12 colonnes (et 36700 lignes si on ne compte pas l'entête !), voici la signification de ces colonnes :

    dep : numéro de département
    nom : nom de la commune
    cp : code postal
    nb_hab_2010 : nombre d'habitants en 2010
    nb_hab_1999 : nombre d'habitants en 1999
    nb_hab_2012 : nombre d'habitants en 2012 (approximatif)
    dens : densité de la population (habitants par kilomètre carré)
    surf : superficie de la commune en kilomètre carré
    long : longitude
    lat : latitude
    alt_min : altitude minimale de la commune (il manque des données pour certains territoires d'outre-mer)
    alt_max : altitude maximale de la commune (il manque des données pour certains territoires d'outre-mer)

**À faire vous-même 6**

En vous aidant du fichier ouvert dans le "À faire vous-même 4", déterminez l'altitude maximale et l'altitude minimale de votre commune.

Autre format de données très courant sur le "web", le **format JSON** (JavaScript Object Notation).

Le JSON fonctionne avec un système de paire clé/valeur.

Un "objet" est encadré par des accolades :


{cle_1 : val_1, cle_2 : val_2, cle_3 : val_3}
		

souvent, pour une question de lisibilité, on écrira :


{
cle_1 : val_1,
cle_2 : val_2,
cle_3 : val_3
}
		

Un fichier au format JSON peut regrouper un grand nombre d'objets :


[{
"nom" : "Durand",
"prenom" : "Jean-Pierre",
"date_naissance" : "23/05/1985"
},
{
"nom" : "Dupont",
"prenom" : "Christophe",
"date_naissance" : "15/12/1967"
},
{
"nom" : "Terta",
"prenom" : "Henry",
"date_naissance" : "12/06/1978"
}]
		

Ci-dessus, nous avons une liste (délimité par [ ]) contenant des objets.

La "valeur" d'une paire "clé/valeur" peut être une liste :


{
"nom" : "Durand",
"prenom" : "Jean-Pierre",
"date_naissance" : "23/05/1985"
"sport" : ["tennis", "football", "pétanque"]
}
		
ou même un autre objet :

{
"nom" : "Durand",
"prenom" : "Jean-Pierre",
"date_naissance" : "23/05/1985"
"adresse" : {"num":6, "rue":"impasse du rossignol", "ville":"Nogent-le-Rotrou", "cp":"28400"}
}
		 

Comme vous pouvez le constater, il est possible d'obtenir des structures de données très complexes avec le format JSON.

**À faire vous-même 7**

Téléchargez le fichier ident.json dans le dossier assets et ouvrez-le à l'aide d'un éditeur de texte.

De nombreux sites web proposent des services basés sur des **API** (Application Programming Interface). Ces sites sont capables de fournir des données aux formats JSON sur "simple demande". Souvent, ces "demandes" sont effectuées par l'intermédiaire d'une url.

Nous allons illustrer ce propos en utilisant l'API d'un site qui fournit des informations météo au format JSON. Vous trouverez ce site à l'adresse suivante : openweathermap.org/api

Pour profiter de ce service, il est nécessaire d'obtenir une clé (API key : 7afbb16d80ba500faebc6ec2cddd08ff).

**À faire vous-même 8**

Ouvrez votre navigateur préféré et copiez-collez l'url suivante dans la barre d'adresse du navigateur :

http://api.openweathermap.org/data/2.5/weather?q=bonneville,fr&lang=fr&units=metric&APPID=XXXXXXXXXXXXX

ATTENTION : il faut remplacer les "X" par la clé (API key) qui vous aura été fournie

Au lieu d'obtenir, comme d'habitude, une page web, vous devriez obtenir uniquement quelque chose qui ressemblera à ceci :


{"coord":{"lon":6.41,"lat":46.08},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"base":"stations","main":{"temp":12.31,"pressure":1026,"humidity":58,"temp_min":11,"temp_max":14},"visibility":10000,"wind":{"speed":2.6,"deg":200},"clouds":{"all":0},"dt":1540373400,"sys":{"type":1,"id":5570,"message":0.0046,"country":"FR","sunrise":1540361039,"sunset":1540398737},"id":3031679,"name":"Bonneville","cod":200}
		

Comme les données sont réactualisées relativement souvent, vous n'obtiendrez pas la même chose que moi !

Avec une simple url, le site open weather renvoie des informations météo sous forme de données JSON.

Détaillons l'url :


http://api.openweathermap.org/data/2.5/weather
		

Cette partie de l'url ne changera pas (sauf si vous désirez autre chose que les conditions météo actuelles, à ce moment-là, il faudra remplacer "weather" par autre chose (consulter le site open weather pour plus d'informations)).


?q=bonneville,fr&lang=fr&units=metric&APPID=XXXXXXXXXXXXX
		

À partir du point d'interrogation, vous devez renseigner les différents paramètres qui permettront à open weather de vous renvoyer les bonnes informations. Ces paramètres sont séparés par le caractère "&".

    "q=bonneville,fr" le paramètre "q" correspond au nom de la ville suivi du pays (fr dans notre cas)
    "lang=fr" la langue utilisée sera le français
    "units=metric" on désire avoir les longueurs en mètres (et les vitesses en mètre par seconde).
    "APPID" correspond à l'API key

Il est possible de construire des requêtes beaucoup plus complexes, encore une fois, veuillez consulter le site open weather pour plus d'informations.

Intéressons-nous maintenant aux données JSON renvoyées (nous n'allons pas tout détailler) :

    "coord":{"lon":6.41,"lat":46.08} latitude et longitude du lieu
    "weather":[{"id":800,"main":"Clear","description":"ensoleillé","icon":"01d"}] "weather" correspond à un tableau qui contient un seul objet.
    "main":{"temp":17.35,"pressure":1016,"humidity":59,"temp_min":16,"temp_max":19} "main" correspond à un objet qui contient différents types d'informations
    "dt":1443975257 "dt" nous donne l'heure et la date de diffusion du bulletin au format "timestamp" (voir en bas de cette page pour plus d'informations sur le format "timestamp")
    "sunrise":1443937018,"sunset":144397849 : respectivement heure de lever et de coucher du soleil au format timestamp

Dernier format de données que nous verrons aujourd'hui le geoJSON. 

Le **format geoJSON** est un format (http://geojson.org/) qui permet d'encoder des données à "caractère géographique". Voici ce que dit Wikipédia à propos de ce format :

    GeoJSON (de l'anglais Geographic JSON, signifiant littéralement JSON géographique) est un format ouvert d'encodage d'ensemble de données géospatiales simples utilisant la norme JSON (JavaScript Object Notation). Il permet de décrire des données de type point, ligne, chaîne de caractères, polygone, ainsi que des ensembles et sous-ensembles de ces types de données et d'y ajouter des attributs d'information qui ne sont pas spatiale. Le format GeoJSON, contrairement à la majorité des standards de systèmes d'informations géographiques, n'est pas écrit par l'Open Geospatial Consortium, mais par un groupe de travail de développeurs au travers d'internet.

Comme indiqué dans Wikipédia, le geoJSON est avant tout du JSON, nous retrouverons donc les mêmes caractéristiques que le JSON (système de clé/valeur).

**À faire vous-même 9**

Dans la barre d'adresse de votre navigateur, tapez l'adresse suivante :


https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2019-07-31&endtime=2019-08-01
		

Vous devriez obtenir quelque chose ressemblant à ceci :

```json
			{"type":"FeatureCollection","metadata":{"generated":1564685404000,"url":"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2019-07-31&endtime=2019-08-01","title":"USGS Earthquakes","status":200,"api":"1.8.1","count":547},"features":[{"type":"Feature","properties":{"mag":0.33000000000000002,"place":"6km NW of The Geysers, CA","time":1564617341320,"updated":1564619343353,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/nc73239641","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=nc73239641&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":2,"net":"nc","code":"73239641","ids":",nc73239641,","sources":",nc,","types":",geoserve,nearby-cities,origin,phase-data,scitech-link,","nst":7,"dmin":0.012579999999999999,"rms":0.029999999999999999,"gap":78,"magType":"md","type":"earthquake","title":"M 0.3 - 6km NW of The Geysers, CA"},"geometry":{"type":"Point","coordinates":[-122.80266570000001,38.819168099999999,3.29]},"id":"nc73239641"},
{"type":"Feature","properties":{"mag":1.28,"place":"22km ESE of Little Lake, CA","time":1564617244070,"updated":1564617457582,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/ci38678103","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=ci38678103&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":25,"net":"ci","code":"38678103","ids":",ci38678103,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,scitech-link,","nst":18,"dmin":0.085260000000000002,"rms":0.11,"gap":94,"magType":"ml","type":"earthquake","title":"M 1.3 - 22km ESE of Little Lake, CA"},"geometry":{"type":"Point","coordinates":[-117.684166,35.867000599999997,3.4300000000000002]},"id":"ci38678103"},
{"type":"Feature","properties":{"mag":1.3,"place":"19km NW of Sutton-Alpine, Alaska","time":1564617217896,"updated":1564617408500,"tz":-540,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/ak0199qzxzh9","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=ak0199qzxzh9&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":26,"net":"ak","code":"0199qzxzh9","ids":",ak0199qzxzh9,","sources":",ak,","types":",geoserve,origin,","nst":null,"dmin":null,"rms":0.35999999999999999,"gap":null,"magType":"ml","type":"earthquake","title":"M 1.3 - 19km NW of Sutton-Alpine, Alaska"},"geometry":{"type":"Point","coordinates":[-149.07429999999999,61.939900000000002,21.5]},"id":"ak0199qzxzh9"},
{"type":"Feature","properties":{"mag":1.72,"place":"9km ENE of Coso Junction, CA","time":1564617174330,"updated":1564617402129,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/ci38678087","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=ci38678087&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":46,"net":"ci","code":"38678087","ids":",ci38678087,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,scitech-link,","nst":14,"dmin":0.050310000000000001,"rms":0.13,"gap":132,"magType":"ml","type":"earthquake","title":"M 1.7 - 9km ENE of Coso Junction, CA"},"geometry":{"type":"Point","coordinates":[-117.85550000000001,36.067166700000001,2.04]},"id":"ci38678087"},
{"type":"Feature","properties":{"mag":1.2,"place":"27km SSW of Hawthorne, Nevada","time":1564616847761,"updated":1564625189016,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/nn00698301","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=nn00698301&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"reviewed","tsunami":0,"sig":22,"net":"nn","code":"00698301","ids":",nn00698301,","sources":",nn,","types":",geoserve,origin,phase-data,","nst":10,"dmin":0.16700000000000001,"rms":0.1709,"gap":129.69,"magType":"ml","type":"earthquake","title":"M 1.2 - 27km SSW of Hawthorne, Nevada"},"geometry":{"type":"Point","coordinates":[-118.7396,38.291699999999999,7.2000000000000002]},"id":"nn00698301"},
{"type":"Feature","properties":{"mag":2.6000000000000001,"place":"58km N of Hatillo, Puerto Rico","time":1564616626170,"updated":1564638696895,"tz":-240,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/pr2019212018","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2019212018&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"reviewed","tsunami":0,"sig":104,"net":"pr","code":"2019212018","ids":",pr2019212018,","sources":",pr,","types":",geoserve,origin,phase-data,","nst":11,"dmin":0.60919999999999996,"rms":0.53000000000000003,"gap":268,"magType":"md","type":"earthquake","title":"M 2.6 - 58km N of Hatillo, Puerto Rico"},"geometry":{"type":"Point","coordinates":[-66.820800000000006,19.0121,50]},"id":"pr2019212018"},
{"type":"Feature","properties":{"mag":1.3700000000000001,"place":"19km NW of Fillmore, CA","time":1564616617590,"updated":1564616843518,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/ci38678055","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=ci38678055&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":29,"net":"ci","code":"38678055","ids":",ci38678055,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,scitech-link,","nst":6,"dmin":0.2787,"rms":0.29999999999999999,"gap":153,"magType":"ml","type":"earthquake","title":"M 1.4 - 19km NW of Fillmore, CA"},"geometry":{"type":"Point","coordinates":[-119.05549999999999,34.530833299999998,2.98]},"id":"ci38678055"},
{"type":"Feature","properties":{"mag":1.3400000000000001,"place":"8km NNE of Coso Junction, CA","time":1564616476700,"updated":1564616704978,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/ci38678039","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=ci38678039&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":28,"net":"ci","code":"38678039","ids":",ci38678039,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,scitech-link,","nst":12,"dmin":0.036769999999999997,"rms":0.14999999999999999,"gap":167,"magType":"ml","type":"earthquake","title":"M 1.3 - 8km NNE of Coso Junction, CA"},"geometry":{"type":"Point","coordinates":[-117.89916669999999,36.109499999999997,1.8500000000000001]},"id":"ci38678039"},
{"type":"Feature","properties":{"mag":0.40000000000000002,"place":"27km SSW of Hawthorne, Nevada","time":1564616385958,"updated":1564625185644,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/nn00698300","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=nn00698300&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"reviewed","tsunami":0,"sig":2,"net":"nn","code":"00698300","ids":",nn00698300,","sources":",nn,","types":",geoserve,origin,phase-data,","nst":4,"dmin":0.17599999999999999,"rms":0.086400000000000005,"gap":282.31999999999999,"magType":"ml","type":"earthquake","title":"M 0.4 - 27km SSW of Hawthorne, Nevada"},"geometry":{"type":"Point","coordinates":[-118.72329999999999,38.289700000000003,9]},"id":"nn00698300"},
{"type":"Feature","properties":{"mag":0.20000000000000001,"place":"27km SSW of Hawthorne, Nevada","time":1564616363045,"updated":1564625185553,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/nn00698299","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=nn00698299&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"reviewed","tsunami":0,"sig":1,"net":"nn","code":"00698299","ids":",nn00698299,","sources":",nn,","types":",geoserve,origin,phase-data,","nst":4,"dmin":0.17199999999999999,"rms":0.054300000000000001,"gap":281.20999999999998,"magType":"ml","type":"earthquake","title":"M 0.2 - 27km SSW of Hawthorne, Nevada"},"geometry":{"type":"Point","coordinates":[-118.7176,38.290300000000002,9.8000000000000007]},"id":"nn00698299"},
{"type":"Feature","properties":{"mag":0.20000000000000001,"place":"27km SSW of Hawthorne, Nevada","time":1564616227368,"updated":1564618837595,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/nn00698298","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=nn00698298&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"reviewed","tsunami":0,"sig":1,"net":"nn","code":"00698298","ids":",nn00698298,","sources":",nn,","types":",geoserve,origin,phase-data,","nst":4,"dmin":0.17599999999999999,"rms":0.0717,"gap":282.49000000000001,"magType":"ml","type":"earthquake","title":"M 0.2 - 27km SSW of Hawthorne, Nevada"},"geometry":{"type":"Point","coordinates":[-118.72329999999999,38.289099999999998,9.0999999999999996]},"id":"nn00698298"},
{"type":"Feature","properties":{"mag":2.79,"place":"14km ENE of Ridgecrest, CA","time":1564615822760,"updated":1564644771698,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/ci38678031","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=ci38678031&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":120,"net":"ci","code":"38678031","ids":",ci38678031,","sources":",ci,","types":",focal-mechanism,geoserve,nearby-cities,origin,phase-data,scitech-link,","nst":38,"dmin":0.047059999999999998,"rms":0.13,"gap":36,"magType":"ml","type":"earthquake","title":"M 2.8 - 14km ENE of Ridgecrest, CA"},"geometry":{"type":"Point","coordinates":[-117.53400000000001,35.659500000000001,9.6500000000000004]},"id":"ci38678031"},
{"type":"Feature","properties":{"mag":0.20000000000000001,"place":"27km SSW of Hawthorne, Nevada","time":1564615732560,"updated":1564618468033,"tz":-480,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/nn00698297","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=nn00698297&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"reviewed","tsunami":0,"sig":1,"net":"nn","code":"00698297","ids":",nn00698297,","sources":",nn,","types":",geoserve,origin,phase-data,","nst":4,"dmin":0.17799999999999999,"rms":0.066900000000000001,"gap":282.25,"magType":"ml","type":"earthquake","title":"M 0.2 - 27km SSW of Hawthorne, Nevada"},"geometry":{"type":"Point","coordinates":[-118.7256,38.291499999999999,7.2999999999999998]},"id":"nn00698297"},
{"type":"Feature","properties":{"mag":1.2,"place":"15km NE of Badger, Alaska","time":1564615237144,"updated":1564616344126,"tz":-540,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/ak0199qzqwsi","detail":"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=ak0199qzqwsi&format=geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":22,"net":"ak","code":"0199qzqwsi","ids":",ak0199qzqwsi,","sources":",ak,","types":",geoserve,origin,","nst":null,"dmin":null,"rms":0.23000000000000001,"gap":null,"magType":"ml","type":"explosion","title":"M 1.2 Explosion - 15km NE of Badger, Alaska"},"geometry":{"type":"Point","coordinates":[-147.32239999999999,64.905799999999999,12.9]},"id":"ak0199qzqwsi"},
			...
```

Vous avez obtenu des informations au format geoJSON, sur les tremblements de Terre ayant eu lieu entre le 31 juillet 2019 et le 01 août 2019, partout dans le monde.

Le site "earthquake.usgs.gov", comme le site "http://openweathermap.org/", propose une API qui renvoie des données à partir d'une simple url. Le site vous propose différentes options pour la requête, vous trouverez une description complète de ces options [ici](https://earthquake.usgs.gov/fdsnws/event/1/).


Attention, vous aurez un message d'erreur si votre requête renvoie plus de 20000 événements

**À faire vous-même 10**

En vous aidant de la documentation présente sur le site http://earthquake.usgs.gov, écrivez une requête sous forme d'url qui permettra d'obtenir des données (au format geoJSON) sur les tremblements de terre, d'une magnitude supérieure à 5, ayant eu lieu ces 30 derniers jours partout dans le monde.

Testez votre requête en la copiant dans la barre d'adresse de votre navigateur. Une fois les données obtenues, étudiez-les afin de comprendre la structure de ces données.

ATTENTION : les dates et les heures sont fournies au format "timestamp". Le "timestamp" désigne le nombre de secondes écoulé depuis le 1er janvier 1970 à minuit UTC précise. Au lieu de donner une date et une heure pour un événement donné, il est possible de donner son "timestamp". Par exemple, au lieu de dire l'événement A a eu lieu le 24 octobre 2018 à 13h 11 minutes et 10 secondes, on pourra dire que l'événement A à pour "timestamp" 1540379470 (durée qui s'est écoulé en seconde entre le 1er janvier 1970 à minuit UTC et le 24 octobre 2018 à 13h 11 minutes et 10 secondes). Vous trouverez un convertisseur de timestamp sur ce [site](http://www.timestamp.fr/?).

 Attention, dans le JSON renvoyé par le site "earthquake.usgs.gov" le timestamp est donné en milliseconde, il est donc nécessaire de diviser par 1000 la valeur que vous allez trouver dans le JSON (et garder uniquement la partie entière du résultat de votre division). 