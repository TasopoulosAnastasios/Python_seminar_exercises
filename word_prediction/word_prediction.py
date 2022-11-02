import operator
import os
import random
import pathlib
import time




def get_words_from_text(file_name):
    #opening file and save to string(text)
    with open(file_name,'rt',encoding='utf-8') as f:
        text=f.read()
    #print(text)
    #print("type of text: ",type(text))
    #replace all whitespaces with one
    #text=" ".join(text.split())
    #make all letters to lower case
    text=text.lower()
    #take away numbers and symbols
    symbols='''|—!()-[]{};:\'\’\“\”\"\"\,<>./?@#$%^&*_~'''
    #print(text)
    for letter in text:
        if letter in symbols or letter.isdigit():
            text=text.replace(letter,'')
            
       
    #replace all whitespaces with one
    text=' '.join(text.split())    
    words=text.split()
    #print(type(words))
    #print(words)
    return words
def get_number_of_words(words):
    return len(words)
def get_unique_words(words):
    #make a set to count the unique words
    unique_words=set(words)
    #print("type of unique_words=",type(unique_words))
    return len(unique_words)
def get_5_least_frequent_words(words):
    #Create a dictionary with keys the words and values their num of apperance
    dict_occurances={}
    for item in words:
        if item in dict_occurances:
            dict_occurances[item]+=1
        else:
            dict_occurances[item]=1
    #print(dict_occurances)
    #create a list of tuples to order the dict by value
    sorted_list=sorted(dict_occurances.items(),key=operator.itemgetter(1))
    #keep first 5 elements of the list
    final_list=sorted_list[:5]
    #Create list for the words
    least_words=[]
    for key,value in final_list:
        least_words.append(key)
    return least_words
#function creating graph dinamically
def graph_add_node(v1,v2):
    #check if two same continuous words
    if v1==v2:
        return
    #check if node v1 exists in graph
    if v1 in my_graph:
        #check if v2 exists in graph
        if v2 in my_graph[v1]:
            #find the index of it's weight
            w_index=my_graph[v1].index(v2)+1
            #increase the weight plus 1
            my_graph[v1][w_index]=my_graph[v1][w_index]+ 1
        else:
            my_graph[v1].append(v2)
            my_graph[v1].append(1)
    else:
        temp_dict={v1:[v2,1]}
        my_graph.update(temp_dict)
#function fo K most used words
def top_k_words(word,k):
    try:
        #empty list to store the vetricles and their edges of word
        v_list=[]
        #read the items of the graph with key the word and save its values on v_list
        #we put step 2 because the list format is ['word','int']
        #append to v_list to have 2 columns col[0]-->words col[1]-->edges
        for x in (range(0,len(my_graph[word]),2)):
            v_list.append([my_graph[word][x],int(my_graph[word][x+1])])##to clear int
        #sort the list descending by the weight(tup[1])
        v_list.sort(key=lambda tup: tup[1],reverse=True)
        #print(v_list)
        #list to store the top words
        top_words_list=[]
        #counter until k words
        i=0
        while i<k:
            #list with the candidates
            cand=[]
            #get the max value by weights(tup[1]) since list is ["word", int(weight)]
            w_max_w=max(v_list,key=lambda tup:tup[1])
            #take only the integer
            w_max=w_max_w[1]
            #print("max is: ",w_max)
            #make a copy of the list 
            v_list2=v_list.copy()
            #loop the list to find the max values
            #start=time.process_time()
            for x in v_list:
                #if the value of the element is equal to max
                #append it to candidates list
                #and remove it from the copy of the list
                #we use it to update the main list later
                if x[1]==w_max:
                    #print("one x found equal=",x)
                    cand.append(x)
                    #removes the selected items 
                    v_list2.remove(x)
                    
                #since the list is sorted descending
                #if the next item isn't equal to w_max
                #there is no reason to loop forward
                else:
                    #print("Break:::")
                    break
            #end=time.process_time()-start
           # print("total time for looping in list:",end)
            #check if the list cand has more than one items
            #if true random.choise gives one random choise from the cand list
            #and append it to top_words_list
            #and remove it from the main list so it won't be found again
            if len(cand)>1:
                #print("Candidates:")
                #print(cand)
                toappend=random.choice(cand)
                #print("to append random is:",toappend)
                top_words_list.append(toappend[0])
                v_list.remove(toappend)
            #if cand has only one item then we append it to top_words_list
            #and remove it from the main list so it won't be found again
            else:
                #print("Cand is: ",cand)
                for x in cand:
                    toappend=x
                #print("toappend is: ",toappend)
                top_words_list.append(toappend[0])
                v_list.remove(toappend)
            #inform the main list to remove the selected item
            v_list2=v_list.copy()
            #increase the counter until K words
            i+=1
        #print("Candidates:",cand)
        #print("Copy list:",v_list)
        #print(heapq.nlargest(k,v_list,key=lambda tup:tup[1]))
        print("top ",k," words are:\n\n",top_words_list)
    except:
        print("\nthere are not so much words")
        print("top ",len(top_words_list)," words are:\n\nB",top_words_list)

