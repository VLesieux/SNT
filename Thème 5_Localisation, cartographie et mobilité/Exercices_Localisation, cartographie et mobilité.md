## Exercices Thème 5 : Localisation, cartographie et mobilité

### Exercice 1

1) Rappeler avec vos mots comment fonctionne le GPS. Quelles sont les informations contenues dans le signal émis par un satellite ? Pourquoi une grande précision dans la mesure du temps est-elle nécessaire ? Il est dit dans la vidéo : " une erreur de 1 millionième de seconde sur le temps mène à une erreur de 300 m ", justifier.

2) En utilisant [Géoportail](https://www.geoportail.gouv.fr/), trouver les coordonnées géographiques (latitude et longitude) du château de Chambord.

3) En utilisant [openStreetMap](https://www.openstreetmap.org/#map=14/45.8359/6.8677), dire ce que l'on peut trouver aux coordonnées (latitude : 45.83267°, longitude : 6.86517°). Il suffit de changer les coordonnées dans l'url.

### Exercice 2

Le lien entre la longitude et le décalage horaire est que la Terre est divisée en 24 fuseaux horaires, chacun couvrant 15 degrés de longitude (car 360°/24h=15°/h). Le temps solaire moyen local (heure locale) est décalé de 1 heure pour chaque tranche de 15 degrés de longitude vers l'est ou vers l'ouest du méridien de Greenwich, qui est le point de référence pour le fuseau horaire GMT (Greenwich Mean Time) ou UTC (Coordinated Universal Time).

1) Compléter la ligne manquante de la fonction `decalage_horaire(ville1,ville2)` pour que le test de la docstring soit validé.  
2) Utiliser le programme pour demander le décalage horaire entre Paris et New York.


```Python
################################ réalisation d'un dictionnaire ########################

localisations={    
"London":(51.509865,-0.1278),
"Hong Kong":(22.302711,114.177216),
"Paris":(48.866667,2.3522),
"New York":(40.712784,-74.005941)
    }

#######################################################################################

def decalage_horaire(ville1,ville2):
    """
    Donne le décalage horaire entre les deux villes
    param : ville 1: str
    param : ville 2: str
    return : str
    >>> decalage_horaire("London","Hong Kong")
    'Le décalage horaire entre Hong Kong et London est de -8 h'
    """
    difference_longitudes=(localisations[ville1][1]-localisations[ville2][1])
    time_zone_difference=...................................................
    phrase="Le décalage horaire entre "+ville2+" et "+ville1+" est de "+str(time_zone_difference)+" h"
    return phrase


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
```

**Indications** : Pour arrondir, utiliser `round()`

```Python
>>> round(1.67)
2
```

Dans ce programme, on a réalisé un **dictionnaire** appelé `localisations` qui associe à une ville (une clé) un tuple correspondant à ses coordonnées géographiques (sa valeur).

```Python
>>> localisations["London"]
(51.509865, -0.1278)#renvoie le tuple associé à la clé "London"
>>> localisations["London"][0]#renvoie la première valeur du tuple, c'est-à-dire la latitude de la ville
51.509865
>>> localisations["London"][1]#renvoie la deuxième valeur du tuple, c'est-à-dire la longitude de la ville
-0.1278
```


### Exercice 3

Il y a plus de 2000 ans, le scientifique et philosophène grec Ératosthène invente la discipline de la géographie dont le terme est encore utilisé aujourd'hui ; il a même réussi à estimer la circonférence de la Terre.

Pour cela il a constaté qu'à midi à Syène (aujourd’hui Assouan en Égypte) les rayons du Soleil sont à la verticale (un puits creusé en donne une preuve expérimentale car il est éclairé tout entier). Le même jour à la même heure, à Alexandrie, ville située quasiment sur le même méridien (à 3° de longitude près), les rayons lumineux forment un angle α de 7,2° avec un bâton planté verticalement.
De plus il sait que les caravanes de chameaux partant de Syène mettent 50 jours pour arriver à Alexandrie en parcourant 100 stades par jour (un stade équivaut à 160m).  


<img width="600" height="400" src="Assets/Erathosthene.png">

1. En utilisant l'égalité des angles alternes et internes, donner l'expression de la circonférence P de la Terre en fonction de l'angle α et de la longueur s de l'arc qui joint A à S. On rappelle que **la longueur s d'un arc de cercle de rayon R sous-tendu par un angle α est donnée par la relation : s=R·α à condition d'exprimer α en radian. On rappelle que π=180° ; on retrouve ainsi l'expression bien connue du périmètre d'un cercle : p=2π·R.**
2. Donner la valeur de la circonférence de la Terre calculée par Ératosthène. 
3. Estimer l'erreur relative commise, exprimée en pourcentage, en utilisant la valeur connue du rayon moyen de la Terre : 6 371 km. Le pourcentage d'erreur relative entre une valeur expérimentale e<sub>exp</sub> et une valeur théorique e<sub>théo</sub> est donné par : 100×|e<sub>exp</sub>-e<sub>théo</sub>|/e<sub>théo</sub>.

