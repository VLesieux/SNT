def multiplication(n1,n2):
    """
    Renvoie le produit des deux entiers relatifs en utilisant uniquement les opérations + et -
    param : n1,n2 : int
    return : int
    >>> multiplication(3,5)
    15
    >>> multiplication(-4,-8)
    32
    >>> multiplication(-2,6)
    -12
    >>> multiplication(-2,0)
    0
    """
    resultat=0
    if n1>0:
        for i in range(n1):
            resultat+=n2
    else:
        for i in range(-n1):
            resultat+=-n2
    return resultat

def moyenne(liste_notes_coef):
    """
    Renvoie la moyenne pondérée d'une liste de notes coefficientées
    param : liste_notes_coef : list
    return : float
    >>> moyenne([(15,2),(9,1),(12,3)])
    12.5
    """
    resultat=0
    total=0
    for element in liste_notes_coef:
        resultat+=element[0]*element[1]
        total+=element[1]
    return resultat/total

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    """
    Renvoie l'indice de position de lettre dans ALPHABET
    param : str
    return : int
    >>> position_alphabet('E')
    4
    >>> position_alphabet('!')
    -1
    """
    for i in range(len(ALPHABET)):
        if ALPHABET[i]==lettre:
            return i
    return -1

def cesar(message, decalage):
    """
    Renvoie le message avec le décalage souhaité
    param : message : str
    param : decalage : int
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE SNT !',4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI WRX !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ XSY !',-5)
    'BONJOUR A TOUS. VIVE LA MATIERE SNT !'
    """
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET :
            indice = ( position_alphabet(lettre) + decalage )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre
    return resultat
       

def inverse_chaine(chaine):
    """
    Renvoie la chaine dans l'odre inverse
    param : str
    return : str
    >>> inverse_chaine('bac')
    'cab'
    """
    result = ''
    for caractere in chaine:
        result = caractere + result
    return result

def est_palindrome(chaine):
    """
    Renvoie True si la chaine est un palindrome, False sinon
    param : str
    return : bool
    >>> est_palindrome('SNT')
    False
    >>> est_palindrome('SNT-TNS')
    True
    """
    inverse = inverse_chaine(chaine)
    return chaine==inverse

def est_nbre_palindrome(nombre):
    """
    Renvoie True si le nombre est un palindrome
    param : nombre : int
    return : bool
    >>> est_nbre_palindrome(214312)
    False
    >>> est_nbre_palindrome(213312)
    True
    """
    chaine = str(nombre)
    return est_palindrome(chaine)

def moyenne(liste_individus):
    """
    Renvoie l'âge moyen d'une liste d'individus
    param : liste_individus : list
    return : float
    >>> moyenne([('Hervé',51),('Sacha',24),('Tom',65),('Rose',16)])
    39.0
    """
    somme=0
    for element in liste_individus:
        somme+=element[1]
    moyenne=somme/len(liste_individus)
    return moyenne
    
    
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)