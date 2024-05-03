#!/usr/bin/env python
# coding: utf-8

# In[92]:


# Student Database

#Defining function to simplify the process
def std_db(user, name_list, hometown_list, fav_food_list):
    
    #assigning a variable to the length of the lists
    list_length = len(name_list)
    
    #validating user entry 
    if user <= list_length:
        
        #Looping through to find the student
        for i in range(list_length+1):
            if user == i:
                j = i-1
                print(f"Student {user} is {name_list[j]}.")
        #Asking for preference about student information
                preference = input("What would you like to know? \nEnter 'hometown' or 'favourite food' \n")
                if preference =='hometown': #if hometwon
                    print(f"{name_list[j]} is from {hometown_list[j]}")
                elif preference =='favourite food': #if favourite food
                    print(f"{name_list[j]}'s favourite food is {fav_food_list[j]}")
                else: #any other irrelevant input
                    print("This category does not exist. Please try again. Enter 'hometown' or 'favourite food' \n")
                    
        #Prompting user for willingness to know more
        user_cnt = input("Would you like to know about another student? (y/n) \n")
        return user_cnt
   
    else: 
        ###If the user enters a number other than 1-6 even once, this loop will run throughout the end of program###
        
        #Getting user input   
        user_try = int(input(f"\nPlease enter a number between 1 and {list_length} to learn more about a student: \n"))
        user_ans = (std_db(user_try,stdname_list,city_list, food_list))
        
        #Looping until the user want to know more
        while user_ans!= 'n':
            
            #Getting user input   
            user_cnt1 = int(input(f"\nOK. \nWhich student would you like to learn more about? Select 1-{list_length1}:  \n"))
            user_request = std_db(user_cnt1,stdname_list,city_list, food_list)
            if user_request == 'y':
                continue #continues to loop through to get student info
            else:  
                print("Thanks!") #Exit message if 'n'
                break 
                
    
#Prompting the user for student information

#Introducing the user to the student database
print("Welcome to GC Student Database!\n \nBelow is the list of all the students in the database \n")

#Creating 3 list for student information
stdname_list = ['Audrey Lim','Marcus Andrews', 'Aaron Glassman', 'Alex Park', 'Shaun Murphy', 'Jordan Allen']
city_list = ['Georgetown', 'Irving', 'Madison', 'Richmond', 'San Jose', 'Santa Monica' ]
food_list = ['Alfredo Pasta', 'Sausage Pizza', 'Tacos', 'French Toast', 'Hot chocolate', 'Croissant']
    
#assigning a variable to the length of the lists
list_length1 = len(stdname_list)

#Printing the list of all students
for i in range(list_length1):
    print(f"{i+1}. {stdname_list[i]}")
    
#Getting user input   
user_data = int(input(f"\nWhich student would you like to learn more about? Select 1-{list_length1}:  \n"))

call_data = std_db(user_data,stdname_list,city_list,food_list)

#####If the user enters number between 1 and 6 throughout the search, this loop will run###

#Looping until the user want to know more
while call_data!= 'n':
            #Getting user input   
            user_cnt1 = int(input(f"\nOK. \nWhich student would you like to learn more about? Select 1-{list_length1}:  \n"))
            user_req = std_db(user_cnt1,stdname_list,city_list, food_list)
            if user_req =='y':
                continue #continues to loop through to get student info
            else:
                #Exit message if 'n'   
                print("Thanks!")
                break
                    


# In[ ]:




