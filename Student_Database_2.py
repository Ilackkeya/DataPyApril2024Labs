#!/usr/bin/env python
# coding: utf-8

# In[45]:


#Student Database 2.0

#Defining list_names functions
def list_names(std_list):
    
    #assigning a variable to the length of the list
    list_length = len(std_list)
        
    #Looping through to print the student names
    for i in range(list_length):   
        j = i+1
        print(f"{j}. {std_list[i]['name']}")
    
#Function for listing student info from a list of dictionaries
def stud_info(user, usr_name,stdlst):

    #assigning a variable to the length of the list
    lst_len = len(stdlst)

    #validating user entry 
    if user<= lst_len:
        
        #Looping through to find the student
        for i in range(lst_len+1):
            if user == i:
                j = i-1
                print(f"Student {user} is {stdlst[j]['name']} \n")

                #Asking for preference about student information
                preference = input("What would you like to know? \nEnter 'hometown' or 'favourite food' \n")
                if preference =='hometown': #if hometwon
                    print(f"{stdlst[j]['name']} is from {stdlst[j]['hometown']}")
                elif preference =='favourite food': #if favourite food
                    print(f"{stdlst[j]['name']}'s favourite food is {stdlst[j]['favourite_food']}")
                else: #any other irrelevant input
                    print("This category does not exist. Please try again. Enter 'hometown' or 'favourite food' \n")

    else:
        ###If the user enters a number other than length of the list even once, this loop will run throughout the end of program###

        #Getting user input
        print("Oops! Looks like you have entered an unmatched name and number \n")
        user_try = int(input(f"\nPlease enter a number between 1 and {lst_len} to learn more about a student: \n"))
        usr_try_name=input(f"\nEnter the correct student name:  \n")
        stud_info(user_try,usr_try_name,stdlst)

#Defining get_new_student

def get_new_student():
    
        #Collecting details to add the student info into a dictionary
        name = input("Please input a name for the new student: \n")
        town = input("Next, please input their hometown: \n")
        food = input("Lastly, Please input their favourite food: \n")

        #creating a new dictionary
        add_stud ={"name":name,"hometown":town,"favourite_food":food}
        return add_stud
        
        
        
#Creating a dictionary for student information
std_data = [
            {"name": 'Audrey Lim',"hometown":"Georgetown","favourite_food":"Alfredo Pasta" },
            {"name":'Marcus Andrews',"hometown":"Irving","favourite_food":"Sausage Pizza" }, 
            {"name":'Aaron Glassman',"hometown":"Madison","favourite_food":"Tacos"},
            {"name":'Alex Park',"hometown":"Richmond","favourite_food":"French Toast"}, 
            {"name":'Shaun Murphy',"hometown":"San Jose","favourite_food":"Hot chocolate"}, 
            {"name":'Jordan Allen',"hometown":"Santa Monica","favourite_food":"Croissant"}
            ]

list_len = len(std_data)

#Prompting the user for options
prompt = input("Please select which option you'd like to do: add, view, or quit \n")


while prompt!= 'quit':

    if prompt == 'view':
        #calling the function to print the student names
        print(list_names(std_data)) #function 1
        
        #Getting user input   
        user_cnt = int(input(f"\nWhich student would you like to learn more about? Enter a number 1-{list_len}:  \n"))
        user_name=input(f"\nEnter the student name:  \n") 
        stud_info(user_cnt,user_name,std_data) #function 2 

        #Prompting the user for options
        prompt = input("Please select which option you'd like to do: add, view, or quit \n")
        
    elif prompt =='add':
        std_data.append(get_new_student())
        list_len = len(std_data)
        prompt = input("Please select which option you'd like to do: add, view, or quit \n")
        
    else:
        print("Oops. Please try again to choose the following options: add, view, or quit \n")

print("Good bye!") #exit message


# In[ ]:





# In[ ]:




