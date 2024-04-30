#!/usr/bin/env python
# coding: utf-8

# In[35]:


#Powers Table

#prompting user details
user_name = input("Please Enter your name: ")
print(f"\nHello, {user_name}. Welcome to GC Powers Table! \t\nLearn your squares and cubes!")

#prompt the user for number
num = int(input("\nEnter any valid integer number: "))

#Confirming the valid entry
confirm = input("\nAre you sure you entered a valid number? (y/n) \n")

column = ["Number", "Squared","Cubed"]
padding1 = "      ".join(column)
print(padding1)
line = ['======', "=======", "======"]
padding2 = "      ".join(line)
print(padding2)

while confirm != 'n':
        for num in range(1,num+1):
            
            squared = str(num*num)
            cubed = str(num*num*num)
            number =str(num)
            
            answer = [number, squared, cubed]
            padding3 ="            ".join(answer)
            print(padding3)
            
        #Extended Challenge:
        print("Multiplication table for reference")
        for row in range(1, num + 1):
            print(*(f"{row*col:3}" for col in range(1, num + 1)))
            
        break

#prompt the user to continue or stop

reply = input("\nDo you want to continue? (y/n)  ")

if reply == 'n': 
    print(f"\nThanks for your time, {user_name}!")

#break
    
while reply != 'n':
    num = int(input("\nEnter any valid integer number: "))

    confirm = input("\nAre you sure you entered a valid number? (y/n) \n")

    column = ["Number", "Squared","Cubed"]
    padding1 = "      ".join(column)
    print(padding1)
    line = ['======', "=======", "======"]
    padding2 = "      ".join(line)
    print(padding2)


    while confirm != 'n':
            for num in range(1,num+1):
                squared = str(num*num)
                cubed = str(num*num*num)
                number =str(num)
                answer = [number, squared, cubed]
                padding3 ="            ".join(answer)
                print(padding3)
            #Extended Challenge:
            print("Multiplication table for reference")
            for row in range(1, num + 1):
                print(*(f"{row*col:3}" for col in range(1, num + 1)))
            break
            
    reply = input("\nDo you want to continue? (y/n)  ")
    if reply == 'n': 
        print(f"\nThanks for your time, {user_name}!")
    