```Python
import math

rayon_terre_theorique=6371#en km

def mesure_rayon_terre(distance_entre_villes,angle_en_degre):
    """
    Renvoie la valeur du rayon de la Terre déterminée
    à partir de la mesure de l'angle et de la mesure de la distance
    ainsi que l'erreur relative par rapport à la valeur théorique
    param : angle_en_degre : float
    param : distance_entre_villes : float
    return : tuple
    >>> mesure_rayon_terre(800,7.2)
    (6366.197723675813, 0.07537712014106114)
    """
    angle_en_radian=math.pi*(angle_en_degre/180)
    rayon_terre=......................
    erreur_relative=(abs(rayon_terre-rayon_terre_theorique)/rayon_terre_theorique)*100
    return rayon_terre,erreur_relative

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
```

### Exercice 4

Compléter la fonction `calcule_distance` ci-dessous telle que si un satellite a envoyé à l'instant t1 un signal, qui ensuite a été reçu à l'instant t2 par un récepteur, `distance(t1,t2)` renvoie la distance entre le satellite et le récepteur exprimée en km.
Les dates t1 et t2 sont données en heure UTC.     

exemple : 064036.261116 signifie que la trame a été envoyée à 06 h 40 min 36.261116 s.      

On donne la valeur exacte de la célérité de la lumière : c=299 792.458 km/s.

On pourra expliquer pourquoi la célérité de la lumière est communément donnée en physique avec 3 chiffres significatifs sous la forme : c=3.00×10<sup>8</sup> m.s<sup>-1</sup>.

```Python

c=299792.458#km/s

def calcule_distance(t1,t2):
    """
    Renvoie la distance en km calculée à partir de la date d'émission t1 du signal
    émis par le satellite et la date t2 de réception du calculateur du G.P.S
    C'est la distance qui nous sépare du satellite
    param : t1 : float
    param : t2 : float
    return : float
    >>> calcule_distance(064036.261116,064036.3284959)
    20199.98584068947
    """
	pass

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

**Indications :** passer par le calcul d'une variable `duree`, puis par le calcul d'une variable `distance` que l'on retournera. 

### Exercice 5

En utilisant [Géoportail](https://www.geoportail.gouv.fr/) et l'outil "mesurer une distance", trouver la distance à vol d'oiseau de la Tour Eiffel à l'Arc de Triomphe.

Latitude de Eiffel Tower :	48.858370.  
Longitude de Eiffel Tower : 2.294481. 

Latitude de arc de triomphe :	48.873792.   
Longitude de arc de triomphe : 2.295028. 

<img src="Assets/Calcul_distance.png">

La démonstration du calcul de la distance à vol d'oiseau à partir des latitudes et longitudes peut se faire aisément en exprimant le [produit scalaire](Assets/produit_scalaire.md) de deux manières différentes. Vérifier sa compréhension sur un [exemple](Assets/exemple.md) simple.

Voir la [démonstration](Assets/demonstration_distance.md).

Le programme ci-dessous a pour but de déterminer la distance à vol d'oiseau entre deux positions en utilisant la méthode explicitée précédemment ; compléter les lignes manquantes.

```Python
import math

PI=math.pi

R=6378137

def conversion_degre_radian(angle):
    """
    Convertit un angle exprimé en degré en radian (proportionnalité)
    >>> conversion_degre_radian(180)
    3.141592653589793
    """
    return ...................

def calcul_distance_a_vol_d_oiseau(A,B):
    """
    Calcule la distance en m entre deux points A et B à partir de leurs coordonnées géographiques
    param : A : tuple : doublet (latitude, longitude)
    param : B : tuple : doublet (latitude, longitude)
    return : float
    >>> calcul_distance_a_vol_d_oiseau((48.858370,2.294481),(48.873792,2.295028))
    1717.236416494379
    """
    dλ=conversion_degre_radian(B[1])-conversion_degre_radian(A[1])
    θ=math.acos(math.sin(conversion_degre_radian(A[0]))*math.sin(conversion_degre_radian(B[0]))+math.cos(conversion_degre_radian(A[0]))*math.cos(conversion_degre_radian(B[0]))*math.cos(dλ))
    d=..............
    return d

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

