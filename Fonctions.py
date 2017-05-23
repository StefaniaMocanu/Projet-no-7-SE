#3
# Fonctions
import random

from Un_jeu_de_cartes import *

from Deux_Classe_JeuDeCartes import *

def valeurcartes(L,coul):
# renvoie les valeurs des cartes qui sont dans L apres choix de l atout
# utile pour le choix de chaque carte jouee a partir du jeu restant L d un joueur
	"Valeur des cartes apres choix de l atout"
	dictio = {}
	for c in jeupoints:
		if c in L:
			if c[1] == coul:
				if c[0] == 7:
					dictio[c] = 0
				if c[0] == 8:
					dictio[c] = 0
				if c[0] == 9:
					dictio[c] = 14
				if c[0] == 10:
					dictio[c] = 10
				if c[0] == 'Valet':
					dictio[c] = 20
				if c[0] == 'Dame':
					dictio[c] = 3
				if c[0] == 'Roi':
					dictio[c] = 4
				if c[0] == 'As':
					dictio[c] = 11
			else:
				if c[0] == 7:
					dictio[c] = 0
				if c[0] == 8:
					dictio[c] = 0
				if c[0] == 9:
					dictio[c] = 0
				if c[0] == 10:
					dictio[c] = 10
				if c[0] == 'Valet':
					dictio[c] = 2
				if c[0] == 'Dame':
					dictio[c] = 3
				if c[0] == 'Roi':
					dictio[c] = 4
				if c[0] == 'As':
					dictio[c] = 11
	return(dictio)

def classementcarte(c,coul):
# prend en argument une carte et l'atout et renvoie un couple (classement, couleur) (remplace la hauteur par son classement)
# utile pour determiner quelle carte est la plus forte dans une liste de cartes
	if c[1] == coul:
		if c[0] == 7:
			return (1, coul)
		if c[0] == 8:
			return (2, coul)
		if c[0] == 9:
			return (7, coul)
		if c[0] == 10:
			return (5, coul)
		if c[0] == 'Valet':
			return (8, coul)
		if c[0] == 'Dame':
			return (3, coul)
		if c[0] == 'Roi':
			return (4, coul)
		if c[0] == 'As':
			return (6, coul)
	else:
		if c[0] == 7:
			return (1, c[1])
		if c[0] == 8:
			return (2, c[1])
		if c[0] == 9:
			return (3, c[1])
		if c[0] == 10:
			return (7, c[1])
		if c[0] == 'Valet':
			return (4, c[1])
		if c[0] == 'Dame':
			return (5, c[1])
		if c[0] == 'Roi':
			return (6, c[1])
		if c[0] == 'As':
			return (8, c[1])

def cartelaplusforte(S,coul):
	#"Fonction qui renvoie la carte la plus forte dans la liste S des cartes et son index en fonction de l'atout"
	if S != []:
		if coul in [S[i][1] for i in range(len(S))]:                                     #si un atout a ete pose

			T = []                                                                         #creer une liste dont les coordonnes sont le classement si c est un atout, -1 sinon
			for i in range(len(S)):
				if S[i][1] == coul:
					T += [classementcarte(S[i],coul)[0]]
				else:
					T += [-1]

			a = max(T)
			k = T.index(a)

			return ([S[k],k])                 						#renvoyer la carte la plus forte et son indice

		else:

			premcoul = S[0][1] 								#couleur de la premiere carte posee

			T = []                                                                        #creer une liste dont les coordonnes sont le classement si meme couleur que premiere carte, -1 sinon
			for i in range(len(S)):
				if S[i][1] == premcoul:
					T += [classementcarte(S[i],coul)[0]]
				else:
					T += [-1]

			a = max(T)
			k = T.index(a)

			return ([S[k],k])
	else:
		return []

def prisepremiertour(L,coul,t):
	"Prise de l atout ou non au premier tour en fonction de la main et de l atout"
	a = totalpoints(L,coul)
	if a > t: #seuil de prise: correspondant a au moins valet et 9 a la couleur prise
		return (["prend et l'atout est {0}." .format(coul), "prend"])
	else:
		return (["passe","passe"])

