#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Heating/Cooling
# Functions, Conditions

# Heating_Cooling function definition

def heating_cooling(actual_temp, desired_temp):
    if actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")
    else:
        print("Standby")
    
#Prompt the user for temperature 

user_actual = int(input("Enter the actual temperature (in Fahrenheit): \n"))
user_desired = int(input("Enter the desired temperature (in Fahrenheit): \n"))

heating_cooling(user_actual,user_desired)


# In[16]:


# Extended Challenge

def convert_temp(temp_celsius, target_unit):
    
    if target_unit == 'F':
        farhenheit = (temp_celsius*1.8) + 32 
        return farhenheit
    elif target_unit == 'K':
        kelvin = temp_celsius + 273.15
        return kelvin  
    else:
        return temp_celsius
    

#Prompt the user for target unit and temperature 

user_unit = (input("Enter the temperature target unit to be converted ('C'or 'F' or 'K'): \n"))
user_temp = int(input("Enter the temperature (in °Celsius): \n"))

temp_converted = convert_temp(user_temp,user_unit)

print(f"\nThe converted temperature of {user_temp} deg Celsius is {temp_converted} {user_unit}")


# In[ ]:




