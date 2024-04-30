#!/usr/bin/env python
# coding: utf-8

# In[37]:


#NUMBER ANALYZER - Decision Maker

#prompting user details
user_name = input("Please Enter your name: ")
print(f"\nHello, {user_name}. Welcome to GC Number Analyzer!")

#prompt the user for number
num = int(input("\nEnter any number from 1 to 100: "))

#validation
if num in range(1,101):
    print(f"\nYay! {num} is a postive integer!\n")
else:
    num = int(input(f"\nOops. It's not working! Please enter a positive integer from 1 to 100: "))
    if num in range(1,101):
        print(f"\nYay! {num} is a postive integer!\n")
    
#Conditions

if num < 60 and num % 2 != 0:
    print(f"\n{user_name}, the number you entered is Odd and less than 60")
elif num in range(2,25) and num % 2 == 0:
    print(f"\n{user_name}, the number you entered is Even and less than 25")    
elif num in range(26, 61) and num % 2 == 0:
    print(f"\n{user_name}, the number you entered is Even and between 26 and 60 inclusive") 
elif num > 60 and num % 2 == 0:
    print(f"\n{user_name}, the number you entered is Even and greater than 60")    
elif num> 60 and num % 2 != 0:
    print(f"\n{user_name}, the number you entered is Odd and greater than 60")
    

#prompt the user to continue or stop

reply = input("\nDo you want to look for another number? (y/n)  ")

if reply == 'n': 
    print(f"\nThanks for your time, {user_name}! Hope you had fun analyzing numbers!")
    
while reply != 'n':

        num = int(input("\nEnter any number from 1 to 100: "))

        #validation
        if num in range(1,101):
            print(f"\nYay! {num} is a postive integer!\n")
        else:
            num = int(input(f"\nOops. It's not working! Please enter a positive integer from 1 to 100: "))
            
            if num in range(1,101):
                print(f"\nYay! {num} is a postive integer!\n")

        #Conditions

        if num < 60 and num % 2 != 0:
            print(f"\n{user_name}, the number you entered is Odd and less than 60")
        elif num in range(2,25) and num % 2 == 0:
            print(f"\n{user_name}, the number you entered is Even and less than 25")    
        elif num in range(26, 61) and num % 2 == 0:
            print(f"\n{user_name}, the number you entered is Even and between 26 and 60 inclusive") 
        elif num > 60 and num % 2 == 0:
            print(f"\n{user_name}, the number you entered is Even and greater than 60")    
        elif num> 60 and num % 2 != 0:
            print(f"\n{user_name}, the number you entered is Odd and greater than 60") 
            
        #prompt the user to continue or stop
        
        reply = input("\nDo you want to look for another number? (y/n)  ")
        
        if reply == 'n': 
            print(f"\nThanks for your time, {user_name}! Hope you had fun analyzing numbers!")

