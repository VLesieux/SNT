## Le Web

### Introduction

Le World Wide Web, en français : la toile d'araignée mondiale, a été inventée en 1989 par deux informaticiens : le Britannique Tim Berners Lee et le Belge Robert Caillau, qui travaillaient au CERN (Conseil Européen pour la Recherche Nucléaire situé à cheval sur la frontière franco-suisse) où se trouve actuellement le LHC (Large Hadron Collider : un accélérateur de particules qui accélère des protons ou des ions à une vitesse proche de la vitesse de la lumière). Cette invention a été conçue et développée pour que des scientifiques travaillant dans des universités et instituts du monde entier puissent s'échanger des informations instantanément.

Communément appelé le Web, il permet, grâce à un navigateur, d'accéder aux différents sites et d'échanger par courrier électronique. Il est devenu incontournable dans pratiquement toutes les activités professionnelles ou de loisir.

### Historique

- 1965 : Invention de la notion d'hypertexte par le sociologue américain Ted Nelson
- 1989 : Au CERN, le chercheur britannique Tim Berners-Lee invente le Web. Le premier site web est disponible.
- 1991 : Naissance du langage HTML
- 1993 : Le CERN rend le Web public.
- 1995 : Création des langages JavaScript et PHP, permettant le développement de sites web dynamiques, c'est-à-dire permettant l'intéraction avec l'utilisateur.
- 1998 : Lancement du moteur de recherche Google

### Fonctionnement du Web

Comme on l'a vu dans le thème précédent, Internet est un gigantesque réseau d'ordinateurs connectés entre eux. Au sein de ce réseau, certains de ces ordinateurs appelés **serveurs** mettent à la disposition des ordinateurs clients des **ressources** (texte, image, vidéo..). Par exemple, une page web constitue un exemple de ressource.
Le World Wide Web permet d'accéder à ces ressources par un système de **liens hypertextes**. Un lien hypertexte ou hyperlien est un élément cliquable d'une ressource permettant d'accéder à une autre ressource web en utilisant son **URL**.

Chaque ressource possède ainsi une adresse web appelée **URL** (Uniform Resource Locator) permettant de l'identifier, de la même façon qu'une adresse postale permet de localiser une habitation.

<u>Remarque</u> : ne pas confondre l'adresse IP qui permet d'identifier de façon unique un ordinateur sur le réseau Internet et l'adresse web qui permet d'identifier une ressource sur un serveur.

Une adresse web doit suivre une **syntaxe** bien précise.

Classiquement elle s'écrit de la manière suivante : 

http://www.example.com/dossier_un_tel/page_un_tel.html

- En premier est indiqué le **protocole** (les règles de communication) utilisé pour demander et recevoir la ressource : **HTTP** (Hypertext Transfer Protocol) est le protocole du Web le plus utilisé en particulier pour les pages web, mais il y en existe d'autres : **FTP** (pour échanger des fichiers : File Transfer Protocol ) ou encore **SMTP** (pour envoyer des e-mails : Simple Mail Transfer Protocol).
- www.example.com est le **nom de domaine** de l'ordinateur sur lequel se trouve la ressource. Comme on l'a vu dans le thème précédent, ce nom de domaine est associé à une adresse IP ; c'est le rôle d'un **serveur DNS** d'interpréter le nom de domaine et de renvoyer l'adresse IP correspondante.
- dossier/page.html est le **chemin** de la ressource sur l'ordinateur. Un chemin est constitué des dossiers (ou répertoires) qu'il faut parcourir pour accéder à un certain fichier. Ici la ressource est donc un **fichier** appelé `page_un_tel.html` lui même situé dans le **dossier**intitulé `dossier_un_tel` sur l'ordinateur portant le nom de domaine `www.example.com`.

### Le protocole HTTP

