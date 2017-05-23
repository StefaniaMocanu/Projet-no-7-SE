# coding=utf-8
#4
#Partie avec un joueur
# coding=utf-8
import copy
#Import des fichiers precedents
from Jeu_de_cartes import *
from Deux_Classe_JeuDeCartes import *
from Fonctions import *
from Fonctions_tours import *

#Import du module pygame
import pygame
from pygame.locals import *

#Initialisation de la bibliotheque Pygame
pygame.init()

def partie_avec_joueur_trois_minmax_simplifie_IG(t):
	
	#Ouverture de la fenetre Pygame
	fenetre = pygame.display.set_mode((650, 650))
	
	#Chargement de la police et de ses caracteristiques (taille, gras, italique)
	font = pygame.font.SysFont('Arial', 36, True, True)
	
	#Chargement et collage du fond
	fond = pygame.image.load("fond_vert.jpg").convert()
	fenetre.blit(fond, (0,0))
	
	#Initialisation : creation de tous les sons qui seront utilises par le programme
	victoire_son = pygame.mixer.Sound("victoire_son.wav")
	defaite_son = pygame.mixer.Sound("defaite_son.wav")
	
	#Initialisation : creation de toutes les images qui seront utilisees par le programme
	fond = pygame.image.load("fond_vert.jpg").convert()
	voulez_vous_jouer = pygame.image.load("voulez_vous_jouer.jpg").convert()
	voulez_vous_continuer_a_jouer = pygame.image.load("voulez_vous_continuer_a_jouer.jpg").convert()
	oui = pygame.image.load("oui.jpg").convert()
	non = pygame.image.load("non.jpg").convert()
	un = pygame.image.load("un.jpg").convert()
	passe = pygame.image.load("passe.jpg").convert()
	prend = pygame.image.load("prend.jpg").convert()
	rect_vert = pygame.image.load("rect_vert.jpg").convert()
	carte_verte_horizontale = pygame.image.load("carte_verte_horizontale.jpg").convert()
	carte_verte_verticale = pygame.image.load("carte_verte_verticale.jpg").convert()
	bordure_verticale = pygame.image.load("bordure_verticale.jpg").convert()
	bordure_horizontale = pygame.image.load("bordure_horizontale.jpg").convert()
	bordure_verte_horizontale = pygame.image.load("bordure_verte_horizontale.jpg").convert()
	bordure_verte_verticale = pygame.image.load("bordure_verte_verticale.jpg").convert()
	pique = pygame.image.load("pique.jpg").convert()
	trefle = pygame.image.load("trefle.jpg").convert()
	coeur = pygame.image.load("coeur.jpg").convert()
	carreau = pygame.image.load("carreau.jpg").convert()
	coul_verte = pygame.image.load("coul_verte.jpg").convert()
	carte_retournee_verticale = pygame.image.load("carte_retournee_verticale.jpg").convert()
	carte_retournee_horizontale = pygame.image.load("carte_retournee_horizontale.jpg").convert()
	sept_trefle_verticale = pygame.image.load("sept_trefle_verticale.jpg").convert()
	sept_trefle_horizontale = pygame.image.load("sept_trefle_horizontale.jpg").convert()
	sept_pique_verticale = pygame.image.load("sept_pique_verticale.jpg").convert()
	sept_pique_horizontale = pygame.image.load("sept_pique_horizontale.jpg").convert()
	sept_coeur_verticale = pygame.image.load("sept_coeur_verticale.jpg").convert()
	sept_coeur_horizontale = pygame.image.load("sept_coeur_horizontale.jpg").convert()
	sept_carreau_verticale = pygame.image.load("sept_carreau_verticale.jpg").convert()
	sept_carreau_horizontale = pygame.image.load("sept_carreau_horizontale.jpg").convert()
	huit_trefle_verticale = pygame.image.load("huit_trefle_verticale.jpg").convert()
	huit_trefle_horizontale = pygame.image.load("huit_trefle_horizontale.jpg").convert()
	huit_pique_verticale = pygame.image.load("huit_pique_verticale.jpg").convert()
	huit_pique_horizontale = pygame.image.load("huit_pique_horizontale.jpg").convert()
	huit_coeur_verticale = pygame.image.load("huit_coeur_verticale.jpg").convert()
	huit_coeur_horizontale = pygame.image.load("huit_coeur_horizontale.jpg").convert()
	huit_carreau_verticale = pygame.image.load("huit_carreau_verticale.jpg").convert()
	huit_carreau_horizontale = pygame.image.load("huit_carreau_horizontale.jpg").convert()
	neuf_trefle_verticale = pygame.image.load("neuf_trefle_verticale.jpg").convert()
	neuf_trefle_horizontale = pygame.image.load("neuf_trefle_horizontale.jpg").convert()
	neuf_pique_verticale = pygame.image.load("neuf_pique_verticale.jpg").convert()
	neuf_pique_horizontale = pygame.image.load("neuf_pique_horizontale.jpg").convert()
	neuf_coeur_verticale = pygame.image.load("neuf_coeur_verticale.jpg").convert()
	neuf_coeur_horizontale = pygame.image.load("neuf_coeur_horizontale.jpg").convert()
	neuf_carreau_verticale = pygame.image.load("neuf_carreau_verticale.jpg").convert()
	neuf_carreau_horizontale = pygame.image.load("neuf_carreau_horizontale.jpg").convert()
	dix_trefle_verticale = pygame.image.load("dix_trefle_verticale.jpg").convert()
	dix_trefle_horizontale = pygame.image.load("dix_trefle_horizontale.jpg").convert()
	dix_pique_verticale = pygame.image.load("dix_pique_verticale.jpg").convert()
	dix_pique_horizontale = pygame.image.load("dix_pique_horizontale.jpg").convert()
	dix_coeur_verticale = pygame.image.load("dix_coeur_verticale.jpg").convert()
	dix_coeur_horizontale = pygame.image.load("dix_coeur_horizontale.jpg").convert()
	dix_carreau_verticale = pygame.image.load("dix_carreau_verticale.jpg").convert()
	dix_carreau_horizontale = pygame.image.load("dix_carreau_horizontale.jpg").convert()
	valet_trefle_verticale = pygame.image.load("valet_trefle_verticale.jpg").convert()
	valet_trefle_horizontale = pygame.image.load("valet_trefle_horizontale.jpg").convert()
	valet_pique_verticale = pygame.image.load("valet_pique_verticale.jpg").convert()
	valet_pique_horizontale = pygame.image.load("valet_pique_horizontale.jpg").convert()
	valet_coeur_verticale = pygame.image.load("valet_coeur_verticale.jpg").convert()
	valet_coeur_horizontale = pygame.image.load("valet_coeur_horizontale.jpg").convert()
	valet_carreau_verticale = pygame.image.load("valet_carreau_verticale.jpg").convert()
	valet_carreau_horizontale = pygame.image.load("valet_carreau_horizontale.jpg").convert()
	dame_trefle_verticale = pygame.image.load("dame_trefle_verticale.jpg").convert()
	dame_trefle_horizontale = pygame.image.load("dame_trefle_horizontale.jpg").convert()
	dame_pique_verticale = pygame.image.load("dame_pique_verticale.jpg").convert()
	dame_pique_horizontale = pygame.image.load("dame_pique_horizontale.jpg").convert()
	dame_coeur_verticale = pygame.image.load("dame_coeur_verticale.jpg").convert()
	dame_coeur_horizontale = pygame.image.load("dame_coeur_horizontale.jpg").convert()
	dame_carreau_verticale = pygame.image.load("dame_carreau_verticale.jpg").convert()
	dame_carreau_horizontale = pygame.image.load("dame_carreau_horizontale.jpg").convert()
	roi_trefle_verticale = pygame.image.load("roi_trefle_verticale.jpg").convert()
	roi_trefle_horizontale = pygame.image.load("roi_trefle_horizontale.jpg").convert()
	roi_pique_verticale = pygame.image.load("roi_pique_verticale.jpg").convert()
	roi_pique_horizontale = pygame.image.load("roi_pique_horizontale.jpg").convert()
	roi_coeur_verticale = pygame.image.load("roi_coeur_verticale.jpg").convert()
	roi_coeur_horizontale = pygame.image.load("roi_coeur_horizontale.jpg").convert()
	roi_carreau_verticale = pygame.image.load("roi_carreau_verticale.jpg").convert()
	roi_carreau_horizontale = pygame.image.load("roi_carreau_horizontale.jpg").convert()
	aas_trefle_verticale = pygame.image.load("as_trefle_verticale.jpg").convert()
	aas_trefle_horizontale = pygame.image.load("as_trefle_horizontale.jpg").convert()
	aas_pique_verticale = pygame.image.load("as_pique_verticale.jpg").convert()
	aas_pique_horizontale = pygame.image.load("as_pique_horizontale.jpg").convert()
	aas_coeur_verticale = pygame.image.load("as_coeur_verticale.jpg").convert()
	aas_coeur_horizontale = pygame.image.load("as_coeur_horizontale.jpg").convert()
	aas_carreau_verticale = pygame.image.load("as_carreau_verticale.jpg").convert()
	aas_carreau_horizontale = pygame.image.load("as_carreau_horizontale.jpg").convert()
	victoire_equipe1 = pygame.image.load("victoire_equipe1.jpg").convert()
	victoire_equipe2 = pygame.image.load("victoire_equipe2.jpg").convert()
	victoire_finale = pygame.image.load("victoire_finale.jpg").convert()
	defaite_finale = pygame.image.load("defaite_finale.jpg").convert()
	egalite_parfaite =  pygame.image.load("egalite_parfaite.jpg").convert()
	
	#Creation d'une fonction qui prend en argument une carte (tuple) et renvoie uen liste avec les deux positions de l'image associee
	def association(c):
		if c == (7, 'Trefle'):
			return [sept_trefle_verticale,sept_trefle_horizontale]
		if c == (7, 'Pique'):
			return [sept_pique_verticale,sept_pique_horizontale]
		if c == (7, 'Coeur'):
			return [sept_coeur_verticale,sept_coeur_horizontale]
		if c == (7, 'Carreau'):
			return [sept_carreau_verticale,sept_carreau_horizontale]
		if c == (8, 'Trefle'):
			return [huit_trefle_verticale,huit_trefle_horizontale]
		if c == (8, 'Pique'):
			return [huit_pique_verticale,huit_pique_horizontale]
		if c == (8, 'Coeur'):
			return [huit_coeur_verticale,huit_coeur_horizontale]
		if c == (8, 'Carreau'):
			return [huit_carreau_verticale,huit_carreau_horizontale]
		if c == (9, 'Trefle'):
			return [neuf_trefle_verticale,neuf_trefle_horizontale]
		if c == (9, 'Pique'):
			return [neuf_pique_verticale,neuf_pique_horizontale]
		if c == (9, 'Coeur'):
			return [neuf_coeur_verticale,neuf_coeur_horizontale]
		if c == (9, 'Carreau'):
			return [neuf_carreau_verticale,neuf_carreau_horizontale]
		if c == (10, 'Trefle'):
			return [dix_trefle_verticale,dix_trefle_horizontale]
		if c == (10, 'Pique'):
			return [dix_pique_verticale,dix_pique_horizontale]
		if c == (10, 'Coeur'):
			return [dix_coeur_verticale,dix_coeur_horizontale]
		if c == (10, 'Carreau'):
			return [dix_carreau_verticale,dix_carreau_horizontale]
		if c == ('Valet', 'Trefle'):
			return [valet_trefle_verticale,valet_trefle_horizontale]
		if c == ('Valet', 'Pique'):
			return [valet_pique_verticale,valet_pique_horizontale]
		if c == ('Valet', 'Coeur'):
			return [valet_coeur_verticale,valet_coeur_horizontale]
		if c == ('Valet', 'Carreau'):
			return [valet_carreau_verticale,valet_carreau_horizontale]
		if c == ('Dame', 'Trefle'):
			return [dame_trefle_verticale,dame_trefle_horizontale]
		if c == ('Dame', 'Pique'):
			return [dame_pique_verticale,dame_pique_horizontale]
		if c == ('Dame', 'Coeur'):
			return [dame_coeur_verticale,dame_coeur_horizontale]
		if c == ('Dame', 'Carreau'):
			return [dame_carreau_verticale,dame_carreau_horizontale]
		if c == ('Roi', 'Trefle'):
			return [roi_trefle_verticale,roi_trefle_horizontale]
		if c == ('Roi', 'Pique'):
			return [roi_pique_verticale,roi_pique_horizontale]
		if c == ('Roi', 'Coeur'):
			return [roi_coeur_verticale,roi_coeur_horizontale]
		if c == ('Roi', 'Carreau'):
			return [roi_carreau_verticale,roi_carreau_horizontale]
		if c == ('As', 'Trefle'):
			return [aas_trefle_verticale,aas_trefle_horizontale]
		if c == ('As', 'Pique'):
			return [aas_pique_verticale,aas_pique_horizontale]
		if c == ('As', 'Coeur'):
			return [aas_coeur_verticale,aas_coeur_horizontale]
		if c == ('As', 'Carreau'):
			return [aas_carreau_verticale,aas_carreau_horizontale]
	
	#Initialisation : voulez_vous jouer?
	fenetre.blit(voulez_vous_jouer, (0,150))
	fenetre.blit(oui, (100,400))
	fenetre.blit(non, (350,400))
	pygame.display.flip()
	
	bouclinf = 0

	while bouclinf == 0:
		for event in pygame.event.get():
			#si on veut fermer la fenetre
			if event.type == QUIT:
				bouclinf = 1
			#si on appuie sur non, la fenetre se ferme
			if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 550 and event.pos[0] > 350 and event.pos[1] < 550 and event.pos[1] > 400:
				bouclinf = 1
			#si on appuie sur oui
			if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 300 and event.pos[0] > 100 and event.pos[1] < 550 and event.pos[1] > 400 :
				continuerajouer = 0					
				totalequipe1entout = 0					
				totalequipe2entout = 0
				p=1
				while continuerajouer == 0:
					pygame.time.delay(500)
					fenetre.blit(fond, (0,0))
					pygame.display.flip()
					fenetre.blit(carte_retournee_verticale, (270,290))
					pygame.time.delay(1000)
					pygame.display.flip()
					pygame.time.delay(1000)
					jeu = JeuDeCartes()
					jeu.battre()
					L = jeu.distribuer([],[],[],[],12,3,(p%4) + 1)            #distribuer d abord 3 cartes
					S = jeu.distribuer(L[0],L[1],L[2],L[3],8,2,(p%4) + 1)     #distribuer ensuite 2 cartes
					for i in range ((p%4)+1,4+(p%4)+1):
						if i%4 == 1:   #pour le joueur 1
							carte = association(S[0][0])
							fenetre.blit(carte[0], (210,475))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[0][1])
							fenetre.blit(carte[0], (270,475))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[0][2])
							fenetre.blit(carte[0], (330,475))
							pygame.display.flip()
							pygame.time.delay(250)
						if i%4 == 2:   #pour le joueur 2
							carte = association(S[1][0])
							fenetre.blit(carte[1], (105,210))
							fenetre.blit(carte_retournee_horizontale, (105,210))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[1][1])
							fenetre.blit(carte[1], (105,270))
							fenetre.blit(carte_retournee_horizontale, (105,270))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[1][2])
							fenetre.blit(carte[1], (105,330))
							fenetre.blit(carte_retournee_horizontale, (105,330))
							pygame.display.flip()
							pygame.time.delay(250)
						if i%4 == 3:   #pour le joueur 3
							carte = association(S[2][0])
							fenetre.blit(carte[0], (390,105))
							fenetre.blit(carte_retournee_verticale, (390,105))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[2][1])
							fenetre.blit(carte[0], (330,105))
							fenetre.blit(carte_retournee_verticale, (330,105))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[2][2])
							fenetre.blit(carte[0], (270,105))
							fenetre.blit(carte_retournee_verticale, (270,105))
							pygame.display.flip()
							pygame.time.delay(250)
						if i%4 == 0:   #pour le joueur 4
							carte = association(S[3][0])
							fenetre.blit(carte[1], (475,390))
							fenetre.blit(carte_retournee_horizontale, (475,390))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[3][1])
							fenetre.blit(carte[1], (475,330))
							fenetre.blit(carte_retournee_horizontale, (475,330))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[3][2])
							fenetre.blit(carte[1], (475,270))
							fenetre.blit(carte_retournee_horizontale, (475,270))
							pygame.display.flip()
							pygame.time.delay(250)
					
					for i in range ((p%4)+1,4+(p%4)+1):
						if i%4 == 1:   #pour le joueur 1
							carte = association(S[0][3])
							fenetre.blit(carte[0], (390,475))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[0][4])
							fenetre.blit(carte[0], (210,555))
							pygame.display.flip()
							pygame.time.delay(250)
						if i%4 == 2:   #pour le joueur 2
							carte = association(S[1][3])
							fenetre.blit(carte[1], (105,390))
							fenetre.blit(carte_retournee_horizontale, (105,390))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[1][4])
							fenetre.blit(carte[1], (25,210))
							fenetre.blit(carte_retournee_horizontale, (25,210))
							pygame.display.flip()
							pygame.time.delay(250)
						if i%4 == 3:   #pour le joueur 3
							carte = association(S[2][3])
							fenetre.blit(carte[0], (210,105))
							fenetre.blit(carte_retournee_verticale, (210,105))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[2][4])
							fenetre.blit(carte[0], (390,25))
							fenetre.blit(carte_retournee_verticale, (390,25))
							pygame.display.flip()
							pygame.time.delay(250)
						if i%4 == 0:   #pour le joueur 4
							carte = association(S[3][3])
							fenetre.blit(carte[1], (475,210))
							fenetre.blit(carte_retournee_horizontale, (475,210))
							pygame.display.flip()
							pygame.time.delay(250)
							carte = association(S[3][4])
							fenetre.blit(carte[1], (555,390))
							fenetre.blit(carte_retournee_horizontale, (555,390))
							pygame.display.flip()
							pygame.time.delay(250)
					
					d = jeu.tirer(1)[0]
					carte_tiree = association(d)
					pygame.time.delay(500)
					fenetre.blit(carte_tiree[0],(330, 290))
					pygame.display.flip()
					
					c = "passe"
					b = p
					compteur = 0
					while c == "passe" and compteur <4:
						pygame.display.flip()
						pygame.time.delay(500)
						compteur += 1
						b = (b%4) + 1
						if b == 1:                                           
							fenetre.blit(passe, (445,480))
							fenetre.blit(prend, (445,520))
							pygame.display.flip()
							temp = 0
							while temp == 0:
								for event in pygame.event.get():
									#si on veut fermer la fenetre
									if event.type == QUIT:
										temp = 1
										bouclinf = 1
									#si on clique sur passe
									if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 545 and event.pos[0] > 445 and event.pos[1] < 510 and event.pos[1] > 480 :
										c = "passe"
										temp = 1
									#si on clique sur prend
									if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 545 and event.pos[0] > 445 and event.pos[1] < 550 and event.pos[1] > 520 :
										c = "prend"
										temp = 1
										coul = d[1]
										if coul == 'Pique':
											fenetre.blit(pique, (450,550))
										if coul == 'Trefle':
											fenetre.blit(trefle, (450,550))
										if coul == 'Coeur':
											fenetre.blit(coeur, (450,550))
										if coul == 'Carreau':
											fenetre.blit(carreau, (450,550))
										pygame.display.flip()
						if b == 2:                                           
							c = prisepremiertour(L[b-1],d[1],t)[1]
							if c == "prend":
								coul = d[1]
								fenetre.blit(prend, (40,445))
								if coul == 'Pique':
									fenetre.blit(pique, (140,445))
								if coul == 'Trefle':
									fenetre.blit(trefle, (140,445))
								if coul == 'Coeur':
									fenetre.blit(coeur, (140,445))
								if coul == 'Carreau':
									fenetre.blit(carreau, (140,445))
								pygame.display.flip()
							else:
								fenetre.blit(passe, (40,445))
								pygame.display.flip()
						if b == 3:                                           
							c = prisepremiertour(L[b-1],d[1],t)[1]
							if c == "prend":
								coul = d[1]
								fenetre.blit(prend, (105,80))
								if coul == 'Pique':
									fenetre.blit(pique, (130,110))
								if coul == 'Trefle':
									fenetre.blit(trefle, (130,110))
								if coul == 'Coeur':
									fenetre.blit(coeur, (130,110))
								if coul == 'Carreau':
									fenetre.blit(carreau, (130,110))
								pygame.display.flip()
							else:
								fenetre.blit(passe, (105,80))
								pygame.display.flip()
						if b == 4:                                           
							c = prisepremiertour(L[b-1],d[1],t)[1]
							if c == "prend":
								coul = d[1]
								fenetre.blit(prend, (525,175))
								if coul == 'Pique':
									fenetre.blit(pique, (525,150))
								if coul == 'Trefle':
									fenetre.blit(trefle, (525,150))
								if coul == 'Coeur':
									fenetre.blit(coeur, (525,150))
								if coul == 'Carreau':
									fenetre.blit(carreau, (525,150))
								pygame.display.flip()
							else:
								fenetre.blit(passe, (525,175))
								pygame.display.flip()
								
					pygame.time.delay(1000)
					fenetre.blit(rect_vert, (445,480))
					fenetre.blit(rect_vert, (445,520))
					fenetre.blit(rect_vert, (40,445))
					fenetre.blit(rect_vert, (105,80))
					fenetre.blit(rect_vert, (525,175))
					pygame.display.flip()
								
					while c == "passe" and compteur <8:
						pygame.display.flip()
						pygame.time.delay(500)
						compteur += 1
						b = (b%4) + 1
						if b == 1:                                           
							fenetre.blit(passe, (445,480))
							if d[1] == 'Trefle':
								fenetre.blit(pique, (460,510))
								fenetre.blit(coeur, (490,510))
								fenetre.blit(carreau, (520,510))
							if d[1] == 'Pique':
								fenetre.blit(trefle, (460,510))
								fenetre.blit(coeur, (490,510))
								fenetre.blit(carreau, (520,510))
							if d[1] == 'Coeur':
								fenetre.blit(trefle, (460,510))
								fenetre.blit(pique, (490,510))
								fenetre.blit(carreau, (520,510))
							if d[1] == 'Carreau':
								fenetre.blit(trefle, (460,510))
								fenetre.blit(pique, (490,510))
								fenetre.blit(coeur, (520,510))
							pygame.display.flip()
							temp = 0
							while temp == 0:
								for event in pygame.event.get():
									#si on veut fermer la fenetre
									if event.type == QUIT:
										temp = 1
										bouclinf = 1
									if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 485 and event.pos[0] > 460 and event.pos[1] < 535 and event.pos[1] > 510 :
										c = "prend"
										if d[1] == 'Trefle':
											coul = 'Pique'
										if d[1] == 'Pique':
											coul = 'Trefle'
										if d[1] == 'Coeur':
											coul = 'Trefle'
										if d[1] == 'Carreau':
											coul = 'Trefle'
										temp = 1
										fenetre.blit(coul_verte, (490,510))
										fenetre.blit(coul_verte, (520,510))
									if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 515 and event.pos[0] > 490 and event.pos[1] < 535 and event.pos[1] > 510 :
										c = "prend"
										if d[1] == 'Trefle':
											coul = 'Coeur'
										if d[1] == 'Pique':
											coul = 'Coeur'
										if d[1] == 'Coeur':
											coul = 'Pique'
										if d[1] == 'Carreau':
											coul = 'Pique'
										temp = 1
										fenetre.blit(coul_verte, (460,510))
										fenetre.blit(coul_verte, (520,510))
									if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 545 and event.pos[0] > 520 and event.pos[1] < 535 and event.pos[1] > 510 :
										c = "prend"
										if d[1] == 'Trefle':
											coul = 'Carreau'
										if d[1] == 'Pique':
											coul = 'Carreau'
										if d[1] == 'Coeur':
											coul = 'Carreau'
										if d[1] == 'Carreau':
											coul = 'Coeur'
										temp = 1
										fenetre.blit(coul_verte, (460,510))
										fenetre.blit(coul_verte, (490,510))
									#si on clique sur passe
									if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 545 and event.pos[0] > 445 and event.pos[1] < 510 and event.pos[1] > 480 :
										c = "passe"
										temp = 1
						if b == 2:                                           
							c = prisesecondtour(L[b-1],t)[2]
							if c == "prend":
								coul = prisesecondtour(L[b-1],t)[1]
								fenetre.blit(prend, (40,445))
								if coul == 'Pique':
									fenetre.blit(pique, (140,445))
								if coul == 'Trefle':
									fenetre.blit(trefle, (140,445))
								if coul == 'Coeur':
									fenetre.blit(coeur, (140,445))
								if coul == 'Carreau':
									fenetre.blit(carreau, (140,445))
								pygame.display.flip()
							else:
								fenetre.blit(passe, (40,445))
								pygame.display.flip()
						if b == 3:                                           
							c = prisesecondtour(L[b-1],t)[2]
							if c == "prend":
								coul = prisesecondtour(L[b-1],t)[1]
								fenetre.blit(prend, (105,80))
								if coul == 'Pique':
									fenetre.blit(pique, (130,110))
								if coul == 'Trefle':
									fenetre.blit(trefle, (130,110))
								if coul == 'Coeur':
									fenetre.blit(coeur, (130,110))
								if coul == 'Carreau':
									fenetre.blit(carreau, (130,110))
								pygame.display.flip()
							else:
								fenetre.blit(passe, (105,80))
								pygame.display.flip()
						if b == 4:                                           
							c = prisesecondtour(L[b-1],t)[2]
							if c == "prend":
								coul = prisesecondtour(L[b-1],t)[1]
								fenetre.blit(prend, (525,175))
								if coul == 'Pique':
									fenetre.blit(pique, (525,150))
								if coul == 'Trefle':
									fenetre.blit(trefle, (525,150))
								if coul == 'Coeur':
									fenetre.blit(coeur, (525,150))
								if coul == 'Carreau':
									fenetre.blit(carreau, (525,150))
								pygame.display.flip()
							else:
								fenetre.blit(passe, (525,175))
								pygame.display.flip()
								
					if c == "passe":
						p = (p%4) + 1
					
					if c != "passe" :
						pygame.time.delay(2000)
						fenetre.blit(rect_vert, (445,480))
						fenetre.blit(rect_vert, (40,445))
						fenetre.blit(rect_vert, (105,80))
						fenetre.blit(rect_vert, (525,175))
						fenetre.blit(rect_vert, (525,175))
						if compteur < 4:
							fenetre.blit(rect_vert, (445,520))
						
						fenetre.blit(carte_verte_verticale, (330,290))
						pygame.display.flip()
						
						S[b-1] += [d]                            #le b final est l indice de celui qui a parle en dernier donc de celui qui a pris
						S[b-1] += jeu.tirer(2)
						T = jeu.distribuer(S[0],S[1],S[2],S[3],9,3,(b%4)+1)
						
						for i in range (b,b+4):
							if i%4 == 1:   #pour le joueur 1
								carte = association(T[0][5])
								fenetre.blit(carte[0], (270,555))
								pygame.display.flip()
								pygame.time.delay(250)
								carte = association(T[0][6])
								fenetre.blit(carte[0], (330,555))
								pygame.display.flip()
								pygame.time.delay(250)
								carte = association(T[0][7])
								fenetre.blit(carte[0], (390,555))
								pygame.display.flip()
								pygame.time.delay(250)
							if i%4 == 2:   #pour le joueur 2
								carte = association(T[1][5])
								fenetre.blit(carte[1], (25,270))
								fenetre.blit(carte_retournee_horizontale, (25,270))
								pygame.display.flip()
								pygame.time.delay(250)
								carte = association(T[1][6])
								fenetre.blit(carte[1], (25,330))
								fenetre.blit(carte_retournee_horizontale, (25,330))
								pygame.display.flip()
								pygame.time.delay(250)
								carte = association(T[1][7])
								fenetre.blit(carte[1], (25,390))
								fenetre.blit(carte_retournee_horizontale, (25,390))
								pygame.display.flip()
								pygame.time.delay(250)
							if i%4 == 3:   #pour le joueur 3
								carte = association(T[2][5])
								fenetre.blit(carte[0], (330,25))
								fenetre.blit(carte_retournee_verticale, (330,25))
								pygame.display.flip()
								pygame.time.delay(250)
								carte = association(T[2][6])
								fenetre.blit(carte[0], (270,25))
								fenetre.blit(carte_retournee_verticale, (270,25))
								pygame.display.flip()
								pygame.time.delay(250)
								carte = association(T[2][7])
								fenetre.blit(carte[0], (210,25))
								fenetre.blit(carte_retournee_verticale, (210,25))
								pygame.display.flip()
								pygame.time.delay(250)
							if i%4 == 0:   #pour le joueur 4
								carte = association(T[3][5])
								fenetre.blit(carte[1], (555,330))
								fenetre.blit(carte_retournee_horizontale, (555,330))
								pygame.display.flip()
								pygame.time.delay(250)
								carte = association(T[3][6])
								fenetre.blit(carte[1], (555,270))
								fenetre.blit(carte_retournee_horizontale, (555,270))
								pygame.display.flip()
								pygame.time.delay(250)
								carte = association(T[3][7])
								fenetre.blit(carte[1], (555,210))
								fenetre.blit(carte_retournee_horizontale, (555,210))
								pygame.display.flip()
								pygame.time.delay(250)
								
						fenetre.blit(carte_verte_verticale, (270,290))
						pygame.display.flip()
						
						S1 = []
						S2 = []
						S3 = []
						S4 = []
						Ss = []
						p = (p%4) + 1
						G1 = copy(T[0])
						G2 = copy(T[1])
						G3 = copy(T[2])
						G4 = copy(T[3])
						x = p
						temp2 = 0
						compteur = 0
						while compteur < 8 and temp2 == 0:
							compteur += 1
							pygame.time.delay(250)
							if x == 1:
								fenetre.blit(un, (450,580))
							if x == 2:
								fenetre.blit(un, (100,445))
							if x == 3:
								fenetre.blit(un, (130,150))
							if x == 4:
								fenetre.blit(un, (560,150))
							pygame.display.flip()
							pygame.time.delay(750)
							S = []                                                             
							for i in range(x,x+4):                                        
								c = ((i-1)%4) + 1
								if c == 1:
									if 0 in regles_IG(G1,T[0],S,coul,x):
										fenetre.blit(bordure_verticale, (207,472))
										fenetre.blit(bordure_verticale, (260,472))
										fenetre.blit(bordure_horizontale, (207,472))
										fenetre.blit(bordure_horizontale, (207,545))
									if 1 in regles_IG(G1,T[0],S,coul,x):
										fenetre.blit(bordure_verticale, (267,472))
										fenetre.blit(bordure_verticale, (320,472))
										fenetre.blit(bordure_horizontale, (267,472))
										fenetre.blit(bordure_horizontale, (267,545))
									if 2 in regles_IG(G1,T[0],S,coul,x):
										fenetre.blit(bordure_verticale, (327,472))
										fenetre.blit(bordure_verticale, (380,472))
										fenetre.blit(bordure_horizontale, (327,472))
										fenetre.blit(bordure_horizontale, (327,545))
									if 3 in regles_IG(G1,T[0],S,coul,x):
										fenetre.blit(bordure_verticale, (387,472))
										fenetre.blit(bordure_verticale, (440,472))
										fenetre.blit(bordure_horizontale, (387,472))
										fenetre.blit(bordure_horizontale, (387,545))
									if 4 in regles_IG(G1,T[0],S,coul,x):
										fenetre.blit(bordure_verticale, (207,552))
										fenetre.blit(bordure_verticale, (260,552))
										fenetre.blit(bordure_horizontale, (207,552))
										fenetre.blit(bordure_horizontale, (207,625))
									if 5 in regles_IG(G1,T[0],S,coul,x):
										fenetre.blit(bordure_verticale, (267,552))
										fenetre.blit(bordure_verticale, (320,552))
										fenetre.blit(bordure_horizontale, (267,552))
										fenetre.blit(bordure_horizontale, (267,625))
									if 6 in regles_IG(G1,T[0],S,coul,x):
										fenetre.blit(bordure_verticale, (327,552))
										fenetre.blit(bordure_verticale, (380,552))
										fenetre.blit(bordure_horizontale, (327,552))
										fenetre.blit(bordure_horizontale, (327,625))
									if 7 in regles_IG(G1,T[0],S,coul,x):
										fenetre.blit(bordure_verticale, (387,552))
										fenetre.blit(bordure_verticale, (440,552))
										fenetre.blit(bordure_horizontale, (387,552))
										fenetre.blit(bordure_horizontale, (387,625))
									pygame.display.flip()
									temp = 0
									while temp == 0:
										for event in pygame.event.get():
											#si on veut fermer la fenetre
											if event.type == QUIT:
												temp = 1
												temp2 = 1
												continuerajouer = 1
												bouclinf = 1
											if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 260 and event.pos[0] > 210 and event.pos[1] < 545 and event.pos[1] > 475 :
												if 0 in regles_IG(G1,T[0],S,coul,x):
													carte = association(G1[0])[0]
													fenetre.blit(carte_verte_verticale, (210,475))
													fenetre.blit(carte, (300,395))
													pygame.display.flip()
													temp = 1
													k = 0
											if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 320 and event.pos[0] > 270 and event.pos[1] < 545 and event.pos[1] > 475 :
												if 1 in regles_IG(G1,T[0],S,coul,x):
													carte = association(G1[1])[0]
													fenetre.blit(carte_verte_verticale, (270,475))
													fenetre.blit(carte, (300,395))
													pygame.display.flip()
													temp = 1
													k = 1
											if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 380 and event.pos[0] > 330 and event.pos[1] < 545 and event.pos[1] > 475 :
												if 2 in regles_IG(G1,T[0],S,coul,x):
													carte = association(G1[2])[0]
													fenetre.blit(carte_verte_verticale, (330,475))
													fenetre.blit(carte, (300,395))
													pygame.display.flip()
													temp = 1
													k = 2
											if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 440 and event.pos[0] > 390 and event.pos[1] < 545 and event.pos[1] > 475 :
												if 3 in regles_IG(G1,T[0],S,coul,x):
													carte = association(G1[3])[0]
													fenetre.blit(carte_verte_verticale, (390,475))
													fenetre.blit(carte, (300,395))
													pygame.display.flip()
													temp = 1
													k = 3
											if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 260 and event.pos[0] > 210 and event.pos[1] < 625 and event.pos[1] > 555 :
												if 4 in regles_IG(G1,T[0],S,coul,x):
													carte = association(G1[4])[0]
													fenetre.blit(carte_verte_verticale, (210,555))
													fenetre.blit(carte, (300,395))
													pygame.display.flip()
													temp = 1
													k = 4
											if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 320 and event.pos[0] > 270 and event.pos[1] < 625 and event.pos[1] > 555 :
												if 5 in regles_IG(G1,T[0],S,coul,x):
													carte = association(G1[5])[0]
													fenetre.blit(carte_verte_verticale, (270,555))
													fenetre.blit(carte, (300,395))
													pygame.display.flip()
													temp = 1
													k = 5
											if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 380 and event.pos[0] > 330 and event.pos[1] < 625 and event.pos[1] > 555 :
												if 6 in regles_IG(G1,T[0],S,coul,x):
													carte = association(G1[6])[0]
													fenetre.blit(carte_verte_verticale, (330,555))
													fenetre.blit(carte, (300,395))
													pygame.display.flip()
													temp = 1
													k = 6
											if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 440 and event.pos[0] > 390 and event.pos[1] < 625 and event.pos[1] > 555 :
												if 7 in regles_IG(G1,T[0],S,coul,x):
													carte = association(G1[7])[0]
													fenetre.blit(carte_verte_verticale, (390,555))
													fenetre.blit(carte, (300,395))
													pygame.display.flip()
													temp = 1
													k = 7
									S += [G1[k]]							
									del (T[0][T[0].index(G1[k])])
									fenetre.blit(bordure_verte_verticale, (207,472))
									fenetre.blit(bordure_verte_verticale, (260,472))
									fenetre.blit(bordure_verte_horizontale, (207,472))
									fenetre.blit(bordure_verte_horizontale, (207,545))
									fenetre.blit(bordure_verte_verticale, (267,472))
									fenetre.blit(bordure_verte_verticale, (320,472))
									fenetre.blit(bordure_verte_horizontale, (267,472))
									fenetre.blit(bordure_verte_horizontale, (267,545))
									fenetre.blit(bordure_verte_verticale, (327,472))
									fenetre.blit(bordure_verte_verticale, (380,472))
									fenetre.blit(bordure_verte_horizontale, (327,472))
									fenetre.blit(bordure_verte_horizontale, (327,545))
									fenetre.blit(bordure_verte_verticale, (387,472))
									fenetre.blit(bordure_verte_verticale, (440,472))
									fenetre.blit(bordure_verte_horizontale, (387,472))
									fenetre.blit(bordure_verte_horizontale, (387,545))
									fenetre.blit(bordure_verte_verticale, (207,552))
									fenetre.blit(bordure_verte_verticale, (260,552))
									fenetre.blit(bordure_verte_horizontale, (207,552))
									fenetre.blit(bordure_verte_horizontale, (207,625))
									fenetre.blit(bordure_verte_verticale, (267,552))
									fenetre.blit(bordure_verte_verticale, (320,552))
									fenetre.blit(bordure_verte_horizontale, (267,552))
									fenetre.blit(bordure_verte_horizontale, (267,625))
									fenetre.blit(bordure_verte_verticale, (327,552))
									fenetre.blit(bordure_verte_verticale, (380,552))
									fenetre.blit(bordure_verte_horizontale, (327,552))
									fenetre.blit(bordure_verte_horizontale, (327,625))
									fenetre.blit(bordure_verte_verticale, (387,552))
									fenetre.blit(bordure_verte_verticale, (440,552))
									fenetre.blit(bordure_verte_horizontale, (387,552))
									fenetre.blit(bordure_verte_horizontale, (387,625))
									pygame.display.flip()
								if c == 2:
									J = []
									for i in regles(T[1],S,coul,p):
										J += [(T[1][i])]				
									k = random.choice(minmaxsimplifie(J,S,Ss,coul,p,1)) 
									n = G2.index(k)
									carte = association(k)[1]
									if n == 0:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (105,210))
										fenetre.blit(carte, (185,300))
										pygame.display.flip()
									if n == 1:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (105,270))
										fenetre.blit(carte, (185,300))
										pygame.display.flip()
									if n == 2:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (105,330))
										fenetre.blit(carte, (185,300))
										pygame.display.flip()
									if n == 3:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (105,390))
										fenetre.blit(carte, (185,300))
										pygame.display.flip()
									if n == 4:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (25,210))
										fenetre.blit(carte, (185,300))
										pygame.display.flip()
									if n == 5:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (25,270))
										fenetre.blit(carte, (185,300))
										pygame.display.flip()
									if n == 6:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (25,330))
										fenetre.blit(carte, (185,300))
										pygame.display.flip()
									if n == 7:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (25,390))
										fenetre.blit(carte, (185,300))
										pygame.display.flip()								
									S += [k]
									Ss += [k]
									del (T[1][T[1].index(k)])							
								if c == 3:
									J = []
									for i in regles(T[2],S,coul,p):
										J += [(T[2][i])]				
									k = random.choice(minmaxsimplifie(J,S,Ss,coul,p,2)) 
									n = G3.index(k)
									carte = association(k)[0]
									if n == 0:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_verticale, (390,105))
										fenetre.blit(carte, (300,185))
										pygame.display.flip()
									if n == 1:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_verticale, (330,105))
										fenetre.blit(carte, (300,185))
										pygame.display.flip()
									if n == 2:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_verticale, (270,105))
										fenetre.blit(carte, (300,185))
										pygame.display.flip()
									if n == 3:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_verticale, (210,105))
										fenetre.blit(carte, (300,185))
										pygame.display.flip()
									if n == 4:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_verticale, (390,25))
										fenetre.blit(carte, (300,185))
										pygame.display.flip()
									if n == 5:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_verticale, (330,25))
										fenetre.blit(carte, (300,185))
										pygame.display.flip()
									if n == 6:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_verticale, (270,25))
										fenetre.blit(carte, (300,185))
										pygame.display.flip()
									if n == 7:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_verticale, (210,25))
										fenetre.blit(carte, (300,185))
										pygame.display.flip()	
									S += [k]
									Ss += [k]
									del (T[2][T[2].index(k)])								
								if c == 4:
									J = []
									for i in regles(T[3],S,coul,p):
										J += [(T[3][i])]				
									k = random.choice(minmaxsimplifie(J,S,Ss,coul,p,1)) 
									n = G4.index(k)
									carte = association(k)[1]
									if n == 0:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (475,390))
										fenetre.blit(carte, (395,300))
										pygame.display.flip()
									if n == 1:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (475,330))
										fenetre.blit(carte, (395,300))
										pygame.display.flip()
									if n == 2:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (475,270))
										fenetre.blit(carte, (395,300))
										pygame.display.flip()
									if n == 3:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (475,210))
										fenetre.blit(carte, (395,300))
										pygame.display.flip()
									if n == 4:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (555,390))
										fenetre.blit(carte, (395,300))
										pygame.display.flip()
									if n == 5:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (555,330))
										fenetre.blit(carte, (395,300))
										pygame.display.flip()
									if n == 6:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (555,270))
										fenetre.blit(carte, (395,300))
										pygame.display.flip()
									if n == 7:
										pygame.time.delay(500)
										fenetre.blit(carte_verte_horizontale, (555,210))
										fenetre.blit(carte, (395,300))
										pygame.display.flip()			
									S += [k]
									Ss += [k]
									del (T[3][T[3].index(k)])
							
							pygame.time.delay(250)

							fenetre.blit(coul_verte, (450,580))
							fenetre.blit(coul_verte, (100,445))
							fenetre.blit(coul_verte, (130,150))
							fenetre.blit(coul_verte, (560,150))
							pygame.display.flip()
							fenetre.blit(carte_verte_verticale, (300,185))
							fenetre.blit(carte_verte_verticale, (300,395))
							fenetre.blit(carte_verte_horizontale, (395,300))
							fenetre.blit(carte_verte_horizontale, (185,300))
							pygame.display.flip()
							pygame.time.delay(250)
							
							q = ( cartelaplusforte(S,coul)[1] + x - 1) % 4 + 1		
							if q == 1:
								S1 += S
							if q == 2:
								S2 += S
							if q == 3:
								S3 += S
							if q == 4:
								S4 += S
							x=q
							
						fenetre.blit(fond,(0,0))
						pygame.display.flip()
						
						"Decompte des points"
					
						total1 = sum (valeurcartes(S1,coul).values())					#points gagnes par le joueur 1
						total2 = sum (valeurcartes(S2,coul).values())
						total3 = sum (valeurcartes(S3,coul).values())
						total4 = sum (valeurcartes(S4,coul).values())
						
						if p == 1:											#dix de der
							total1 += 10
						if p == 2:
							total2 += 10
						if p == 3:
							total3 += 10
						if p == 4:
							total4 += 10
						
						totalequipe1 = total1 + total3							#points gagnes par l'equipe 1 lors de cette manche
						totalequipe2 = total2 + total4
						
						totalequipe1entout += totalequipe1
						totalequipe2entout += totalequipe2
						
						text1 = font.render("L'equipe 1 a {0} points.".format(totalequipe1), 1, (10, 10, 10))
						text2 = font.render("L'equipe 2 a {0} points.".format(totalequipe2), 1, (10, 10, 10))
						x = fond.get_rect().centerx
						y = fond.get_rect().centery
						fenetre.blit(text1, (x-190,y-25))
						fenetre.blit(text2, (x-190,y+25))
						pygame.display.flip()
						pygame.time.delay(3000)
						fenetre.blit(fond,(0,0))
						pygame.display.flip()
						
						if b in [1,3]: 										#b est le numero du joueur qui a pris l'atout
							if totalequipe1 > totalequipe2:
								fenetre.blit(victoire_equipe1, (0,225))
							else:
								fenetre.blit(victoire_equipe2, (0,225))
						
						if b in [2,4]:
							if totalequipe2 > totalequipe1:
								fenetre.blit(victoire_equipe2, (0,225))
							else:
								fenetre.blit(victoire_equipe1, (0,225))
						pygame.display.flip()
					
					pygame.time.delay(2500)
					fenetre.blit(fond, (0,0))
					text1 = font.render("Au total, l'equipe 1 a {0} points.".format(totalequipe1entout), 1, (10, 10, 10))
					text2 = font.render("Au total, l'equipe 2 a {0} points.".format(totalequipe2entout), 1, (10, 10, 10))
					x = fond.get_rect().centerx
					y = fond.get_rect().centery
					fenetre.blit(text1, (x-265,y-25))
					fenetre.blit(text2, (x-265,y+25))
					pygame.display.flip()
					
					pygame.time.delay(3000)
					fenetre.blit(fond, (0,0))
					fenetre.blit(voulez_vous_continuer_a_jouer, (0,150))
					fenetre.blit(oui, (100,400))
					fenetre.blit(non, (350,400))
					pygame.display.flip()
					temp = 0
					while temp == 0:
						for event in pygame.event.get():
							#si on veut fermer la fenetre
							if event.type == QUIT:
								temp = 1
								bouclinf = 1
								continuerajouer = 1
							#si on appuie sur non, afficher le resultat final
							if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 550 and event.pos[0] > 350 and event.pos[1] < 550 and event.pos[1] > 400:
								temp = 1
								bouclinf = 1
								continuerajouer = 1
								pygame.time.delay(250)
								fenetre.blit(fond, (0,0))
								if totalequipe1entout > totalequipe2entout:
									fenetre.blit(victoire_finale, (0,0))
									victoire_son.play()
									pygame.display.flip()
									pygame.time.delay(3109)
								if totalequipe1entout < totalequipe2entout:
									fenetre.blit(defaite_finale, (0,0))
									defaite_son.play()
									pygame.display.flip()
									pygame.time.delay(2952)
								if totalequipe1entout == totalequipe2entout:
									fenetre.blit(egalite_parfaite, (0,0))
									pygame.display.flip()
									pygame.time.delay(2000)
								pygame.display.flip()
							#si on appuie sur oui, on recommence
							if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 300 and event.pos[0] > 100 and event.pos[1] < 550 and event.pos[1] > 400 :
								continuerajouer = 0
								temp = 1
							
					
				
					


