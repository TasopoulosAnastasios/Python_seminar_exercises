#imports
import pickle
import os

#global variables
#create dictionary with key countries and values its capitals
eu ={"Αυστρία" : "Βιέννη",
	"Βέλγιο" : "Βρυξέλλες",
	"Βουλγαρία" : "Σόφια",
	"Κροατία" : "Ζάγκρεμπ",
	"Κύπρος" : "Λευκωσία",
	"Τσεχία" : "Πράγα",
	"Δανία" : "Κοπεγχάγη",
	"Εσθονία" : "Τάλιν",
	"Φινλανδία" : "Ελσίνκι",
	"Γαλλία" : "Παρίσι",
	"Γερμανία" : "Βερολίνο",
	"Ελλάδα" : "Αθήνα",
	"Ουγγαρία" : "Βουδαπέστη",
	"Ιρλανδία" : "Δουβλίνο",
	"Ιταλία" : "Ρώμη",
	"Λετονία" : "Ρίγα",
	"Λιθουανία" : "Βίλνιους",
	"Λουξεμβούργο" : "Λουξεμβούργο",
	"Μάλτα" : "Βαλέτα",
	"Ολλανδία" : "Άμστερνταμ",
	"Πολωνία" : "Βαρσοβία",
	"Πορτογαλία" : "Λισαβόνα",
	"Ρουμανία" : "Βουκουρέστι",
	"Σλοβακία" : "Μπρατισλάβα",
	"Σλοβενία" : "Λιουμπλιάνα",
	"Ισπανία" : "Μαδρίτη",
	"Σουηδία" : "Στοκχόλμη"}
#create dictionary copy
eu_all = eu.copy()

#functions

#function for first message
def intro():
    #information for the user
    print("The game's perpose is to find the countries that belong to EU and their capitals.")

#function of basic menu wich returns user's choise
def menu():
    print("\nOptions - Type:\n- One country of EU to start the game")
    print("- 1 to check how many you have found till now")
    print("- 2 save and exit, to continue later")
    print("- 3 exit and see all answers")
    kratos = input("give your choise: ")

    if kratos == "1":
        return 1
    elif kratos == "2":
        return 2
    elif kratos == "3":
        return 3
    else:
        return kratos

#function takes a string and checks if is correct country
#if true asks the capital and shows three more cities of the country
def check_answer(kratos):
    #check if country exixts
    if kratos in eu:
        #if true ask the capital
        proteuousa = input ("Type the countys capital: ")

        #check if capital true
        if eu[kratos] == proteuousa:
            #delete country from dictionary
            eu.pop(kratos)
            #Show three more cities
            load_cities_csv(kratos,3)
            print("Right Guess! Countries you still have to find:",len(eu))
        else:
            print("Corect Country wrong Capital\nTry again\n ")
    else:
        if kratos in eu_all:
            print("Correct Country but you have allready guessed it")
        else:
            print("Country not in EU try again")

#function printing all countries
def view_all_countries():
    print("\nWhole list\nCountry - Capital")
    #print
    for k in eu_all.keys():
        print(k,"-",eu_all[k])

#function checks if there are any saved games
#and informs user of the options he has
#returns either the saved game of False if there isn't one
#or user wants to start from beggining
def load_game():
    #check if there is saved game
    if os.path.exists("saved.game"):
        print("Found saved game")

        #defending programming
        flag = 0
        while flag == 0:
            cont = input("Do you want to continue (1 = yes, 2 = no)?")
            if cont == "1" or cont == "2":
                flag = 1

        #if user continues
        #load from pickle
        if cont == "1":
            #open file with saved game for read
            f = open('saved.game','rb')
            #load dictionary from last time
            eu_load = pickle.load(f)
            f.close()
            print("Success loading game")
            print("Countries to find:",len(eu_load))
            return eu_load
        #else delete saved game
        else:
            print("saved game has been deleted. Start from beggining")
            os.remove("saved.game")
            return False
    else:
        return False

#function save game
#parameter current game
def save_game(current_eu):
    f = open('saved.game','wb')
    pickle.dump(current_eu, f)
    f.close()
    print("game saved!")
    print("see you soon")

#funtion returns three more cities parameters country,number of cities
def load_cities_csv(user_country,num_cities):
    #create dictionary with all eu countries
    #and their two letter code (ISO 3166-1 alpha-2)
    #to take information from CSV
    eu_iso ={"Αυστρία" : "AT",
    "Βέλγιο" : "BE",
    "Βουλγαρία" : "BG",
    "Κροατία" : "HR",
    "Κύπρος" : "CY",
    "Τσεχία" : "CZ",
    "Δανία" : "DK",
    "Εσθονία" : "EE",
    "Φινλανδία" : "FI",
    "Γαλλία" : "FR",
    "Γερμανία" : "DE",
    "Ελλάδα" : "GR",
    "Ουγγαρία" : "HU",
    "Ιρλανδία" : "IE",
    "Ιταλία" : "IT",
    "Λετονία" : "LV",
    "Λιθουανία" : "LT",
    "Λουξεμβούργο" : "LU",
    "Μάλτα" : "MT",
    "Ολλανδία" : "NL",
    "Πολωνία" : "PL",
    "Πορτογαλία" : "PT",
    "Ρουμανία" : "RO",
    "Σλοβακία" : "SK",
    "Σλοβενία" : "SI",
    "Ισπανία" : "ES",
    "Σουηδία" : "SE"}

    if os.path.exists('worldcities.csv'):
        worldcities = open('worldcities.csv','r',encoding='utf8')
        lines=worldcities.readlines()
    else:
        print("file with cities not found")
        return
    print("cities of this country besides capital")

    i=0
    for line in lines:
        #split with , to take the cols
        cols = line.split(",")

        #take the cols we want
        country = cols[5].replace("\"","")
        city = cols[1].replace("\"","")
        is_capital = cols[8].replace("\"","")

        #show citie for the country asked
        if country == eu_iso[user_country] and is_capital != 'primary':
            i+=1
            print(city)
        #if printed number of cities asked end loop
        if i == num_cities:
            break

#function to show the progress(counties found)
def view_progress():
    #empty list with progress
    progress = []

    #check whick countries of eu_all dont exit in eu
    #if dont they have been found
    for c in eu_all:
        #if get dont find the country returns 0
        check = eu.get(c,0)
        if check == 0:
            progress.append(c)
    if len(progress) == 0:
        print("No countries found till now")
    else:
        print("Countries found till now:")
        for f in progress:
            print(f)


#Main program

#print start information
intro()

#check for saved game
loaded_eu = load_game()
#if loaded game dictionary takes values of saved one
if loaded_eu != False:
    eu = loaded_eu.copy()

#set option to 0
#for def menu() runs at least one time
option = 0
while (option == 0):
    #user has found all
    if len(eu) == 0:
        print("well done you found all countries! end of game\n ")
        break
    #if not all found call menu
    if option == 0:
        option=menu()
    #if opion 1 view_progress
    if option == 1:
        view_progress()
        option=0

    #if 2 save and exit
    elif option == 2:
        save_game(eu)

    #if 3 exit
    elif option == 3:
        view_all_countries()
    else:
        #if user doesnt ask anything from above we check his answer
        check_answer(option)
        option=0
    

    
