# Lien gitHub: https://github.com/binetouguey3s/menu_ussd_om/edit/main/menu_ussd.py

solde = 4000
code = "#144#"
code_secret = "4321"
numero = "771234567"
historique = [] #stockage des transferts


def menu_principal():
    print("-"*40,"\n Menu principal du services USSD OM \n","-"*40)
    print("1. Consulter le solde Orange Money")
    print("2. Effectuer des transferts,")
    print("3. Acheter du crédit")
    print("4. Autres")
    print("5. Forfaits Internet")
    print("6. Anuuler_transfert")  
    print("0. Quitter\n")
#Sous menu_principale

#Code de validation gerer la saisie
def code_ussd(): # code d'acces OM
    while True:
        code_valide = input("Saisir le code pour acceder au service d'Orange Money:  ")
        if code_valide == code:
            print("Accès autorisé")
            break
        else:
            print("Veuillez saisir le bon code qui est #144#")

def code_pin(): #code secret
    for i in range(3): # 3tentatives max
        pin_valide = input("Saisir votre code secret: ")
        if pin_valide == code_secret:
            print("Code pin correct")
            return True
        else:
            print(f"Code pin incorrect. Tentatives restantes: {2-i}")
    print("Tentatives atteintes")
    return False
#Fin Code de validation gerer la saisie

#Fonction de consultation de solde 
def consulter_solde():
    global solde
    print(f"Votre solde Orange Money est de {solde} FCFA")
    print("9. precedent")        
#Fin consultation

#Effectuer des transferts
def effectuer_transfert():
    global solde
    global historique

    print("Fonction pour effectuer des transferts")
    #DONNER LE NUMERO à ENVOYER
    while True:
        try:
            numero_saisi =input("Donnez le numero à transferer")
            if len(numero_saisi) == 9 and numero_saisi.isdigit():
                break
            else:
                print("Numero Invalide. Doit contenir 9 chiffres")
        except:
            print("Erreur de saisie")

    #Donner le montant
    while True:
        try:
            montant = float(input("Saisir le montant: \n"))
            if montant < 5:
                print("Le montant doir etre superieur a 5")
            elif montant > solde:
                print(f"Votre solde est insuffisant et est de {solde} FCFA \n")
            else:
                break
        except ValueError:
                print("Saisissez un montant valide")

    #Verification du code pin
    if not code_pin():
        return #retourne au menu si incorrect
    
    # Effectuer le transfert
    ancien_solde = solde
    solde -= montant
    
    # Ajouter à l'historique
    transfert = {
        'type': 'transfert',
        'numero_saisi': numero_saisi,
        'montant': montant,
        'solde_avant': ancien_solde,
        'solde_apres': solde
    }
    historique.append(transfert)

    print(f"Vous avez envoyer {montant} FCFA au {numero_saisi}")
    print(f"Transfer effectuer avec succes! Votre nouveau solde est de {solde} FCFA")
#Fin transfert

#Fonction pour annuler un transfert
def annuler_transfert():
    global solde
    global historique
    print("-"*40,"\n Annulation de transfert d'argent\n","-"*40)

    if not historique:
        print("Aucun transfert à annuler")
        return
    
    #Recuperons le dernier transfert
    dernier_transfert = None
    for i in range(len(historique)-1, -1, -1): 
        if historique[i]['type'] == 'transfert':
            dernier_transfert = historique[i]
            break

    if not dernier_transfert:
        print("Aucun transfert à annuler")
        return
    
    #Affichons les derniers transferts
    print(f"Dernier transfert trouvé:")
    print(f"  Montant: {dernier_transfert['montant']} FCFA")
    print(f"  Destinataire: {dernier_transfert['numero_saisi']}")
    print(f"  Solde avant: {dernier_transfert['solde_avant']} FCFA")
    print(f"  Solde après: {dernier_transfert['solde_apres']} FCFA")
    print(f"  Votre solde actuel: {solde} FCFA")

    #Demande de confirmation
    confirmer = input("Voulez vous annuler ce transfert? Repondez par Oui ou Non:  ").lower().strip()

    if confirmer == 'oui':
        if not code_pin():
            return  
       
        # Annuler le transfert
        solde += dernier_transfert['montant']

        # Marquer le transfert comme annulé
        dernier_transfert['annule'] = True

        print(f"\nTransfert annulé avec succès!")

        print(f"{dernier_transfert['montant']} FCFA ont été réintégrés à votre compte.  \n")
        print(f"Votre nouveau solde est de {solde} FCFA \n")
    else:
        print("Annulation de transfert annulée.")
  
#Fin annuler un transfert

