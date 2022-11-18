#DEBUT

#On admet que la fonction random existe et qu'elle retourne un nombre aleatoirement
#On admet que la fonction input exist et qu'elle permet de recuperer la reponse d'un user depuis le terminal

#definir la fonction pierreFeuilleCiseau qui retourne les victoires et defaite (VictoireDefaite defini en chaine de caractere vide) de userName(defini a None)

    #créé un tableau iaCoup qui enregistre les differents coup disponible pour l'IA en string
    #Crée un tableau vide ListeAction qui enregistrera toute les actions de la partie
    #Crée un tableau vide ListeScore qui enregistrera tous les scores de la partie
    
    #si userName est egal à None alors on demande au joueur un pseudo
        #variable userName qui recupere la reponse a la demande "Qu'elle est ton pseudo ? :" en str
    #variable boCombien qui recupere la reponse a la demande "En combien de victoire veut tu arreter ? (Bo1 : 1 / Bo2 : 2 / Bo3 : 3 ...) :" en int
    
    #ecrire Voici les coups que tu peut jouer :
    #ecrire Pierre : P / Feuille : F / Ciseau : C
    #ecrire Pour jouer écris l'une de ces lettres afin de selectionner un coups
    
    
    
    #variable scoreJ egal à 0
    #variable scoreIa egal à 0
    
    #tant que le score du joueur et celui de l'ia est différent de boCombien 
        
        #alors
        #ecrire un espace 
    
        #variable iaAction qui recupere un element du tableau iaCoup avec la fonction random.randrange(0,3)

        #ecrire Pierre : P / Feuille : F / Ciseau : C
        #variable jAction qui recupere la reponse a la demande "Qu'elle est ton coup " +userName+  " ? :" en str
        
        
        #si jAction est egal à P ou p et iaAction est egale à pierre 
            #alors
            #ecrire Pierre contre Pierre !
            #ecrire Egalité !
            #la liste action apprend Pierre : Pierre
        #sinon si jAction est egal à F ou f et iaAction est egale à feuille :
            #alors
            #ecrire Feuille contre Feuille !
            #ecrire Egalité !
            #la listeAction apprend Feuille : Feuille
        #sinon si jAction est egal à C ou c et iaAction est egale à ciseau
            #alors
            #ecrire Ciseau contre Ciseau !
            #ecrire Egalité !
            #ListeAction apprend Ciseau : Ciseau
        
        #sinon si jAction est egal à P ou p et iaAction est egale à feuille
            #alors
            #ecrire Pierre contre Feuille !
            #ecrire Perdu !
            #j'incremente scoreIa de 1
            #ListeAction apprend Pierre : Feuille
        #sinon si jAction est egal à F ou f et iaAction est egale à ciseau     
            #ecrire Perdu !
            #j'incremente scoreIa de 1
            #ListeAction apprend Feuille : Ciseau
        #sinon si jAction est egal à C ou c et iaAction est egale à pierre    
            #ecrire Perdu !
            #j'incremente scoreIa de 1
            #ListeAction apprend Ciseau : Pierre

        #sinon si jAction est egal à P ou p et iaAction est egale à ciseau
            #alors
            #ecrire Pierre contre Ciseau !
            #ecrire Gagné !
            #j'incremente scoreJ de 1
            #ListeAction apprend Pierre : Ciseau
        #sinon si jAction est egal à F ou f et iaAction est egale à pierre
            #alors
            #ecrire Feuille contre Pierre !
            #ecrire Gagné !
            #j'incremente scoreJ de 1
            #ListeAction apprend Feuille : Pierre
        #sinon si jAction est egal à C ou c et iaAction est egale à feuille
            #alors
            #ecrire Ciseau contre Feuille !
            #ecrire Gagné !
            #j'incremente scoreJ de 1
            #ListeAction apprend Ciseau : Feuille
        #sinon si jAction est egal à puits
            #scoreJ est egal à boCombien
            #ListeAction apprend Puits
            
        #listeScore apprend str(scoreJ) +" : "+str(scoreIa)

    #ecrire un espace vide
    #ecrire La partie est finis !

    #ecrire un espace vide
    #ecrire Récapitulatif de la partie :
    #pour i de 0 à len(ListeAction)
        #ecrire ListeScore[i]
        #ecrire ListeAction[i]

    #si scoreJ est superieur à scoreIa
        #alors
        #ecrire " Vous avez gagné " + userName
        #j'incremente victoire à VictoireDefaite
    #sinon    
        #ecrire L'IA à gagnée !
        #j'incremente defaite à VictoireDefaite
    
    
    #variable restart qui recupere la reponse a la demande Voulez vous rejouer ? (oui , non) : 
    #si restart est different de oui et restart est different de non:
        #alors
        #ecrire désolé je n'ai pas compris
        #variable restart qui recupere la reponse a la demande Voulez vous rejouer ? (oui , non) :
    #sinon si restart est egale à oui
        #alors
        #rappeler la fonction pierreFeuilleCiseau(userName , VictoireDefaite)
    #sinon
        #retourner VictoireDefaite

#Executer la fonction pierreFeuilleCiseau()

#fin