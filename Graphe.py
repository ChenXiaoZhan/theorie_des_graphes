# -*- coding: utf-8 -*-

print 'Selectionner le nom du fichier:'
Nom_du_fichier = raw_input() #raw_input recupère les entrées du type string
with open(Nom_du_fichier,'r') as file: #la commande 'with open' permet de fermer le file apres la lecture
    all_data = file.readlines() #readlines permet de recuperer l'ensembre d'elements dans le file
    print all_data

nombre_de_sommets = all_data[0][:-1]
nombre_de_arcs = all_data[1][:-1]

print('il y a {} sommets'.format(nombre_de_sommets))
print('et {} arcs dans ce graphe, et ils sont:'.format(nombre_de_arcs))

for i in range(2,int(nombre_de_arcs)+2):
    print(all_data[i].split(" ")[0]+'-->' + all_data[i].split(" ")[1]+ " = " +all_data[i].split(" ")[2][:-1])

print("")
print('Représentation du graphe sous forme matricielle')
print('Matrice d’adjacence')

sommet = int(nombre_de_sommets)
arc = int(nombre_de_arcs)



matrice_adj = [[0 for x in range(sommet)] for y in range(sommet)] #on déclare une matrice de dimension sommet*sommet,
#et initialise tous les éléments = 0

matrice_valeur_des_arcs = [['*' for x in range(sommet)] for y in range(sommet)]



arc_depart = list()
arc_arrivee = list()
valeur_des_arcs=list()

for i in range(2,int(nombre_de_arcs)+2):
    arc_depart.append(all_data[i].split(" ")[0])
    arc_arrivee.append(all_data[i].split(" ")[1])
    valeur_des_arcs.append(all_data[i].split(" ")[2][:-1])

for i in range(0,len(arc_depart)):
    de = int(arc_depart[i])
    vers = int(arc_arrivee[i])
    matrice_adj[de][vers] = 1


print(' '),
for j in range(0,sommet):
    print('  ' + (str(j))),
print


for ligne in range(sommet):
    print(str(ligne)),
    for col in range(sommet):
        print('  '+str(matrice_adj[ligne][col])),
    print

print
print
print('Matrice d’adjacence')
print(' '),
for j in range(0,sommet):
    print('  ' + (str(j))),
print

for i in range(0,len(arc_depart)):
    de = int(arc_depart[i])
    vers = int(arc_arrivee[i])
    valeur = int(valeur_des_arcs[i])
    matrice_valeur_des_arcs[de][vers] = valeur

for ligne in range(sommet):
    print(str(ligne)),
    for col in range(sommet):
        print('  '+str(matrice_valeur_des_arcs[ligne][col])),
    print

print
print
print('Détection de circuit méthode de Roy-Warshal (fermeture transitive)')

matrice_fermeture_transitive = [[0 for x in range(sommet)] for y in range(sommet)]

for i in range(sommet):
    for j in range(sommet):
        matrice_fermeture_transitive[i][j] = matrice_adj[i][j] = matrice_adj[i][j]

for k in range(sommet):
    for i in range(sommet):
        for j in range(sommet):
            matrice_fermeture_transitive[i][j] = matrice_fermeture_transitive[i][j] or (matrice_fermeture_transitive[i][k] and matrice_fermeture_transitive[k][j])


print('matrice de fermeture transitive')
print

for ligne in range(sommet):
    for col in range(sommet):
        print('  '+str(matrice_fermeture_transitive[ligne][col])),
    print

print

somme_diagonale=0
for row in range(sommet):
    somme_diagonale += matrice_fermeture_transitive[row][row]

if somme_diagonale == 0:
    print("il n'y a pas de circuit dans ce graphe")
    print
    print('On peut donc calculer le rang de chaque sommet')
    print('Méthode d’élimination des points d’entrée')
    liste_de_tous_les_rang = list(str(x) for x in range(sommet))

    arc_arrivee_copie = arc_arrivee
    arc_depart_copie = arc_depart

    racine = [item for item in liste_de_tous_les_rang if item not in arc_arrivee_copie]

    print racine
    count=0
    print 'Rang courant = '+ str(count)
    print "point d'entrée: " + str(racine)
    print

    new_racine = racine
    arc_arrivee_tempor = list()
    element_du_rang = list()
    de_vers = {}

    for i in range(len(arc_depart_copie)):
        if arc_depart_copie[i] in de_vers:
            de_vers[arc_depart_copie[i]].append(arc_arrivee_copie[i])
        else :
            list_de_valeurs=[]
            list_de_valeurs.append(arc_arrivee_copie[i])
            de_vers[arc_depart_copie[i]]=list_de_valeurs
    #print (de_vers)

    while len(de_vers.keys()) != 0:
        count = count + 1
        for ra in new_racine:
            if ra in de_vers.keys():
                del de_vers[ra]
        del arc_arrivee_tempor[:]
        for i in de_vers.values():
            for j in i:
                arc_arrivee_tempor.append(j)
        element_du_rang = [x for x in arc_arrivee_copie if x not in arc_arrivee_tempor]
        arc_arrivee_copie = list(arc_arrivee_tempor)
        new_racine = list(element_du_rang)
        print 'Rang courant = ' + str(count)
        print 'Points d’entrée : '+str(set(element_du_rang))


    print
    print
    print "on va vérifier si le graphe est un graphe d’ordonnancement"
    print "les caractères pour un graphe d’ordonnancement sont les suivants: "
    print " - un seul point d’entrée"
    print " - un seul point de sortie"
    print " - absence de circuit"
    print " - valeurs identiques pour tous les arcs incidents vers l’extérieur à un sommet"
    print " - arcs incidents vers l’extérieur au point d’entrée de valeur nulle"
    print " - pas d’arc à valeur négative"
    print
    print
    print "pour ce graphe, on a les caractère suivant:"


    les_point_entree = list()
    les_point_arrive = list()
    les_valeur_arc = list()

    for i in range(2, int(nombre_de_arcs) + 2):
        les_point_entree.append(all_data[i].split(" ")[0])
        les_point_arrive.append(all_data[i].split(" ")[1])
        les_valeur_arc.append(all_data[i].split(" ")[2][:-1])

    #print les_point_entree
    #print les_point_arrive
    #print les_valeur_arc

    copie_les_point_entree = les_point_entree[:]
    copie_les_point_arrive = les_point_arrive[:]

    for element in copie_les_point_entree:
        if element in copie_les_point_arrive:
            les_point_entree.remove(element)

    for element_arrive in copie_les_point_arrive:
        if element_arrive in copie_les_point_entree:
            les_point_arrive.remove(element_arrive)

    #print set(les_point_entree)
    #print set(les_point_arrive)

    len_les_point_entree = len(set(les_point_entree))
    len_les_point_arrive = len(set(les_point_arrive))

    print("nombre de points d'entrée: {}".format(len_les_point_entree))
    print("nombre de points d'arrivé: {}".format(len_les_point_arrive))
    print "pas de circuit"



    index_of_zero = list()
    for i, j in enumerate(copie_les_point_entree):
        if j == '0':
            index_of_zero.append(i)


    value_arc_zero = list()
    for i in index_of_zero:
        value_arc_zero.append(les_valeur_arc[i])

    value_arc_zero_bool = None
    if set(value_arc_zero) == set(['0']):
        value_arc_zero_bool = True

    print ("arcs incidents vers l’extérieur au point d’entrée de valeur nulle : {}".format(value_arc_zero_bool))

    #print value_arc_zero_bool

    groupe_entree_and_valeur = zip(copie_les_point_entree,les_valeur_arc)
    #print set(groupe_entree_and_valeur)

    first_elements_of_zip = zip(*set(groupe_entree_and_valeur))[0]
    #print first_elements_of_zip

    value_arcs_bool = None
    if len(first_elements_of_zip) == len(set(groupe_entree_and_valeur)):
        value_arcs_bool = True

    #print value_arc_bool
    print ("valeurs identiques pour tous les arcs incidents vers l’extérieur à un sommet : {}".format(value_arcs_bool))

    value_arcs_int = list()

    for i in les_valeur_arc:
        integer = int(i,10)
        value_arcs_int.append(integer)


    #print value_arcs_int

    value_arcs_int_bool = True
    for i in value_arcs_int:
        if i<0:
            value_arcs_int_bool = False
            break

    print ("pas d’arc à valeur négative : {}".format(value_arcs_int_bool))

    if ((len_les_point_entree==1) and (len_les_point_arrive==1) and (value_arc_zero_bool) and (value_arcs_bool) and (value_arcs_int_bool)) :
        print '-----------------------------------------------------------------------------------'
        print "ce graphe est un graphe d'ordonancement correct"
        print "on peut calculer les dates au plus tôt et les dates au plus tard"
        print '-----------------------------------------------------------------------------------'

    else:
        print '------------------------------------------------------------------------------------'
        print "ce graphe n'est pas un graphe d'ordonancement correct"
        print '------------------------------------------------------------------------------------'






else:
    print '------------------------------------------------------------------------------------'
    print 'il exsite au moins un circuit dans ce graphe'
    print "ce graphe n'est pas un graphe d'ordonancement correct"
    print '------------------------------------------------------------------------------------'


