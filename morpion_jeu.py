#DEBUT
#on admet la fonction tkinter qui permet de créér une interface graphique
from tkinter import *
#on admet la fonction messagebox de tkinter qui permet d'afficher un petit message
from tkinter.messagebox import *
#on admet la fonction global qui permet de transmettre des variable local a tous le code sans les retourner
#on admet la fonction event qui permet de remarquer un click avec la souris 
#on admet la fonction showinfo qui crée une fentre qui affiche un message
import random


#crée un tableau plateau [ [0, 0, 0],[0, 0, 0],[0, 0, 0]]
plateau=[ [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
#variable quiJoue , un boolen definis a True
quiJoue = True
w = 1
#variable nTour defini a 1                              
nTour = 1 
rOrJ = w                                     

#definir afficher qui affichera tour par tour les croix, rond et messages (event)
def afficher(event) :
    #attribuer les variables quiJoue , plateau , nTour en global 
    global quiJoue, plateau, nTour ,w ,rOrJ

    


    #variable l qui recupere l'abscisse grace a event
    #en windows il existe un decalage de 2 pixel on soustrais alors l par 2
    # afin d'obtenir son numero de colonne on la double divise par 100 afin d'obtenir son quotient entier 
    l = (event.y-2)//100
    #variable c qui recupere l'ordonné grace a event
    #en windows il existe un decalage de 2 pixel on soustrais alors c par 2
    # afin d'obtenir son numero de ligne on la double divise par 100 afin d'obtenir son quotient entier               
    c = (event.x-2)//100
                       
    #si nTour est inferieur a 10 et plateau[l][c] est egal à 0

    if (nTour < 10) and (plateau[l][c] == 0):
        #alors 
        #si quiJoue est vrai
        if quiJoue == True :
            #on dessine une ligne (100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = '#26583a')                            
            dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = '#26583a')
            #on dessine une ligne (100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = '#26583a')
            dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = '#26583a')
            #plateau[l][c] apprend 1
            plateau[l][c] = 1
            #on affiche le message Aux tour des ronds :
            message.configure(text='Aux tour des ronds :')
            #quiJoue est faux
            quiJoue = False
            rOrJ = w
        
        #sinon   
        elif rOrJ == 1 :
            #on dessine un oval (100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = '#b61b1c')
            dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = '#b61b1c')
            #plateau[l][c] apprend -1
            plateau[l][c] = -1
            #on affiche le message Aux tour des croix :
            message.configure(text='Aux tour des croix :')
            #quiJoue est vrai
            quiJoue = True
            rOrJ = 0

        #si nTour est superieur ou egal à 5 et nTour est inferieur ou egal a 9
        if (nTour >= 5) and (nTour <= 9):
            #variable v contenant la valeur retourner de verif(plateau)
            v=verif(plateau)
            #si v est egal a 1 ou v est egal a -1
            if v == 1 or v == -1:
                #alors
                #executer la fonction gagner(v)
                gagner(v)
            #sinon si v est egal a 9
            elif v == 9:
                #executer la fonction gagner(0)
                gagner(0)
        #on acremente nTour de 1        
        nTour += 1
        print(plateau[0])
        print(plateau[1])
        print(plateau[2])

