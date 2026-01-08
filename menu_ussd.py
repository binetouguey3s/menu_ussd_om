# Lien gitHub:

solde = 4000
code = "#144#"
code_secret = "otocad00"
numero = "771234567"

def menu_principal():
    print("-"*40,"\n Menu principal du services USSD OM \n","-"*40)
    print("1. Consulter le solde Orange Money")
    print("2. Effectuer des transferts,")
    print("3. Acheter du crédit")
    print("4. Autres")
    print("0. Quitter\n")

#Sous menu_principale

#Code de validation gerer la saisie
def code_ussd():
    while True:
        try:
            code_valide = input("Saisir le code pour acceder au service d'Orange Money:  ").strip
            if code == code_valide:
                print(f"Donnez le code de validation {code_valide}")
            else:
                print("Veuillez saisir le bon code ")
                break
        except ValueError:
            print("Resaisir a nouveau")
#Fin Code de validation gerer la saisie

#Fonction de consultation de solde 
def consulter_solde():
    print(f"Votre solde Orange Money est de {solde} FCFA")
    print("9. precedent")
#Fin consultation

#Effectuer des transferts
def effectuer_transfert():
    acheter_credit()
    global solde
    print("Fonction pour effectuer des transferts")
    print("9. precedent")
    numero_saisi = float(input("Donnez le bon numero telephonique"))
    while True:
        try:
            montant = float(input("Saisir le montant: \n"))
            if (montant > solde):
                print("Le montant doit etre inferieur au solde\n")
            else:
                solde = solde - montant
                print("Vous pouvez envoyez de l'argent au {numero_saisi}")
                break
        except ValueError:
            print("Montant incomplet")



#Fin transfert

#Achat credit
def acheter_credit():
    global solde
    print("\nJe souhaite acheter du credit telephonique:")
    print("1. Pour mon numero")
    print("2. Pour un autre numero Orange ou Kirene ou bien un numero Promobile\n       ---      ")
    print("9. precedent\n")

    choix_achat = input("Choisir une option d'achat: ")

    #Option 1. Pour mon numero
   
    if choix_achat == "1":
        while True:
            try:
                montant = float(input("Saisir le montant: \n"))
                if (montant > solde):
                    print("Le montant doit etre inferieur au solde\n")
                else:
                    solde = solde - montant
                    print("Vous pouvez acheter du credit")
                    break
            except ValueError:
                print("Montant incomplet")
    
            #Fin
            #Option 2. Pour un autre numero
    elif choix_achat == "2":
        print("Vous allez acheter du credit telephonique \n pour un autre numero Orange ou Kirene avec Orange ou \n flexbox.\n")
        while True:
            try:
                montant = float(input("Saisir le montant\n"))
                numero_saisi = input("Donnez le bon numero telephonique")
                if numero == numero_saisi:
                    if (montant > solde):
                        print("Solde insuffisant, recharger votre compte")
                    else:
                        solde = solde - montant
                        print(f"Vous pouvez acheter du credit sur le {numero_saisi}")
                        break
                else:
                    print("Numero invalide")
            except ValueError:
                    print("Choix invalide, saisie entre 1 et 3 ou bien 9")
    else:
        print("Montant invalide")
#Fin achat

#Autres
def autre():
    print("")
    print("9. precedent")
#Fin autre

#Fin sous menu principal 

#Debut Fonctions principales 
def main():
    code_ussd()
    # while True:
        # code_saisi = input("\nSaisir le code #144# ")
        # if code_saisi == code:
    menu_principal()
    while True:
        choix_option = input("\n Choisir une option entre 0 et 9: \n")
        if choix_option == "1":
            consulter_solde()   
        elif choix_option == "2":
            effectuer_transfert()
        elif choix_option == "3":
            acheter_credit()
        elif choix_option == "4":
            autre()
        elif choix_option == "9":
            menu_principal()
        elif choix_option == "0":
            print("\nQuitter")
            break
        else:
            print("Choix invalide, saisie encore")
        # else:
        #     print("Code invalide, veuillez réessayer!")
main()
            

