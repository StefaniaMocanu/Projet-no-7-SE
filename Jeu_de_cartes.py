# 1
# Jeu de cartes (pour les points) et dictionnaire associe

couleur = ('Pique', 'Trefle', 'Carreau', 'Coeur')
valeur = (7, 8, 9, 10, 'Valet', 'Dame', 'Roi', 'As')

"Creation du jeu de cartes"

jeupoints = []
for coul in couleur:
    for val in valeur:
        jeupoints += [(val,coul)]


"Creation du dictionnaire"

def dico(coul):
    "Valeur des cartes apres choix de l'atout"
    dictio = {}
    for c in jeupoints:
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

#Dico renvoie un dictionnaire qui a chaque carte associe sa valeur apres choix de l atout