modif=True
def ai():
    global quiJoue, w , nTour , rOrJ , modif
    aJouer = False
    
    
    if modif == True and nTour < 3:
        modif = False
        w = 2
        rOrJ = w

    print(rOrJ)
    if rOrJ == 2 : 
        #first side
        if nTour < 3 and plateau[1][1] == 0:
            dessin.create_oval(100*1+8, 100*1+8, 100*1+96, 100*1+96, width = 5, outline = '#b61b1c')
            plateau[1][1] = -1
            message.configure(text='Aux tour des croix :')
            quiJoue = True
            rOrJ = 0
            aJouer = True

        
        #win side
        if aJouer == False:
            if (plateau[0][0] + plateau[0][1]) == -2 or (plateau[0][0] + plateau[0][2]) == -2 or (plateau[0][1] + plateau[0][2]) == -2:
                for i2 in range(0,3):
                    if plateau[0][i2] == 0:
                        print("1")
                        dessin.create_oval(100*i2+8, 100*0+8, 100*i2+96, 100*0+96, width = 5, outline = '#b61b1c')
                        plateau[0][i2] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        if aJouer == False:
            if (plateau[1][0] + plateau[1][1]) == -2 or (plateau[1][0] + plateau[1][2]) == -2 or (plateau[1][1] + plateau[1][2]) == -2:
                for i2 in range(0,3):
                    if plateau[1][i2] == 0:
                        print("2")
                        dessin.create_oval(100*i2+8, 100*1+8, 100*i2+96, 100*1+96, width = 5, outline = '#b61b1c')
                        plateau[1][i2] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        if aJouer == False:
            if (plateau[2][0] + plateau[2][1]) == -2 or (plateau[2][0] + plateau[2][2]) == -2 or (plateau[2][1] + plateau[2][2]) == -2:
                for i2 in range(0,3):
                    if plateau[2][i2] == 0:
                        print("3")
                        dessin.create_oval(100*i2+8, 100*2+8, 100*i2+96, 100*2+96, width = 5, outline = '#b61b1c')
                        plateau[2][i2] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        
        if aJouer == False:
            if (plateau[0][0] + plateau[1][0]) == -2 or (plateau[0][0] + plateau[2][0]) == -2 or (plateau[1][0] + plateau[2][0]) == -2:
                for i in range(0,3):
                    if plateau[i][0] == 0:
                        print("4")
                        dessin.create_oval(100*0+8, 100*i+8, 100*0+96, 100*i+96, width = 5, outline = '#b61b1c')
                        plateau[i][0] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        if aJouer == False:
            if (plateau[0][1] + plateau[1][1]) == -2 or (plateau[0][1] + plateau[2][1]) == -2 or (plateau[1][1] + plateau[2][1]) == -2:
                for i in range(0,3):
                    if plateau[i][1] == 0:
                        print("5")
                        dessin.create_oval(100*1+8, 100*i+8, 100*1+96, 100*i+96, width = 5, outline = '#b61b1c')
                        plateau[i][1] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        if aJouer == False:
            if (plateau[0][2] + plateau[1][2]) == -2 or (plateau[0][2] + plateau[2][2]) == -2 or (plateau[1][2] + plateau[2][2]) == -2:
                for i in range(0,3):
                    if plateau[i][2] == 0:
                        print("6")
                        dessin.create_oval(100*2+8, 100*i+8, 100*2+96, 100*i+96, width = 5, outline = '#b61b1c')
                        plateau[i][2] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        
        if aJouer == False:
            if (plateau[0][0] + plateau[0][1]) == -2 or (plateau[0][0] + plateau[0][2]) == -2 or (plateau[0][1] + plateau[0][2]) == -2:
                for i in range(0,3):
                    for i2 in range(0,3):
                        if (i == 0 and i2 == 0) or (i == 1 and i2 == 1) or (i == 2 and i2 == 2) :
                            if plateau[i][i2] == 0:
                                if d==True:
                                    d=False
                                    print("7")
                                    dessin.create_oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                    plateau[i][i2] = -1
                                    message.configure(text='Aux tour des croix :')
                                    quiJoue = True
                                    rOrJ = 0
                                    aJouer = True
        
        if aJouer == False:
            d=True
            if (plateau[0][2] + plateau[1][1]) == -2 or (plateau[0][2] + plateau[2][0]) == -2 or (plateau[1][1] + plateau[2][0]) == -2:
                for i in range(0,3):
                    for i2 in range(0,3):
                        if (i == 0 and i2 == 2) or (i == 1 and i2 == 1) or (i == 2 and i2 == 0) :
                            if plateau[i][i2] == 0:
                                print("8")
                                dessin.create_oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                plateau[i][i2] = -1
                                message.configure(text='Aux tour des croix :')
                                quiJoue = True
                                rOrJ = 0
                                aJouer = True
        
        #counter side
        if aJouer == False:
            if (plateau[0][0] + plateau[0][1]) == 2 or (plateau[0][0] + plateau[0][2]) == 2 or (plateau[0][1] + plateau[0][2]) == 2:
                for i2 in range(0,3):
                    if plateau[0][i2] == 0:
                        print("9")
                        dessin.create_oval(100*i2+8, 100*0+8, 100*i2+96, 100*0+96, width = 5, outline = '#b61b1c')
                        plateau[0][i2] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        
        if aJouer == False:
            if (plateau[1][0] + plateau[1][1]) == 2 or (plateau[1][0] + plateau[1][2]) == 2 or (plateau[1][1] + plateau[1][2]) == 2:
                for i2 in range(0,3):
                    if plateau[1][i2] == 0:
                        print("10")
                        dessin.create_oval(100*i2+8, 100*1+8, 100*i2+96, 100*1+96, width = 5, outline = '#b61b1c')
                        plateau[1][i2] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        
        if aJouer == False:
            if (plateau[2][0] + plateau[2][1]) == 2 or (plateau[2][0] + plateau[2][2]) == 2 or (plateau[2][1] + plateau[2][2]) == 2:
                for i2 in range(0,3):
                    if plateau[2][i2] == 0:
                        print("11")
                        dessin.create_oval(100*i2+8, 100*2+8, 100*i2+96, 100*2+96, width = 5, outline = '#b61b1c')
                        plateau[2][i2] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        
        if aJouer == False:
            if (plateau[0][0] + plateau[1][0]) == 2 or (plateau[0][0] + plateau[2][0]) == 2 or (plateau[1][0] + plateau[2][0]) == 2:
                for i in range(0,3):
                    if plateau[i][0] == 0:
                        print("13")
                        dessin.create_oval(100*0+8, 100*i+8, 100*0+96, 100*i+96, width = 5, outline = '#b61b1c')
                        plateau[i][0] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        if aJouer == False:
            if (plateau[0][1] + plateau[1][1]) == 2 or (plateau[0][1] + plateau[2][1]) == 2 or (plateau[1][1] + plateau[2][1]) == 2:
                for i in range(0,3):
                    if plateau[i][1] == 0:
                        print("14")
                        dessin.create_oval(100*1+8, 100*i+8, 100*1+96, 100*i+96, width = 5, outline = '#b61b1c')
                        plateau[i][1] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        if aJouer == False:
            if (plateau[0][2] + plateau[1][2]) == 2 or (plateau[0][2] + plateau[2][2]) == 2 or (plateau[1][2] + plateau[2][2]) == 2:
                for i in range(0,3):
                    if plateau[i][2] == 0:
                        print("15")
                        dessin.create_oval(100*2+8, 100*i+8, 100*2+96, 100*i+96, width = 5, outline = '#b61b1c')
                        plateau[i][2] = -1
                        message.configure(text='Aux tour des croix :')
                        quiJoue = True
                        rOrJ = 0
                        aJouer = True
        
        if aJouer == False:
            d=True
            if (plateau[0][0] + plateau[1][1]) == 2 or (plateau[0][0] + plateau[2][2]) == 2 or (plateau[1][1] + plateau[2][2]) == 2:
                for i in range(0,3):
                    for i2 in range(0,3):
                        if plateau[i][i2] == 0:
                            if (i == 0 and i2 == 0) or (i == 1 and i2 == 1) or (i == 2 and i2 == 2) :
                                if d == True:
                                    d=False
                                    print("16")
                                    dessin.create_oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                    plateau[i][i2] = -1
                                    message.configure(text='Aux tour des croix :')
                                    quiJoue = True
                                    rOrJ = 0
                                    aJouer = True
            
        if aJouer == False:
            d=True
            if (plateau[0][2] + plateau[1][1]) == 2 or (plateau[0][2] + plateau[2][0]) == 2 or (plateau[1][1] + plateau[2][0]) == 2:
                for i in range(0,3):
                    for i2 in range(0,3):
                        if (i == 0 and i2 == 2) or (i == 1 and i2 == 1) or (i == 2 and i2 == 0) :
                            if plateau[i][i2] == 0:
                                if d == True:
                                    d=False
                                    print("17")
                                    print(i,i2)
                                    dessin.create_oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                    plateau[i][i2] = -1
                                    message.configure(text='Aux tour des croix :')
                                    quiJoue = True
                                    rOrJ = 0
                                    aJouer = True
        
        #opposite side
        if aJouer == False:
            if plateau[0][0] == 1 : 
                if plateau[2][2] == 0:
                    print("18")
                    dessin.create_oval(100*2+8, 100*2+8, 100*2+96, 100*2+96, width = 5, outline = '#b61b1c')
                    plateau[2][2] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[2][2] == 1 :
                if plateau[0][0] == 0:
                    print("19")
                    dessin.create_oval(100*0+8, 100*0+8, 100*0+96, 100*0+96, width = 5, outline = '#b61b1c')
                    plateau[0][0] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True

        if aJouer == False:
            if plateau[0][2] == 1 : 
                if plateau[2][0] == 0:
                    print("20")
                    dessin.create_oval(100*0+8, 100*2+8, 100*0+96, 100*2+96, width = 5, outline = '#b61b1c')
                    plateau[2][0] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[2][0] == 1 : 
                if plateau[0][2] == 0:
                    print("21")
                    dessin.create_oval(100*2+8, 100*0+8, 100*2+96, 100*0+96, width = 5, outline = '#b61b1c')
                    plateau[0][2] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[0][1] == 1 : 
                if plateau[2][1] == 0:
                    print("22")
                    dessin.create_oval(100*1+8, 100*2+8, 100*1+96, 100*2+96, width = 5, outline = '#b61b1c')
                    plateau[2][1] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[2][1] == 1 : 
                if plateau[0][1] == 0:
                    print("23")
                    dessin.create_oval(100*1+8, 100*0+8, 100*1+96, 100*0+96, width = 5, outline = '#b61b1c')
                    plateau[0][1] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[1][0] == 1 : 
                if plateau[1][2] == 0:
                    print("24")
                    dessin.create_oval(100*2+8, 100*1+8, 100*2+96, 100*1+96, width = 5, outline = '#b61b1c')
                    plateau[1][2] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[1][2] == 1 : 
                if plateau[1][0] == 0:
                    print("25")
                    dessin.create_oval(100*0+8, 100*1+8, 100*0+96, 100*1+96, width = 5, outline = '#b61b1c')
                    plateau[1][0] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        #milieux
        if aJouer == False:
            if plateau[1][1] == 1 :
                i=random.randint(0,2)
                i2=random.randint(0,2)
                while plateau[i][i2] != 0 or (i == 0 and i2 == 1) or (i == 1 and i2 == 0) or (i == 2 and i2 == 1) or (i == 1 and i2 == 2) :
                    i=random.randint(0,2)
                    i2=random.randint(0,2)
                dessin.create_oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                plateau[i][i2] = -1
                message.configure(text='Aux tour des croix :')
                quiJoue = True
                rOrJ = 0
                aJouer = True
        
        #random
        if aJouer == False:
            i=random.randint(0,2)
            i2=random.randint(0,2)
            while plateau[i][i2] != 0 or (i == 0 and i2 == 0) or (i == 0 and i2 == 2) or (i == 2 and i2 == 0) or (i == 2 and i2 == 0) or (i == 2 and i2 == 2):
                i=random.randint(0,2)
                i2=random.randint(0,2)
            print("26")
            dessin.create_oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
            plateau[i][i2] = -1
            message.configure(text='Aux tour des croix :')
            quiJoue = True
            rOrJ = 0
            aJouer = True

        #si nTour est superieur ou egal à 5 et nTour est inferieur ou egal a 9
        if (nTour >= 5) and (nTour <= 9):
            #variable v contenant la valeur retourner de verif(plateau)
            v=verif(plateau)
            #si v est egal a 1 ou v est egal a -1
            if v == 1 or v == -1:
                #alors
                #executer la fonction gagner(v)
                gagner(v)
            #sinon si v est egal a 9
            elif v == 9:
                #executer la fonction gagner(0)
                gagner(0)
        #on acremente nTour de 
        nTour += 1
        print(rOrJ)  
        print(plateau[0])
        print(plateau[1])
        print(plateau[2])
            
                            
#definir la fonctin verif qui retourne une valeur en fonction du resultat du match
def verif(tableau):
    #variable test defini à 0 
    test=0
    #pour i de 0 à 3
    for i in range(3):
        #pour i2 de 0 à 3
        for i2 in range(3):
            #si tableau[i][i2] est different de 0
            if tableau[i][i2] != 0:
                #on acremente test de 1
                test+=1
    #si test est egal à 9
    if test == 9:
        #si (tableau[0][0] + tableau[0][1] + tableau[0][2]) == 3 ou (tableau[1][0] + tableau[1][1] + tableau[1][2])== 3 ou (tableau[2][0] + tableau[2][1] + tableau[2][2])==3 ou (tableau[0][0] + tableau[1][0] + tableau[2][0]) == 3 ou (tableau[0][1] + tableau[1][1] + tableau[2][1]) == 3 ou (tableau[0][2] + tableau[1][2] + tableau[2][2]) == 3 ou (tableau[0][0] + tableau[1][1] + tableau[2][2]) == 3 ou (tableau[0][2] + tableau[1][1] + tableau[2][0])== 3
        if (tableau[0][0] + tableau[0][1] + tableau[0][2]) == 3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== 3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == 3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == 3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == 3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == 3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== 3:
            #retourner 1
            return 1
        #sinon si (tableau[0][0] + tableau[0][1] + tableau[0][2]) == -3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== -3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==-3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == -3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == -3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == -3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == -3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== -3
        elif (tableau[0][0] + tableau[0][1] + tableau[0][2]) == -3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== -3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==-3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == -3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == -3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == -3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == -3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== -3:
            #retourner -1
            return -1
        #retourner 9
        return 9
    #sinon
    else:
        #si (tableau[0][0] + tableau[0][1] + tableau[0][2]) == 3 ou (tableau[1][0] + tableau[1][1] + tableau[1][2])== 3 ou (tableau[2][0] + tableau[2][1] + tableau[2][2])==3 ou (tableau[0][0] + tableau[1][0] + tableau[2][0]) == 3 ou (tableau[0][1] + tableau[1][1] + tableau[2][1]) == 3 ou (tableau[0][2] + tableau[1][2] + tableau[2][2]) == 3 ou (tableau[0][0] + tableau[1][1] + tableau[2][2]) == 3 ou (tableau[0][2] + tableau[1][1] + tableau[2][0])== 3
        if (tableau[0][0] + tableau[0][1] + tableau[0][2]) == 3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== 3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == 3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == 3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == 3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == 3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== 3:
            #retourner 1
            return 1
        #sinon si (tableau[0][0] + tableau[0][1] + tableau[0][2]) == -3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== -3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==-3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == -3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == -3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == -3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == -3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== -3
        elif (tableau[0][0] + tableau[0][1] + tableau[0][2]) == -3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== -3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==-3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == -3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == -3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == -3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == -3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== -3:
            #retourner -1
            return -1

