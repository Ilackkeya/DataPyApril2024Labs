#EXERCISE 1: Echo String

user = input("Enter some text: ")
print (user)

#EXERCISE 2: Adding a number to an integer

num1 = input("Enter a number: ")
num2 = int(num1) + 1
print(num2)

#EXERCISE 3: Adding a number to a float
num3  = input("Enter a number: ")
num4 = float(num3) + 0.5
print(num4)

#EXERCISE 4: Adding Two Floats
num5  = input("Enter a number: ")
num6 = input("Enter another number: ")
sum = float(num5) + float(num6)
print("The sum is ", sum)

#EXERCISE 5: Multiplying Floats
num7  = input("Enter a number: ")
num8 = input("Enter another number: ")
pdt = float(num7) * float(num8)
print("The product is ", pdt)

#EXERCISE 6: Dividing Integers
num9  = input("Enter a number: ")
num10 = input("Enter another number: ")
div = int(num9) / int(num10)
print("The result is ", div)

#When two numbers don't divide evenly, the output appears as a float
#When the input is entered as decimal numbers, there appears an error since the type conversion is meant for integer.
# If it is resolved into float data type, the output will be float.
