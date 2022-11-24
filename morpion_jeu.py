#Importation
from tkinter import *
from tkinter.messagebox import *
import random


#crétion du jeu
plateau=[ [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
quiJoue = True
w = 1                             
nTour = 1 
rOrJ = w
modif=True                                     

#definir afficher qui affichera tour par tour les croix, rond et messages (event)
def afficher(event) :
    global quiJoue, plateau, nTour ,w ,rOrJ 

    


    #variable l qui recupere l'abscisse grace a event
    #en windows il existe un decalage de 2 pixel on soustrais alors l par 2
    # afin d'obtenir son numero de colonne on la double divise par 100 afin d'obtenir son quotient entier 
    l = (event.y-2)//100
    #variable c qui recupere l'ordonné grace a event              
    c = (event.x-2)//100
                       
    #joué tant qu'il n'y a pas egalité

    if (nTour < 10) and (plateau[l][c] == 0):
        #joueur 1
        if quiJoue == True :                            
            dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = '#26583a')
            dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = '#26583a')
            plateau[l][c] = 1
            message.configure(text='Aux tour des ronds :')
            quiJoue = False
            rOrJ = w
        
        #joueur 2 
        elif rOrJ == 1 :
            dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = '#b61b1c')
            plateau[l][c] = -1
            message.configure(text='Aux tour des croix :')
            quiJoue = True
            rOrJ = 0

        #regarde si quelqu'un à gagné
        if (nTour >= 5) and (nTour <= 9):
            v=verif(plateau)
            if v == 1 or v == -1:
                gagner(v)
            elif v == 9:
                gagner(0)

        nTour += 1

#robot (cpu)
def ai():
    global quiJoue, w , nTour , rOrJ , modif
    aJouer = False
    
    #permettre au robot de jouer en premier
    if modif == True and nTour < 3:
        modif = False
        w = 2
        rOrJ = w

    if rOrJ == 2 : 
        #premier coup du robot
        if nTour < 3 and plateau[1][1] == 0:
            dessin.create_oval(100*1+8, 100*1+8, 100*1+96, 100*1+96, width = 5, outline = '#b61b1c')
            plateau[1][1] = -1
            message.configure(text='Aux tour des croix :')
            quiJoue = True
            rOrJ = 0
            aJouer = True

        
        #win action
        if aJouer == False:
            if (plateau[0][0] + plateau[0][1]) == -2 or (plateau[0][0] + plateau[0][2]) == -2 or (plateau[0][1] + plateau[0][2]) == -2:
                for i2 in range(0,3):
                    if plateau[0][i2] == 0:
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
                                dessin.create_oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                plateau[i][i2] = -1
                                message.configure(text='Aux tour des croix :')
                                quiJoue = True
                                rOrJ = 0
                                aJouer = True
        
        #counter action
        if aJouer == False:
            if (plateau[0][0] + plateau[0][1]) == 2 or (plateau[0][0] + plateau[0][2]) == 2 or (plateau[0][1] + plateau[0][2]) == 2:
                for i2 in range(0,3):
                    if plateau[0][i2] == 0:
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
                                    print(i,i2)
                                    dessin.create_oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                    plateau[i][i2] = -1
                                    message.configure(text='Aux tour des croix :')
                                    quiJoue = True
                                    rOrJ = 0
                                    aJouer = True
        
        #opposite action
        if aJouer == False:
            if plateau[0][0] == 1 : 
                if plateau[2][2] == 0:
                    dessin.create_oval(100*2+8, 100*2+8, 100*2+96, 100*2+96, width = 5, outline = '#b61b1c')
                    plateau[2][2] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[2][2] == 1 :
                if plateau[0][0] == 0:
                    dessin.create_oval(100*0+8, 100*0+8, 100*0+96, 100*0+96, width = 5, outline = '#b61b1c')
                    plateau[0][0] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True

        if aJouer == False:
            if plateau[0][2] == 1 : 
                if plateau[2][0] == 0:
                    dessin.create_oval(100*0+8, 100*2+8, 100*0+96, 100*2+96, width = 5, outline = '#b61b1c')
                    plateau[2][0] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[2][0] == 1 : 
                if plateau[0][2] == 0:
                    dessin.create_oval(100*2+8, 100*0+8, 100*2+96, 100*0+96, width = 5, outline = '#b61b1c')
                    plateau[0][2] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[0][1] == 1 : 
                if plateau[2][1] == 0:
                    dessin.create_oval(100*1+8, 100*2+8, 100*1+96, 100*2+96, width = 5, outline = '#b61b1c')
                    plateau[2][1] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[2][1] == 1 : 
                if plateau[0][1] == 0:
                    dessin.create_oval(100*1+8, 100*0+8, 100*1+96, 100*0+96, width = 5, outline = '#b61b1c')
                    plateau[0][1] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[1][0] == 1 : 
                if plateau[1][2] == 0:
                    dessin.create_oval(100*2+8, 100*1+8, 100*2+96, 100*1+96, width = 5, outline = '#b61b1c')
                    plateau[1][2] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        
        if aJouer == False:
            if plateau[1][2] == 1 : 
                if plateau[1][0] == 0:
                    dessin.create_oval(100*0+8, 100*1+8, 100*0+96, 100*1+96, width = 5, outline = '#b61b1c')
                    plateau[1][0] = -1
                    message.configure(text='Aux tour des croix :')
                    quiJoue = True
                    rOrJ = 0
                    aJouer = True
        #milieux action(corner action)
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
            while plateau[i][i2] != 0 :
                i=random.randint(0,2)
                i2=random.randint(0,2)
            dessin.create_oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
            plateau[i][i2] = -1
            message.configure(text='Aux tour des croix :')
            quiJoue = True
            rOrJ = 0
            aJouer = True

        #verifie si quelqu'un a gagné
        if (nTour >= 5) and (nTour <= 9):
            v=verif(plateau)
            if v == 1 or v == -1:
                gagner(v)
            elif v == 9:
                gagner(0)

        nTour += 1
    
    #easter egg 1
    elif rOrJ == 0 and nTour == 3:
        for i in range(0,3) :
            for i2 in range(0,3):
                if plateau[i][i2] == 1:
                    dessin.create_line(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, fill = 'gold')
                    dessin.create_line(100*i2+8, 100*i+96, 100*i2+96, 100*i+8, width = 5, fill = 'gold')

        
            
                            
