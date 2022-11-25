#definir la fonction ai
    #on met les variable quiJoue, w , nTour , rOrJ , modif en global
    #la variable aJouer devient fausse
    
    #si modif est vrai et que nTour est inferieur a 3
        #modif est faux
        #w est egal a 2
        #rorj est egal a w

    #si rorj est egal a 2
        #si ntour est inferieur a 3 et plateau[1][1] est egal a 0
            #on dessine un oval (100*1+8, 100*1+8, 100*1+96, 100*1+96, width = 5, outline = '#b61b1c')
            #dessine un oval(100*1+8, 100*1+8, 100*1+96, 100*1+96, width = 5, outline = '#b61b1c')
            #plateau[1][1] est egal à -1
            #on change le message en Aux tour des croix :
            #quiJoue devient vrai
            #rorj est egal a 0
            #aJouer est egal a true
            

        
        #win action
        #si aJouer est egal a faux
            #si (plateau[0][0] plus plateau[0][1]) est egal a -2 ou (plateau[0][0] plus plateau[0][2]) est egal a -2 or (plateau[0][1] plus plateau[0][2]) est egal a -2:
                #pour i2 dans range(0,3):
                    #si plateau[0][i2] est egal a 0
                        #dessine un oval(100*i2+8, 100*0+8, 100*i2+96, 100*0+96, width = 5, outline = '#b61b1c')
                        #plateau[0][i2] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        #si aJouer est egal a faux
            #si (plateau[1][0] plus plateau[1][1]) est egal a -2 ou (plateau[1][0] plus plateau[1][2]) est egal -2 ou (plateau[1][1] plus plateau[1][2]) est egal -2:
                #pour i2 dans range(0,3):
                    #si plateau[1][i2] est egal a 0
                        #dessine un oval(100*i2+8, 100*1+8, 100*i2+96, 100*1+96, width = 5, outline = '#b61b1c')
                        #plateau[1][i2] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        #si aJouer est egal a faux
            #si (plateau[2][0] plus plateau[2][1]) est egal a -2 or (plateau[2][0] plud plateau[2][2]) est egal a -2 or (plateau[2][1] plus plateau[2][2]) est egal a -2:
                #pour i2 dans range(0,3):
                    #si plateau[2][i2] est egal a 0
                        #dessine un oval(100*i2+8, 100*2+8, 100*i2+96, 100*2+96, width = 5, outline = '#b61b1c')
                        #plateau[2][i2] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        
        #si aJouer est egal a faux
            #si (plateau[0][0] plus plateau[1][0]) est egal a -2 ou (plateau[0][0] plus plateau[2][0]) est egal a -2 ou (plateau[1][0] plus plateau[2][0]) est egal a -2:
                #pour i dans range(0,3):
                    #si plateau[i][0] est egal a 0
                        #dessine un oval(100*0+8, 100*i+8, 100*0+96, 100*i+96, width = 5, outline = '#b61b1c')
                        #plateau[i][0] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        #si aJouer est egal a faux
            #si (plateau[0][1] plus plateau[1][1]) est egal a -2 ou (plateau[0][1] plus plateau[2][1]) est egal a -2 ou (plateau[1][1] plus plateau[2][1]) est egal a -2:
                #for i dans range(0,3):
                    #si plateau[i][1] est egal a 0
                        #dessine un oval(100*1+8, 100*i+8, 100*1+96, 100*i+96, width = 5, outline = '#b61b1c')
                        #plateau[i][1] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        #si aJouer est egal a faux
            #si (plateau[0][2] plus plateau[1][2]) est egal a -2 ou (plateau[0][2] plus plateau[2][2]) est egal a -2 ou (plateau[1][2] plus plateau[2][2]) est egal a -2:
                #pour i dans range(0,3):
                    #si plateau[i][2] est egal a 0
                        #dessine un oval(100*2+8, 100*i+8, 100*2+96, 100*i+96, width = 5, outline = '#b61b1c')
                        #plateau[i][2] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        
        #si aJouer est egal a faux
        #d est egal a vrai
            #si (plateau[0][0] plus plateau[0][1]) est egal a -2 ou (plateau[0][0] plus plateau[0][2]) est egal a -2 ou (plateau[0][1] plus plateau[0][2]) est egal a -2:
                #pour i dans range(0,3):
                    #pour i2 dans range(0,3):
                        #si (i est egal a 0 et i2 est egal a 0) ou (i est egal a 1 et i2 est egal a 1) ou (i est egal a 2 et i2 est egal a 2) :
                            #si plateau[i][i2] est egal a 0
                                #si d est egal a vrai
                                    #d deviens faux
                                    #dessine un oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                    #plateau[i][i2] est egal a -1
                                    #on change le message en Aux tour des croix :
                                    #quiJoue devient vrai
                                    #rorj est egal a 0
                                    #aJouer est egal a true
        
        #si aJouer est egal a faux
            #d est egal a vrai
            #si (plateau[0][2] plus plateau[1][1]) est egal a -2 ou (plateau[0][2] plus plateau[2][0]) est egal a -2 ou (plateau[1][1] plus plateau[2][0]) est egal a -2:
                #pour i dans range(0,3):
                    #pour i2 dans range(0,3):
                        #si (i est egal a 0 et i2 est egal a 2) ou (i est egal a 1 et i2 est egal a 1) ou (i est egal a 2 et i2 est egal a 0) :
                            #si plateau[i][i2] est egal a 0
                                #dessine un oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                #plateau[i][i2] est egal a -1
                                #on change le message en Aux tour des croix :
                                #quiJoue devient vrai
                                #rorj est egal a 0
                                #aJouer est egal a true
        
        #counter action
        #si aJouer est egal a faux
            #si (plateau[0][0] plus plateau[0][1]) est egal a 2 ou (plateau[0][0] plus plateau[0][2]) est egal a 2 ou (plateau[0][1] plus plateau[0][2]) est egal a 2:
                #pour i2 dans range(0,3):
                    #si plateau[0][i2] est egal a 0
                        #dessine un oval(100*i2+8, 100*0+8, 100*i2+96, 100*0+96, width = 5, outline = '#b61b1c')
                        #plateau[0][i2] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        
        #si aJouer est egal a faux
            #si (plateau[1][0] plus plateau[1][1]) est egal a 2 ou (plateau[1][0] plus plateau[1][2]) est egal a 2 ou (plateau[1][1] plus plateau[1][2]) est egal a 2:
                #pour i2 dans range(0,3):
                    #si plateau[1][i2] est egal a 0
                        #dessine un oval(100*i2+8, 100*1+8, 100*i2+96, 100*1+96, width = 5, outline = '#b61b1c')
                        #plateau[1][i2] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true

        #si aJouer est egal a faux
            #si (plateau[2][0] + plateau[2][1]) est egal a 2 ou (plateau[2][0] + plateau[2][2]) est egal a 2 ou (plateau[2][1] + plateau[2][2]) est egal a 2:
                #pour i2 dans range(0,3):
                    #si plateau[2][i2] est egal a 0
                        #dessine un oval(100*i2+8, 100*2+8, 100*i2+96, 100*2+96, width = 5, outline = '#b61b1c')
                        #plateau[2][i2] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        
        #si aJouer est egal a faux
            #si (plateau[0][0] + plateau[1][0]) est egal a 2 ou (plateau[0][0] + plateau[2][0]) est egal a 2 ou (plateau[1][0] + plateau[2][0]) est egal a 2:
                #pour i dans range(0,3):
                    #si plateau[i][0] est egal a 0
                        #dessine un oval(100*0+8, 100*i+8, 100*0+96, 100*i+96, width = 5, outline = '#b61b1c')
                        #plateau[i][0] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true

        #si aJouer est egal a faux
            #si (plateau[0][1] + plateau[1][1]) est egal a 2 ou (plateau[0][1] + plateau[2][1]) est egal a 2 ou (plateau[1][1] + plateau[2][1]) est egal a 2:
                #pour i dans range(0,3):
                    #si plateau[i][1] est egal a 0
                        #dessine un oval(100*1+8, 100*i+8, 100*1+96, 100*i+96, width = 5, outline = '#b61b1c')
                        #plateau[i][1] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        #si aJouer est egal a faux
            #si (plateau[0][2] + plateau[1][2]) est egal a 2 ou (plateau[0][2] + plateau[2][2]) est egal a 2 ou (plateau[1][2] + plateau[2][2]) est egal a 2:
                #pour i dans range(0,3):
                    #si plateau[i][2] est egal a 0
                        #dessine un oval(100*2+8, 100*i+8, 100*2+96, 100*i+96, width = 5, outline = '#b61b1c')
                        #plateau[i][2] est egal a -1
                        #on change le message en Aux tour des croix :
                        #quiJoue devient vrai
                        #rorj est egal a 0
                        #aJouer est egal a true
        
        #si aJouer est egal a faux
            #d est egal a vrai
            #si (plateau[0][0] + plateau[1][1]) est egal a 2 ou (plateau[0][0] + plateau[2][2]) est egal a 2 ou (plateau[1][1] + plateau[2][2]) est egal a 2:
                #pour i dans range(0,3):
                    #pour i2 dans range(0,3):
                        #si plateau[i][i2] est egal a 0
                            #si (i est egal a 0 et i2 est egal a 0) ou (i est egal a 1 et i2 est egal a 1) ou (i est egal a 2 et i2 est egal a 2) :
                                #si d est egal a vrai:
                                    #d est egal a faux
                                    #dessine un oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                    #plateau[i][i2] est egal a -1
                                    #on change le message en Aux tour des croix :
                                    #quiJoue devient vrai
                                    #rorj est egal a 0
                                    #aJouer est egal a true
            
        #si aJouer est egal a faux
            #d est egal a vrai
            #si (plateau[0][2] + plateau[1][1]) est egal a 2 ou (plateau[0][2] + plateau[2][0]) est egal a 2 ou (plateau[1][1] + plateau[2][0]) est egal a 2:
                #pour i dans range(0,3):
                    #pour i2 dans range(0,3):
                        #si (i est egal a 0 et i2 est egal a 2) ou (i est egal a 1 et i2 est egal a 1) ou (i est egal a 2 et i2 est egal a 0) :
                            #si plateau[i][i2] est egal a 0
                                #si d est egal a vrai:
                                    #d est egal a faux
                                    #dessine un oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                                    #plateau[i][i2] est egal a -1
                                    #on change le message en Aux tour des croix :
                                    #quiJoue devient vrai
                                    #rorj est egal a 0
                                    #aJouer est egal a true
        
        #opposite action
        #si aJouer est egal a faux
            #si plateau[0][0] est egal a 1 
                #si plateau[2][2] est egal a 0
                    #dessine un oval(100*2+8, 100*2+8, 100*2+96, 100*2+96, width = 5, outline = '#b61b1c')
                    #plateau[2][2] est egal a -1
                    #on change le message en Aux tour des croix :
                    #quiJoue devient vrai
                    #rorj est egal a 0
                    #aJouer est egal a true
        
        #si aJouer est egal a faux
            #si plateau[2][2] est egal a 1
                #si plateau[0][0] est egal a 0
                    #dessine un oval(100*0+8, 100*0+8, 100*0+96, 100*0+96, width = 5, outline = '#b61b1c')
                    #plateau[0][0] est egal a -1
                    #on change le message en Aux tour des croix :
                    #quiJoue devient vrai
                    #rorj est egal a 0
                    #aJouer est egal a true

        #si aJouer est egal a faux
            #si plateau[0][2] est egal a 1
                #si plateau[2][0] est egal a 0
                    #dessine un oval(100*0+8, 100*2+8, 100*0+96, 100*2+96, width = 5, outline = '#b61b1c')
                    #plateau[2][0] est egal a -1
                    #on change le message en Aux tour des croix :
                    #quiJoue devient vrai
                    #rorj est egal a 0
                    #aJouer est egal a true
        
        #si aJouer est egal a faux
            #si plateau[2][0] est egal a 0 
                #si plateau[0][2] est egal a 0
                    #dessine un oval(100*2+8, 100*0+8, 100*2+96, 100*0+96, width = 5, outline = '#b61b1c')
                    #plateau[0][2] est egal a -1
                    #on change le message en Aux tour des croix :
                    #quiJoue devient vrai
                    #rorj est egal a 0
                    #aJouer est egal a true
        
        #si aJouer est egal a faux
            #si plateau[0][1] est egal a 1 
                #si plateau[2][1] est egal a 0
                    #dessine un oval(100*1+8, 100*2+8, 100*1+96, 100*2+96, width = 5, outline = '#b61b1c')
                    #plateau[2][1] est egal a -1
                    #on change le message en Aux tour des croix :
                    #quiJoue devient vrai
                    #rorj est egal a 0
                    #aJouer est egal a true
        
        #si aJouer est egal a faux
            #si aJouer est egal a faux
                #si plateau[0][1] est egal a 0
                    #dessine un oval(100*1+8, 100*0+8, 100*1+96, 100*0+96, width = 5, outline = '#b61b1c')
                    #plateau[0][1] est egal a -1
                    #on change le message en Aux tour des croix :
                    #quiJoue devient vrai
                    #rorj est egal a 0
                    #aJouer est egal a true
        
        #si aJouer est egal a faux
            #si aJouer est egal a faux 
                #si plateau[1][2] est egal a 0
                    #dessine un oval(100*2+8, 100*1+8, 100*2+96, 100*1+96, width = 5, outline = '#b61b1c')
                    #plateau[1][2] est egal a -1
                    #on change le message en Aux tour des croix :
                    #quiJoue devient vrai
                    #rorj est egal a 0
                    #aJouer est egal a true
        
        #si aJouer est egal a faux
            #si aJouer est egal a faux
                #si plateau[1][0] est egal a 0
                    #dessine un oval(100*0+8, 100*1+8, 100*0+96, 100*1+96, width = 5, outline = '#b61b1c')
                    #plateau[1][0] est egal a -1
                    #on change le message en Aux tour des croix :
                    #quiJoue devient vrai
                    #rorj est egal a 0
                    #aJouer est egal a true

        #milieux action(corner action)
        #si aJouer est egal a faux
            #si plateau[1][1] est egal a 0
                #i est egal a random.randint(0,2)
                #i2 est egal a random.randint(0,2)
                #tant que plateau[i][i2] est different de 0 ou (i est egal a 0 et i2 est egal a 1) ou (i est egal a 1 et i2 est egal a 0) ou (i est egal a 2 et i2 est egal a 1) ou (i est egal a 1 et i2 est egal a 2) :
                    #i est egal a random.randint(0,2)
                    #i2 est egal a random.randint(0,2)
                #dessine un oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
                #plateau[i][i2] est egal a -1
                #on change le message en Aux tour des croix :
                #quiJoue devient vrai
                #rorj est egal a 0
                #aJouer est egal a true
        
        #random
        #si aJouer est egal a faux
            #i est egal a random.randint(0,2)
            #i2 est egal a random.randint(0,2)
            #tant que plateau[i][i2] est different de 0
                #i est egal a random.randint(0,2)
                #i2 est egal a random.randint(0,2)
            #dessine un oval(100*i2+8, 100*i+8, 100*i2+96, 100*i+96, width = 5, outline = '#b61b1c')
            #plateau[i][i2] est egal a -1
            #on change le message en Aux tour des croix :
            #quiJoue devient vrai
            #rorj est egal a 0
            #aJouer est egal a truee

        #si nTour est superieur ou egal à 5 et nTour est inferieur ou egal a 9
            #variable v contenant la valeur retourner de verif(plateau)
            #si v est egal a 1 ou v est egal a -1
                #alors
                #executer la fonction gagner(v , w)
            #sinon si v est egal a 9
                #executer la fonction gagner(0 , w)
        #on acremente nTour de 1 
    