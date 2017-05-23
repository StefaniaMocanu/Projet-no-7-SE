#2
# Classe JeuDeCartes

from random import randrange

class JeuDeCartes:

    couleur = ('Pique', 'Trefle', 'Carreau', 'Coeur')
    valeur = (7, 8, 9, 10, 'Valet', 'Dame', 'Roi', 'As')

    def __init__(self):
        "Construction du jeu de 32 cartes"
        self.carte = []
        for coul in JeuDeCartes.couleur:
            for val in JeuDeCartes.valeur:
                self.carte.append((val,coul))

    def nom_carte(self,c):
        "Renvoi du nom de la carte"
        return "{0} de {1}" .format(self.valeur[c[0]],self.couleur[c[1]])

    def battre(self):
        "Melange des cartes"
        t = len(self.carte)             # nombre de cartes restantes
        for i in range(t):
            h1, h2 = randrange(t), randrange(t)
            self.carte[h1], self.carte[h2] = self.carte[h2], self.carte[h1]

    def tirer(self,n):
        "Tirage des n premieres cartes de la pile"
        L = []
        for i in range(n):
            t = len(self.carte)              # verifier qu il reste des cartes
            if t >0:
                L += [self.carte[0]]       # choisir la premiere carte du jeu
                del(self.carte[0])          # la retirer du jeu
        return L

    def couper(self):
        "Coupe"
        a = randrange(8,25)
        L = []
        for i in range(a,32):
            L += [self.carte[i]]
        for i in range(a):
            L += [self.carte[i]]
        return L

    def distribuer(self,L1,L2,L3,L4,n,k,p):
        "Tirage de n cartes par k pour quatre joueurs en commencant par le joueur p"
        for j in range(0,n,k):
            if len(self.carte) > 0:
                if (j//k)%4 == (1-p)%4:                     
                    L1 += JeuDeCartes.tirer(self,k)           
                elif (j//k)%4 == (2-p)%4:
                    L2 += JeuDeCartes.tirer(self,k)
                elif (j//k)%4 == (3-p)%4:
                    L3 += JeuDeCartes.tirer(self,k)
                else:
                    L4 += JeuDeCartes.tirer(self,k)
        return ([L1,L2,L3,L4])

# Classe: pour l initialisation de chaque partie (jeu de cartes)
# Sans classe: pour les fonctions restantes
