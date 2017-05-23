from Fonctions import *

def select_couleur(L,coul):
	#select selectionne les cartes de la liste L dont la couleur est coul
    #si pas de cartes de couleur coul, renvoie L
    result = []
    if L != []:
        for i in range(0,len(L)):
            if L[i][1] == coul:
                result += [L[i]]
    if result == []:
        return L
    else:
        return result

def select_type(L,type):
	#select selectionne les cartes de la liste L dont le type (as, roi...) est type
    result = []
    if L != []:
    	for i in range(0,len(L)):
    		if L[i][0] == type:
    			result += [L[i]]
    if result == []:
        return L
    else:
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
    #supprime les elements de l1 de la liste l2
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

#Pour detecter les appels du partenaire:
    #Liste contenant ce que le partenaire a joue dans l ordre et si j etais maitre a ce moment la

def appel_as(jeu_partenaire,coul):
    #Le partenaire met une faible carte quand je suis maitre
    #jeu_partenaire est une liste qui contient ce que le partenaire a joue dans l ordre et si j etais maitre a ce moment la
    couleurs = []
    n = len(jeu_partenaire)
    if n >= 1:
        for i in range(0,n):
            if (jeu_partenaire[i][0][0] == 9 or jeu_partenaire[i][0][0] == 8 or jeu_partenaire[i][0][0] == 7) and jeu_partenaire[i][1] and jeu_partenaire[i][0][1] != coul:
                couleurs = couleurs + [jeu_partenaire[i][0][1]]
    return couleurs

def appel_suite(jeu_partenaire,coul):
    #Le partenaire joue un as puis une faible carte quand je suis maitre
    #jeu_partenaire est une liste qui contient ce que le partenaire a joue dans l ordre et si j etais maitre a ce moment la
    couleurs = []
    n = len(jeu_partenaire)
    if n > 1:
        for i in range(0,n):
            for j in range(i,len(jeu_partenaire)):
                if (jeu_partenaire[i][0][0] == 7 or jeu_partenaire[i][0][0] == 8 or jeu_partenaire[i][0][0] == 9) and jeu_partenaire[i][1] and jeu_partenaire[j][0][0] == 'As' and jeu_partenaire[i][0][1] != coul:
                    couleurs = couleurs + [jeu_partenaire[i][0][1]]
    return couleurs

def my_call(jeu,atout):
    #Appels que je peux realiser a partir de mon jeu
    result = []
    n = len(jeu)
    if n > 1:
        for i in range(0,n):
            for j in range(0,n):
                if (jeu[i][1] not in result) and jeu[i][1] != atout and jeu[j][1] == jeu[i][1] and jeu[j][0] == 'As' and (jeu[i][0] == 7 or jeu[i][0] == 8 or jeu[i][0] == 9):
                    result = result + [jeu[i][1]]
    return result

def suppr_as(l):
    result = []
    n = len(l)
    for i in range(0,n):
        if l[i][0] != 'As':
            result = result + [l[i]]
    if result == []:
        return l
    else:
        return result

def appartient(e,l):
    return (e in l)

def remporte_pli(S,coul,J):
    #S les cartes deja posees
    #J les cartes jouables
    result = []
    for i in range(0,len(J)):
        if cartelaplusforte(S + [J[i]],coul)[0] == J[i]:
            result += [J[i]]
    return result

#Confirme developpe la strategie du debutant sur un tour
#On garde en memoire (des autres tours) le nb d atouts tombes, le nb d atouts total obtenu par le joueur au debut du jeu et le jeu du partenaire en fonction de ma maitrise

def confirme(J,L,S,coul,pris,nb_atouts_main,compteur,jeu_partenaire):
    

    nb_atouts_restant = len(select_couleur(L,coul))
    result = []
    mesas = select_type(J,'As')
    atouts = select_couleur(J,coul)
    appels = appel_as(jeu_partenaire,coul) + appel_suite(jeu_partenaire,coul)
    calls = my_call(L,coul)
    temp = J

    #Si len(S)=1 ou 0, on joue en fonction des appels precedents du partenaire
    if len(S) == 0:
        if compteur < 8 - nb_atouts_main and nb_atouts_restant > 0 and pris:
            result = [cartelaplusforte(atouts,coul)[0]]
        elif appels != []:
            result = [cartelamoinsforte(select_couleur(J,appels[0]),coul)[0]]
        else:
            result = [cartelamoinsforte(mesas,coul)[0]]

    if len(S) == 1:
        if pris and S[0][1] == coul:
            if atouts != []:
                result = [cartelaplusforte(J,coul)[0]]   #et c est forcement un atout
            else:
                result = [cartelaplusforte(suppr_as(J),coul)[0]]

        elif not(pris) and S[0][1] == coul:
            result = [cartelamoinsforte(J,coul)[0]]

        else:
            if appels != [] and appartient(S[0][1],appels):
                result = [cartelaplusforte(J,coul)[0]]
            else:
                result = [cartelamoinsforte(mesas,coul)[0]]  #met un as s il peut, sinon la moins forte

    #Si len(S)=3 ou 2, on joue en fonction de ce que le partenaire vient de jouer
    if len(S) == 2:
        if pris and S[0][1] == coul:
            if atouts != []:
                result = [cartelaplusforte(J,coul)[0]]  #et c est forcement un atout
            elif calls != []:
                result = [cartelamoinsforte(J,calls[0])[0]]
            else:
                result = [cartelaplusforte(J,coul)[0]]
        elif not(pris) and S[0][1] == coul:
            if atouts != []:
                result = [cartelamoinsforte(J,coul)[0]]  #et c est forcement un atout
            elif calls != []:
                result = [cartelamoinsforte(J,calls[0])[0]]
            else:
                result = [cartelaplusforte(J,coul)[0]] #si mon equipe na pas pris et que mon partenaire joue atout, cest quil est sur de remporter le pli
        else:
            if partenaire_maitre(S,coul):
                result = [cartelaplusforte(J,coul)[0]]
            else:
                result = [cartelamoinsforte(J,coul)[0]]

    if len(S) == 3:
        if remporte_pli(S,coul,J) != []:
            result = [remporte_pli(S,coul,J)[0]]
        elif partenaire_maitre(S,coul) and appels != []:
            result = [cartelamoinsforte(J,appels[0])[0]]
        elif partenaire_maitre(S,coul):
            result = [cartelaplusforte(J,coul)[0]]
        else:
            result = [cartelamoinsforte(J,coul)[0]]
    return result