#function to find the next verticle of the graph by its weight
#if the same weght choose random
def graph_next_vertice(current):
    try:
        #empty list to store the vetricles and their edges of word
        v_list=[]
        #read the items of the graph with key the current verticle(word) and save its values on v_list
        #we put step 2 because the list format is ['word','int']
        #append to v_list to have 2 columns col[0]-->words col[1]-->edges
        for x in (range(0,len(my_graph[current]),2)):
            v_list.append([my_graph[current][x],int(my_graph[current][x+1])])##to clear int
        #sort the list descending by the weight(tup[1])
        v_list.sort(key=lambda tup: tup[1],reverse=True)
        #print("lista ypopsifion korifon:",v_list)
        #list with the candidates
        cand=[]
        #get the max value by weights(tup[1]) since list is ["word", int(weight)]
        w_max_w=max(v_list,key=lambda tup:tup[1])
        #take only the integer
        w_max=w_max_w[1]
        #print("max is: ",w_max)
        #make a copy of the list 
        #v_list2=v_list.copy()
        #loop the list to find the max values
        #start=time.process_time()
        for x in v_list:
            #if the value of the element is equal to max
            #append it to candidates list
            #and remove it from the copy of the list
            #we use it to update the main list later
            if x[1]==w_max:
                #print("one x found equal=",x)
                cand.append(x)
                #removes the selected items 
                v_list.remove(x)
                    
            #since the list is sorted descending
            #if the next item isn't equal to w_max
            #there is no reason to loop forward
            else:
                #print("Break:::")
                break
        #check if the list cand has more than one items
        #if true random.choise returns one random choise from the cand list
        if len(cand)>1:
            ##return the random choise
            return random.choice(cand[0])

        #if cand has only one item return it
        else:
            #print("Cand is: ",cand)
            for x in cand:
                toappend=x
            #print("next vertice is: ",toappend[0])
            return toappend[0]
    except:
        print("\nthere is no next word")
        return ''

#function for finding next possible N words
#using graph_next_vertice to run the graph
def find_next_possible_words(word,N):
    #set the output == word given
    output=word
    temp=N
    #set the parameter for the function graph_next_vertice=word given
    next_vertice=word
    #loop until N becomes zero to find N possible words
    while N>0:
        #return the possible word
        next_vertice=graph_next_vertice(next_vertice)
        #if not '' format the output
        if next_vertice!='':
            output+=" "+next_vertice
            #decrease the N by one 
            N=N-1
        else:
            #break the loop if there is a problem
            break
    print(f"The next possible {temp} words are: ",output)
