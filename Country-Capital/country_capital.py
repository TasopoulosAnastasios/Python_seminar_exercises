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
eu_all=eu.copy()
print("gess all European countries and their capitals")
while True:
    if len(eu)==0:
        print("well dane you guessed all of them")
        break
    kratos=input("type a european country or e for exit:")
    if kratos=="e":
        break
    if kratos in eu:
        proteuousa=input("give its capital:")
        if eu[kratos]==proteuousa:
            eu.pop(kratos)
            print("well done you still have to find:",len(eu))
        else:
            print("right country wrong capital\n try again")
    else:
        if kratos in eu_all:
            print("already guessed try again")
        else:
            print("wrong country try again")
if len(eu)>0:
    print("whole list with country-capital")
    for k in eu_all.keys():
        print(k,"-",eu_all[k])
