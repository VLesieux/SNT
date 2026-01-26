#########################################LECTURE DU FICHIER CSV############################
import csv
fichier=open("donnees-hospitalieres-relatives-a-lepidemie-de-covid-19-en-france.csv","r",encoding="utf-8-sig")
table_des_donnees=[]
for ligne in fichier:
    table_des_donnees.append(ligne.rstrip().split(';'))
fichier.close()
#########################################RECHERCHER LES POSITIONS DES DESCRIPTEURS#############
# 
# >>> table_des_donnees[0]
# ['Code du Département', 'Date', 'Nb actuellement hospitalisés', 'Nb actuellement en soins intensifs', 'Total retour à domicile', 'Total Décès', 'Code région', 'Code ISO 3166 de la zone', 'Nom région', 'Nom département', 'Sexe', 'geo_point_2d', 'HospConv', 'SSR_USLD', 'autres', 'Nb Quotidien Admis Hospitalisation', 'Nb Quotidien Admis Réanimation', 'Nb Quotidien Décès', 'Nb Quotidien Retour à Domicile']

# >>> table_des_donnees[0].index('Code du Département')
# 0

# >>> table_des_donnees[0].index('Date')
# 1

# >>> table_des_donnees[0].index('Nb actuellement hospitalisés')
# 2

# >>> table_des_donnees[0].index('Sexe')#######Les possibilités sont Homme, Femme, Tous
# 10

del table_des_donnees[0]

#########################################QUESTION 1################################

# Quels sont les noms des départements de Bretagne qui ont eu au moins 100 hospitalisations, tout sexe confondu, le 19 avril 2022 (2022-04-19)?

def filtrer_selon_conditions(tableau):
    solution=[]
    for ligne in tableau:
        if int(ligne[2])>=100 and ligne[10]=="Tous" and ligne[1]=="2022-04-19":
            solution.append(ligne)
    return solution


# >>> filtrer_selon_conditions(table_des_donnees)
# [['35', '2022-04-19', '496', '31', '7098', '1056', '53', 'FRA', 'Bretagne', 'Ille-et-Vilaine', 'Tous', '48.1584949366, -1.63554809717', '347.0', '112.0', '6.0', '14', '7', '2', '13'], ['22', '2022-04-19', '204', '6', '3103', '399', '53', 'FRA', 'Bretagne', "Côtes-d'Armor", 'Tous', '48.4390612443, -2.86206319142', '140.0', '46.0', '12.0', '54', '4', '1', '54'], ['29', '2022-04-19', '440', '25', '3469', '526', '53', 'FRA', 'Bretagne', 'Finistère', 'Tous', '48.2628706879, -4.05692098846', '235.0', '150.0', '30.0', '87', '10', '3', '24'], ['56', '2022-04-19', '231', '12', '4117', '649', '53', 'FRA', 'Bretagne', 'Morbihan', 'Tous', '47.8441455862, -2.8088066223', '168.0', '49.0', '2.0', '33', '1', '4', '21']]
# >>> len(filtrer_selon_conditions(table_des_donnees))
# 4

# Conclusion : Il y a 4 departements de Bretagne répondant à cette recherche : 35, 22, 29, 56