```

En déduire la distance à vol d'oiseau entre ces deux villes : Lille : (50.636565,3.063528) - Dunkerque : (51.034771,2.377253)

Retrouver le résultat à cette [adresse](https://www.coordonnees-gps.fr/distance).


### Exercice 6

Donner l'heure et les coordonnées d'acquisition de la trame NMEA 0183 suivante :
'$GPGLL,4835.07,N,235.47,E,203712,A'

Compléter la fonction `exploitation_trame` définie ci-dessous : 

```Python

def exploitation_trame(trame):
    """
    Renvoie l'heure, la latitude et la longitude à partir de la trame
    param : trame : string
    return : string
    >>> exploitation_trame("$GPGLL,4916.45,N,12311.12,W,225444,A")
    'position géographique : latitude : 49 deg. 16.45 min. N ; longitude : 123 deg. 11.12 min. W ; acquisition : 22:54:44 UTC'
    """
    valeurs=trame.split(',')
    latitude=valeurs[1]
    degre_latitude=latitude[:-5]
    minute_latitude=latitude[-5:]
    longitude=valeurs[3]
    degre_longitude=............
    minute_longitude=...........
    date=valeurs[5]
    heure=date[0:2]
    minute=...........
    seconde=............
    texte='position géographique : latitude : '+degre_latitude+' deg. '+ minute_latitude+' min. '+ valeurs[2]+' ; longitude : '+ degre_longitude +' deg. '+minute_longitude+' min. '+valeurs[4]+' ; acquisition : '+heure+':'+minute+':'+seconde+' UTC'
    return texte
  
    
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
  
```

**Indications :**

- Pour transformer une chaîne de caractères en liste en utilisant un séparateur, afin d'en prélever ensuite un élement

```Python
>>> "poisson,chien,chat".split(",")
['poisson', 'chien', 'chat']
>>> "poisson,chien,chat".split(",")[1]
'chien'
```

- Pour extraire une partie d'une chaîne de caractères à l'aide d'une découpe ou `slicing`

```Python
>>> "poisson"[3:5]
'ss'
>>> "poisson"[3:]
'sson'
>>> "poisson"[:3]
'poi'
>>> "poisson"[-3:]
'son'
>>> "poisson"[:-3]
'pois'
```

- Pour accoler ou concaténer plusieurs morceaux de texte, utiliser l'opérateur + :

```Python
>>> "requin"+"-"+"marteau"
'requin-marteau'
```

### Exercice 7

1) Déterminer "au jugé" le ou les plus courts chemin de A (sommet 0) à B (somme 4) dans le graphe suivant. Chaque arête possède une longueur qui pourrait être exprimée en km dans le cas d'un réseau routier. Donner également la longueur de ce plus court chemin.

<img width="600" height="300" src="Assets/chemin_plus_court.png">

2) Utiliser l'**algorithme de Dijkstra** explicité sur un exemple dans ce document Word : [Tableau.doc](Assets/Tableau.doc) pour retrouver le résultat précédent.
    
On peut résumer ainsi la construction du tableau : pour passer d'une ligne à l'autre, on détermine le sommet à marquer en retenant le sommet pour lequel on a la plus petite distance (False représente une distance infinie), puis pour chacune des colonnes des sommets non marqués, on écrit la distance (si elle existe, sinon False) entre le sommet marqué et le sommet non marqué si, après addition de la retenue, celle-ci est **strictement inférieure** à la valeur inscrite dans la ligne précédente ; on précise également la provenance correspondant au sommet marqué.
Pour obtenir le résultat final, on part du sommet d'arrivée et on remonte en passant par les provenances.

3) L'implémentation en Python de cet algorithme est donnée ci-dessous : on y retrouvera la construction du tableau dans `ajout_ligne(T,S_marques,Graphe)` puis dans `calcule_tableau(Graphe, depart)`.

```Python
#  Implémentation  de  l’algorithme  de  Dijkstra

#  Graphe 1 est le graphe correspondant à l'exemple du document ; il faudra donc l'adapter à notre exemple

Graphe1 = [
          [0,2,5,False,3,False,False],
          [2,0,2,1,False,False,8],
          [5,2,0,1,4,2,False],
          [False,1,1,0,False,False,5],
          [3,False,4,False,0,False,False],
          [False,False,2,False,False,0,1],
          [False,8,False,5,False,1,False]
          ]

def SommetSuivant(T, S_marques) :
    """
    En  considérant  un  tableau  et  un  ensemble  de  sommets  marqués, détermine  le  prochain  sommet  marqué.
    param : T : list
    param : S_marques : list
    return : int
    >>> T=[[False, [2, 0], [5, 0], False, [3, 0], False, False],[False, False, [4, 1], [3, 1], [3, 0], False, [10, 1]]]
    >>> S_marques=[0,1]
    >>> SommetSuivant(T, S_marques)
    3
    """
    L = T[-1]
    n = len(L)
