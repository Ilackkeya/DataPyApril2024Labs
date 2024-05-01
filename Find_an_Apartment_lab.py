#!/usr/bin/env python
# coding: utf-8

# In[67]:


# Find an Apartment

# function apt_search1

def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed == "True":
        print(f"\nWelcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments " 
              f"that allow pets, all within a budget of {max_rent} per month.....")
    else: 
        print(f"\nWelcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, "
              f"all within a budget of {max_rent} per month.....")        
        
#prompt the user     
print("\nHello, Please enter your requirements for finding your home!\n")
user_city = input("Enter the city you are looking for: \n")
user_rent = int(input("Enter the budget of the rent ($): \n"))
user_beds = int(input("Enter the number of bedrooms: \n"))
user_pets = bool(input("Are you looking for pet-friendly apartments? (True/False)  \n"))

apt_search1(user_city, user_rent, user_beds, user_pets)


# 
# 
# 

# In[68]:


# function apt_search2        
def apt_search2(city, max_rent, min_beds = 1, pets_allowed = True):
    if pets_allowed == False:
        print(f"\nWelcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, "
              f"all within a budget of {max_rent} per month.....")    
    else: 
        print(f"\nWelcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments "
               f"that allow pets, all within a budget of {max_rent} per month.....")



apt_search2("Alaska", 2400)
apt_search2("Alaska", 2400, 2)
apt_search2("Alaska", 2400, 2, False)


# In[72]:


#  simple lambda functions

plus_one_hundred = lambda x : x+100
square_num = lambda z : z*z
concatenate = lambda y : '-'+' '+ y
divide_by_three = lambda a : a/3

x = 45
z = 6
y= 'hello'
a = 27

print(plus_one_hundred(x))  
print(square_num(z)) 
print(concatenate(y))  
print(divide_by_three(a)) 


# In[ ]:




