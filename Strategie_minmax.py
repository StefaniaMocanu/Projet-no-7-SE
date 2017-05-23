#Methode minmax

from copy import copy

from Un_jeu_de_cartes import *

from Trois_fonctions import *

couleur = ('Pique', 'Trefle', 'Carreau', 'Coeur')
valeur = (7, 8, 9, 10, 'Valet', 'Dame', 'Roi', 'As')

jeupoints = []

for coul in couleur:
    for val in valeur:
        jeupoints += [(val,coul)]

jeupoints

def suppr(e,l):
    result = copy(l)
    if l != []:
        if l[0] == e:
            result = l[1:]
        else:
            result = [l[0]] + suppr(e,l[1:])
    return result

def suppr_cartes(cartes,l):
    result = []
    for c in l:
        if c not in cartes:
            result.append(c)
    return result

def gagnant_pli(p0,S1,coul):
    result = 0
    #result: indice du gagnant du pli entre 0 et 3
    #S1 est de longueur 4
    #p0: indice du joueur qui pose la premiere carte
    #coul: atout
    gagnant = cartelaplusforte(S1,coul)[0]
    for k in range(0,4):
        if S1[k] == gagnant:
            result = k
    return result

def dict_into_list(dico):
    result = []
    for key, value in dico:
        temp = [(key,value),dico[key,value]]
        result += temp
    return result

def indicegagnant(l,coul):
    result = 0
    if l != []:
        carte = cartelaplusforte(l,coul)[0]
        for k in range(0, len(l)):
            if l[k] == carte:
                result = k
        return result
    else:
        return "liste vide"

def somme_valeurs(l):
    result = 0
    if l != 0:
        for i in range(0, len(l)):
            result += l[i]
    return result

