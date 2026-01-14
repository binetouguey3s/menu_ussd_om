# Lien gitHub: https://github.com/binetouguey3s/menu_ussd_om


#Debut du projet sur la simulation USSD Orange Money 

# initialisation du compte
compte = {
    'solde' : 40000.0
}

#Initialisation du code ussd, du code secret et du numero de l'utilisatteur
code = "#144#"
code_secret = "4321"
numero = "771234567"
historique = [] #stockage du dernier transfert effectuer

# Pour sauvegarder et charger nos données avec json

import os   #Module pour interagir avec le terminal 
import json #Module pour créer des fichier json 

fichier_json = "ussd.json" #Nom du fichier json

#Voir si on modifie le solde directement sur ussd.json
def solde_json():

    #Verifier si le fichier json existe ou pas 
    if not os.path.exists(fichier_json):
        print(f"{'ussd.json'} n'existe pas")
        return
    try:
        with open(fichier_json, 'r') as f:
            donnees = json.load(f) # Chargement des donnees
            solde = donnees.get('solde') # Recuperer le solde
            print("\n Modifier le solde dans le json directement puis voir dans le terminal \n")
            print(f"Le solde actuel est de: {solde} FCFA") #Afficher le solde
    except json.JSONDecodeError:  
        print("Le fichier_n'est pas un fichier json.")
# Fin solde_json

# Sauvegarder les données dans un fichier json 
def sauvegarder():
    global compte
    global historique
    compte_donnees = { 
        'solde': compte['solde'],
        'transactions': historique
    }
        
    fichier_json = "ussd.json" # nom du fichier json
    with open(fichier_json, "w") as fichier: 
        json.dump(compte_donnees, fichier , indent=4)  

 
# Fin sauvetage

# Charger les données du fichier json
def charger():
    global compte 

    fichier_json = "ussd.json"
    with open("ussd.json", "r") as fichier: 
        ussd_fichier = json.load(fichier)
        return ussd_fichier 
   
    with open(fichier_json, "r") as f: 
        donnees = json.load(f)
        return donnees
       

# Fin chargement    
# Fonction principal
def menu_principal():
    print("-"*40,"\n Menu principal du services USSD OM \n","-"*40)
    print("1. Consulter le solde Orange Money")
    print("2. Effectuer des transferts")
    print("3. Acheter du crédit")
    print("4. Forfaits Internet")
    print("5. Annuler_transfert")
    print("6. Historique des transferts")  
    print("7. Modifier le solde directement sur ussd.json")
    print("0. Quitter\n")
#Sous menu_principale

#Code de validation gerer la saisie
def code_ussd(): # code d'acces OM
    while True:
        code_valide = input(" \n Saisir le code pour acceder au service d'Orange Money:  ")
        if code_valide == code:
            print("Accès autorisé!")
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
    print("-"*50,"\n1. Consulter le solde \n",50*"-")
    print(f"\nVotre solde Orange Money est de {compte['solde']} FCFA")
    print("\n9.Precedent")
#Fin consultation

#Effectuer des transferts d'argent
def effectuer_transfert():
    global historique

    print("-"*40,"\n Effectuer des transferts \n","-"*40)
    #DONNER LE NUMERO à ENVOYER
    while True:
        try:
            numero_saisi =input("Donnez le numero à transferer:   ").strip()
            if len(numero_saisi) != 9:
                print("Le numero doit contenir 9 chiffres")
                continue
            if not numero_saisi.isdigit():
                print("\n Le numero doit contenir que des chiffres")
                continue
            if not (numero_saisi.startswith("77") or numero_saisi.startswith("78")):
                print("\n Le numero doit commencer par 77, 78")
                continue
            break
        except ValueError:
            print("Saisissez un numero valide\n")

    #Donner le montant
    while True:
        try:
            montant = float(input("Saisir le montant:  "))

            #Verification du code pin
            code_pin()
            
            if montant < 5:
                print("Le montant doir etre superieur a 5")
            elif montant > compte['solde']:
                print(f"Votre solde est insuffisant et est de {compte['solde']} FCFA \n")
            else:
                compte['solde'] = compte['solde'] - montant
                print(f"Trasfert réussi! : nouveau solde = {compte['solde']} FCFA \n") 
                sauvegarder()
                break
        except ValueError:
                print("Saisissez un montant valide")

    
    
    # Effectuer le transfert
    ancien_solde = compte['solde']
    compte['solde'] -= montant
    
     # Ajouter à l'historique
    transfert = {
        'type': 'transfert',
        'numero_saisi': numero_saisi,
        'montant': montant,
        'solde_avant': ancien_solde,
        'solde_apres': compte['solde']
    }
    historique.append(transfert)
    #Mettre a jour dans le fichier json
    sauvegarder()

    print(f"Vous avez envoyer {montant} FCFA au {numero_saisi}")
    print(f"Transfer effectuer avec succes! Votre nouveau solde est de {compte['solde']} FCFA")
#Fin transfert

#Historique de tous les transferts effectués
def transferts_historique(): 
    global historique
    print("-"*40,"\nAffichage de l'historique de tous les transferts effectués,\n","-"*40)
    
    # # Recuperation de tous les historiques effectués
    tout_historique = None #initialisons 
    for i in range(len(historique)):
        if historique[i]['type'] == 'transfert':
            tout_historique = historique[i]
            break
    if not tout_historique:
        print("Pas de transfert effectué pour le moment!")
        return

    #Affichage des transferts
    print("Historique des transferts effectués:")
    print(f"  Montant: {tout_historique['montant']} FCFA")
    print(f"  Destinataire: {tout_historique['numero_saisi']}")
    print(f"  Solde avant: {tout_historique['solde_avant']} FCFA")
    print(f"  Solde apres: {tout_historique['solde_apres']} FCFA")            
