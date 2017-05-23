#3bis
#Fonctions tours pour les differentes strategies
from copy import copy

from Un_jeu_de_cartes import *

from Deux_Classe_JeuDeCartes import *

from Trois_fonctions import *

from Huit_strategie_debutant import *

from Neuf_strategie_confirme import *

from Dix_Ter_strategie_minmax import *

from Dix_Quad_strategie_minmax import *

def touravecjoueur_random_random(L1,L2,L3,L4,S1,S2,S3,S4,coul,p):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1

		if c == 1:
			print ( "Voici votre main : {0}" .format(L1) )
			print ( "Voici les indices que vous pouvez jouer : {0}" .format(regles(L1,S,coul,p)) )
			a = 'non'
			while a not in regles(L1,S,coul,p):
				a = int(input("Quelle carte voulez-vous jouer? (Taper l'indice de la carte) "))
				if a not in regles(L1,S,coul,p):
					print("Vous ne pouvez pas jouer cette carte.")
			S += [L1[a]]
			del (L1[a])
			print (S)

		else:
			if c == 2:
				k = random.choice(regles(L2,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
				S += [L2[k]]
				del (L2[k])
				print ("Cartes sur la table : {0}" .format(S))
			if c == 3:
				k = random.choice(regles(L3,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
				S += [L3[k]]
				del (L3[k])
				print ("Cartes sur la table : {0}" .format(S))
			if c == 4:
				k = random.choice(regles(L4,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
				S += [L4[k]]
				del (L4[k])
				print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli

	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )

def toursansjoueur_random_random(L1,L2,L3,L4,S1,S2,S3,S4,coul,p):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1

		if c == 1:
			k = random.choice(regles(L1,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L1[k]]
			del (L1[k])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			k = random.choice(regles(L2,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L2[k]]
			del (L2[k])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			k = random.choice(regles(L3,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L3[k]]
			del (L3[k])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			k = random.choice(regles(L4,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L4[k]]
			del (L4[k])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli

	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )


def toursansjoueur_beginner_random(L1,L2,L3,L4,S1,S2,S3,S4,coul,p,pris,nb_atouts_main_1,nb_atouts_main_3,atouts_tombes):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	#Equipe 1 : strategie debutant
	#Equipe 2 : strategie random
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1

		if c == 1:
			J = []
			for i in regles(L1,S,coul,p):
				J += [(L1[i])]
			k = random.choice(debutant(J,L1,S,p,coul,pris,nb_atouts_main_1,atouts_tombes))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			if k[1] == coul:
				atouts_tombes += [k]
			del (L1[L1.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			k = random.choice(regles(L2,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L2[k]]
			if L2[k][1] == coul:
				atouts_tombes += L2[k]
			del (L2[k])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			J = []
			for i in regles(L3,S,coul,p):
				J += [(L3[i])]
			k = random.choice(debutant(J,L3,S,p,coul,pris,nb_atouts_main_3,atouts_tombes))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			if k[1] == coul:
				atouts_tombes += [k]
			del (L3[L3.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			k = random.choice(regles(L4,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L4[k]]
			if L4[k][1] == coul:
				atouts_tombes += L4[k]
			del (L4[k])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli

	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )


def toursansjoueur_confirme_random(L1,L2,L3,L4,S1,S2,S3,S4,coul,p,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1,nb_atouts_main_3,compteur_3,jeu_partenaire_3):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	#Equipe 1 : strategie debutant
	#Equipe 2 : strategie random
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1

		if c == 1:
			J = []
			for i in regles(L1,S,coul,p):
				J += [(L1[i])]
			if confirme(J,L1,S,coul,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1) == []:
				print (J,L1,S,coul,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1)
			k = random.choice(confirme(J,L1,S,coul,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			jeu_partenaire_3 += [(k,True)]
			del (L1[L1.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			k = random.choice(regles(L2,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L2[k]]
			compteur_1 += compteur_atouts_joues([L2[k]],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([L2[k]],coul,compteur_3)
			del (L2[k])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			J = []
			for i in regles(L3,S,coul,p):
				J += [(L3[i])]
			if confirme(J,L3,S,coul,pris,nb_atouts_main_3,compteur_3,jeu_partenaire_3) == []:
				print(J,L3,S,coul,pris,nb_atouts_main_3,compteur_3,jeu_partenaire_3)
			k = random.choice(confirme(J,L3,S,coul,pris,nb_atouts_main_3,compteur_3,jeu_partenaire_3))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			jeu_partenaire_1 += [(k,True)]
			del (L3[L3.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			k = random.choice(regles(L4,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L4[k]]
			compteur_1 += compteur_atouts_joues([L4[k]],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([L4[k]],coul,compteur_3)
			del (L4[k])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli

	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )
	
def toursansjoueur_confirme_beginner(L1,L2,L3,L4,S1,S2,S3,S4,coul,p,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1,nb_atouts_main_3,compteur_3,jeu_partenaire_3,nb_atouts_main_2,nb_atouts_main_4,atouts_tombes):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	#Equipe 1 : strategie debutant
	#Equipe 2 : strategie random
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1

		if c == 1:
			J = []
			for i in regles(L1,S,coul,p):
				J += [(L1[i])]
			k = random.choice(confirme(J,L1,S,coul,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			if k[1] == coul:
				atouts_tombes += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			jeu_partenaire_3 += [(k,True)]
			del (L1[L1.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			J = []
			for i in regles(L2,S,coul,p):
				J += [(L2[i])]
			k = random.choice(debutant(J,L2,S,p,coul,pris,nb_atouts_main_2,atouts_tombes))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			if k[1] == coul:
				atouts_tombes += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			del (L2[L2.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			J = []
			for i in regles(L3,S,coul,p):
				J += [(L3[i])]
			k = random.choice(confirme(J,L3,S,coul,pris,nb_atouts_main_3,compteur_3,jeu_partenaire_3))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			if k[1] == coul:
				atouts_tombes += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			jeu_partenaire_1 += [(k,True)]
			del (L3[L3.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			J = []
			for i in regles(L4,S,coul,p):
				J += [(L4[i])]
			k = random.choice(debutant(J,L4,S,p,coul,pris,nb_atouts_main_4,atouts_tombes))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			if k[1] == coul:
				atouts_tombes += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			del (L4[L4.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli

	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )


def toursansjoueur_algonormal_random(L1,L2,L3,L4,S1,S2,S3,S4,coul,p,p0,Ss):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#Ss cartes deja jouees
	#renvoie le numero du joueur qui gagne le pli
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	Ss2 = copy(Ss)
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1

		if c == 1:
			J = []
			for i in regles(L1,S,coul,p):
				J += [(L1[i])]			
			k = random.choice(minmaxnormal(J,S,Ss,coul,p0,0))              
			S += [k]
			Ss2 += [k]
			del (L1[L1.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			k = random.choice(regles(L2,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L2[k]]
			Ss2 += [L2[k]]
			del (L2[k])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			J = []
			for i in regles(L3,S,coul,p):
				J += [(L3[i])]						
			k = random.choice(minmaxnormal(J,S,Ss,coul,p0,2))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [k]
			Ss2 += [k]
			del (L3[L3.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			k = random.choice(regles(L4,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L4[k]]
			Ss2 += [L4[k]]
			del (L4[k])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli
	Ss = copy(Ss2)
	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )
	
	
def toursansjoueur_beginner_algonormal(L1,L2,L3,L4,S1,S2,S3,S4,coul,p,pris,nb_atouts_main_1,nb_atouts_main_3,atouts_tombes,p0,Ss):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1
		Ss2 = copy(Ss)
		if c == 1:
			J = []
			for i in regles(L1,S,coul,p):
				J += [(L1[i])]			
			k = random.choice(debutant(J,L1,S,p,coul,pris,nb_atouts_main_1,atouts_tombes))
			S += [k]
			Ss2 += [k]
			if k[1] == coul:
				atouts_tombes += [k]			
			del (L1[L1.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			J = []
			for i in regles(L2,S,coul,p):
				J += [(L2[i])]			
			k = random.choice(minmaxnormal(J,S,Ss,coul,p0,1))              
			S += [k]
			Ss2 += [k]
			if k[1] == coul:
				atouts_tombes += [k]			
			del (L2[L2.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			J = []
			for i in regles(L3,S,coul,p):
				J += [(L3[i])]						
			k = random.choice(debutant(J,L3,S,p,coul,pris,nb_atouts_main_3,atouts_tombes))
			S += [k]
			Ss2 += [k]
			if k[1] == coul:
				atouts_tombes += [k]			
			del (L3[L3.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			J = []
			for i in regles(L4,S,coul,p):
				J += [(L4[i])]			
			k = random.choice(minmaxnormal(J,S,Ss,coul,p0,3))              
			S += [k]
			Ss2 += [k]
			if k[1] == coul:
				atouts_tombes += [k]			
			del (L4[L4.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli
	Ss = copy(Ss2)
	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )
	
	
	
def toursansjoueur_confirme_algonormal(L1,L2,L3,L4,S1,S2,S3,S4,coul,p,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1,nb_atouts_main_3,compteur_3,jeu_partenaire_3,p0,Ss):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	#Equipe 1 : strategie debutant
	#Equipe 2 : strategie random
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1
		Ss2 = copy(Ss)
		if c == 1:
			J = []
			for i in regles(L1,S,coul,p):
				J += [(L1[i])]
			k = random.choice(confirme(J,L1,S,coul,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			Ss2 += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			jeu_partenaire_3 += [(k,True)]
			del (L1[L1.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			J = []
			for i in regles(L2,S,coul,p):
				J += [(L2[i])]			
			k = random.choice(minmaxnormal(J,S,Ss,coul,p0,1))              
			S += [k]
			Ss2 += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			del (L2[L2.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			J = []
			for i in regles(L3,S,coul,p):
				J += [(L3[i])]
			k = random.choice(confirme(J,L3,S,coul,pris,nb_atouts_main_3,compteur_3,jeu_partenaire_3))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			Ss2 += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			jeu_partenaire_1 += [(k,True)]
			del (L3[L3.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			J = []
			for i in regles(L4,S,coul,p):
				J += [(L4[i])]			
			k = random.choice(minmaxnormal(J,S,Ss,coul,p0,3))              
			S += [k]
			Ss2 += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			del (L4[L4.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli
	Ss = copy(Ss2)
	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )
	
	
def toursansjoueur_algosimplifie_random(L1,L2,L3,L4,S1,S2,S3,S4,coul,p,p0,Ss):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	Ss2 = []
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1
		if c == 1:
			print("L1={0}".format(L1))
			print("S={0}".format(S))
			print("Ss={0}".format(Ss))
			print("p0={0},p={1},coul={2}".format(p0,p,coul))
			J = []
			for i in regles(L1,S,coul,p):
				J += [(L1[i])]			
			k = random.choice(minmaxsimplifie(J,S,Ss,coul,p0,0))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [k]
			Ss2 += [k]
			del (L1[L1.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			k = random.choice(regles(L2,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L2[k]]
			Ss2 += [L2[k]]
			del (L2[k])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			print("L3={0}".format(L3))
			print("S={0}".format(S))
			print("Ss={0}".format(Ss))
			print("p0={0},p={1},coul={2}".format(p0,p,coul))
			J = []
			for i in regles(L3,S,coul,p):
				J += [(L3[i])]						
			k = random.choice(minmaxsimplifie(J,S,Ss,coul,p0,2))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			
			S += [k]
			Ss2 += [k]
			del (L3[L3.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			k = random.choice(regles(L4,S,coul,p))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [L4[k]]
			Ss2 += [L4[k]]
			del (L4[k])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli
	Ss += Ss2
	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )
	
	
def toursansjoueur_beginner_algosimplifie(L1,L2,L3,L4,S1,S2,S3,S4,coul,p,pris,nb_atouts_main_1,nb_atouts_main_3,atouts_tombes,p0,Ss):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1

		if c == 1:
			J = []
			for i in regles(L1,S,coul,p):
				J += [(L1[i])]			
			k = random.choice(debutant(J,L1,S,p,coul,pris,nb_atouts_main_1,atouts_tombes))
			S += [k]
			Ss += [k]
			if k[1] == coul:
				atouts_tombes += [k]			
			del (L1[L1.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			J = []
			for i in regles(L2,S,coul,p):
				J += [(L2[i])]				
			k = random.choice(minmaxsimplifie(J,S,Ss,coul,p0,1))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [k]
			Ss += [k]
			if k[1] == coul:
				atouts_tombes += [k]			
			del (L2[L2.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			J = []
			for i in regles(L3,S,coul,p):
				J += [(L3[i])]						
			k = random.choice(debutant(J,L3,S,p,coul,pris,nb_atouts_main_3,atouts_tombes))
			S += [k]
			Ss += [k]
			if k[1] == coul:
				atouts_tombes += [k]			
			del (L3[L3.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			J = []
			for i in regles(L4,S,coul,p):
				J += [(L4[i])]			
			k = random.choice(minmaxsimplifie(J,S,Ss,coul,p0,3))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [k]
			Ss += [k]
			if k[1] == coul:
				atouts_tombes += [k]			
			del (L4[L4.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli

	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )
	
	
	
def toursansjoueur_confirme_algosimplifie(L1,L2,L3,L4,S1,S2,S3,S4,coul,p,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1,nb_atouts_main_3,compteur_3,jeu_partenaire_3,p0,Ss):
	#L1 L2 L3 L4 mains des quatre joueurs
	#S1 S2 S3 S4 les plis gagnes par chaque joueur depuis le debut de la partie
	#p joueur qui commence a ce tour
	#renvoie le numero du joueur qui gagne le pli
	#Equipe 1 : strategie debutant
	#Equipe 2 : strategie random
	"Tour en fonction des mains des quatre joueurs, des plis gagnes, de la couleur et du numero p du joueur qui commence"

	S = []                                                             #cartes posees sur la table
	for i in range(p,p+4):                                        #i et c representent le joueur, c entre 1 et 4

		c = ((i-1)%4) + 1

		if c == 1:
			J = []
			for i in regles(L1,S,coul,p):
				J += [(L1[i])]
			if confirme(J,L1,S,coul,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1) == []:
				print (J,L1,S,coul,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1)
			k = random.choice(confirme(J,L1,S,coul,pris,nb_atouts_main_1,compteur_1,jeu_partenaire_1))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			jeu_partenaire_3 += [(k,True)]
			del (L1[L1.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 2:
			J = []
			for i in regles(L2,S,coul,p):
				J += [(L2[i])]				
			k = random.choice(minmaxsimplifie(J,S,Ss,coul,p0,1))             
			S += [k]
			Ss += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			del (L2[L2.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 3:
			J = []
			for i in regles(L3,S,coul,p):
				J += [(L3[i])]
			if confirme(J,L3,S,coul,pris,nb_atouts_main_3,compteur_3,jeu_partenaire_3) == []:
				print(J,L3,S,coul,pris,nb_atouts_main_3,compteur_3,jeu_partenaire_3)
			k = random.choice(confirme(J,L3,S,coul,pris,nb_atouts_main_3,compteur_3,jeu_partenaire_3))              #choisir une carte aleatoirement parmi les cartes proposees par debutant
			S += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			jeu_partenaire_1 += [(k,True)]
			del (L3[L3.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))
		if c == 4:
			J = []
			for i in regles(L4,S,coul,p):
				J += [(L4[i])]			
			k = random.choice(minmaxsimplifie(J,S,Ss,coul,p0,3))              #choisir une carte aleatoirement parmi les cartes jouables (jeu de l ordi)
			S += [k]
			Ss += [k]
			compteur_1 += compteur_atouts_joues([k],coul,compteur_1)
			compteur_3 += compteur_atouts_joues([k],coul,compteur_3)
			del (L4[L4.index(k)])
			#print ("Cartes sur la table : {0}" .format(S))                      #les cartes ont ete posees sur la table

	q = ( cartelaplusforte(S,coul)[1] + p - 1) % 4 + 1		# numero du joueur ayant gagne le pli

	if q == 1:
		S1 += S
	if q == 2:
		S2 += S
	if q == 3:
		S3 += S
	if q == 4:
		S4 += S

	#print ( "Le pli est remporte par le joueur {0}." .format(q) )
	return ( q )