def decompte(p0,S,coul):
    result = [0,0,0,0]
    p_deb = copy(p0)
    #Attention: p0: indice global constant du premier joueur
    #p_deb: indice variable de celui qui commence le kieme pli
    if len(S)%4 != 0:
        print("Au moins un des plis n'est pas termine")
    else:
        for k in range(0,len(S)//4):
            indice = gagnant_pli(p0,S[(4*k):(4*k+4)],coul)
            result[(p_deb + indice)%4] += somme_valeurs(myvaleurcartes(S[(4*k):(4*k+4)],coul))
            p_deb = (p_deb+indice)%4
    return resul

def cartes_jouables(L,S,coul,p):
    J = []
    for i in regles(L,S,coul,p):
        J = J + [L[i]]
    return J

#print(decompte(0,[('As','Coeur'),('Valet','Coeur'),(9,'Coeur'),(7,'Coeur'),('Valet','Trefle'),('As','Trefle'),(9,'Trefle'),(7,'Trefle')],'Coeur'))
#print(decompte(1,[('Valet','Coeur'),('As','Coeur'),(9,'Coeur'),(7,'Coeur'),('Valet','Trefle'),('As','Trefle'),(9,'Trefle'),(7,'Trefle')],'Coeur'))
#print(decompte(1,[('Valet','Coeur'),('As','Coeur'),(9,'Coeur'),(7,'Coeur'),('Valet','Trefle'),('As','Trefle'),(9,'Trefle'),(7,'Trefle')],'Carreau'))

def minmax(J,L,S1,S2,coul,p0,my_p0,p):
    #J: mes cartes jouables a ce tour
    #L: mes cartes restantes
    #S1: les cartes posees a ce tour
    #S2: les cartes posees aux tours precedents
    #coul: atout
    #p0: le numero (constant) du joueur qui a pose la premiere carte du jeu
    #my_p0: indice auquel j ai commence au premier tour
    #On peut ainsi reconstituer le deroulement du jeu
    #p: mon numero de joueur (constant et different de len(S1))
    gains = []
    #gains: en case k, le nombre de points obtenu si je joue J[k]
    result = copy(J[0])
    #result: la carte a jouer a ce tour pour maximiser les gains
    S2temp = copy(S2)
    S1temp = copy(S1)
    cartes_restantes_totales = suppr_cartes(S2+S1,jeupoints)                    #cartes non posees
    cartes_restantes_autres = suppr_cartes(L,cartes_restantes_totales)          #cartes que les autres que moi peuvent jouer
    nb_cartes_restantes = len(cartes_restantes_totales)
    monindice_prec = 0                                                          #indice auquel j ai joue au tour precedent
    #initialisation de monindice_prec
    if S2temp != []:
        monindice_prec = indicegagnant(S2temp[(len(S2temp)-4):],coul)
    else:
        monindice_prec = copy(my_p0)

    for k in range(0,len(J)):
        #Supposons que la carte posee par moi est J[k]
        cartes_restantes_totales = suppr_cartes([J[k]],cartes_restantes_totales)
        cartes_restantes_autres = suppr_cartes([J[k]],cartes_restantes_autres)
        S1temp += [J[k]]

        nb_cartes_restantes = nb_cartes_restantes - 1

        if len(S1temp) == 1:
            #On ajoute trois cartes avant de terminer le pli
            for i in range(0,3):
                print(cartes_restantes_autres)
                print(nb_cartes_restantes)
                carte = minmax(cartes_jouables(cartes_restantes_autres,S1temp,coul,(p+i+1)%4), cartes_restantes_autres, S1temp, S2temp, coul, p0, my_p0, (p+i+1)%4)
 
                S1temp += [carte]
                cartes_restantes_totales = suppr_cartes([carte],cartes_restantes_totales)
                cartes_restantes_autres = suppr_cartes([carte],cartes_restantes_autres)
                nb_cartes_restantes = nb_cartes_restantes - 1

        elif len(S1temp) == 2:
            #On ajoue deux cartes avant de terminer le pli
            for i in range(0,2):
                print(cartes_restantes_autres)
                print(nb_cartes_restantes)
                carte = minmax(cartes_jouables(cartes_restantes_autres,S1temp,coul,(p+i+1)%4), cartes_restantes_autres, S1temp, S2temp, coul, p0, my_p0, (p+i+1)%4)

                S1temp += [carte]
                cartes_restantes_totales = suppr_cartes([carte],cartes_restantes_totales)
                cartes_restantes_autres = suppr_cartes([carte],cartes_restantes_autres)
                nb_cartes_restantes = nb_cartes_restantes - 1

        elif len(S1temp) == 3:
            #On ajoue une carte avant de terminer le pli
            for i in range(0,1):
                print(cartes_restantes_autres)
                print(nb_cartes_restantes)
                carte = minmax(cartes_jouables(cartes_restantes_autres,S1temp,coul,(p+i+1)%4), cartes_restantes_autres, S1temp, S2temp, coul, p0, my_p0, (p+i+1)%4)

                S1temp += [carte]
                cartes_restantes_totales = suppr_cartes([carte],cartes_restantes_totales)
                cartes_restantes_autres = suppr_cartes([carte],cartes_restantes_autres)
                nb_cartes_restantes = nb_cartes_restantes - 1


        #Maintenant S1temp contient 4 cartes: on peut les basculer dans S2temp
        S2temp = S2temp + S1temp
        monindice_prec = len(S1temp) - 1
        S1temp = []

        #Finir la partie
        for i in range(0,nb_cartes_restantes):
 
            if (i == 0) or (indicegagnant(S2temp[(len(S2temp)-4):],coul) == monindice_prec): #cest moi qui joue

                L_new = suppr_cartes([J[k]],L)
                J_new = cartes_jouables(L_new,S1temp,coul,p)
                carte = minmax(J_new, L_new, S1temp, S2temp, coul, p0, my_p0, p)
                S1temp += [carte]
                cartes_restantes_totales = suppr_cartes([carte],cartes_restantes_totales)
                cartes_restantes_autres = suppr_cartes([carte],cartes_restantes_autres)
                nb_cartes_restantes = nb_cartes_restantes - 1
 
                if len(S1temp) == 4:
                    S2temp = S2temp + S1temp
                    S1temp = []
            else: #ce nest moi qui joue
                carte = minmax(cartes_jouables(cartes_restantes_autres,S1temp,coul,(p+i)%4), cartes_restantes_autres, S1temp, S2temp, coul, p0, my_p0, (p+i)%4) #carte jouee par ladversaire: nimporte laquelle des cartes restantes sauf celles de mon jeu
                S1temp += [carte]
                cartes_restantes_totales = suppr_cartes([carte],cartes_restantes_totales)
                cartes_restantes_autres = suppr_cartes([carte],cartes_restantes_autres)
                nb_cartes_restantes = nb_cartes_restantes - 1
                monindice_prec = len(S1temp)
 
                if len(S1temp) == 4:
                    S2temp = S2temp + S1temp
                    S1temp = []
        #On obtient dans S2temp toutes les cartes jouees

        #On peut donc calculer les gains suite au jeu de J[k]
        gains[k] = decompte(p0,S2temp,coul)[p]

    #Conclure sur la carte a jouer sachant que gains est rempli
    temp_gain = gains[0]
    for k in range(0,len(J)):
        if gains[k] > temp_gain:
            result = J[k]
    return [result]

L = [('Valet','Coeur'), (9,'Coeur'), ('As','Carreau'), ('Dame','Pique'), ('As','Carreau'), (9,'Pique'), (9,'Carreau')]
J = [('Valet','Coeur'), (9,'Coeur')]
S1 = [('Roi','Coeur'), ('As','Coeur'), ('Dame','Coeur')]
S2 = [(7,'Carreau'), (7,'Coeur'),(8,'Carreau'),(8,'Coeur')]
coul = 'Coeur'
p0 = 1
my_p0 = 1
p = 1
print(minmax(J,L,S1,S2,coul,p0,my_p0,p))
