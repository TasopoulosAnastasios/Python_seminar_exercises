import sys
string=""
while True:
    string=input("type a word or e for exit: ")
    if(string=="e"):
        break
    else:
        i=0
        mystr=""
        string=string.lower()
        string=string.replace(" ","")
        for i in range(len(string)-1,-1,-1):
            mystr+=string[i]
        if(mystr==string):
            print("palindrome")
        else:
            print("not palindrome")
    print("user input = {} bytes".format(sys.getsizeof(string)))
    print("counter i = {} bytes".format(sys.getsizeof(i)))
    #print("boolean result = {} bytes".format(sys.getsizeof(palindrome)))        
            
            
