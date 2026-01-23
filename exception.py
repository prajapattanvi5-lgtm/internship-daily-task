#Take two numbers from the user and handle division by zero.
'''
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    result = num1 / num2
    print("Division is:",result)

except ZeroDivisionError:
    print("Error: Divide by zero not allowed")

else:
    print("Number divided successfully!")

finally:
    print("Code executed Successfully!!")
'''

#Ask the user to enter an integer. Handle the case where the user enters a string.
'''
try:
    num = int(input("Enter an integer:"))
    print(num)

except ValueError:
    print("Please Enter a valid integer.")

else:
    print("Integer is:", num)

finally:
    print("Code executed.")
'''

#Divide two user inputs and handle both ValueError and ZeroDivisionError.
'''
try:
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))

    result = n1 / n2
    print(result)

except ZeroDivisionError:
    print("Divide by zero not allowed")

except ValueError:
    print("Enter a valid number.")

else:
    print("code executed without error...")
'''
#Write a program that prints “Division successful” only if no exception occurs.
'''
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    result = num1 / num2
    print("Division is:",result)

except ZeroDivisionError:
    print("Error: Divide by zero not allowed")

else:
    print("Division successful!")
'''

#Open a file and close it using finally, even if an error occurs.
'''
f = None
try:
    f = open("Demofile.txt")

except FileNotFoundError:
    print("File doesn't exists!!!")

finally:
   if f:
    f.close()
   print("File CLOSED..")
'''

#Read a file and handle the case when the file does not exist.
'''
file = None
try:
    file = open("Demo.txt","r")

except FileNotFoundError:
    print("File doesn't exist.")

finally:
    if file:
        file.read()
        file.close()
    print("File readed successfully!!")
'''

#Access an index in a list that may not exist.
try:
    list1 = [10,20,30,40,50]
    print(list1[6])

except IndexError:
    print("Index not exists...")
