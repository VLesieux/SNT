
### Pour simuler et comprendre le fonctionnement d'un réseau, utilisez le logiciel gratuit **Filius**


1) Réalisez l'architecture d'un réseau en plaçant deux ordinateurs Portable ; en cliquant sur eux, donnez-leur des noms simples M1 et M2 et des adresses IP simples : 192.168.0.1 et  192.168.0.2 ; les relier par un câble Ethernet puis passer en mode simulation (triangle vert à côté du marteau). 
En cliquant sur une machine, on ouvre une fenêtre qui permet d'utiliser un logiciel sur un ordinateur ; on installe le logiciel Ligne de commande (appliquer les modifications) pour écrire des **lignes de commande** : on utilise la commande **ipconfig** pour vérifier l'adresse IP de la machine ; celle-ci est formée de 4 octets en notation décimale, ainsi que l'adresse MAC de la machine donnée par le constructeur ; celle-ci est formée de 6 octets en notation hexadécimale, puis on envoie un **ping** sur la  machine M2 en renseignant son adresse IP.
Observer que les échanges de packets sont visibles par le changement de couleur du câble réseau. 
<img src="Filius1.png"> 

2) Revenons maintenant à la configuration du réseau (avec le marteau) et supprimons le câble (clic droit sur celui-ci) pour placer un troisième ordinateur M3 d'IP 192.168.0.3 ; connectons les trois ordinateurs à l'aide d'un switch avec trois câbles vers ce switch qui les unifie au sein d'un réseau ; en mode simulation maintenant faire un ping depuis la machine M1 vers la machine M3 en repassant au mode simulation pour vérifier la bonne transmission et la bonne réception de paquets grâce à l'intermédiaire du Switch.  
<img src="Filius2.png"> 

3) Réaliser maintenant deux réseaux comportant chacun trois machines (M1,M2,M3) et (M4,M5,M6) et deux Switch R1 et R2 ; on choisit l'adresse réseau de R1 : 192.168.1.0 et celle de R2 : 192.168.2.0 ; affecter en conséquence les IP des machines affectées à ces réseaux. 
Relier les deux réseaux en connectant les Switch grâce à un Routeur (sélectionner 2 interfaces). En cliquant sur le Routeur, renseigner son adresse IP 192.168.1.254 pour le réseau R1 et 192.168.2.254  pour le réseau R2.
Sélectionner dans l'onglet Général l'option 'Routage automatique' pour que le routeur gère automatiquement les tables de routage ; puis pour chaque machine du réseau R1 et pour chaque machine du réseau R2, renseigner la Passerelle correspondant à l'adresse IP du routeur donnée plus haut.
Testons l'architecture en faisant un ipconfig sur la machine M1 pour voir l'IP du routeur puis en réalisant un ping entre deux machines n'appartenant pas au même réseau; utiliser également la commande traceroute suivi de l'IP de la machine à atteindre pour suivre le chemin suivi par un paquet de données.
<img src="Filius3.png"> 

4) Ajouter maintenant à cette configuration un ordinateur que l'on nommera "Serveur DNS" en le câblant au routeur après avoir ajouté ce dernier (signe +)  avec le bouton Gérer les connexions ; renseigner l'IP 192.168.3.1 et la Passerelle  192.168.3.254 ; puis en cliquant sur le Routeur après câblage ajouter l'adresse IP 192.168.3.254. Puis en cliquant sur la machine M1 changer Serveur DNS en lui donnant l'adresse IP 192.168.3.1.
Passer en mode simulation, cliquer sur l'ordinateur Serveur DNS et installer le logiciel Serveur DNS ; ouvrir le logiciel, donner le nom de domaine M4 à l'adresse IP 192.168.2.1, ajouter puis démarrer.
À partir de M1 maintenant, on peut maintenant écrire directement ' ping M4 ' car le serveur DNS a associé le nom M4 à l'adresse IP de cette machine.
<img src="Filius4.png"> 

5) Ajouter maintenant un ordinateur que l'on nommera "Serveur Web" à cette configuration en le connectant au Routeur : déclarer l'adresse IP 192.168.4.1 ; la Passerelle 192.168.4.254 et le Serveur DNS 192.168.3.1 ; indiquer également l'IP 192.168.4.254 dans la configuration du routeur. 
En mode simulation, cliquer sur la machine Serveur Web pour installer les logiciels File Explorer (Explorateur de fichiers), Text Editor (éditeur de texte) et Web Server  ; démarrer le Serveur Web (modifier la page d'accueil index.html avec l'éditeur de texte, fichier, ouvrir..pour la personnaliser, elle est située dans le dossier web serveur ) ; associer maintenant le nom de domaine my_web par exemple à l'adresse IP du Serveur Web avec le Serveur DNS ; à partir de la machine M1 , installer un Web browser (ou navigateur) et visualiser la page d'accueil fournie par le Serveur Web : http://my_web ou http://192.168.4.1/; vérifier que la page est également accessible depuis tout autre ordinateur du réseau 2 après avoir précisé pour celui-ci l'adresse du Serveur DNS.
<img src="Filius5.png"> 
<img src="Filius6.png"> 