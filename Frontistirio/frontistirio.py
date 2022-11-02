data = """Δημήτρης,M,Αγγλικά,Μαθηματικά,Φυσική
Αντώνης,M,Μαθηματικά,Φυσική,Έκθεση
Δήμητρα,F,Μαθηματικά,Φυσική,Έκθεση,Αγγλικά
Κική,F,Μαθηματικά
Ειρήνη,F,Μαθηματικά,Φυσική,Έκθεση,Αγγλικά
Δέσποινα,F,Έκθεση,Αγγλικά
Σοφία,F,Μαθηματικά,Αγγλικά
Γιώργος,M,Αγγλικά
Γεωργία,F,Φυσική,Αγγλικά
Αλέξανδρος,M,Μαθηματικά,Φυσική,Έκθεση,Αγγλικά
Αλέξης,M,Φυσική,Έκθεση
Μαρία,F,Φυσική,Έκθεση,Αγγλικά
Βασίλης,M,Έκθεση,Αγγλικά
Ιουλία,F,Μαθηματικά,Έκθεση
Ελένη,F,Μαθηματικά,Φυσική"""
male=set()
female=set()
agglika=set()
mathimatika=set()
fysiki=set()
ekthesi=set()
lines=data.split("\n")
for line in lines:
    s=line.split(",")
    print(s)
    mathitis=s[0]
    fylo=s[1]
    if "M" in fylo:
        male.add(mathitis)
    if "F" in fylo:
        female.add(mathitis)
    if "Αγγλικά" in s:
        agglika.add(mathitis)
    if "Μαθηματικά" in s:
        mathimatika.add(mathitis)
    if "Φυσική" in s:
        fysiki.add(mathitis)
    if "Έκθεση" in s:
        ekthesi.add(mathitis)
print ("to frontistirio exei {} agoria kai {} koritsia".format(len(male),len(female)))
print ("Μαθητές ανά μάθημα")
print ("Αγγλικά: {} μαθητές".format(len(agglika)))
print ("Μαθηματικά: {} μαθητές".format(len(mathimatika)))
print ("Φυσική: {} μαθητές".format(len(fysiki)))
print ("Έκθεση: {} μαθητές\n".format(len(ekthesi)))
#erotima 3
q3= agglika.intersection(mathimatika)
print("erotima 3: {} mathites\n".format(len(q3)))
#Ερώτημα 4
q4 = agglika.union(ekthesi)
print ("Ερώτημα 4: {} μαθητές\n".format(len(q4)))
#Ερώτημα 5
q5_a = fysiki.difference(mathimatika)
q5 = q5_a.intersection(female)
print ("Ερώτημα 5: {} κορίτσια".format(len(q5)))
for n in q5:
    print (n)
