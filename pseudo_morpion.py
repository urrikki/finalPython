#DEBUT
#on admet la fonction tkinter qui permet de créér une interface graphique
#on admet la fonction messagebox de tkinter qui permet d'afficher un petit message
#on admet la fonction global qui permet de transmettre des variable local a tous le code sans les retourner
#on admet la fonction event qui permet de remarquer un click avec la souris 
#on admet la fonction showinfo qui crée une fentre qui affiche un message


#crée un tableau plateau [ [0, 0, 0],[0, 0, 0],[0, 0, 0]]
#variable quiJoue , un boolen definis a True
#variable nTour defini a 1  

#definir afficher qui affichera tour par tour les croix, rond et messages (event)
    #attribuer les variables quiJoue , plateau , nTour en global 

    #variable l qui recupere l'abscisse grace a event
    #en windows il existe un decalage de 2 pixel on soustrais alors l par 2
    # afin d'obtenir son numero de colonne on la double divise par 100 afin d'obtenir son quotient entier 
    #variable c qui recupere l'ordonné grace a event
    #en windows il existe un decalage de 2 pixel on soustrais alors c par 2
    # afin d'obtenir son numero de ligne on la double divise par 100 afin d'obtenir son quotient entier               
                       
    #si nTour est inferieur a 10 et plateau[l][c] est egal à 0
        #alors 
        #si quiJoue est vrai
            #on dessine une ligne (100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = '#26583a')                            
            #on dessine une ligne (100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = '#26583a')
            #plateau[l][c] apprend 1
            #on affiche le message Aux tour des ronds :
            #quiJoue est faux
        
        #sinon   
            #on dessine un oval (100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = '#b61b1c')
            #plateau[l][c] apprend -1
            #on affiche le message Aux tour des croix :
            #quiJoue est vrai
        
        #si nTour est superieur ou egal à 5 et nTour est inferieur ou egal a 9
            #variable v contenant la valeur retourner de verif(plateau)
            #si v est egal a 1 ou v est egal a -1
                #alors
                #executer la fonction gagner(v)
            #sinon si v est egal a 9
                #executer la fonction gagner(0)
        #on acremente nTour de 1        

#definir la fonctin verif qui retourne une valeur en fonction du resultat du match
    #variable test defini à 0 
    #pour i de 0 à 3
        #pour i2 de 0 à 3
            #si tableau[i][i2] est different de 0
                #on acremente test de 1
    #si test est egal à 9
        #si (tableau[0][0] + tableau[0][1] + tableau[0][2]) == 3 ou (tableau[1][0] + tableau[1][1] + tableau[1][2])== 3 ou (tableau[2][0] + tableau[2][1] + tableau[2][2])==3 ou (tableau[0][0] + tableau[1][0] + tableau[2][0]) == 3 ou (tableau[0][1] + tableau[1][1] + tableau[2][1]) == 3 ou (tableau[0][2] + tableau[1][2] + tableau[2][2]) == 3 ou (tableau[0][0] + tableau[1][1] + tableau[2][2]) == 3 ou (tableau[0][2] + tableau[1][1] + tableau[2][0])== 3
            #retourner 1
        #sinon si (tableau[0][0] + tableau[0][1] + tableau[0][2]) == -3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== -3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==-3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == -3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == -3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == -3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == -3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== -3
            #retourner -1
        #retourner 9
    #sinon
        #si (tableau[0][0] + tableau[0][1] + tableau[0][2]) == 3 ou (tableau[1][0] + tableau[1][1] + tableau[1][2])== 3 ou (tableau[2][0] + tableau[2][1] + tableau[2][2])==3 ou (tableau[0][0] + tableau[1][0] + tableau[2][0]) == 3 ou (tableau[0][1] + tableau[1][1] + tableau[2][1]) == 3 ou (tableau[0][2] + tableau[1][2] + tableau[2][2]) == 3 ou (tableau[0][0] + tableau[1][1] + tableau[2][2]) == 3 ou (tableau[0][2] + tableau[1][1] + tableau[2][0])== 3
            #retourner 1
        #sinon si (tableau[0][0] + tableau[0][1] + tableau[0][2]) == -3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== -3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==-3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == -3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == -3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == -3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == -3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== -3
            #retourner -1

#definirla fonction gagner qui retourn une un message via showinfo par rapport au a que on lui donne
    #si a est egal a 1
        #alors
        #showinfo(title='Victoire',message='Les croix ont gagné !')
    #sinon si a est egal a -1
        #alors
        #showinfo(title='Victoire',message='Les ronds ont gagné !')
    #sinon si a est egal a 0
        #showinfo(title='Egalité',message='Match nul !')

#definir la fonction reinitialisation qui remet tout les parametre de base
    
    #attribuer les variables quiJoue , plateau , nTour en global
    #crée un tableau plateau [ [0, 0, 0],[0, 0, 0],[0, 0, 0]]
    #variable quiJoue , un boolen definis a True 
    #variable nTour defini a 1         

    #on affiche le message Aux tour des croix :
    #on supprime tous les dessins
    #on definie le tableau ligne comme vide      
    #pour i de 0 à 4
      #le tableau ligne apprend (dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3 , fill='#d68839'))
      #le tableau ligne apprend (dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3 , fill='#d68839'))
#on crée une fenetre dans la variable fen
#le titre de cette fenetre est morpion

#crée la variable message qui ecris Aux tour des croix :
#on definie la position du message (row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)

#créé un bouton bouton_quitter qui permet de detruire la fenetre
#on definie la taille du bouton 

#créé un bouton bouton_reload qui permet de reinitialiser la fenetre
#on definie la taille du bouton

#on créé le plateau de jeu 
#on definie la taille du plateau 

#on cree un tableau lignes vides

#definir la fonction bind qui detecte un click de souris et quand il se detecte la fonction affficher s'execute

#executer reinitialisation

#executer la fenetre

#exit on click qui permet de toute fermer des que on appuie sur la croix
#FIN