**HTTP** est composé de **requêtes** permettant l'échange de ressources entre un client et un serveur. 
Le protocole **HTTPS** (S signifie secure) est semblable au protocole HTTP sauf que les domaines sont chiffrés : une personne interceptant les communications ne serait pas capable d'en connaître le contenu. Ce protocole est notamment utilisé pour les transactions d'argent et il est indiqué par un cadenas signalé dans le navigateur.

### Navigateur web

Il serait fastidieux de consulter un site web en écrivant des requêtes HTTP. Un **navigateur** web simplifie grandement l'utilisation du Web en envoyant et recevant ces requêtes automatiquement. Il s'occupe aussi de l'affichage graphique des ressources obtenues, de façon plus esthétique que sous forme de simples lignes de texte.
Les navigateurs les plus utilisés sont : Chrome (Google), Safari (Apple), Firefox (Mozilla), Internet Explorer (Microsoft).
La **barre d'adresse** d'un navigateur permet de connaître et de modifier l'URL de la ressource web affichée.

### Moteurs de recherche

Pour accéder à une ressource Web, il faut connaître son URL. Seulement un internaute intéressé par un sujet particulier ne connaît pas, à priori, tous les URL des pages traitant de ce sujet. Un **moteur de recherche** permet de trouver des pages web à partir de **mots-clés**. Les moteurs de recherche sont Google, Baidu, Bing, Yahoo et DuckDuckGo.
Le fonctionnement d'un moteur de recherche comporte trois parties :
1. L'**exploration**, réalisé par un logiciel que l'on appelle **robot**, consiste à visiter des pages web de proche en proche en suivant des hyperliens. Il existe plusieurs façons possibles d'effectuer cette exploration du Web, suivant l'ordre dans lequel les pages sont visitées. Par exemple, un parcours en largeur consiste à partir d'une page puis visiter toutes les pages y étant référencées, puis les pages référencées sur ces dernières...
Certaines pages peuvent ne pas être accessibles lors de cette exploration (par exemple, si aucun lien hypertexte ne pointe dessus) et ne sont donc pas référencées par le moteur de recherche : ces pages forment ce que l'on appelle le **deep web** (web profond en français).
2. L'**indexation** associe à chaque mot-clé l'ensemble des pages en rapport avec ce mot-clé ; cette association entre un mot-clé et un ensemble de pages peut être stockée sous la forme d'un **dictionnaire**. 
Avec Python, on peut créer aisément un tel dictionnaire :

 ```Python
D={'sport':['www.sports.fr','www.lequipe.fr'],'information':['www.20minutes.fr','www.lemonde.fr']}
>>> type(D)
<class 'dict'>    
>>> D['sport']
['www.sports.fr', 'www.lequipe.fr']
>>> D['information']
['www.20minutes.fr', 'www.lemonde.fr']
 ```