#  minimum  des  longueurs,  initialisation
    minimum = False
    for i in range(n) :
        if not(i in S_marques) :
#  si  le  sommet  d’indice  i  n’est  pas  marqué
            if L[i]:
                if not(minimum) or L[i][0] < minimum :
#  on  trouve  un  nouveau  minimum
#  ou  si  le  minimum  n’est  pas  défini
                    minimum = L[i][0]
                    marque = i
    return(marque)

def ajout_ligne(T,S_marques,Graphe) :
    """
    Ajoute  une  ligne  supplémentaire  au  tableau
    param : T : list
    param : S_marques : list
    param : Graphe : list
    return : list, list    
    """
    L = T[-1]
    n = len(L)
#  La  prochaine  ligne  est  une  copie  de  la  précédente, #  dont  on  va  modifier  quelques  valeurs.
    Lnew = L.copy()
#  sommet  dont  on  va  étudier  les  voisins
    S = S_marques[-1]
#  la  longueur  du  (plus  court)  chemin  associé
    retenue = L[S][0]
######################## Code à interpréter ###########################
    for j in range(n) :
        if j not in S_marques:
            poids = Graphe[S][j]
            if poids :
                if not(L[j]) :
                    Lnew[j] = [ retenue + poids, S ]
                else :
                    if retenue + poids < L[j][0]:
                        Lnew[j] = [ retenue + poids, S ]
    T.append(Lnew)
#######################################################################
#  Calcul  du  prochain  sommet  marqué
    S_marques.append(SommetSuivant(T, S_marques))
    return T, S_marques

def calcule_tableau(Graphe, depart) :
    """
    Calcule  le  tableau  de  l’algorithme  de  Dijkstra
    param : Graphe : list
    param : depart : int
    return : list
    """
    n = len(Graphe)
#  Initialisation  de  la  première  ligne  du  tableau
#  Avec  ces  valeurs,  le  premier  appel  à  ajout_ligne
#  fera  le  vrai  travail  d’initialisation
    T=[[False] *n]
    T[0][depart] = [depart, 0]
#  liste  de  sommets  marques
    S_marques = [ depart ]
    while len(S_marques) < n :
        T, S_marques = ajout_ligne(T, S_marques, Graphe)
    return T

def plus_court_chemin(Graphe, depart, arrivee) :
    """
    Détermine  le  plus  court  chemin  entre  depart  et  arrivee  dans le  Graphe
    param : Graphe : list
    param : depart : int
    param : arrivee : int
    return : list
    >>> plus_court_chemin(Graphe1,0,6)
    [0, 1, 2, 5, 6]
    """
    n = len(Graphe)
#  calcul  du  tableau  de  Dijkstra
    T = calcule_tableau (Graphe,depart)
#  liste  qui  contiendra  le  chemin  le  plus  court,  on  place  l’arrivée
    C = [ arrivee ]
    while C[-1] != depart :
        C.append( T[-1][C[-1]][1] )
#  Renverse  C,  pour  qu’elle  soit  plus  lisible
    C.reverse()
    return C

def distance_deux_points(Graphe,i,j):
    """
    Renvoie la distance entre deux sommets i et j
    param : Graphe : list
    param : i : int
    param : j : int
    return : int
    >>> distance_deux_points(Graphe1,0,2)
    5
    """
    pass

def distance_totale(Graphe,i,j):
    """
    Renvoie la distance correspondant au chemin le plus court du sommet i au sommet j
    param : Graphe : list
    param : i : int
    param : j : int
    return : list
    >>> distance_totale(Graphe1,0,6)
    7
    """
    pass
    

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)    
 
```

Ajouter deux fonctions à ce programme : `distance_deux_points(graphe,i,j)` et `distance_totale(graphe,liste)` pour que le programme retourne la longueur du chemin le plus court. Le programme sera validé par les tests fournis dans les docstrings.

**Indication:**

```Python
>>> Graphe1 = [
          [0,2,5,False,3,False,False],
          [2,0,2,1,False,False,8],
          [5,2,0,1,4,2,False],
          [False,1,1,0,False,False,5],
          [3,False,4,False,0,False,False],
          [False,False,2,False,False,0,1],
          [False,8,False,5,False,1,False]
          ]
>>> Graphe1[1][6]
8
```
4) Après avoir défini `Graphe2` dans votre programme, retrouvez les résultats de la question 1. Indiquer par écrit les instructions passées dans la console.