#Fin affichage historique de transfert

#Fonction pour annuler un transfert
def annuler_transfert():
    global historique
    print("-"*40,"\n Annulation de transfert d'argent\n","-"*40)

    if not historique:
        print("Aucun transfert à annuler")
        return
    
    #Recuperons le dernier transfert
    dernier_transfert = None
    for i in range(len(historique)-1): 
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
    print(f"  Solde apres: {dernier_transfert['solde_apres']} FCFA")
    print(f"  Votre solde actuel: {compte['solde']} FCFA")

    #Demande de confirmation
    confirmer = input("Voulez vous annuler ce transfert? Repondez par Oui ou Non:  ").lower().strip()

    if confirmer == 'oui':
        code_pin()
       
        # Annuler le transfert
        compte['solde'] += dernier_transfert['montant']

        # Marquer le transfert comme annulé
        dernier_transfert['annule'] = True

        print(f"\nTransfert annulé avec succès!")

        print(f"{dernier_transfert['montant']} FCFA ont été réintégrés à votre compte.  \n")
        print(f"Votre nouveau solde est de {compte['solde']} FCFA \n")
    else:
        print("Annulation de transfert annulée.")
  
#Fin annuler un transfert

#Achat credit
def acheter_credit():
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
                    montant = float(input("Saisir le montant:   "))
                    if montant > compte['solde']:
                        print("Le montant doit etre inferieur au solde\n")
                    elif montant < 5:
                        print("Le montant doit etre superieur a 5\n")
                    else:
                        code_pin()
                        compte['solde'] = compte['solde'] - montant
                        print(f"Vous avez acheter {montant} FCFA de credit ")
                        sauvegarder()
                        break
                except ValueError:
                    print("Montant incomplet")
            
                #Fin
                #Option 2. Pour un autre numero
        elif choix_achat == "2":
            print("Vous allez acheter du credit telephonique\npour un autre numero Orange ou Kirene avec Orange ou\nflexbox.\n")
            while True:
                montant = float(input("Saisir le montant:  "))
                if montant < 5:  
                    print("Le montant doit etre superieur a 5 \n")
                    continue  
                break

            while True:
                numero_saisi = input("Donnez le numero telephonique:  ")
                if len(numero_saisi) == 9 and numero_saisi.isdigit():
                    break

            code_pin()
            compte['solde'] = compte['solde'] - montant 
            print(f"Vous avez acheter {montant} FCFA de credit sur le {numero_saisi} ")
            sauvegarder()
        else:
            break
    menu_principal()
#Fin achat

#Fonction pour forfait internet
def forfait_internet():
    while True:
        print("\n Liste de forfaits disponibles\n")
        print("1.  Pass 100 Mo - 500 FCFA ")
        print("2.  Pass 500 Mo - 1 000 FCFA")
        print("3.  Pass 1 Go - 2 000 FCFA")
        print("9.  Quitter")

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
    print("\nKheweul du forfait 100 Mo\n")
    # while True
    pass_forfait = 500
    if (pass_forfait > compte['solde']):
        print("Le pass doit etre inferieur au solde\n")
    else:
        code_pin()
        compte['solde'] = compte['solde'] - pass_forfait
        print(f"Vous pouvez acheter un forfait de {pass_forfait} FCFA et votre nouveau solde est : {compte['solde']} FCFA")   
        sauvegarder()
        menu_principal()
#Fin sous menu de forfait 1

#Sous menu de forfait 2
def forfait_2():

    print("\nKheweul du forfait 500 Mo\n")
    # while True
    pass_forfait = 1000
    if (pass_forfait > compte['solde']):
        print("Le pass doit etre inferieur au solde\n")
    else:
        code_pin()
        compte['solde'] = compte['solde'] - pass_forfait
        print(f"Vous avez acheter un forfait de {pass_forfait} FCFA et votre nouveau solde est : {compte['solde']} FCFA")   
        sauvegarder()
        menu_principal()
#Fin sous menu de forfait 2

#Sous menu de forfait 3
def forfait_3():

    print("\nKheweul du forfait 1 Go\n")
    # while True
    pass_forfait = 2000
    if (pass_forfait > compte['solde']):
        print("Le pass doit etre inferieur au solde\n")
    else:
        code_pin()
        compte['solde'] = compte['solde'] - pass_forfait
        print(f"Vous avez acheter un forfait de {pass_forfait} FCFA et votre nouveau solde est : {compte['solde']} FCFA") 
        sauvegarder()
        menu_principal()      
#Fin sous menu de forfait 3
#Fin sous menu principal 

#Debut Fonctions principales 
def main():
    print("-"*60,"\n \nPersistance du projet USSD Orange Money (version simplifiée\n \n","-"*60) 
    code_ussd() 
    sauvegarder() 
    charger() 
    
    while True:
        menu_principal()

        choix_option = input("Choisir une option entre 0 et 9:  ")
        if choix_option == "1":
            consulter_solde()   
        elif choix_option == "2":
            effectuer_transfert()
        elif choix_option == "3":
            acheter_credit()
        elif choix_option == "4":
            forfait_internet()   
        elif choix_option == "5":
            annuler_transfert()  
        elif choix_option == "6":
            transferts_historique()
        elif choix_option == "7":
            solde_json()
            try:
                while True: 
                    input("Appuyez sur Entrée \n")
                    solde_json()
            except KeyboardInterrupt: 
                print("Fermer la consultation du solde.\n") 
        elif choix_option == "0":
            print("\nQuitter")
            break
        elif choix_option == "9":
            menu_principal()
        else:
            print("Choix invalide, saisie encore")       
main()
            