Un dictionnaire constitue un **type construit** (de type dict) qui permet d'associer une valeur à une clé. Il est plus pratique qu'une liste où les éléments sont repérés par leur indice de position.
3. La **recherche** est réalisée à partir d'une **requête** sous forme de mots-clés d'un utilisateur. Le moteur de recherche renvoie une liste de pages web triés par ordre de pertinence et de popularité de sorte que les premiers résultats affichés soient les plus susceptibles d'intéresser l'utilisateur.
Les moteurs de recherche utilisent différents moyens pour mesurer la popularité d'une page. Par exemple, Google utilise un **algorithme** appelé **PageRank** qui parcourt le Web en suivant aléatoirement un hyperlien sur chaque page. Ainsi, plus il y a de liens vers une page, plus sa "popularité" est élévée et plus il y a de chances qu'elle soit affichée en premier lors d'une recherche Google.
Il est possible de payer (sous forme d'enchères) pour qu'un site web soit plus souvent en tête de recherches Google. La majeure partie des revenus de Google provient ainsi de cette publicité.  

### Confidentialité et vie privée

Avez-vous déjà reçu des publicités sur différents sites correspondant exactement à la recherche que vous veniez de faire ? Ce n'est pas un hasard : votre navigation sur le Web laisse des traces qui peuvent être collectés par des entreprises. Ces données peuvent ensuite être revendues.
Un **cookie** est un fichier stocké sur l'ordinateur de l'utilisateur et contenant des informations relatives à la navigation sur un site particulier. Le cookie est lu par le site en question à chaque visite.
Par exemple, un cookie peut contenir les paramètres de l'utilisateur, les articles d'un panier d'achat etc..Les cookies sont donc potentiellement utiles pour l'utilisateur.
Un **cookie tiers** est un cookie placé par un publicitaire sur d'autres sites web de façon à suivre un utilisateur et récupérer différentes informations sur lui. Ce type de cookie n'est pas donc utile pour l'utilisateur, sauf éventuellement pour recevoir de la publicité ciblée.
La legislation européenne impose aux sites web de demander à l'utilisateur d'accepter ou non l'utilisation de cookies. 
Avant d'entrer sur le site de Larousse, on trouve affiché : 
<img src="Assets/cookie_larousse.png"> 
Il est possible de voir les cookies sur son propre ordinateur, de les supprimer et de les bloquer.
Dans Firefox, aller dans menu Préférences Vie privée et sécurité.
Sur un ordinateur public, il est vivement conseillé de supprimer les cookies et l'historique de navigation (c'est-à-dire l'ensemble des sites visités).
Il existe également des utilitaires permettant d'éviter les traceurs.

### Sécurité sur le web

Voici certains riques les plus fréquents lorsqu'on navigue sur le Web :
- L'**hameçonnage** (fishing en anglais) consiste à leurrer un internaute à l'aide d'un faux site ou mail pour lui soutirer des données personnelles (numéro de carte bancaire, mot de passe, etc..). Souvent le site en question possède la même apparence que l'original avec une URL très légèrement différente (une lettre en plus par exemple).
Les certificats électroniques peuvent permettre de garentir l'authenticité d'un site web. Lorsqu'un site utilise le protocole HTTPS sans certificat valide, le navigateur web affiche normalement un message d'avertissement. De manière générale, il faut éviter de communiquer des informations sensibles en particulier en l'absence de protocole sécurisé HTTPS ou de certificat valide.
- Certains sites web peuvent essayer d'exécuter un **programme malveillant** sur votre appareil, souvent en demandant de télécharger un fichier exécutable (.exe sous Windows). Ce programme peut contenir un "keylogger" qui enregistre vos frappes de clavier pour récupérer vos mots de passe, un rançongiciel qui chiffre vos fichiers puis demande de l'argent pour pouvoir les récupérer..
Certains de ces programmes tentent de s'exécuter directement dans le navigateur via un langage web comme JavaScript. L'ANSSI (Agence Nationale de Sécurité des Systèmes d'Information) conseille de désactiver Javascript dans la mesure du possible. Récemment, les principaux navigateurs ont décidé de désactiver Flash par défaut qui posait trop de problèmes de sécurité. 


### Développement Web avec HTML

On trouvera [ici](Assets/Creation_page_web.md) une page entièrement consacrée au développement Web avec HTML 5, cela vous permettra de créer votre propre page web.
Pour la diffuser, vous devrez ensuite disposer d'un **hébergeur** ; on peut commencer avec un hébergeur web gratuit tel que alwaysdata. On peut également utiliser un créateur de site web tel que WordPress qui permet de réaliser plus rapidement son site web. Il existe également des logiciels du type WYSIWYG (« what you see is what you get ») qui dispose d'une interface graphique qui permet à l'utilisateur de voir son document tel qu'il sera publié ; l'un des plus connus est Dreamweaver de chez Adobe (payant), toutefois il est bon d'avoir des connaissances de base pour écrire correctement le code d'une page web et être capable d'y apporter des corrections ou des améliorations rapidement.