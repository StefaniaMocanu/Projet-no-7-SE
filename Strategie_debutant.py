#Strategie debutant

#Restreint la liste des cartes jouables selon la strategie debutant

from Trois_fonctions import *

def select_couleur(L,coul):
	#select selectionne les cartes de la liste L dont la couleur est coul
    result = []
    if L != []:
        for i in range(0,len(L)):
            if L[i][1] == coul:
                result += [L[i]]
    return result

def select_type(L,type):
	#select selectionne les cartes de la liste L dont le type (as, roi...) est type
    result = []
    if L != []:
    	for i in range(0,len(L)):
    		if L[i][0] == type:
    			result += [L[i]]
    return result

def partenaire_maitre(S,coul):
	#Fonction qui indique, uniquement si len(S) >= 2, si le partenaire est maitre, a partir des cartes posees
	#coul est l atout et S la liste des cartes posees
	plus_forte = cartelaplusforte(S,coul)[0]
	result = (plus_forte == S[len(S)-2])                                        #La carte du partenaire est a l indice len(S)-2
	return result

def suppr_liste(e,l):
    result = []
    if l == []:
        result = l
    elif l[0] == e:
        result = l[1:]
    else:
        result = [l[0]] + suppr_liste(e,l[1:])
    return result

def suppr(l1,l2):
    result = list(l2)
    if l1 != []:
        for e in l1:
            result = suppr_liste(e,result)
    return result

def cartelamoinsforte(S,coul):
	result = S
	while len(result) > 1:
		del(S[cartelaplusforte(result,coul)[1]])
	return result

#Debutant developpe la strategie du debutant sur un tour
#On garde en memoire (des autres tours) seulement le nb d atouts tombes et le nb d atouts total obtenu par le joueur au debut du jeu

def debutant(J,L,S,p,coul,pris,nb_atouts_main,atouts_tombes):
	#J est la liste des cartes jouables a ce tour obtenue par application stricte des regles
	#L est la liste des cartes restantes de ma main (J inclus dans L)
	#S est la liste des cartes posees a ce tour
	#p le numero joueur qui commence ce tour
	#coul est l atout
	#pris est un booleen qui vaut vrai si j ai pris ou si le partenaire a pris, faux sinon
	#nb_atouts_main est le nombre d atouts que j avais dans ma main AU DEBUT DU JEU (variable globale)
	#atouts_tombes est la liste des atouts deja tombes
	#Remarque
	#mon numero de joueur est alors (p+length(S)-1)%4

    nb_atouts_restant = len(select_couleur(L,coul))
    result = []
    compteur = len(atouts_tombes)
    atouts = [('Valet',coul),(9,coul),('As',coul),(10,coul),('Roi',coul),('Dame',coul),(8,coul),(7,coul)]
    atouts_non_tombes = suppr(atouts_tombes,atouts)

	#S il y a au moins deux cartes posees, il maximise ou minimise le nb de points poses en fonction de la maitrise du partenaire

    if len(S) >= 2 and partenaire_maitre(S,coul):
        result = [cartelaplusforte(J,coul)[0]]                                  #Les regles sont respectees car la carte est jouable
    elif len(S) >= 2 and not(partenaire_maitre(S,coul)):
        result = cartelamoinsforte(J,coul)
    else:                                                                       #Il y a seulement 0 ou une carte posee
        if pris and compteur < 8 - nb_atouts_main and nb_atouts_restant > 0 and select_couleur(J,coul) != []:    #Sil me reste encore des atouts et que les autres en ont aussi
            if cartelaplusforte(select_couleur(J,coul),coul) == cartelaplusforte(atouts_non_tombes,coul):    #si j ai en main l atout le plus fort
                result = [cartelaplusforte(select_couleur(J,coul),coul)[0]]
            else:
                result = cartelamoinsforte(select_couleur(J,coul),coul)
        elif select_type(J,'As') != []:
            result = select_type(J,'As')                                        #Sil ne me reste plus d atout ou que les autres n en ont plus, jouer un as, sinon la liste initiale (random)
        else:                                                                   #Je n ai pas pris
            result = cartelamoinsforte(J,coul)
    return result

#Tests
#L1 = [('As','Coeur'), (9,'Coeur'), ('Roi','Carreau'), ('Dame','Pique')]
#J1 = [('As','Coeur'), (9,'Coeur')]
#S1 = [('Valet','Coeur'), ('Dame','Coeur'), ('As','Coeur')]
#S2 = [('Dame','Coeur'), (7,'Coeur')]

#print(cartelaplusforte(J1,'Coeur'))

#print(cartelamoinsforte(J1,'Coeur'))

#print(select_couleur(L1,'Pique'))

#print(select_type(L1,'Dame'))

#print(suppr_liste(('Valet','Coeur'),L1))

#print(partenaire_maitre(S1,'Carreau'))

#print(partenaire_maitre(S2,'Coeur'))

#print(cartelamoinsforte(S1,'Trefle'))

#print(cartelaplusforte([('Dame','Coeur'), ('As','Coeur')],'Coeur'))

#print(debutant(J1,L1,S2,0,'Coeur',False,len(select_couleur(L1,'Carreau')),[('Valet','Coeur')]))