def graph_next_random_vertice(current):
    #create empty list
    v_list=[]
    #create empty list for the possibilities
    p_list=[]

    try:
        #get the list of words from current vertice
        #2 step to make a 2d list ['word',int(weight)]
        for x in (range(0,len(my_graph[current]),2)):
            #append to v_list the rresults
            v_list.append([my_graph[current][x],my_graph[current][x+1]])
        #print(v_list)
        #calculate the sum of all weights in v_list
        sum_weight=sum(j for i,j in v_list)
        #print(sum_weight)
        #calculate the possibilitys for each worrd
        #and append it to p_list
        for x in v_list:
            p_list.append(x[1]/sum_weight)
        #print("List of sums:\n",p_list)
        #return the random choice from the v_list with weights the p_list
        
        for x in random.choices(v_list,p_list,k=1):
            choice=x
        return(choice[0])
    except:
        print("\nThere are't so much words")
#function for finding next random N words
#using graph_next_randon_vertice to run the graph
def find_next_random_words(word,N):
    #set the output == word given
    output=word
    temp=N
    #set the parameter for the function graph_next_vertice=word given
    next_vertice=word
    #loop until N becomes zero to find N possible words
    while N>0:
        #return the possible word
        next_vertice=graph_next_random_vertice(next_vertice)
        #if not '' format the output
        if next_vertice!='':
            output+=" "+next_vertice
            #decrease the N by one 
            N=N-1
        else:
            #break the loop if there is a problem
            break
    print(f"The {temp} possible random words are: ",output)
def user_input():
    #make the word given to lower case
    word=input("\nGive your word in English:").lower()
    #check if word in the list of wprds
    if word not in words:
        word='word_error'
        num='num_error'
        print("The word given doesn't exist in the text\n")
        return word,num
    try:
        #check if is number
        num=int(input("\nGive give an integer:"))
    except:
        print("\nnot a number or not an integer ")
        num='num_error'
    else:
        #check if number given is more than the number of words in list
        if num>len(words):
            print("\nThe number of words given is bigger than existing words")
    return word,num
def menu():
    while True:
        print("\nMenu of choices please select one typing the letter respectively\n")
        print("A - Return of K possible words\n")
        print("B - Production of N possible words\n")
        print("C - Production of N random words\n")
        print("D - Exit\n")
        
        choice=input("Give your choice: ")
        if choice=="A":
            word,num=user_input()
            if word!='word_error' and num!='num_error':
                print("\nStarting A.....\n")
                top_k_words(word,num)
                print("\nEnding A.....\n")
            else:
                continue
        elif choice=="B":
            word,N=user_input()
            if word!='word_error' and N!='num_error':
                print("\nStarting B.....\n")
                find_next_possible_words(word,N-1)
                print("\nEnding B......\n")
            else:
                continue
        elif choice=="C":
            word,N=user_input()
            if word!='word_error' and N!='num_error':
                print("\nStarting C.....\n")
                find_next_random_words(word,N-1)
                print("\nEnding C......\n")
            else:
                continue
        elif choice=="D":
            print("Exiting program....")
            break
        else:
            print("\nThe given choice is not correct")
            
    
#get current dir
current_dir=os.getcwd()
#files counter
files_count=0
#list words
words=[]
print("Starting the program\n")
#get the files that are .txt
for file in pathlib.Path(current_dir).glob('**/*.txt'):
    files_count+=1
    #file.stem uses the Path("some path").stem which takes only the name of the file
    print("reading file: ",file.stem+".txt\n")
    #print('type= ',type(file))
    #extend the list with all the words
    words.extend(get_words_from_text(file))
#print(words)
print("-------BASIC STATISTICS--------\n")
print("current directoty: ",current_dir)
print("\nNumber of files used for the training: ",files_count)
#words=get_words_from_text(file_name)
#print(words)
print("\nNumber of words: ",get_number_of_words(words))
print("\nNumber of unique words: ",get_unique_words(words))
print("\nFive least frequent words:\n\n",get_5_least_frequent_words(words))
#create empty graph
my_graph={}
#insert nodes and calculate edges
for i in range(len(words)):
    #add the nodes in the graph except the last word
    if i !=len(words)-1:
        graph_add_node(words[i],words[i+1])
    else:
        if words[i] in my_graph:
            continue
        else:
            temp_dict={words[i]:[]}
            my_graph.update(temp_dict)

menu()
