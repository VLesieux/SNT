############Exercice 1####################

def prix(n):
    """
    Renvoie le prix à payer pour un achat de n ramettes de papier
    param : n: int
    return : float
    C.U : aucune
    >>> prix(100)
    345.0
    """
    if n<=50:
        return 3.68*n
    else:
        return 3.68*50+3.22*(n-50)
    
#nombre=int(input("nombre de lots de ramettes de papier achetés ? "))
#
#print("Il vous en reviendra "+str(prix(nombre))+"€")

############Exercice 2####################

def abo1(n):
    """
    Affiche s'il est avantageux de prendre le pass
    return : float
    C.U : aucune
    >>> abo1(2)
    'Ne prenez pas le pass, il est désavantageux ; vous payez 17.4€ sans le pass au lieu de 26.0€ avec le pass'
    >>> abo1(8)
    'Prenez le pass, il est avantageux ; vous payez 59.0€ avec le pass au lieu de 69.6€ sans le pass'
    """
    prix_sans_abonnement=n*8.70
    prix_avec_abonnement=15+n*5.50
    difference=prix_avec_abonnement-prix_sans_abonnement
    if difference<0:
        return 'Prenez le pass, il est avantageux ; vous payez '+str(prix_avec_abonnement)+'€ avec le pass'+' au lieu de '+str(prix_sans_abonnement)+'€ sans le pass'
    else:
        return 'Ne prenez pas le pass, il est désavantageux ; vous payez '+str(prix_sans_abonnement)+'€'+' sans le pass au lieu de '+str(prix_avec_abonnement)+'€ avec le pass'
        

#nombre=int(input("combien de séances de cinéma allez-vous prendre ? "))
#print(abo1(nombre))

def abo2(n):
    """
    Renvoie un tuple prix_sans_abonnement,prix_avec_abonnement
    param : n : int
    return : tuple (float,float)
    C.U : aucune
    >>> abo2(2)
    (17.4, 26.0)
    >>> abo2(8)
    (69.6, 59.0)
    """    
    prix_sans_abonnement=n*8.70
    prix_avec_abonnement=15+n*5.50
    return prix_sans_abonnement,prix_avec_abonnement
        

#nombre=int(input("combien de séances de cinéma allez-vous prendre ? "))
#abo2(nombre)

############Exercice 3 ####################

def avantage():
    """
    Renvoie le nombre de séances à partir duquel le pass devient avantageux
    param: none
    return : int
    C.U : aucune
    >>> avantage()
    5
    """ 
    n=0
    while abo2(n)[0]<abo2(n)[1]:
        n+=1
    return n

#print('Prendre le pass devient avantageux à partir de '+str(avantage())+' séances.')
#    
############Exercice 4 ####################

a=-1
b=2
#for i in range(1,5):
#    a=b-a+i
#    b=2*a+1
#print(a,b)

#i=1
#while i<=4:
#    a=b-a+i
#    b=2*a+1
#    i+=1
#print(a,b)    

#    
############Exercice 6 ####################

def recherche_min_max(L):
    longueur=len(L)
    maxi=L[0]
    mini=L[0]
    for i in range(1,longueur):
        if L[i]>maxi:
            maxi=L[i]
        if L[i]<mini:
            mini=L[i]        
    return mini,maxi

############Exercice 9 ####################

def concat1(L1,L2):
    L=[]
    for i in range(len(L1)):
        L.append(L1[i])
    for i in range(len(L2)):
        L.append(L2[i])
    return L

def concat2(L1,L2):
    L=[]
    for i in L1:
        L.append(i)
    for i in L2:
        L.append(i)
    return L

############Exercice 10 ####################

def Fibo(n):
    liste=[1,1]
    i=2
    while i<=n:
        liste.append(liste[i-1]+liste[i-2])
        i+=1
    return liste[n-1]

****Autre méthode****

def fibo_iter(n):
    liste=[0]
    u,v=0,1
    for i in range(n-1):
        u,v=v,u+v
        liste.append(v)     
    return liste

############Exercice 11 ####################

def nombre_or():
    n=2
    while abs((Fibo(n+1)/Fibo(n))-1.6180339887) > 10**(-10):
        n+=1
    return n,Fibo(n+1)/Fibo(n)

########################Exercice 12 (DM) ######################################
import random

def lancers_de_des(n):
    liste=[]
    for i in range(n):
        lancer=random.randint(1,6)
        liste.append(lancer)
    return liste

########################Exercice 13 (DM) ######################################
import random

def lancers_de_pieces(n):
    compteur=0
    for i in range(n):
        lancer=random.randint(0,1)
        if lancer==1:
            compteur+=1                
    return compteur/n

########################Exercice 14 (DM) ######################################
import random

def lancers_de_pieces_truquees(n,p):
    compteur=0
    for i in range(n):
        lancer=int(random.random()+p)
        if lancer==1:
            compteur+=1                
    return compteur/n

########################Exercice 16 (DM) ######################################
from turtle import *

def trace(n,larg):
    reset()
    for i in range(1,n+1):
        forward(larg*i)
        left(120)

###################################################################################################

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=False)