#fonction qui verifie si quelqu'un a gagné
def verif(tableau):
    test=0
    for i in range(3):
        for i2 in range(3):
            if tableau[i][i2] != 0:
                test+=1
    if test == 9:
        if (tableau[0][0] + tableau[0][1] + tableau[0][2]) == 3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== 3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == 3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == 3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == 3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == 3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== 3:
            return 1
        elif (tableau[0][0] + tableau[0][1] + tableau[0][2]) == -3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== -3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==-3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == -3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == -3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == -3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == -3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== -3:
            return -1
        return 9
    else:
        if (tableau[0][0] + tableau[0][1] + tableau[0][2]) == 3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== 3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == 3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == 3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == 3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == 3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== 3:
            return 1
        elif (tableau[0][0] + tableau[0][1] + tableau[0][2]) == -3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== -3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==-3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == -3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == -3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == -3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == -3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== -3:
            return -1

#definirla fonction gagner qui renvoie une un message via showinfo par rapport au a que on lui donne
def gagner(a):
    if a == 1:
        showinfo(title='Victoire',message='Les croix ont gagné !')
    elif a == -1:
        print('ok')
        if w == True:
            showinfo(title='Victoire',message='Les ronds ont gagné !')
        if w == False:
            showinfo(title='Perdu',message='Le robot vous à battu')
    elif a == 0:
        if plateau == [[1,-1,1],[1,-1,1],[-1,1,-1]]:
                       showinfo(title='easter egg', message='Vous avez debloqué une égalité spéciale !')
        if w == False:
            showinfo(title='Dommage ... ',message="Vous n'avez pas battu le robot !")
        else:
            showinfo(title='Egalité',message='Match nul !')

#permettre de remttre les parametre à 0
def reinitialisation():
    
    global quiJoue, plateau, nTour,w,rOrJ , modif
    plateau=[ [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    quiJoue = True
    w = 1                            
    nTour = 1   
    rOrJ = w
    modif=True 

    message.configure(text='Aux tour des croix :')
    dessin.delete(ALL)      
    lignes = []
    for i in range(4):
      lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3 , fill='#d68839'))
      lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3 , fill='#d68839'))

#creation de l'interface
fen = Tk()

fen.title('Morpion')

message=Label(fen, text='Aux tour des croix :')
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)

bouton_quitter = Button(fen, text='Robot', command=ai)
bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

bouton_reload = Button(fen, text='Recommencer', command=reinitialisation)
bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)

dessin=Canvas(fen, bg="#e1caae", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)
lignes = []

dessin.bind('<Button-1>', afficher)

reinitialisation()

fen.mainloop()  