def prisesecondtour(L,t):
	"Prise de l'atout ou non au second tour, et si oui choix de l'atout, en fonction de la main et de l'atout"
	T = [totalpoints(L,coul) for coul in couleur]
	a = max(T)
	if a > t:
		return (["prend et l'atout est {0}." .format(couleur[T.index(a)]), couleur[T.index(a)], "prend"])
	else:
		return (["passe","","passe"])

def totalpoints(L,coul):
	"Total des points d une liste de cartes L en fonction de l atout, sans le dix de der"
	l = 0
	for i in jeupoints:
		if i in L:
			l += dico(coul)[i]
	return (l)

def regles(L,S,coul,p): #Fonction invariable qui renvoie la liste des cartes jouables
	"Regles du jeu : quelle carte peut etre jouee de la main L (mon jeu) en fonction de la liste S des cartes posees pour ce tour et de la couleur de l atout"

	if S != []:                                               	    #si au moins un joueur a deja joue

		if len(S) == 1 :		# si le joueur allie n'a pas deja joue

			if S[0][1] == coul:                                    #si la premiere carte posee est un atout
				
				U = []			#liste U des valeurs des cartes de la main L
				for i in L:
					if i[1] == coul:
						U += [classementcarte(i,coul)[0]]
					else:
						U += [-1]
				
				if max(U) > -1:		#si il y a des atouts dans la main L
					
					T = []			#liste T des valeurs des cartes posees S
					for i in S:
						if i[1] == coul:
							T += [classementcarte(i,coul)[0]]
					
					if max(U) > max(T):		#si le joueur a des atouts plus forts dans sa main
						
						result = []
						for i in range(len(L)):
							if U[i] > max(T):
								result += [i]
						return result
						
					else:					#si le joueur n'a pas d'atout plus fort
						
						result = []
						for i in range(len(L)):
							if U[i] >= 0:
								result += [i]
						return result
				
				else:
					return [i for i in range(len(L))]
						
				
			else: 				#si la premiere carte poseee n'est pas un atout
				
				premcoul = S[0][1]		#couleur de la premiere carte
				
				U = []			#liste U des valeurs des cartes de la main L pour premcoul
				for i in L:
					if i[1] == premcoul:
						U += [classementcarte(i,premcoul)[0]]
					else:
						U += [-1]
				
				if max(U) > -1:			#si le joueur a des cartes de la meme couleur que la premiere carte posee
					result = []
					for i in range(len(L)):
						if U[i] > 0:
							result += [i]
					return result
				
				else:
					
					V = []			#liste V des valeurs des cartes de la main L pour l'atout
					for i in L:
						if i[1] == coul:
							V += [classementcarte(i,coul)[0]]
						else:
							V += [-1]
					
					T = []				#liste T des valeurs des cartes posees S
					for i in S:
						if i[1] == coul:
							T += [classementcarte(i,coul)[0]]
							
					if max(V) > -1:			#si le joueur a des atouts
						
						if T != []:		#si il y a des atouts poses
							
							if max(V) > max(T):		#si le joueur a des atouts plus forts
								result = []
								for i in range(len(L)):
									if V[i] > max(T):
										result += [i]
								return result
							
							else:
								result = []
								for i in range(len(L)):
									if V[i] >= 0:
										result += [i]
								return result
										
						else:			#si il n'y a pas d'atout pose
							
							result = []
							for i in range(len(L)):
								if V[i] >= 0:
									result += [i]
							return result		
						
					else:					#si le joueur n'a pas d'atout
						
						return [i for i in range(len(L))]
										
		else:				#si le joueur allie a deja joue
			
			k = ( cartelaplusforte(S,coul)[1] + p - 1 ) % 4 + 1			#numero du joueur ayant la carte la plus forte parmi les cartes posees
			u = ( len(S) + p - 1) % 4 + 1						#numero du joueur qui va jouer
			
			if (u+k)%2 == 0 and S[0][1] != coul:					#si le joueur qui a la carte la plus forte est mon allie et la carte demandee n'est pas un atout
				
				U = []			#liste U des valeurs des cartes de la main L pour la couleur demandee
				for i in L:
					if i[1] == S[0][1]:
						U += [classementcarte(i,S[0][1])[0]]
					else:
						U += [-1]
				
				if max(U) == -1:
					return [i for i in range(len(L))]		#toutes les cartes sont jouables
				else:
					result = []
					for i in range(len(L)):
						if U[i] > 0:
							result += [i]
					return result
			else:								#si le joueur qui a la carte la plus forte n'est pas mon allie
				
				if S[0][1] == coul:                                    #si la premiere carte posee est un atout
					
					U = []			#liste U des valeurs des cartes de la main L
					for i in L:
						if i[1] == coul:
							U += [classementcarte(i,coul)[0]]
						else:
							U += [-1]
					
					if max(U) > -1:		#si il y a des atouts dans la main L
						
						T = []			#liste T des valeurs des cartes posees S
						for i in S:
							if i[1] == coul:
								T += [classementcarte(i,coul)[0]]
						
						if max(U) > max(T):		#si le joueur a des atouts plus forts dans sa main
							
							result = []
							for i in range(len(L)):
								if U[i] > max(T):
									result += [i]
							return result
							
						else:					#si le joueur n'a pas d'atout plus fort
							
							result = []
							for i in range(len(L)):
								if U[i] >= 0:
									result += [i]
							return result
							
					else:
						return [i for i in range(len(L))]
					
				else: 				#si la premiere carte poseee n'est pas un atout
					
					premcoul = S[0][1]		#couleur de la premiere carte
					
					U = []			#liste U des valeurs des cartes de la main L pour premcoul
					for i in L:
						if i[1] == premcoul:
							U += [classementcarte(i,premcoul)[0]]
						else:
							U += [-1]
					
					if max(U) > -1:			#si le joueur a des cartes de la meme couleur que la premiere carte posee
						result = []
						for i in range(len(L)):
							if U[i] > 0:
								result += [i]
						return result
					
					else:
						
						V = []			#liste V des valeurs des cartes de la main L pour l'atout
						for i in L:
							if i[1] == coul:
								V += [classementcarte(i,coul)[0]]
							else:
								V += [-1]
						
						T = []				#liste T des valeurs des cartes posees S pour l'atout
						for i in S:
							if i[1] == coul:
								T += [classementcarte(i,coul)[0]]

						if max(V) > -1:			#si le joueur a des atouts
							
							if T != []:		#si il y a des atouts poses
								
								if max(V) > max(T):		#si le joueur a des atouts plus forts
									result = []
									for i in range(len(L)):
										if V[i] > max(T):
											result += [i]
									return result
								
								else:
									result = []
									for i in range(len(L)):
										if V[i] >= 0:
											result += [i]
									return result
											
							else:			#si il n'y a pas d'atout pose
								
								result = []
								for i in range(len(L)):
									if V[i] >= 0:
										result += [i]
								return result		
							
						else:					#si le joueur n'a pas d'atout
							
							return [i for i in range(len(L))]
	
	else:
		return [i for i in range(len(L))]
				
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

def cartes_jouables(L,S,coul,p):
	J = []
	for i in regles(L,S,coul,p):
		J = J + [L[i]]
	return J

def regles_IG(G,L,S,coul,p):
	#meme principe que pour regles, sauf que G est la main initiale (avec 8 cartes) tandis que L est la main actuelle
	#renvoie les indices des cartes jouables, mais pour la main initiale G
	#fonction utile pour l'IG (pour reperer les cartes=
	T = cartes_jouables(L,S,coul,p)
	result = []
	for c in T:
		result += [G.index(c)]
	return result


def compteur_atouts_main_initiale(L,coul):
	compt = 0
	for i in L:
		if i[1] == coul:
			compt += 1
	return compt

def compteur_atouts_joues(S,coul,compt):
#S est la liste des cartes posees a ce tour
#compteur est le nombre d'atouts deja joues avant ce tour
	for i in S:
		if i[1] == coul:
			compt +=1
	return compt