#definirla fonction gagner qui retourn une un message via showinfo par rapport au a que on lui donne
def gagner(a):
    #si a est egal a 1
    if a == 1:
        #alors
        #showinfo(title='Victoire',message='Les croix ont gagné !')
        showinfo(title='Victoire',message='Les croix ont gagné !')
    #sinon si a est egal a -1
    elif a == -1:
        #alors
        #showinfo(title='Victoire',message='Les ronds ont gagné !')
        showinfo(title='Victoire',message='Les ronds ont gagné !')
    #sinon si a est egal a 0
    elif a == 0:
        #showinfo(title='Egalité',message='Match nul !')
        showinfo(title='Egalité',message='Match nul !')

#definir la fonction reinitialisation qui remet tout les parametre de base
def reinitialisation():
    
    #attribuer les variables quiJoue , plateau , nTour en global
    global quiJoue, plateau, nTour,w
    #crée un tableau plateau [ [0, 0, 0],[0, 0, 0],[0, 0, 0]]
    plateau=[ [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    #variable quiJoue , un boolen definis a True
    quiJoue = True
    w = True
    #variable nTour defini a 1                              
    nTour = 1    

    #on affiche le message Aux tour des croix :
    message.configure(text='Aux tour des croix :')
    #on supprime tous les dessins
    dessin.delete(ALL)
    #on definie le tableau ligne comme vide      
    lignes = []
    #pour i de 0 à 4
    for i in range(4):
      #le tableau ligne apprend (dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3 , fill='#d68839'))
      lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3 , fill='#d68839'))
      #le tableau ligne apprend (dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3 , fill='#d68839'))
      lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3 , fill='#d68839'))
#on crée une fenetre dans la variable fen
fen = Tk()
#le titre de cette fenetre est morpion
fen.title('Morpion')

#crée la variable message qui ecris Aux tour des croix :
message=Label(fen, text='Aux tour des croix :')
#on definie la position du message (row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)

#créé un bouton bouton_quitter qui permet de detruire la fenetre
bouton_quitter = Button(fen, text='Robot', command=ai)
#on definie la taille du bouton 
bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

#créé un bouton bouton_reload qui permet de reinitialiser la fenetre
bouton_reload = Button(fen, text='Recommencer', command=reinitialisation)
#on definie la taille du bouton
bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)

#on créé le plateau de jeu 
dessin=Canvas(fen, bg="#e1caae", width=301, height=301)
#on definie la taille du plateau 
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)

#on cree un tableau lignes vides
lignes = []

#definir la fonction bind qui detecte un click de souris et quand il se detecte la fonction affficher s'execute
dessin.bind('<Button-1>', afficher)

#executer reinitialisation
reinitialisation()

#executer la fenetre
fen.mainloop()  