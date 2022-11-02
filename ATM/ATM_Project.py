user={
   'lastname' : 'monty',
   'pin' : 1234,
   'balance' : 2000
    }
#συναρτηση για το αρχικο menu
def start_menu():
    print("Welcome to python bank\n")
    if log_in():
        main_menu()
    else:
        print('something went wrong')
            
#συναρτηση ελέγχου εγκυροτητας του pin
def check_pin(pin):
    if pin == user['pin']:
        return True
    else:
        return False

#Συναρτηση περιορισμου προσπαθειων PIN
def log_in():
    tries = 0
    while tries<3:
        try:
            pin = int(input("enter your 4-digit pin:"))
            if check_pin(pin):
                print("pin ok")
                return True
            else:
                print("You entered wrong pin")
                tries += 1
        except ValueError:
            print("you must enter only numbers")
            tries += 1
    print("You have no more tries\nYour card has been locked for security reasons") 
    return False
#Συναρτηση συνεχιση συνναλαγων
def other_transaction():
    
    while True:
        try:
            other_trans=input("do you want another transaction? press Y/y(yes) or N/n(no):")
            
            if other_trans == 'y' or other_trans == 'Y':
                return True
            elif other_trans == 'n' or other_trans == 'N':
                return False
            else:
                print("enter a valid letter Y/y or N/n")
        except ValueError:
            print("enter a valid letter Y/y or N/n")
# Συναρτηση  προβολη μενου
def menu():
    
    print('please choose one of the following actions:')
    print("""choose 1 for Withdrow
choose 2 for Deposit
choose 3 for Balance
choose 4 for Cancel
choose 5 for Change Password""")
    
#Συναρτηση αρχικο μενου
def main_menu():
    print(f'Welcome Mr/Ms {user["lastname"]}')
    menu()
    while True:
        try:
            option = int(input("Select the number for the transaction you want to make:"))
            
            if option == 1:
                withdrow()
                if other_transaction():
                    menu()
                    continue
                else:
                    print('Please take your card')
                    break
            elif option == 2:
                deposit()
                if other_transaction():
                    menu()
                    continue
                else:
                    print('Please take your card')
                    break

            elif option == 3:
                balance()
                if other_transaction():
                    menu()
                    continue
                else:
                    print('Please take your card')
                    break

            elif option == 4:
                print("Canceled transaction...\nPlease take your Card\nThank you")
                break
            elif option == 5:
                if change_pin():
                    start_menu()
                
                else:
                    if other_transaction():
                        menu()
                    else:
                        break
                    
                    
                  
                
            else:
                print("Please choose one of the above options 1 , 2 , 3, 4")
        except ValueError:
            print("Please choose one of the above options 1 , 2 , 3, 4")
#Συναρτηση ελεγχου ποσου
def check_amount(amount):
    if amount <= user['balance']:
        return True

#Συναρτηση αναληψης
def withdrow():
    while True:
        try:
            amount = int(input('enter the amount:'))
            #Ελεγχος ποσου
            if(check_amount(amount)):
                user['balance'] = user['balance'] - amount
                print(f'The amount of {amount} Euro have been withdrowed')
                print(f'your new balance is {user["balance"]} Euro')
                break
            else:
                print("your balance is not enough for the withdrow")
        except ValueError:
            print("please enter a valid number")
        
#Συναρτηση καταθεσης
def deposit():
    while True:
        try:
            amount = int(input("enter the amount for deposit:"))
            if amount > 0:
                user['balance'] = user['balance'] + amount
                print("Successfull deposit.")
                print(f'your new balance is {user["balance"]} Euro')
                
                break
            else:
                print('enter a valid amount')
        except ValueError:
            print("please enter a valid number")
#Συναρτηση ελεγχος υπολοιπου            
def balance():
    print(f'Your balance is {user["balance"]} Euro')
#Συναρτηση αλλαγη password
def change_pin():
    try:
        pin = int(input("give your pin:"))
        if pin == user['pin']:
            try:
                new_pin = int(input("give your new pin:"))
                if new_pin>999 and new_pin<=9999:
                    user['pin']=new_pin
                    print('pin successfully changed')
                    print(f'your new pin is :{user["pin"]}')
                    return True
                else:
                    print("pin must be only four digits")
            except ValueError:
                 print("Please enter only numbers")
        else:
                        
              print("not valid pin")
              return False

    except ValueError:
        print("Please enter only numbers")
start_menu()
        
