##########################Lecture et mise en tableau du fichier csv###########################
import csv
fichier=open("les_salles_de_cinemas_en_ile-de-france.csv","r")
table_des_donnees=[]
for ligne in fichier:
    table_des_donnees.append(ligne.rstrip().split(';'))
fichier.close
###############################Réponse à des questions utiles dans la console####################################
# a) len(table_des_donnees) 311 : il y a 311 lignes
# 
# b) table_des_donnees[0] 
# 
# c) len(table_des_donnees[0]) 37 : il y a 37 colonnes
# 
# d) table_des_donnees[0].index('dep') # l'information 'dep' se trouve dans la colonne 1 ou indice 1 dans la ligne
# 
# e) table_des_donnees[0].index('entrees_2020') # l'information 'entrees_2020' se trouve dans la colonne 22
# 
# f) table_des_donnees[0].index('fauteuils') # l'information 'fauteuils' se trouve dans la colonne 9
# 
# g) table_des_donnees[0].index('ecrans') # l'information 'ecrans' se trouve dans la colonne 8
# 
# h) table_des_donnees[0].index('geo') # l'information 'geo' se trouve dans la colonne 36
##################################################################################################
del table_des_donnees[0]#suppression de la première ligne des descripteurs
###############################################################################################
# On se demande combien il y a de cinémas dans le département 95
# Il faut ne garder que les lignes concernant le département 95 : FILTRER
# On crée une fonction qui va filtrer dans un tableau
#les données en ne gardant que les lignes correspondant à un département donné

def filtrer_selon_departement(tableau,departement):#la fonction attend deux paramètres
    solution=[]
    for ligne in tableau:
        if ligne[1]==departement:# le departement est la donnée en indice 1 dans la ligne
            solution.append(ligne)
    return solution
#######################Dans la console##############
#filtrer_selon_departement(table_des_donnees,"95")#la fonction renvoie un tableau filtré

#pour compter le nombre de lignes il suffit d'utiliser len pour obtenir la longueur

#len(filtrer_selon_departement(table_des_donnees,"95"))
#28

#Conclusion : il y a 28 cinémas dans le département du 95

########################################################################################
#QUESTION : Quel est le nom du cinéma d'Île de France (tous départements confondus)
#qui a fait le plus d'entrée en 2020

#SOLUTION : trier dans l'ordre décroissant selon le nombre d'entrée en 2020 : TRIER
#la ligne qui apparaîtra en premier sera le cinéma qui a fait le plus d'entrée

def critere_entree(ligne):#le critère de tri consiste à regarder la donnée dans la colonne 22 correspondant aux entrées
    return ligne[22]
    
def trier_selon_nombre_entree_2020(tableau):#la fonction attend un seul paramètre
    return sorted(tableau, key=critere_entree, reverse=True)

#A FAIRE DANS LA CONSOLE
#trier_selon_nombre_entree_2020(table_des_donnees)
# Conclusion : le cinéma qui a fait le plus d'entrées en 2020 est Les 2 SCENES

########################################################################################

#QUESTION : Quel est le nom du cinéma du département 95 qui a fait le plus d'entrée en 2020 ?

#Cette fois il faut d'abord filtrer selon le département 95 puis trier selon les entrées
#On reprend donc les fonctions précédentes

#DANS LA CONSOLE:
#trier_selon_nombre_entree_2020(filtrer_selon_departement(table_des_donnees,"95"))

#Conclusion : le cinéma du département 95 qui a fait le plus d'entrées en 2020 est STUDIO CINE


############################################################################################
#QUESTION : Combien y-a-t-il de cinémas dans le département 95 possédant plus de 5, plus de 8 écrans ?

#Il faut d'abord filtrer selon le département 95 comme fait précédemment

#Il faut ensuite filtrer en respectant la condition sur le nombre d'écrans

def filtrer_plus_de_nombre_ecrans(tableau,nombre):#la fonction attend deux paramètres tableau et nombre
    solution=[]
    for ligne in tableau:
        if int(ligne[8])>nombre:# le nb d'écrans est la donnée en indice 8 dans la ligne, il faut transformer la donnée littérale en nombre avec int()
            solution.append(ligne)
    return solution

#DANS LA CONSOLE
#len(filtrer_plus_de_nombre_ecrans(filtrer_selon_departement(table_des_donnees,"95"),5))
#3
#len(filtrer_plus_de_nombre_ecrans(filtrer_selon_departement(table_des_donnees,"95"),8))
#2


# CONCLUSION: 3 cinémas dans le 95 ont plus de 5 écrans ; 2 ont plus de 8 écrans