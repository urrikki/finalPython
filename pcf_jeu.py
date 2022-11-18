#DEBUT

#On admet que la fonction random existe et qu'elle retourne un nombre aleatoirement
import random
#On admet que la fonction input exist et qu'elle permet de recuperer la reponse d'un user depuis le terminal

#definir la fonction pierreFeuilleCiseau qui retourne les victoires et defaite (defini en chaine de caractere vide) de userName(defini a None)
def pierreFeuilleCiseau(userName=None , VictoireDefaite=''):

    #créé un tableau iaCoup qui enregistre les differents coup disponible pour l'IA en string
    iaCoup = ["pierre","feuille","ciseau"]
    #Crée un tableau vide ListeAction qui enregistrera toute les actions de la partie
    ListeAction = []
    #Crée un tableau vide ListeScore qui enregistrera tous les scores de la partie
    ListeScore = []
    
    #si userName est egal à None alors on demande au joueur un pseudo
    if userName == None:
        #variable userName qui recupere la reponse a la demande "Qu'elle est ton pseudo ? :" en str
        userName = str(input("Qu'elle est ton pseudo ? :"))
    #variable boCombien qui recupere la reponse a la demande "En combien de victoire veut tu arreter ? (Bo1 : 1 / Bo2 : 2 / Bo3 : 3 ...) :" en int
    boCombien = int(input("En combien de victoire veut tu arreter ? (Bo1 : 1 / Bo2 : 2 / Bo3 : 3 ...) :"))
    
    #ecrire Voici les coups que tu peut jouer :
    print("Voici les coups que tu peut jouer : ")
    #ecrire Pierre : P / Feuille : F / Ciseau : C
    print("Pierre : P / Feuille : F / Ciseau : C")
    #ecrire Pour jouer écris l'une de ces lettres afin de selectionner un coups
    print("Pour jouer écris l'une de ces lettres afin de selectionner un coups")
    
    
    
    #variable scoreJ egal à 0
    scoreJ = 0
    #variable scoreIa egal à 0
    scoreIa = 0
    
    #tant que le score du joueur et celui de l'ia est différent de boCombien 
    while scoreJ!=boCombien and scoreIa!=boCombien:
        
        #alors
        #ecrire un espace 
        print(' ')
    
        #variable iaAction qui recupere un element du tableau iaCoup avec la fonction random.randrange(0,3)
        iaAction = iaCoup[random.randrange(0,3)]

        #ecrire Pierre : P / Feuille : F / Ciseau : C
        print("Pierre : P / Feuille : F / Ciseau : C")
        #variable jAction qui recupere la reponse a la demande "Qu'elle est ton coup " +userName+  " ? :" en str
        jAction = str(input("Qu'elle est ton coup " +userName+  " ? :"))
        
        
        #si jAction est egal à P ou p et iaAction est egale à pierre 
        if (jAction == "P" or jAction == "p") and iaAction == "pierre":
            #alors
            #ecrire Pierre contre Pierre !
            print("Pierre contre Pierre !")
            #ecrire Egalité !
            print("Egalité !")
            #la liste action apprend Pierre : Pierre
            ListeAction.append("Pierre : Pierre") 
        #sinon si jAction est egal à F ou f et iaAction est egale à feuille 
        elif (jAction == "F" or jAction == "f") and iaAction == "feuille":
            #alors
            #ecrire Feuille contre Feuille !
            print("Feuille contre Feuille !")
            #ecrire Egalité !
            print("Egalité !")
            #la listeAction apprend Feuille : Feuille
            ListeAction.append("Feuille : Feuille")
        #sinon si jAction est egal à C ou c et iaAction est egale à ciseau
        elif (jAction == "C" or jAction == "c") and iaAction == "ciseau":
            #alors
            #ecrire Ciseau contre Ciseau !
            print("Ciseau contre Ciseau !")
            #ecrire Egalité !
            print("Egalité !")
            #ListeAction apprend Ciseau : Ciseau
            ListeAction.append("Ciseau : Ciseau")
        
        #sinon si jAction est egal à P ou p et iaAction est egale à feuille
        elif (jAction == "P" or jAction == "p") and iaAction == "feuille":
            #alors
            #ecrire Pierre contre Feuille !
            print("Pierre contre Feuille !")
            #ecrire Perdu !
            print("Perdu !")
            #j'incremente scoreIa de 1
            scoreIa = scoreIa + 1
            #ListeAction apprend Pierre : Feuille
            ListeAction.append("Pierre : Feuille")
        #sinon si jAction est egal à F ou f et iaAction est egale à ciseau     
        elif (jAction == "F" or jAction == "f") and iaAction == "ciseau":
            print("Feuille contre ciseau !")
            #ecrire Perdu !
            print("Perdu !")
            #j'incremente scoreIa de 1
            scoreIa = scoreIa + 1
            #ListeAction apprend Feuille : Ciseau
            ListeAction.append("Feuille : Ciseau")
        #sinon si jAction est egal à C ou c et iaAction est egale à pierre    
        elif (jAction == "C" or jAction == "c") and iaAction == "pierre":
            print("Ciseau contre Pierre !")
            #ecrire Perdu !
            print("Perdu !")
            #j'incremente scoreIa de 1
            scoreIa = scoreIa + 1
            #ListeAction apprend Ciseau : Pierre
            ListeAction.append("Ciseau : Pierre")

        #sinon si jAction est egal à P ou p et iaAction est egale à ciseau
        elif (jAction == "P" or jAction == "p") and iaAction == "ciseau":
            #alors
            #ecrire Pierre contre Ciseau !
            print("Pierre contre Ciseau !")
            #ecrire Gagné !
            print("Gagné !")
            #j'incremente scoreJ de 1
            scoreJ = scoreJ + 1
            #ListeAction apprend Pierre : Ciseau
            ListeAction.append("Pierre : Ciseau")
        #sinon si jAction est egal à F ou f et iaAction est egale à pierre
        elif (jAction == "F" or jAction == "f") and iaAction == "pierre":
            #alors
            #ecrire Feuille contre Pierre !
            print("Feuille contre Pierre !")
            #ecrire Gagné !
            print("Gagné !")
            #j'incremente scoreJ de 1
            scoreJ = scoreJ + 1
            #ListeAction apprend Feuille : Pierre
            ListeAction.append("Feuille : Pierre")
        #sinon si jAction est egal à C ou c et iaAction est egale à feuille
        elif (jAction == "C" or jAction == "c") and iaAction == "feuille":
            #alors
            #ecrire Ciseau contre Feuille !
            print("Ciseau contre Feuille !")
            #ecrire Gagné !
            print("Gagné !")
            #j'incremente scoreJ de 1
            scoreJ = scoreJ + 1
            #ListeAction apprend Ciseau : Feuille
            ListeAction.append("Ciseau : Feuille")
        #sinon si jAction est egal à puits
        elif jAction == "puits":
            #scoreJ est egal à boCombien
            scoreJ = boCombien
            #ListeAction apprend Puits
            ListeAction.append("Puits")

        #listeScore apprend str(scoreJ) +" : "+str(scoreIa)
        ListeScore.append(str(scoreJ) +" : "+str(scoreIa))

    #ecrire un espace vide
    print(' ')
    #ecrire La partie est finis !
    print("La partie est finis !")

    #ecrire un espace vide
    print(' ')
    #ecrire Récapitulatif de la partie :
    print("Récapitulatif de la partie :")
    #pour i de 0 à len(ListeAction)
    for i in range(len(ListeAction)):
        #ecrire ListeScore[i]
        print(ListeScore[i])
        #ecrire ListeAction[i]
        print(ListeAction[i])

    #si scoreJ est superieur à scoreIa
    if scoreJ > scoreIa:
        #alors
        #ecrire " Vous avez gagné " + userName
        print("Vous avez gagné " + userName)
        #j'incremente victoire à VictoireDefaite
        VictoireDefaite = VictoireDefaite + (" Victoire")
    #sinon    
    else:
        #ecrire L'IA à gagnée !
        print("L'IA à gagnée !")
        #j'incremente defaite à VictoireDefaite
        VictoireDefaite = VictoireDefaite + (" Defaite")
    
    
    #variable restart qui recupere la reponse a la demande Voulez vous rejouer ? (oui , non) : 
    restart = str(input("Voulez vous rejouer ? (oui , non) : "))
    #si restart est different de oui et restart est different de non
    if restart != "oui" and restart !="non":
        #alors
        #ecrire désolé je n'ai pas compris
        print("désolé je n'ai pas compris")
        #variable restart qui recupere la reponse a la demande Voulez vous rejouer ? (oui , non) :
        restart = str(input("Voulez vous rejouer ? (oui , non) : "))
    #sinon si restart est egale à oui
    elif restart == "oui":
        #alors
        #rappeler la fonction pierreFeuilleCiseau(userName , VictoireDefaite)
        pierreFeuilleCiseau(userName , VictoireDefaite)
    #sinon
    else :
        #retourner VictoireDefaite
        return VictoireDefaite

#Executer la fonction pierreFeuilleCiseau
pierreFeuilleCiseau()

#fin