#Achat credit
def acheter_credit():
    global solde
    global code_secret
    global numero
    while True:
        print("\nJe souhaite acheter du credit telephonique:")
        print("1. Pour mon numero")
        print("2. Pour un autre numero Orange ou Kirene ou bien un numero Promobile\n       ---      ")
        print("9. precedent\n")

        choix_achat = input("Choisir une option d'achat: ").strip()

        #Option 1. Pour mon numero
    
        if choix_achat == "1":
            while True:
                try:               
                    montant = float(input("Saisir le montant: \n"))
                    if (montant > solde):
                        print("Le montant doit etre inferieur au solde\n")
                    elif montant < 5:
                        print("Le montant doit etre superieur a 5\n")
                    else:
                        code_pin()
                        solde = solde - montant
                        print(f"Vous avez acheter {montant} FCFA de credit ")
                        break
                except ValueError:
                    print("Montant incomplet")
            
                #Fin
                #Option 2. Pour un autre numero
        elif choix_achat == "2":
            print("Vous allez acheter du credit telephonique \n pour un autre numero Orange ou Kirene avec Orange ou \n flexbox.\n")
            while True:
                # try:
                #     montant = float(input("Saisir le montant\n"))
                #     try:
                #         if (montant < 5):
                #             print("Le montant doit etre superieur a 5\n")
                #         elif montant > solde: 
                #             print("Solde insuffisant est de {solde} FCFA, recharger votre compte")
                #         else:
                #             break
                #     except ValueError:
                #         print("montant invalide")
                #     numero_saisi = input("Donnez le numero telephonique")
                   
                #     if len(numero_saisi) == 9 and numero_saisi.isdigit():
                #         code_pin()
                #         solde = solde - montant 
                #         print(f"Vous avez acheter {montant} FCFA de credit sur le {numero_saisi} ")
                #     else:
                #         break
                # except ValueError:
                #     print("Montant invalide") 
                montant = float(input("Saisir le montant\n"))
                if montant < 5:  
                    print("Le montant doit etre superieur a 5\n")
                    continue  
                break

            while True:
                numero_saisi = input("Donnez le numero telephonique")
                if len(numero_saisi) == 9 and numero_saisi.isdigit():
                    break
            print("...") 

            if not code_pin():
                return
            solde = solde - montant 
            print(f"Vous avez acheter {montant} FCFA de credit sur le {numero_saisi} ")
        else:
            break
    menu_principal()
#Fin achat

#Autres
def autre():
    print(" Autres fonctionnalite à venir ")
    print("9. precedent")
#Fin autre

#Fonction pour forfait internet
def forfait_internet():
    global solde
    while True:
        print("\n Liste de forfaits disponibles\n")
        print("1.  Pass 100 Mo - 500 FCFA ")
        print("2.  Pass 500 Mo - 1 000 FCFA")
        print("3.  Pass 1 Go - 2 000 FCFA")

        choix_achat = input("Choisir une option entre 1 et 3 et 9 :  ")
            
        if choix_achat == "1":
            forfait_1()   
        elif choix_achat == "2":
            forfait_2()
        elif choix_achat == "3":
            forfait_3()
        elif choix_achat == "9":
            print("\nQuitter")
            break
        else:
            print("Choix invalide, saisie encore")
#Fin Fonction pour forfait internet

#Sous menu de forfait 1
def forfait_1():
    global solde

    print("\nKheweul du forfait 100 Mo\n")
    # while True
    pass_forfait = 500
    if (pass_forfait > solde):
        print("Le pass doit etre inferieur au solde\n")
    else:
        code_pin()
        solde = solde - pass_forfait
        print(f"Vous pouvez acheter un forfait de {pass_forfait} FCFA et votre nouveau solde est : {solde} FCFA")   
        menu_principal()
#Fin sous menu de forfait 1

#Sous menu de forfait 2
def forfait_2():
    global solde

    print("\nKheweul du forfait 500 Mo\n")
    # while True
    pass_forfait = 1000
    if (pass_forfait > solde):
        print("Le pass doit etre inferieur au solde\n")
    else:
        code_pin()
        solde = solde - pass_forfait
        print(f"Vous avez acheter un forfait de {pass_forfait} FCFA et votre nouveau solde est : {solde} FCFA")   
        menu_principal()
#Fin sous menu de forfait 2

#Sous menu de forfait 3
def forfait_3():
    global solde

    print("\nKheweul du forfait 1 Go\n")
    # while True
    pass_forfait = 2000
    if (pass_forfait > solde):
        print("Le pass doit etre inferieur au solde\n")
    else:
        code_pin()
        solde = solde - pass_forfait
        print(f"Vous avez acheter un forfait de {pass_forfait} FCFA et votre nouveau solde est : {solde} FCFA") 
        menu_principal()      
#Fin sous menu de forfait 3

#Fin sous menu principal 

#Debut Fonctions principales 
def main():
    code_ussd() #144#
   
    while True:
        # menu_principal()

        choix_option = input("\n Choisir une option entre 0 et 9: \n")
        if choix_option == "1":
            consulter_solde()   
        elif choix_option == "2":
            effectuer_transfert()
        elif choix_option == "3":
            acheter_credit()
        elif choix_option == "4":
            autre()
        elif choix_option == "5":
            forfait_internet()   
        elif choix_option == "6":
            annuler_transfert()    
        elif choix_option == "0":
            print("\nQuitter")
            break
        elif choix_option == "9":
            menu_principal()
        else:
            print("Choix invalide, saisie encore")       
main()
            

#os est un module qui permet d'interagir avec le systeme
#exit pour sortir du programme


